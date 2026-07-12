from auctionlab.observation.swing import Swing
from auctionlab.reality.bar_series import BarSeries
from auctionlab.research.atr import atr14


def detect_swings(
    bars: BarSeries,
    atr_multiple: float = 0.5,
) -> list[Swing]:

    atr_values = atr14(bars)

    swings: list[Swing] = []

    last_confirmed_high: Swing | None = None
    last_confirmed_low: Swing | None = None

    for index in range(2, len(bars) - 2):

        current = bars[index]

        atr = atr_values[index]

        if atr is None:
            continue

        is_high = (
            current.high > bars[index - 1].high
            and current.high > bars[index - 2].high
            and current.high > bars[index + 1].high
            and current.high > bars[index + 2].high
        )

        is_low = (
            current.low < bars[index - 1].low
            and current.low < bars[index - 2].low
            and current.low < bars[index + 1].low
            and current.low < bars[index + 2].low
        )

        if is_high:

            if (
                last_confirmed_low is not None
                and (
                    current.high
                    - last_confirmed_low.candle.low
                ) < atr_multiple * atr
            ):
                continue

            swing = Swing(
                timestamp=current.timestamp,
                name="Swing High",
                candle=current,
                index=index,
                is_high=True,
            )

            swings.append(swing)
            last_confirmed_high = swing

        if is_low:

            if (
                last_confirmed_high is not None
                and (
                    last_confirmed_high.candle.high
                    - current.low
                ) < atr_multiple * atr
            ):
                continue

            swing = Swing(
                timestamp=current.timestamp,
                name="Swing Low",
                candle=current,
                index=index,
                is_high=False,
            )

            swings.append(swing)
            last_confirmed_low = swing

    return swings