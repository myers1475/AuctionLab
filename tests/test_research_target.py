from auctionlab.research.direction import Direction
from auctionlab.research.research_target import ResearchTarget
from auctionlab.research.target_type import TargetType


def test_research_target():

    target = ResearchTarget(
        direction=Direction.LONG,
        target_type=TargetType.PREVIOUS_DAY_HIGH,
        price=25410.0,
    )

    assert target.direction == Direction.LONG
    assert target.target_type == TargetType.PREVIOUS_DAY_HIGH
    assert target.price == 25410.0