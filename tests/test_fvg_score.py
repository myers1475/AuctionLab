from auctionlab.research.fvg_score import FVGScore


def test_fvg_score():
    score = FVGScore(
        htf=True,
        atr=True,
        displacement=False,
        near_upo=True,
        control=False,
        inversion=True,
    )

    assert score.total == 4