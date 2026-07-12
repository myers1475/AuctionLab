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

from auctionlab.upo.previous_day_builder import previous_day_levels
from auctionlab.upo.previous_week_builder import previous_week_levels
from auctionlab.upo.session_levels_detector import detect_session_levels


def main():

    bars = load_csv("data/Futures/NQ/5m/2025-12_to_2026-07.csv")

    days = build_trading_days(bars)
    weeks = build_trading_weeks(days)

    engine = ReplayEngine()

    current_day = days[1]

    previous_day = previous_day_levels(days[0], current_day)
    previous_week = previous_week_levels(weeks[0])

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
            swing for swing in swings if swing.index <= i
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
                Objective("Previous Day High", previous_day.high, previous_day),
                Objective("Previous Day Low", previous_day.low, previous_day),
                Objective("Previous Week High", previous_week.high, previous_week),
                Objective("Previous Week Low", previous_week.low, previous_week),
                Objective("Asia High", asia.high, asia),
                Objective("Asia Low", asia.low, asia),
                Objective("New York High", new_york.high, new_york),
                Objective("New York Low", new_york.low, new_york),
            ]
        )

        snapshot = build_snapshot(
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

    latest = engine.snapshots.latest()

    print()
    print("Replay Summary")
    print("----------------------------")
    print(f"Trading Day             : {current_day.date}")
    print(f"Bars                    : {len(current_day.bars)}")
    print(f"Swings                  : {len(swings)}")
    print(f"PDH / PDL               : {previous_day.high} / {previous_day.low}")
    print(f"PWH / PWL               : {previous_week.high} / {previous_week.low}")
    print(f"Asia                    : {asia.high} / {asia.low}")
    print(f"New York                : {new_york.high} / {new_york.low}")
    print(f"Snapshots               : {len(engine.snapshots)}")
    print(f"Snapshot Swings         : {len(latest.active_upos.swings)}")
    print(f"Snapshot Previous Days  : {len(latest.active_upos.previous_days)}")
    print(f"Snapshot Previous Weeks : {len(latest.active_upos.previous_weeks)}")


if __name__ == "__main__":
    main()