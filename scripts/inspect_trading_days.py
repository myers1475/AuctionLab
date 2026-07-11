from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from auctionlab.io.csv_loader import load_csv
from auctionlab.observation.trading_day_builder import build_trading_days

bars = load_csv("data/Futures/NQ/5m/2025-12_to_2026-07.csv")

days = build_trading_days(bars)

print(f"Trading Days: {len(days)}")
print()

first = days[0]

print(f"Date : {first.date}")
print(f"Open : {first.open}")
print(f"High : {first.high}")
print(f"Low  : {first.low}")
print(f"Close: {first.close}")
print(f"Bars : {len(first.bars)}")