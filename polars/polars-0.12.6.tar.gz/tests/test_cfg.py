import os
from typing import Generator

import pytest

import polars as pl


@pytest.fixture()
def environ() -> Generator:
    """Fixture to restore the environment variables after the test"""
    old_environ = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(old_environ)


def test_tables(environ: None) -> None:
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})

    pl.Config.set_ascii_tables()
    df_asci = str(df)
    assert (
        df_asci == "shape: (3, 3)\n"
        "+-----+-----+-----+\n"
        "| a   | b   | c   |\n"
        "| --- | --- | --- |\n"
        "| i64 | i64 | i64 |\n"
        "+=================+\n"
        "| 1   | 4   | 7   |\n"
        "|-----+-----+-----|\n"
        "| 2   | 5   | 8   |\n"
        "|-----+-----+-----|\n"
        "| 3   | 6   | 9   |\n"
        "+-----+-----+-----+"
    )

    pl.Config.set_utf8_tables()
    df_utf8 = str(df)
    assert (
        df_utf8 == "shape: (3, 3)\n"
        "┌─────┬─────┬─────┐\n"
        "│ a   ┆ b   ┆ c   │\n"
        "│ --- ┆ --- ┆ --- │\n"
        "│ i64 ┆ i64 ┆ i64 │\n"
        "╞═════╪═════╪═════╡\n"
        "│ 1   ┆ 4   ┆ 7   │\n"
        "├╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤\n"
        "│ 2   ┆ 5   ┆ 8   │\n"
        "├╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤\n"
        "│ 3   ┆ 6   ┆ 9   │\n"
        "└─────┴─────┴─────┘"
    )


def test_tbl_width_chars(environ: None) -> None:
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    pl.Config.set_tbl_width_chars(100)
    assert max(len(line) for line in str(df).split("\n")) == 19

    pl.Config.set_tbl_width_chars(15)
    assert max(len(line) for line in str(df).split("\n")) == 15

    # this will not squeezed below 13 characters, so 10 yields 13
    pl.Config.set_tbl_width_chars(10)
    assert max(len(line) for line in str(df).split("\n")) == 13


def test_tbl_cols(environ: None) -> None:
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})

    pl.Config.set_tbl_cols(1)
    assert str(df).split("\n")[2] == "│ a   ┆ ... │"
    pl.Config.set_tbl_cols(2)
    assert str(df).split("\n")[2] == "│ a   ┆ ... ┆ c   │"
    pl.Config.set_tbl_cols(3)
    assert str(df).split("\n")[2] == "│ a   ┆ b   ┆ c   │"


@pytest.mark.skip("not correctly implemented at the moment")
def test_set_tbl_rows(environ: None) -> None:
    # df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    pass
    #
    # pl.Config.set_tbl_rows(3)


def test_string_cache(environ: None) -> None:

    df1 = pl.DataFrame({"a": ["foo", "bar", "ham"], "b": [1, 2, 3]})
    df2 = pl.DataFrame({"a": ["foo", "spam", "eggs"], "c": [3, 2, 2]})

    # ensure cache is off when casting to categorical; the join will fail
    pl.Config.unset_global_string_cache()
    df1a = df1.with_column(pl.col("a").cast(pl.Categorical))
    df2a = df2.with_column(pl.col("a").cast(pl.Categorical))
    with pytest.raises(RuntimeError):
        _ = df1a.join(df2a, on="a", how="inner")

    # now turn on the cache
    pl.Config.set_global_string_cache()
    df1b = df1.with_column(pl.col("a").cast(pl.Categorical))
    df2b = df2.with_column(pl.col("a").cast(pl.Categorical))
    out = df1b.join(df2b, on="a", how="inner")
    assert out.frame_equal(pl.DataFrame({"a": ["foo"], "b": [1], "c": [3]}))

    # turn off again so we do not break other tests (TODO: environ fixture does not roll this back?)
    pl.Config.unset_global_string_cache()
