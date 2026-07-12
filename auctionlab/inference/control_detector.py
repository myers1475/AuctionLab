from auctionlab.inference.control import Control


def detect_control(
    bullish_ifvgs: int,
    bearish_ifvgs: int,
) -> Control:
    if bullish_ifvgs > bearish_ifvgs:
        return Control.BULLISH

    if bearish_ifvgs > bullish_ifvgs:
        return Control.BEARISH

    return Control.NEUTRAL