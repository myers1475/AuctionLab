from datetime import datetime, time

from auctionlab.sessions.session import Session


def session_for(timestamp: datetime) -> Session:
    current = timestamp.time()

    if time(18, 0) <= current <= time(23, 59, 59):
        return Session.GLOBEX

    if time(0, 0) <= current < time(9, 30):
        return Session.GLOBEX

    if time(9, 30) <= current < time(16, 15):
        return Session.RTH

    return Session.CLOSED