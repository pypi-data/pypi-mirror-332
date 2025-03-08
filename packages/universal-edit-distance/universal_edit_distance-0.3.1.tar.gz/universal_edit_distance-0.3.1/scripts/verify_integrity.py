import polars as pl
import datasets
from universal_edit_distance import (
    character_edit_distance,
    character_error_rate,
    character_mean_error_rate,
)

import evaluate
import jiwer
import logging
from rich.logging import RichHandler
from text_process.normalise import cleanup_spaces

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()],
)
_logger = logging.getLogger(__name__)
cer = evaluate.load("cer")


def main() -> None:
    df = load_dataset()
    _logger.info(f"Length of dataset: {len(df):,}")
    df = df.filter(pl.col("transcription").str.len_chars() >= 1)
    verify_mean_error_rate(df)


def verify_mean_error_rate(df: pl.DataFrame) -> None:
    evaluate_res = cer.compute(
        predictions=df["transcription"], references=df["sentence"]
    )
    jiwer_res = jiwer.cer(df["sentence"].to_list(), df["transcription"].to_list())
    ued_res = character_mean_error_rate(df["transcription"], df["sentence"])

    print(f"Evaluate: {evaluate_res}")
    print(f"JiWER:    {jiwer_res}")
    print(f"UED:      {ued_res}")


def load_dataset() -> pl.DataFrame:
    return (
        datasets.load_dataset("prvInSpace/eval-kaldi-full-model", split="test")
        .select_columns(["sentence", "transcription"])
        .to_polars()
        .with_columns(
            pl.col("sentence")
            .str.strip_chars()
            .map_elements(cleanup_spaces, pl.String),
            pl.col("transcription")
            .str.strip_chars()
            .map_elements(cleanup_spaces, pl.String),
        )
        .filter(pl.col("sentence").str.len_chars() >= 1)
    )


if __name__ == "__main__":
    main()
