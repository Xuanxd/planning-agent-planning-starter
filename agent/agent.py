from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .planning import Planner, SimplePlanner, Plan
from .executor import Executor, StepResult


@dataclass
class RunResult:
    plan: Plan
    step_results: List[StepResult]
    reflection: str


class PlanningAgent:
    def __init__(self, planner: Planner | None = None, executor: Executor | None = None):
        self.planner = planner or SimplePlanner()
        self.executor = executor or Executor()

    def run(self, task: str) -> RunResult:
        plan = self.planner.make_plan(task)
        step_results = self.executor.run(plan)
        reflection = self.reflect(plan, step_results)
        return RunResult(plan=plan, step_results=step_results, reflection=reflection)

    @staticmethod
    def reflect(plan: Plan, step_results: List[StepResult]) -> str:
        # Placeholder reflection.
        done = len(step_results)
        criteria = "; ".join(plan.success_criteria) if plan.success_criteria else "(none)"
        return f"Completed {done} steps. Success criteria: {criteria}"
