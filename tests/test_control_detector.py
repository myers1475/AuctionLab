from auctionlab.inference.control import Control
from auctionlab.inference.control_detector import detect_control


def test_bullish_control():
    assert detect_control(3, 1) == Control.BULLISH


def test_bearish_control():
    assert detect_control(1, 3) == Control.BEARISH


def test_neutral_control():
    assert detect_control(2, 2) == Control.NEUTRAL