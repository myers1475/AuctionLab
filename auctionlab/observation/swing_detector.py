from auctionlab.observation.swing import Swing
from auctionlab.reality.bar_series import BarSeries


def detect_two_bar_swings(bars: BarSeries) -> list[Swing]:
    swings: list[Swing] = []

    for i in range(1, len(bars) - 1):
        prev = bars[i - 1]
        cur = bars[i]
        nxt = bars[i + 1]

        if cur.high > prev.high and cur.high > nxt.high:
            swings.append(Swing(cur, i, True))

        if cur.low < prev.low and cur.low < nxt.low:
            swings.append(Swing(cur, i, False))

    return swings