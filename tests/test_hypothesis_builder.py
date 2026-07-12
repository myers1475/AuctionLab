from auctionlab.research.hypothesis_builder import build_hypothesis


def test_build_hypothesis():

    hypothesis = build_hypothesis(
        observation="Bullish iFVG",
        inference="Nearest UPO = PDH",
        prediction="Reach PDH",
    )

    assert hypothesis.observation == "Bullish iFVG"
    assert hypothesis.inference == "Nearest UPO = PDH"
    assert hypothesis.prediction == "Reach PDH"
    assert hypothesis.outcome is None