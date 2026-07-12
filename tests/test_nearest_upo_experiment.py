from auctionlab.research.nearest_upo_experiment import (
    NearestUPOExperiment,
)


def test_experiment():

    experiment = NearestUPOExperiment(
        target_name="PDH",
        target_price=25410,
    )

    assert experiment.target_name == "PDH"
    assert experiment.reached is False