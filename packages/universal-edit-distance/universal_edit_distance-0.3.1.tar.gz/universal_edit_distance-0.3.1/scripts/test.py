from universal_edit_distance import (
    word_error_rate,
    word_mean_error_rate,
    word_edit_distance,
    universal_error_rate,
    universal_edit_distance,
    character_error_rate,
    character_edit_distance,
    character_mean_error_rate,
)


from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


assert Point(1, 2) == Point(1, 2)


class Test:
    def __init__(self, a):
        self.a = a


list1 = [Point(1, 2), Point(3, 2), ["hello"], Point(5, 4), Test(2)]
list2 = [Point(1, 2), Point(3, 2), Point(2, 3)]


print(universal_edit_distance([list1], [list2]))


list1 = [Test(1), Test(2), Test(3)]
list2 = [Test(1), Test(2), Test(3), Test(4)]

# list1 = ["hello", "world", 0]
# list2 = ["hello", 0, Test(2), Test(3)]

for item1, item2 in zip(list1, list2):
    assert item1 != item2

print(universal_edit_distance([list1], [list2]))

exit(0)

test1 = ["hello", "world"]
test2 = ["helo", "world"]

print(word_error_rate(["hello world"], ["helo world"]))
print(universal_error_rate([["hello", "world"]], [["helo", "world"]]))

test1a = [c for c in " ".join(test1)]
test2a = [c for c in " ".join(test2)]
print(
    universal_error_rate(
        [test1a, test2a],
        [test2a, test1a],
    )
)


import polars as pl

df = pl.read_csv("full.csv")
print(df)


def calculate_wer() -> pl.Series:
    results = pl.Series(
        "wer",
        word_error_rate(
            df["normalised"].to_list(),
            df["transcription"].to_list(),
        ),
    )
    return results


def calculate_cer() -> pl.Series:
    results = pl.Series(
        "cer",
        character_error_rate(
            df["normalised"].to_list(),
            df["transcription"].to_list(),
        ),
    )
    return results


def calculate_ced() -> pl.Series:
    return pl.Series(
        "ced",
        character_edit_distance(
            df["normalised"].to_list(),
            df["transcription"].to_list(),
        ),
    )


df = df.with_columns(calculate_wer(), calculate_cer(), calculate_ced())

print(df)
total_chars = df["normalised"].str.len_chars().sum()
wrong = df["ced"].sum()
print(f"{total_chars:,} {wrong:,} CER: {wrong / total_chars:.2%}")

print(character_mean_error_rate(df["transcription"], df["normalised"]))
