from auctionlab.inference.active_upos import ActiveUPOs


def test_active_upos():

    upos = ActiveUPOs(
        swings=(),
        previous_days=(),
        previous_weeks=(),
        fvgs=(),
        ifvgs=(),
    )

    assert len(upos.swings) == 0
    assert len(upos.fvgs) == 0
    assert len(upos.ifvgs) == 0