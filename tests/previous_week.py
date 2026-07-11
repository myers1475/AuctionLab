from auctionlab.upo.previous_week_builder import build_previous_week


def test_previous_week():
    pw = build_previous_week(
        high=22350.25,
        low=21987.75,
    )

    assert pw.high == 22350.25
    assert pw.low == 21987.75