import math
from abc import ABCMeta, abstractmethod
from functools import lru_cache
from typing import Any, Dict, List, Optional

from indigo import Indigo  # type: ignore

from bingo_elastic.model.record import IndigoRecord, IndigoRecordMolecule
from bingo_elastic.utils import PostprocessType, head_by_path


def clauses(fingerprint, fingerprint_name) -> List[Dict]:
    return [
        {
            "term": {
                fingerprint_name: {
                    "value": clause,
                }
            }
        }
        for clause in fingerprint
    ]


def default_script_score(query: Dict) -> None:
    script_score_head = head_by_path(
        query,
        (
            "query",
            "script_score",
        ),
    )
    if not script_score_head.get("script"):
        script_score_head["script"] = {"source": "_score"}


class CompilableQuery(metaclass=ABCMeta):
    field: str = ""

    @abstractmethod
    def compile(
        self, query: Dict, postprocess_actions: PostprocessType = None
    ) -> None:
        pass


class KeywordQuery(CompilableQuery):
    def __init__(self, value: str):
        self._value = value

    def compile(
        self, query: Dict, postprocess_actions: PostprocessType = None
    ) -> None:
        bool_head = head_by_path(
            query, ("query", "script_score", "query", "bool")
        )
        if not bool_head.get("must"):
            bool_head["must"] = []
        bool_head["must"].append(
            {"match": {self.field: {"query": self._value, "boost": 0}}}
        )
        default_script_score(query)


class SubstructureQuery(CompilableQuery):
    def __init__(self, key: str, value: IndigoRecord) -> None:
        if not isinstance(value, IndigoRecord):
            raise AttributeError(
                "Argument for substructure search must be IndigoRecord"
            )
        self._key = key
        self._value = value

    # pylint: disable=inconsistent-return-statements
    def postprocess(
        self, record: IndigoRecord, indigo: Indigo
    ) -> Optional[IndigoRecord]:
        if indigo.substructureMatcher(record.as_indigo_object(indigo)).match(
            indigo.loadQueryMolecule(
                self._value.as_indigo_object(indigo).canonicalSmiles()
            )
        ):
            return record
        return None

    @lru_cache(maxsize=None)
    def clauses(self) -> List[Dict]:
        return clauses(self._value.sub_fingerprint, "sub_fingerprint")

    def compile(
        self, query: Dict, postprocess_actions: PostprocessType = None
    ) -> None:
        # This code same as ExactMatch.
        # ExactMatch will use search by hash in next releases
        bool_head = head_by_path(
            query, ("query", "script_score", "query", "bool")
        )
        if not bool_head.get("must"):
            bool_head["must"] = []
        bool_head["must"] += self.clauses()
        script_score_head = head_by_path(query, ("query", "script_score"))
        script_score_head["script"] = {
            "source": "_score / doc['sub_fingerprint_len'].value"
        }
        query["min_score"] = 1
        assert postprocess_actions is not None
        postprocess_actions.append(getattr(self, "postprocess"))


class RangeQuery(CompilableQuery):
    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper

    def compile(
        self, query: Dict, postprocess_actions: PostprocessType = None
    ) -> None:
        bool_head = head_by_path(
            query, ("query", "script_score", "query", "bool")
        )
        if not bool_head.get("must"):
            bool_head["must"] = []
        bool_head["must"].append(
            {
                "range": {
                    self.field: {
                        "from": self.lower,
                        "to": self.upper,
                        "include_lower": True,
                        "include_upper": True,
                    }
                }
            }
        )
        default_script_score(query)


class WildcardQuery(CompilableQuery):
    def __init__(self, wildcard: str) -> None:
        self.wildcard = wildcard

    def compile(
        self, query: Dict, postprocess_actions: PostprocessType = None
    ) -> None:
        bool_head = head_by_path(
            query, ("query", "script_score", "query", "bool")
        )
        if not bool_head.get("must"):
            bool_head["must"] = []
        bool_head["must"].append(
            {"wildcard": {f"{self.field}": {"wildcard": self.wildcard}}}
        )
        default_script_score(query)


class BaseMatch(metaclass=ABCMeta):
    def __init__(self, target: IndigoRecord, threshold: float):
        self._target = target
        self._threshold = threshold

    @lru_cache(maxsize=None)
    def clauses(self) -> List[Dict]:
        return clauses(self._target.sim_fingerprint, "sim_fingerprint")

    # pylint: disable=unused-argument
    def compile(
        self, query: Dict, postprocess_actions: PostprocessType = None
    ) -> None:
        bool_head = head_by_path(
            query, ("query", "script_score", "query", "bool")
        )
        if not bool_head.get("should"):
            bool_head["should"] = []
        bool_head["should"] += self.clauses()
        bool_head["minimum_should_match"] = self.min_should_match(
            len(self.clauses())
        )

        script_score_head = head_by_path(query, ("query", "script_score"))
        script_score_head["script"] = self.script
        query["min_score"] = self._threshold

    @abstractmethod
    def min_should_match(self, length: int):
        pass

    @property
    @abstractmethod
    def script(self) -> Dict:
        pass


class TanimotoSimilarityMatch(BaseMatch):
    @property
    def target(self) -> IndigoRecord:
        return self._target

    @property
    def script(self) -> Dict:
        assert self._target.sim_fingerprint
        return {
            "source": "_score / (params.a + "
            "doc['sim_fingerprint_len'].value - _score)",
            "params": {"a": len(self._target.sim_fingerprint)},
        }

    def min_should_match(self, length: int) -> str:
        assert self.target.sim_fingerprint
        min_match = (
            math.floor(
                (self._threshold * (len(self.target.sim_fingerprint) + 1))
                / (1.0 + self._threshold)
            )
            / length
        )

        return f"{int(min_match * 100)}%"


class EuclidSimilarityMatch(BaseMatch):
    @property
    def script(self) -> Dict:
        assert self._target.sim_fingerprint
        return {
            "source": "_score / params.a",
            "params": {"a": len(self._target.sim_fingerprint)},
        }

    def min_should_match(self, length: int):
        assert self._target.sim_fingerprint
        min_match = (
            math.floor(self._threshold * len(self._target.sim_fingerprint))
        ) / length

        return f"{int(min_match * 100)}%"


class TverskySimilarityMatch(BaseMatch):
    def __init__(
        self,
        target: IndigoRecord,
        threshold: float,
        alpha: float = 0.5,
        beta: float = 0.5,
    ):
        super().__init__(target, threshold)
        self._alpha = alpha
        self._beta = beta

    @property
    def script(self) -> Dict:
        assert self._target.sim_fingerprint
        return {
            "source": "_score / ((params.a - _score) * "
            "params.alpha + (doc['sim_fingerprint_len'].value - "
            "_score) * params.beta + _score)",
            "params": {
                "a": len(self._target.sim_fingerprint),
                "alpha": self._alpha,
                "beta": self._beta,
            },
        }

    def min_should_match(self, length: int) -> str:
        assert self._target.sim_fingerprint
        top = self._alpha * len(self._target.sim_fingerprint) + self._beta
        down = self._threshold + self._alpha + self._beta - 1.0
        min_match = math.floor((top / down)) / length
        return f"{int(min_match * 100)}%"


class ExactMatch(CompilableQuery):
    def __init__(self, target):
        self._target = target

    @lru_cache(maxsize=None)
    def clauses(self) -> List[Dict]:
        return clauses(self._target.sub_fingerprint, "sub_fingerprint")

    # pylint: disable=inconsistent-return-statements
    def postprocess(
        self, record: IndigoRecord, indigo: Indigo
    ) -> Optional[IndigoRecord]:

        # postprocess only on molecule search
        if not isinstance(record, IndigoRecordMolecule):
            return record

        if indigo.substructureMatcher(record.as_indigo_object(indigo)).match(
            indigo.loadQueryMolecule(
                self._target.as_indigo_object(indigo).canonicalSmiles()
            )
        ):
            return record
        return None

    def compile(
        self, query, postprocess_actions: PostprocessType = None
    ) -> None:
        bool_head = head_by_path(
            query, ("query", "script_score", "query", "bool")
        )
        if not bool_head.get("must"):
            bool_head["must"] = []
        bool_head["must"] += self.clauses()
        script_score_head = head_by_path(query, ("query", "script_score"))
        script_score_head["script"] = {
            "source": "_score / doc['sub_fingerprint_len'].value"
        }
        query["min_score"] = 1
        assert postprocess_actions is not None
        postprocess_actions.append(getattr(self, "postprocess"))


# Alias to default similarity match
SimilarityMatch = TanimotoSimilarityMatch


def query_factory(key: str, value: Any) -> CompilableQuery:
    if key == "exact":
        return ExactMatch(value)
    if key == "substructure":
        return SubstructureQuery(key, value)
    if isinstance(value, CompilableQuery):
        value.field = key
        return value
    if isinstance(value, str):
        value = KeywordQuery(value)
        value.field = key
        return value

    raise AttributeError(
        f"Unsupported request with key: {key}, value: {value}",
    )
