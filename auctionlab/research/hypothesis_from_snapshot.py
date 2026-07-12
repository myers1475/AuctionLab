from auctionlab.inference.objective_context import ObjectiveContext
from auctionlab.research.hypothesis_builder import build_hypothesis


def hypothesis_from_context(
    context: ObjectiveContext,
):

    if context.upside_objective is None:
        return None

    return build_hypothesis(
        observation="Market Snapshot",
        inference=f"Nearest upside UPO = {type(context.upside_objective).__name__}",
        prediction=(
            f"Price will seek "
            f"{context.upside_objective.rep_price}"
        ),
    )