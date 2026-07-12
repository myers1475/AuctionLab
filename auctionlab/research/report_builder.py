from auctionlab.research.research_report import ResearchReport
from auctionlab.research.research_session import ResearchSession


def build_report(session: ResearchSession) -> ResearchReport:

    return ResearchReport(
        active=len(session.active),
        completed=len(session.completed),
    )