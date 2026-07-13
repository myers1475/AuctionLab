from auctionlab.research.experiments.observation import Observation


class ExcursionTracker:

    def __init__(
        self,
        observation: Observation,
    ):
        self._entry = observation.current_price

        self.maximum_favorable_excursion = 0.0
        self.maximum_adverse_excursion = 0.0

    def update(
        self,
        price: float,
    ) -> None:

        move = price - self._entry

        if move > self.maximum_favorable_excursion:
            self.maximum_favorable_excursion = move

        if move < self.maximum_adverse_excursion:
            self.maximum_adverse_excursion = move