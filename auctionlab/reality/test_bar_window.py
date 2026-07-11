from datetime import datetime

from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.bar_window import BarWindow
from auctionlab.reality.candle import Candle
from auctionlab.reality.window_iterator import windows


def make(price: float) -> Candle:
    return Candle(
        timestamp=datetime.now(),
        open=price,
        high=price,
        low=price,
        close=price,
    )


def test_windows():
    bars = BarSeries(
        [
            make(1),
            make(2),
            make(3),
            make(4),
        ]
    )

    result = list(windows(bars))

    assert len(result) == 2

    first = result[0]

    assert isinstance(first, BarWindow)
    assert first.previous.open == 1
    assert first.current.open == 2
    assert first.next.open == 3