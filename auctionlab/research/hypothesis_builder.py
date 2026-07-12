from datetime import datetime

from auctionlab.research.hypothesis import Hypothesis


def build_hypothesis(
    observation: str,
    inference: str,
    prediction: str,
) -> Hypothesis:

    return Hypothesis(
        created=datetime.now(),
        observation=observation,
        inference=inference,
        prediction=prediction,
    )