from auctionlab.reality.candle import Candle
from auctionlab.research.experiments.observation import Observation


class ExcursionTracker:

    def __init__(
        self,
        observation: Observation,
    ):
        self._entry = observation.current_price
        self._is_long = (
            observation.nearest_objective.price >= observation.current_price
        )

        self.maximum_favorable_excursion = 0.0
        self.maximum_adverse_excursion = 0.0

    def update(
        self,
        candle: Candle,
    ) -> None:

        if self._is_long:

            favorable = candle.high - self._entry
            adverse = candle.low - self._entry

        else:

            favorable = self._entry - candle.low
            adverse = self._entry - candle.high

        if favorable > self.maximum_favorable_excursion:
            self.maximum_favorable_excursion = favorable

        if adverse < self.maximum_adverse_excursion:
            self.maximum_adverse_excursion = adverse