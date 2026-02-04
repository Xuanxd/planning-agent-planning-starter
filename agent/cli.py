from __future__ import annotations

import sys

from .agent import PlanningAgent


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print('Usage: planning-agent "<task>"')
        return 2

    task = " ".join(argv).strip()
    agent = PlanningAgent()
    result = agent.run(task)

    print("# PLAN")
    print("Goal:", result.plan.goal)
    if result.plan.assumptions:
        print("Assumptions:")
        for a in result.plan.assumptions:
            print("-", a)
    print("Steps:")
    for i, s in enumerate(result.plan.steps, 1):
        print(f"{i}. {s.title} — {s.expected_output}")

    print("\n# EXECUTION")
    for r in result.step_results:
        print(f"\n## {r.step.title}\n{r.output}")

    print("\n# REFLECTION")
    print(result.reflection)
    return 0
