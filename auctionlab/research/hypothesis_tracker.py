from auctionlab.research.hypothesis import Hypothesis


class HypothesisTracker:

    def __init__(self):
        self._hypotheses: list[Hypothesis] = []

    def add(
        self,
        hypothesis: Hypothesis,
    ) -> None:

        self._hypotheses.append(hypothesis)

    @property
    def hypotheses(self) -> tuple[Hypothesis, ...]:
        return tuple(self._hypotheses)

    def __len__(self) -> int:
        return len(self._hypotheses)