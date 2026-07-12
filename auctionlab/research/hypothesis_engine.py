from auctionlab.research.hypothesis import Hypothesis
from auctionlab.research.hypothesis_builder import build_hypothesis


def generate_hypothesis(
    observation: str,
    inference: str,
    prediction: str,
) -> Hypothesis:

    return build_hypothesis(
        observation=observation,
        inference=inference,
        prediction=prediction,
    )