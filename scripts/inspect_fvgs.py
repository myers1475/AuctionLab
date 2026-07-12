from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from auctionlab.io.csv_loader import load_csv
from auctionlab.upo.fvg_detector import detect_bullish_fvgs

bars = load_csv("data/Futures/NQ/5m/2025-12_to_2026-07.csv")

fvgs = detect_bullish_fvgs(bars)

print(f"Detected {len(fvgs):,} bullish FVGs\n")

for fvg in fvgs[:50]:
    print(
        f"{fvg.created} | "
        f"{fvg.low:.2f} -> {fvg.high:.2f} | "
        f"{fvg.status.name}"
    )