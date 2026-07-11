from auctionlab.io.csv_loader import load_csv


def test_load_csv():
    bars = load_csv("data/Futures/NQ/5m/2025-12_to_2026-07.csv")

    assert len(bars) > 0

    first = bars[0]

    assert first.open > 0
    assert first.high >= first.low