from auctionlab.observation.swing import Swing
from auctionlab.reality.bar_series import BarSeries


def detect_swings(bars: BarSeries) -> list[Swing]:
    swings: list[Swing] = []

    for index in range(2, len(bars) - 2):

        current = bars[index]

        if (
            current.high > bars[index - 1].high
            and current.high > bars[index - 2].high
            and current.high > bars[index + 1].high
            and current.high > bars[index + 2].high
        ):
            swings.append(
                Swing(
                    timestamp=current.timestamp,
                    name="Swing High",
                    candle=current,
                    index=index,
                    is_high=True,
                )
            )

        if (
            current.low < bars[index - 1].low
            and current.low < bars[index - 2].low
            and current.low < bars[index + 1].low
            and current.low < bars[index + 2].low
        ):
            swings.append(
                Swing(
                    timestamp=current.timestamp,
                    name="Swing Low",
                    candle=current,
                    index=index,
                    is_high=False,
                )
            )

    return swings