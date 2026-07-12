from auctionlab.inference.bias_detector import detect_bias
from auctionlab.inference.control import Control
from auctionlab.inference.market_bias import MarketBias
from auctionlab.inference.nearest_objective import Objective


def test_bullish_bias():

    bias = detect_bias(
        Control.BULLISH,
        Objective(
            kind="Swing Low",
            price=100,
            source=None,
        ),
    )

    assert bias == MarketBias.BULLISH


def test_bearish_bias():

    bias = detect_bias(
        Control.BEARISH,
        Objective(
            kind="Swing High",
            price=100,
            source=None,
        ),
    )

    assert bias == MarketBias.BEARISH


def test_neutral_bias():

    bias = detect_bias(
        Control.BULLISH,
        Objective(
            kind="PDH",
            price=100,
            source=None,
        ),
    )

    assert bias == MarketBias.NEUTRAL