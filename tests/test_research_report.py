from auctionlab.research.report_builder import build_report
from auctionlab.research.research_session import ResearchSession


def test_report():

    session = ResearchSession()

    report = build_report(session)

    assert report.active == 0
    assert report.completed == 0
    assert report.total == 0