from auctionlab.research.active_hypothesis import ActiveHypothesis


class ActiveHypothesisManager:

    def __init__(self):
        self._active: list[ActiveHypothesis] = []

    def add(
        self,
        hypothesis: ActiveHypothesis,
    ) -> None:

        self._active.append(hypothesis)

    @property
    def active(self) -> tuple[ActiveHypothesis, ...]:
        return tuple(self._active)

    def __len__(self) -> int:
        return len(self._active)