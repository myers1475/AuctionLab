from __future__ import annotations

from auctionlab.observation.market_snapshot import MarketSnapshot
from auctionlab.replay.snapshot_sequence import SnapshotSequence


class ReplayEngine:

    def __init__(self):
        self._sequence = SnapshotSequence()

    @property
    def snapshots(self) -> SnapshotSequence:
        return self._sequence

    def process(self, snapshot: MarketSnapshot) -> None:
        self._sequence.add(snapshot)