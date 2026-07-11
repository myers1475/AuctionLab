from auctionlab.io.csv_loader import load_csv

bars = load_csv("data/CME_MINI_NQ1!, 5_33ece.csv")

print(f"Loaded {len(bars):,} bars")

print("\nFirst bar:")
print(bars[0])

print("\nLast bar:")
print(bars[-1])