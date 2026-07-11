from auctionlab.observation.swing import Swing
from auctionlab.reality.bar_series import BarSeries


def detect_swings(bars: BarSeries) -> list[Swing]:
    swings: list[Swing] = []

    for i in range(1, len(bars) - 1):
        prev = bars[i - 1]
        cur = bars[i]
        nxt = bars[i + 1]

        if cur.high > prev.high and cur.high > nxt.high:
            swings.append(
                Swing(
                    timestamp=cur.timestamp,
                    name="Swing High",
                    candle=cur,
                    index=i,
                    is_high=True,
                )
            )

        if cur.low < prev.low and cur.low < nxt.low:
            swings.append(
                Swing(
                    timestamp=cur.timestamp,
                    name="Swing Low",
                    candle=cur,
                    index=i,
                    is_high=False,
                )
            )

    return swings