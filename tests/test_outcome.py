from auctionlab.research.experiments.outcome import Outcome


def test_efficiency():

    outcome = Outcome(
        observation_time=None,
        outcome_time=None,
        target_kind="PDH",
        target_price=110,
        reached=True,
        bars_to_outcome=5,
        maximum_favorable_excursion=15,
        maximum_adverse_excursion=-3,
        distance_to_target=10,
        percent_to_target=100,
    )

    assert outcome.efficiency == 1.5


def test_efficiency_none_when_no_distance():

    outcome = Outcome(
        observation_time=None,
        outcome_time=None,
        target_kind="PDH",
        target_price=110,
        reached=False,
        bars_to_outcome=None,
        maximum_favorable_excursion=5,
        maximum_adverse_excursion=-2,
        distance_to_target=0,
        percent_to_target=50,
    )

    assert outcome.efficiency is None


def test_efficiency_none_when_no_mfe():

    outcome = Outcome(
        observation_time=None,
        outcome_time=None,
        target_kind="PDH",
        target_price=110,
        reached=False,
        bars_to_outcome=None,
        maximum_favorable_excursion=None,
        maximum_adverse_excursion=None,
        distance_to_target=10,
        percent_to_target=50,
    )

    assert outcome.efficiency is None


def test_reward_risk():

    outcome = Outcome(
        observation_time=None,
        outcome_time=None,
        target_kind="PDH",
        target_price=110,
        reached=True,
        bars_to_outcome=5,
        maximum_favorable_excursion=15,
        maximum_adverse_excursion=-3,
        distance_to_target=10,
        percent_to_target=100,
    )

    assert outcome.reward_risk == 5.0


def test_reward_risk_none_when_no_mae():

    outcome = Outcome(
        observation_time=None,
        outcome_time=None,
        target_kind="PDH",
        target_price=110,
        reached=False,
        bars_to_outcome=None,
        maximum_favorable_excursion=10,
        maximum_adverse_excursion=None,
        distance_to_target=10,
        percent_to_target=50,
    )

    assert outcome.reward_risk is None


def test_reward_risk_none_when_zero_risk():

    outcome = Outcome(
        observation_time=None,
        outcome_time=None,
        target_kind="PDH",
        target_price=110,
        reached=False,
        bars_to_outcome=None,
        maximum_favorable_excursion=10,
        maximum_adverse_excursion=0,
        distance_to_target=10,
        percent_to_target=50,
    )

    assert outcome.reward_risk is None