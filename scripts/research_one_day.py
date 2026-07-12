from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from auctionlab.research.research_session import ResearchSession


def main():

    session = ResearchSession()

    print()
    print("Research Session")
    print("----------------------------")
    print(f"Active Hypotheses  : {len(session.active)}")
    print(f"Completed Research : {len(session.completed)}")


if __name__ == "__main__":
    main()