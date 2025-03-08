import logging
import timeit
from typing import Protocol

import datasets
import evaluate
import jiwer
import polars as pl
import universal_edit_distance as ued
from rich.logging import RichHandler
from importlib.metadata import version

_logger = logging.getLogger(__name__)

MIN_TIME_PER_TEST = 2.0


class Library(Protocol):
    def test_wmer(self, df: pl.DataFrame) -> None: ...
    def test_cmer(self, df: pl.DataFrame) -> None: ...
    def test_wer(self, df: pl.DataFrame) -> None: ...
    def test_cer(self, df: pl.DataFrame) -> None: ...


def main() -> None:
    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler()],
    )
    _logger.info("Hello from ued-benchmarks!")
    _logger.info(
        f"evaluate={version('evaluate')} "
        f"jiwer={version('jiwer')} "
        f"ued={version('universal-edit-distance')} "
    )
    libraries: dict[str, Library] = {
        "Evaluate": Evaluate(),
        "JiWER": JiWER(),
        "UED": UED(),
    }

    df = load_dataset()
    _logger.info(f"Length of dataset {len(df):,}")

    summary = pl.DataFrame(
        [test_library(name, library, df) for name, library in libraries.items()]
    )
    _logger.info(summary)
    metrics = summary.transpose(
        include_header=True, header_name="metric", column_names="library"
    ).with_columns(
        (pl.col("Evaluate") / pl.col("UED")).alias("Speed-up vs Evaluate"),
        (pl.col("JiWER") / pl.col("UED")).alias("Speed-up vs JiWER"),
    )
    _logger.info(metrics)


def test_library(name: str, library: Library, df: pl.DataFrame) -> dict:
    _logger.info(f"Testing library: {name}")
    return {
        "library": name,
        "wmer": auto_timeit(lambda: library.test_wmer(df)),
        "cmer": auto_timeit(lambda: library.test_cmer(df)),
        "wer": auto_timeit(lambda: library.test_wer(df)),
        "cer": auto_timeit(lambda: library.test_cer(df)),
    }


def auto_timeit(stmt="pass", setup="pass"):
    n = 1
    t = timeit.timeit(stmt, setup, number=n)

    while t < MIN_TIME_PER_TEST:
        n *= 10
        t = timeit.timeit(stmt, setup, number=n)

    return t / n  # normalise to time-per-run


def load_dataset() -> pl.DataFrame:
    return (
        datasets.load_dataset("prvInSpace/eval-kaldi-full-model", split="test")
        .select_columns(["sentence", "transcription"])
        .to_polars()
        .with_columns(
            pl.col("sentence").str.strip_chars(),
            pl.col("transcription").str.strip_chars(),
        )
        .filter(pl.col("sentence").str.len_chars() >= 1)
        .drop_nulls()
    )


class Evaluate(Library):
    def __init__(self):
        self._wer = evaluate.load("wer")
        self._cer = evaluate.load("cer")

    def test_wmer(self, df: pl.DataFrame) -> None:
        self._wer.compute(predictions=df["transcription"], references=df["sentence"])

    def test_cmer(self, df: pl.DataFrame) -> None:
        self._cer.compute(predictions=df["transcription"], references=df["sentence"])

    def test_wer(self, df: pl.DataFrame) -> None:
        df.with_columns_seq(
            pl.struct(["transcription", "sentence"]).map_elements(
                lambda row: self._wer.compute(
                    predictions=[row["transcription"]], references=[row["sentence"]]
                ),
                pl.Float64,
            )
        )

    def test_cer(self, df: pl.DataFrame) -> None:
        df.with_columns_seq(
            pl.struct(["transcription", "sentence"]).map_elements(
                lambda row: self._cer.compute(
                    predictions=[row["transcription"]], references=[row["sentence"]]
                ),
                pl.Float64,
            )
        )


class JiWER(Library):
    def test_wmer(self, df: pl.DataFrame) -> None:
        jiwer.wer(df["sentence"].to_list(), df["transcription"].to_list())

    def test_cmer(self, df: pl.DataFrame) -> None:
        jiwer.cer(df["sentence"].to_list(), df["transcription"].to_list())

    def test_wer(self, df: pl.DataFrame) -> None:
        # For some reason this crashes if we set the return type to float
        # Since object can be anything we're basically ignoring the return type
        df.with_columns(
            pl.struct(["sentence", "transcription"]).map_elements(
                lambda row: jiwer.wer(row["sentence"], row["transcription"]), pl.Object
            )
        )
        df

    def test_cer(self, df: pl.DataFrame) -> None:
        # For some reason this crashes if we set the return type to float
        # Since object can be anything we're basically ignoring the return type
        df.with_columns(
            pl.struct(["sentence", "transcription"]).map_elements(
                lambda row: jiwer.cer(row["sentence"], row["transcription"]), pl.Object
            )
        )


class UED(Library):
    def test_wmer(self, df: pl.DataFrame) -> None:
        ued.word_mean_error_rate(
            predictions=df["transcription"], references=df["sentence"]
        )

    def test_cmer(self, df: pl.DataFrame) -> None:
        ued.character_mean_error_rate(
            predictions=df["transcription"], references=df["sentence"]
        )

    def test_wer(self, df: pl.DataFrame) -> None:
        ued.word_error_rate(predictions=df["transcription"], references=df["sentence"])

    def test_cer(self, df: pl.DataFrame) -> None:
        ued.character_error_rate(
            predictions=df["transcription"], references=df["sentence"]
        )

if __name__ == "__main__":
    main()

