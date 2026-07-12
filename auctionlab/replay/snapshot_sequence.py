from __future__ import annotations

from auctionlab.observation.market_snapshot import MarketSnapshot


class SnapshotSequence:

    def __init__(self):
        self._snapshots: list[MarketSnapshot] = []

    def add(self, snapshot: MarketSnapshot) -> None:
        self._snapshots.append(snapshot)

    def __len__(self) -> int:
        return len(self._snapshots)

    def __iter__(self):
        return iter(self._snapshots)

    def latest(self) -> MarketSnapshot | None:
        if not self._snapshots:
            return None

        return self._snapshots[-1]