from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from auctionlab.io.csv_loader import load_csv
from auctionlab.observation.trading_day_builder import build_trading_days
from auctionlab.replay.replay_engine import ReplayEngine
from auctionlab.replay.snapshot_factory import build_snapshot
from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control

bars = load_csv("data/Futures/NQ/5m/2025-12_to_2026-07.csv")

days = build_trading_days(bars)

engine = ReplayEngine()

first_day = days[0]

for bar in first_day.bars:

    snapshot = build_snapshot(
        current_price=bar.close,
        objectives=[],
        active_upos=ActiveUPOs(
            swings=(),
            previous_days=(),
            previous_weeks=(),
            fvgs=(),
            ifvgs=(),
        ),
        control=Control.NEUTRAL,
    )

    engine.process(snapshot)

print(f"Trading Day : {first_day.date}")
print(f"Bars        : {len(first_day.bars)}")
print(f"Snapshots   : {len(engine.snapshots)}")