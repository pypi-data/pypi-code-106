from copy import deepcopy

from deepmerge import always_merger
from octadocs.types import Context


def merge(first: Context, second: Context) -> Context:
    """
    Merge two contexts into one.

    Second context can override the first.
    """
    return deepcopy(always_merger.merge(
        base=first,
        nxt=second,
    ))
