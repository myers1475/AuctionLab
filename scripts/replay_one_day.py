from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from auctionlab.io.csv_loader import load_csv
from auctionlab.observation.trading_day_builder import build_trading_days
from auctionlab.observation.swing_detector import detect_swings
from auctionlab.research.swing_filters import minimum_move
from auctionlab.inference.nearest_objective import Objective
from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.replay.replay_engine import ReplayEngine
from auctionlab.replay.snapshot_factory import build_snapshot


def main():

    bars = load_csv("data/Futures/NQ/5m/2025-12_to_2026-07.csv")

    days = build_trading_days(bars)

    engine = ReplayEngine()

    first_day = days[0]

    # Detect every objective fractal swing
    raw_swings = detect_swings(first_day.bars)

    # Research filter (temporary constant)
    swings = minimum_move(
        raw_swings,
        minimum=20,
    )

    for i, bar in enumerate(first_day.bars):

        visible_swings = tuple(
            swing
            for swing in swings
            if swing.index <= i
        )

        objectives = [
            Objective(
                kind=swing.name,
                price=(
                    swing.candle.high
                    if swing.is_high
                    else swing.candle.low
                ),
                source=swing,
            )
            for swing in visible_swings
        ]

        snapshot = build_snapshot(
            current_price=bar.close,
            objectives=objectives,
            active_upos=ActiveUPOs(
                swings=visible_swings,
                previous_days=(),
                previous_weeks=(),
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
    print(f"Trading Day            : {first_day.date}")
    print(f"Bars                   : {len(first_day.bars)}")
    print(f"Raw Swings             : {len(raw_swings)}")
    print(f"Filtered Swings        : {len(swings)}")
    print(f"Snapshots              : {len(engine.snapshots)}")
    print(f"Latest Snapshot Swings : {len(latest.active_upos.swings)}")


if __name__ == "__main__":
    main()