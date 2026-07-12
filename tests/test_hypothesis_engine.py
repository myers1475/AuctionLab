from auctionlab.research.hypothesis_engine import generate_hypothesis


def test_generate_hypothesis():

    hypothesis = generate_hypothesis(
        observation="Bullish iFVG",
        inference="Nearest UPO = PDH",
        prediction="Price reaches PDH",
    )

    assert hypothesis.observation == "Bullish iFVG"
    assert hypothesis.inference == "Nearest UPO = PDH"
    assert hypothesis.prediction == "Price reaches PDH"