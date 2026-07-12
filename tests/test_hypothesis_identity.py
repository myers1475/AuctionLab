from auctionlab.research.hypothesis_builder import build_hypothesis


def test_hypotheses_have_unique_ids():

    first = build_hypothesis(
        "A",
        "B",
        "C",
    )

    second = build_hypothesis(
        "A",
        "B",
        "C",
    )

    assert first.id != second.id