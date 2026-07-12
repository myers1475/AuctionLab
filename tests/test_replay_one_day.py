from auctionlab.replay.replay_engine import ReplayEngine


def test_replay_engine_starts_empty():
    engine = ReplayEngine()

    assert len(engine.snapshots) == 0