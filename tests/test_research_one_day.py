from auctionlab.research.research_session import ResearchSession


def test_research_session_starts_empty():

    session = ResearchSession()

    assert len(session.active) == 0
    assert len(session.completed) == 0