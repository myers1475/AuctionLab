from auctionlab.io.csv_loader import load_csv


def test_load_csv():
    bars = load_csv("data/CME_MINI_NQ1!, 5_33ece.csv")

    assert len(bars) > 0

    first = bars[0]

    assert first.open > 0
    assert first.high >= first.low