from auctionlab.inference.objective_context import ObjectiveContext


def dominant_objective(
    context: ObjectiveContext,
):

    if context.upside_objective is None:
        return context.downside_objective

    if context.downside_objective is None:
        return context.upside_objective

    upside_distance = (
        context.upside_objective.rep_price
        - context.current_price
    )

    downside_distance = (
        context.current_price
        - context.downside_objective.rep_price
    )

    if upside_distance < downside_distance:
        return context.upside_objective

    return context.downside_objective