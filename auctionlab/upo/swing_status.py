from auctionlab.observation.swing import Swing
from auctionlab.upo.upo import UPOStatus


def swing_status(
    swing: Swing,
    current_high: float,
    current_low: float,
) -> UPOStatus:
    if swing.is_high:
        if current_high > swing.candle.high:
            return UPOStatus.COMPLETED
    else:
        if current_low < swing.candle.low:
            return UPOStatus.COMPLETED

    return UPOStatus.ACTIVE