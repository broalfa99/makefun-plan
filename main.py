#!/usr/bin/env python3
"""Write the winning 30-day $100 plan to /output/entry.txt.

Plan (drafted fresh, judged pairwise against the brief's five criteria
in order: agent-executable, expected money, works today, concrete,
edge): sell proof-first website fixes to small businesses.
"""
import os

PLAN = (
    "Day 1: crawl 500 sites from Google Maps; keep the 100 with broken links. "
    "Email owners a screenshot of the fault: fixed in 24h for $99, "
    "pay by Stripe link on delivery. Expect 5 sales = $495, cost ~$20. "
    "Edge: proof-first beats 1,000 generic pitches; "
    "no human scans 500 by lunch."
)

def main() -> None:
    assert 1 <= len(PLAN) <= 280, f"plan is {len(PLAN)} code points"
    assert PLAN.strip(), "plan must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)

if __name__ == "__main__":
    main()
