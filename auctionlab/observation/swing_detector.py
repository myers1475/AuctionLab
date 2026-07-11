from auctionlab.observation.swing import Swing
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.window_iterator import windows


def detect_swings(bars: BarSeries) -> list[Swing]:
    swings: list[Swing] = []

    for index, window in enumerate(windows(bars), start=1):
        if (
            window.current.high > window.previous.high
            and window.current.high > window.next.high
        ):
            swings.append(
                Swing(
                    timestamp=window.current.timestamp,
                    name="Swing High",
                    candle=window.current,
                    index=index,
                    is_high=True,
                )
            )

        if (
            window.current.low < window.previous.low
            and window.current.low < window.next.low
        ):
            swings.append(
                Swing(
                    timestamp=window.current.timestamp,
                    name="Swing Low",
                    candle=window.current,
                    index=index,
                    is_high=False,
                )
            )

    return swings