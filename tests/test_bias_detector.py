from auctionlab.inference.bias_detector import detect_bias
from auctionlab.inference.control import Control
from auctionlab.inference.market_bias import MarketBias
from auctionlab.inference.objective_direction import ObjectiveDirection


def test_bullish_bias():

    bias = detect_bias(
        Control.BULLISH,
        ObjectiveDirection.ABOVE,
    )

    assert bias == MarketBias.BULLISH


def test_bearish_bias():

    bias = detect_bias(
        Control.BEARISH,
        ObjectiveDirection.BELOW,
    )

    assert bias == MarketBias.BEARISH


def test_neutral_bias():

    bias = detect_bias(
        Control.BULLISH,
        ObjectiveDirection.BELOW,
    )

    assert bias == MarketBias.NEUTRAL