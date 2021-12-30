"""Tools for accessing text metrics etc.
"""

# import logging
import unicodedata
from glob import glob

import numpy as np
import spacy
from spacy_syllables import SpacySyllables
import logging


def replace_quotes(s: str) -> str:
    """replace dificult characters"""
    return s.translate(str.maketrans("‘’“”", "''\"\""))


def replace_accented_letters(s: str) -> str:
    """replace accented letters with their ascii counterpart"""
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode("utf-8")


def init_nlp(language: str = "es"):
    """Initialize the NLP pipeline"""

    if language == "en":
        # nlp = spacy.load("en_core_web1_trf")
        _nlp = spacy.load("en_core_web_lg")
    elif language in ["de", "es", "fr"]:
        # nlp = spacy.load(f"{language}_dep_news_trf")
        _nlp = spacy.load(f"{language}_core_news_lg")
    else:
        raise NotImplementedError(f"{language} is not (yet) supported")
    # spacy_stopwords = eval(f"spacy.lang.{language}.stop_words.STOP_WORDS")

    _nlp.add_pipe("syllables", after="morphologizer", config={"lang": language})

    return _nlp


def get_bag_of_words(doc: spacy.tokens.doc.Doc) -> tuple[set]:
    """generate a bag of normalized words from text"""

    # without_stopwords = {word.text for word in doc if word.is_alpha and not word.is_stop}
    normalized_bow = sorted(
        {
            word.lemma_.lower()
            for word in doc
            if word.is_alpha and not word.is_stop and len(word) > 1
        }
    )
    places = sorted(
        {word.text.title() for word in doc.ents if word.label_ in ["GPE", "LOC"]}
    )
    people = sorted({word.text.title() for word in doc.ents if word.label_ == "PER"})
    orgs = sorted({word.text for word in doc.ents if word.label_ == "ORG"})

    # add GPEs from files
    gpes_from_files = []
    for f in glob("monito/gpe_*.txt"):
        with open(f) as fp:
            gpes_from_files += [line.strip() for line in fp.readlines()]

    gpes_from_files = set(gpes_from_files)

    found_gpes = [
        word.title()
        for word in normalized_bow
        if word.lower() in map(str.lower, gpes_from_files)
    ]
    places = sorted(set(places + found_gpes))

    # fix some frequent errors
    if "Mich." in people:
        people.remove("Mich.")
        places = sorted(set(places + ["Michoacán"]))

    if "MORELIA" in orgs:
        orgs.remove("MORELIA")
        places = sorted(set(places + ["Morelia"]))

    for p in people.copy():
        if "\n" in p:
            people.remove(p)
            people = sorted(set(people + [p.split("\n")[0]]))

    for p1 in people.copy():
        for p2 in people.copy():
            if p1 != p2 and p2.startswith(p1) and p1 in people:
                people.remove(p1)

    for p in places.copy():
        if "\n" in p:
            places.remove(p)
            places = sorted(set(places + [p.split("\n")[0]]))


    # print(text)
    # print(without_stopwords)
    # print(normalized_bow)
    # print(places)
    # print(people)
    # for ent in doc.ents:
    #     print(ent.text, ent.label_)
    # sys.exit(999)

    return normalized_bow, places, people, orgs


def process_article_text(article_dict: dict, config: dict) -> None:
    """analyse the article text and add the information to the article dict"""
    if "text" not in article_dict:
        logging.warning("no text found")
        return
    if len(article_dict["text"]) < 100:
        logging.warning("found very short text")
        return

    article_dict["text"] = article_dict["text"].replace("\n\n", "\n")

    # initialize nlp
    nlp = init_nlp(config["locale"][:2])
    text_doc = nlp(article_dict["text"])

    # get bag of words
    (
        article_dict["bag_of_words"],
        article_dict["places"],
        article_dict["people"],
        article_dict["orgs"],
    ) = get_bag_of_words(text_doc)

    # get legibility and stats
    article_dict["legibility"] = legibility_es(text_doc)

    article_dict["stats"] = {}
    article_dict["stats"]["n_characters"] = len(article_dict["text"])
    article_dict["stats"]["n_letters"] = count_letters(text_doc)
    article_dict["stats"]["n_syllables"] = count_syllables(text_doc)
    article_dict["stats"]["n_words"] = count_words(text_doc)
    article_dict["stats"]["n_sentences"] = count_sentences(text_doc)
    article_dict["stats"]["n_bag_of_words"] = len(article_dict["bag_of_words"])


def sanitize_filename(s: str) -> str:
    """replace characters that should not be in a filename"""

    return s.translate(
        str.maketrans("áéíóúñÁÉÍÓÚÑü", "aeiounAEIOUNu", ",\"'“”|.;/‘’?¿!¡&")
    )


def count_syllables(doc: spacy.tokens.doc.Doc) -> int:
    """Count syllables in text"""
    # logging.debug(str([(token.text, token._.syllables_count) for token in doc if not token.is_punct]))
    return sum(
        token._.syllables_count
        for token in doc
        if not token.is_punct and token._.syllables_count is not None
    )


def count_letters(doc: spacy.tokens.doc.Doc) -> int:
    """Count letters in text"""
    return sum(len(word) for word in doc if not word.is_punct)


def count_words(doc: spacy.tokens.doc.Doc) -> int:
    """Count words in text"""
    return len(list(word for word in doc if not word.is_punct))


def count_sentences(doc: spacy.tokens.doc.Doc) -> int:
    """Count sentences in text"""
    return len(list(doc.sents))


def legibility_es(doc: spacy.tokens.doc.Doc) -> dict:
    """Get legibility measures for Spanish text"""
    result = {}

    n_letters = count_letters(doc)
    n_syllables = count_syllables(doc)
    n_words = count_words(doc)
    n_sentences = count_sentences(doc)
    result["FH"] = result["Fernández Huerta"] = round(
        206.84 - 60 * n_syllables / n_words - 102 * n_sentences / n_words, 1
    )
    result["SP"] = result["Szigriszt-Pazos"] = round(
        206.835 - 62.3 * n_syllables / n_words - n_words / n_sentences, 1
    )
    letters_per_word = [len(word) for word in doc if not word.is_punct]
    result["mu"] = round(
        n_words
        / (n_words - 1)
        * (n_letters / n_words)
        / np.var(letters_per_word)
        * 100,
        1,
    )

    return result


if __name__ == "__main__":

    nlp = spacy.load("es_core_news_lg")
    nlp.add_pipe("syllables", after="morphologizer", config={"lang": "es"})

    assert count_letters(nlp("Esto es un texto.")) == 13
    assert count_syllables(nlp("Esto es un texto.")) == 6
    assert count_words(nlp("Esto es un texto.")) == 4
    assert count_sentences(nlp("Esto es un texto. Y esto es otro.")) == 2

    print(legibility_es(nlp("Esto es un texto muy simple.")))

    long_text = nlp(
        "Tomando en cuenta la complejidad del vocabulario,"
        " esto se podría considerar un texto más complicado y menos legible."
    )

    print(
        count_letters(long_text),
        count_syllables(long_text),
        count_words(long_text),
        count_sentences(long_text),
    )
    print(legibility_es(nlp(long_text)))
