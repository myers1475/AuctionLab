from datetime import datetime

from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle

from auctionlab.research.nearest_upo_runner import target_reached


def test_target_reached():

    bars = BarSeries(
        [
            Candle(datetime.now(),100,101,99,100),
            Candle(datetime.now(),100,104,99,103),
            Candle(datetime.now(),103,111,102,110),
        ]
    )

    assert target_reached(
        bars,
        start_index=0,
        target_price=110,
    )


def test_target_not_reached():

    bars = BarSeries(
        [
            Candle(datetime.now(),100,101,99,100),
            Candle(datetime.now(),100,104,99,103),
            Candle(datetime.now(),103,109,102,108),
        ]
    )

    assert not target_reached(
        bars,
        start_index=0,
        target_price=110,
    )