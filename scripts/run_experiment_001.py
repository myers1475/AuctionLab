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
from auctionlab.inference.nearest_objective import Objective

from auctionlab.replay.replay_engine import ReplayEngine
from auctionlab.replay.snapshot_factory import build_snapshot

from auctionlab.research.experiment_runner import ExperimentRunner
import auctionlab.research.experiments.nearest_objective as nearest_objective
from auctionlab.research.experiments.csv_exporter import export_csv
from auctionlab.research.experiments.outcome_log import OutcomeLog
from auctionlab.research.experiments.outcome_resolver import resolve
from auctionlab.research.experiments.outcome_statistics import calculate
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

        objectives = [
            Objective(
                kind=swing.name,
                price=swing.candle.high if swing.is_high else swing.candle.low,
                source=swing,
            )
            for swing in visible_swings
        ]

        objectives.extend(
            [
                Objective(
                    kind="Previous Day High",
                    price=previous_day.high,
                    source=previous_day,
                ),
                Objective(
                    kind="Previous Day Low",
                    price=previous_day.low,
                    source=previous_day,
                ),
                Objective(
                    kind="Previous Week High",
                    price=previous_week.high,
                    source=previous_week,
                ),
                Objective(
                    kind="Previous Week Low",
                    price=previous_week.low,
                    source=previous_week,
                ),
                Objective(
                    kind="Asia High",
                    price=asia.high,
                    source=asia,
                ),
                Objective(
                    kind="Asia Low",
                    price=asia.low,
                    source=asia,
                ),
                Objective(
                    kind="New York High",
                    price=new_york.high,
                    source=new_york,
                ),
                Objective(
                    kind="New York Low",
                    price=new_york.low,
                    source=new_york,
                ),
            ]
        )

        snapshot = build_snapshot(
            timestamp=bar.timestamp,
            current_price=bar.close,
            objectives=objectives,
            active_upos=ActiveUPOs(
                swings=visible_swings,
                previous_days=(previous_day,),
                previous_weeks=(previous_week,),
                fvgs=(),
                ifvgs=(),
            ),
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

    statistics = calculate(outcomes)

    print()
    print("Experiment 001")
    print("----------------------------")
    print(f"Observations : {len(log)}")
    print(f"CSV          : output/experiment_001.csv")

    print_report(statistics)

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