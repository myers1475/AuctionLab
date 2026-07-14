from pathlib import Path
import sys
from datetime import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from auctionlab.io.csv_loader import load_csv

from auctionlab.observation.trading_day_builder import build_trading_days
from auctionlab.observation.trading_week_builder import build_trading_weeks
from auctionlab.observation.session_builder import build_session
from auctionlab.observation.swing_detector import detect_swings

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.objective_builder import build_objectives

from auctionlab.replay.replay_engine import ReplayEngine
from auctionlab.replay.snapshot_factory import build_snapshot

from auctionlab.research.experiment_runner import ExperimentRunner
import auctionlab.research.experiments.nearest_objective as nearest_objective

from auctionlab.research.experiments.csv_exporter import export_csv
from auctionlab.research.experiments.outcome_csv_exporter import (
    export_outcomes,
)
from auctionlab.research.experiments.outcome_log import OutcomeLog
from auctionlab.research.experiments.outcome_resolver import resolve
from auctionlab.research.experiments.outcome_statistics import (
    calculate,
    calculate_by_target_kind,
)
from auctionlab.research.experiments.outcome_report import print_report

from auctionlab.upo.previous_day_builder import previous_day_levels
from auctionlab.upo.previous_week_builder import previous_week_levels
from auctionlab.upo.session_levels_detector import detect_session_levels


def main():

    bars = load_csv("data/Futures/NQ/5m/2025-12_to_2026-07.csv")

    days = build_trading_days(bars)
    weeks = build_trading_weeks(days)

    engine = ReplayEngine()

    current_day = days[1]

    previous_day = previous_day_levels(
        days[0],
        current_day,
    )

    previous_week = previous_week_levels(
        weeks[0],
    )

    asia = detect_session_levels(
        build_session(
            current_day,
            "Asia",
            time(20, 0),
            time(23, 59),
        )
    )

    new_york = detect_session_levels(
        build_session(
            current_day,
            "New York",
            time(9, 30),
            time(16, 0),
        )
    )

    swings = detect_swings(current_day.bars)

    for i, bar in enumerate(current_day.bars):

        visible_swings = tuple(
            swing
            for swing in swings
            if swing.index <= i
        )

        active_upos = ActiveUPOs(
            swings=visible_swings,
            previous_days=(previous_day,),
            previous_weeks=(previous_week,),
            fvgs=(),
            ifvgs=(),
        )

        objectives = build_objectives(active_upos)

        snapshot = build_snapshot(
            timestamp=bar.timestamp,
            candle=bar,
            current_price=bar.close,
            objectives=objectives,
            active_upos=active_upos,
            control=Control.NEUTRAL,
        )

        engine.process(snapshot)

    runner = ExperimentRunner()

    log = runner.run(
        snapshots=engine.snapshots,
        experiment=nearest_objective,
    )

    export_csv(
        log,
        "output/experiment_001.csv",
    )

    outcomes = OutcomeLog()

    for observation in log.observations:

        outcome = resolve(
            observation,
            engine.snapshots,
        )

        if outcome is not None:
            outcomes.add(outcome)

    export_outcomes(
        outcomes,
        "output/experiment_001_outcomes.csv",
    )

    statistics = calculate(outcomes)
    by_target = calculate_by_target_kind(outcomes)

    print()
    print("Experiment 001")
    print("----------------------------")
    print(f"Observations       : {len(log)}")
    print("Observation CSV    : output/experiment_001.csv")
    print("Outcome CSV        : output/experiment_001_outcomes.csv")
    print("Target Summary CSV : output/experiment_001_outcomes_by_target.csv")

    print_report(statistics)

    print()
    print("Hit Rate by Target Type")
    print("----------------------------")

    for row in by_target:
        print(
            f"{row.target_kind:<20}"
            f"{row.reached:>5}/{row.total:<5}"
            f"{row.hit_rate:>8.2%}"
        )

    if len(log):

        print()
        print("First Observation")
        print("----------------------------")
        print(log.observations[0])

        print()
        print("Last Observation")
        print("----------------------------")
        print(log.observations[-1])


if __name__ == "__main__":
    main()