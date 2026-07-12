from auctionlab.research.target_type import TargetType


def test_target_type():

    assert TargetType.PREVIOUS_DAY_HIGH.value == "Previous Day High"
    assert TargetType.IFVG.value == "iFVG"