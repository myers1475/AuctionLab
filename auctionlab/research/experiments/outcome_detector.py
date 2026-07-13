from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.outcome import Outcome


def detect_outcome(
    observation: Observation,
):
    nearest = observation.nearest_objective

    if nearest is None:
        return None

    return Outcome(
        observation_time=observation.timestamp,
        outcome_time=None,
        target_kind=nearest.kind,
        target_price=nearest.price,
        reached=False,
        bars_to_outcome=None,
        maximum_favorable_excursion=None,
        maximum_adverse_excursion=None,
        distance_to_target=None,
        percent_to_target=None,
    )