from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.objective_builder import build_objectives

from auctionlab.observation.swing import Swing
from auctionlab.reality.candle import Candle

from auctionlab.upo.previous_day import PreviousDay
from auctionlab.upo.previous_week import PreviousWeek
from auctionlab.upo.upo import UPOStatus


def test_build_objectives():

    swing = Swing(
        timestamp=None,
        name="Swing High",
        candle=Candle(
            timestamp=None,
            open=100,
            high=110,
            low=95,
            close=105,
            volume=None,
        ),
        index=0,
        is_high=True,
    )

    objectives = build_objectives(
        ActiveUPOs(
            swings=(swing,),
            previous_days=(
                PreviousDay(
                    high=120,
                    low=80,
                    status=UPOStatus.ACTIVE,
                ),
            ),
            previous_weeks=(
                PreviousWeek(
                    high=130,
                    low=70,
                ),
            ),
            fvgs=(),
            ifvgs=(),
        )
    )

    assert len(objectives) == 5

    assert objectives[0].kind == "Swing High"
    assert objectives[1].kind == "Previous Day High"
    assert objectives[2].kind == "Previous Day Low"
    assert objectives[3].kind == "Previous Week High"
    assert objectives[4].kind == "Previous Week Low"