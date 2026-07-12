from auctionlab.research.experiments.observation import Observation


class ObservationLog:

    def __init__(self):
        self._observations: list[Observation] = []

    def add(
        self,
        observation: Observation,
    ) -> None:

        self._observations.append(observation)

    @property
    def observations(self) -> tuple[Observation, ...]:
        return tuple(self._observations)

    def __len__(self) -> int:
        return len(self._observations)