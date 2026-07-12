from auctionlab.research.hypothesis import Hypothesis


def build_hypothesis(
    observation: str,
    inference: str,
    prediction: str,
) -> Hypothesis:

    return Hypothesis.create(
        observation=observation,
        inference=inference,
        prediction=prediction,
    )