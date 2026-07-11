from auctionlab.observation.trading_session import TradingSession
from auctionlab.upo.session_levels import SessionLevels


def detect_session_levels(session: TradingSession) -> SessionLevels:
    return SessionLevels(
        session=session.name,
        high=session.high,
        low=session.low,
    )