import pytest
from strings_to_positions import to_strings


@pytest.mark.parametrize(
    "source_text, offsets, expected",
    [
        ("abc", [(0, 1), (1, 2), (2, 3)], ["a", "b", "c"]),
        ("abc", [(0, 1), (1, 2), (2, 3), None], ["a", "b", "c", None]),
        (
            "abc",
            [(0, 1), (1, 2), (2, 3), None],
            ["a", "b", "c", None],
        ),
        (
            "abc",
            [(0, 1), (1, 2), (2, 3), None],
            ["a", "b", "c", None],
        ),
        (
            "abcdef",
            [(0, 2), (1, 3), (2, 4), (3, 5)],
            ["ab", "bc", "cd", "de"],
        ),
        (
            "abcdef",
            [(0, 2), None, (2, 4), None],
            ["ab", None, "cd", None],
        ),
    ],
)
def test_naive_basic(source_text, offsets, expected):
    """Test conversion for typical alphabetic strings, including uppercase mix."""
    result = to_strings(source_text, offsets)
    assert result == expected


def test_naive_sequence(
    markdown_source, seq_chunk_1, seq_chunk_2, seq_chunk_3, seq_offsets
):
    """Test conversion for a long text with multiple chunks."""
    result = to_strings(markdown_source, seq_offsets)
    assert result == [seq_chunk_1, seq_chunk_2, seq_chunk_3]


def test_naive_overlap(
    markdown_source,
    overlap_chunk_1,
    overlap_chunk_2,
    overlap_chunk_3,
    overlap_chunk_4,
    overlap_offsets,
):
    """Test conversion for a long text with overlapping chunks."""
    result = to_strings(
        markdown_source,
        overlap_offsets,
    )
    assert result == [
        overlap_chunk_1,
        overlap_chunk_2,
        overlap_chunk_3,
        overlap_chunk_4,
    ]


def test_overlap_size(overlap_size_document, overlap_size_chunks, overlap_size_offsets):
    """Test conversion for a long text with overlapping chunks."""
    result = to_strings(overlap_size_document, overlap_size_offsets)
    assert result == overlap_size_chunks
