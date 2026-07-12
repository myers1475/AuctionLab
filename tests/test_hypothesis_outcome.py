from auctionlab.research.hypothesis import Hypothesis
from auctionlab.research.hypothesis_outcome import HypothesisOutcome
from datetime import datetime


def test_new_hypothesis_is_pending():

    hypothesis = Hypothesis(
        created=datetime.now(),
        observation="Bullish iFVG",
        inference="Nearest UPO = PDH",
        prediction="Reach PDH",
    )

    assert hypothesis.outcome == HypothesisOutcome.PENDING