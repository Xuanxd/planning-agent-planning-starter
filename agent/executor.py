from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Optional

from .planning import Plan, PlanStep


@dataclass
class StepResult:
    step: PlanStep
    output: str


class Executor:
    """Executes a plan step-by-step.

    This starter implementation uses a simple callable for each step.
    Swap this with real tool-calling and safety checks.
    """

    def __init__(self, step_fn: Optional[Callable[[PlanStep, str], str]] = None):
        self.step_fn = step_fn or self._default_step_fn

    def run(self, plan: Plan) -> List[StepResult]:
        results: List[StepResult] = []
        context = ""
        for step in plan.steps:
            out = self.step_fn(step, context)
            results.append(StepResult(step=step, output=out))
            context += f"\n\n## {step.title}\n{out}".strip()
        return results

    @staticmethod
    def _default_step_fn(step: PlanStep, context: str) -> str:
        # Placeholder: in a real agent, this is where you'd call an LLM or tools.
        if step.title.lower().startswith("clarify"):
            return "Spec: keep it short; include key points; no fluff."
        if step.title.lower().startswith("draft"):
            return "Draft: (replace with your real generation step)."
        return "Review: (replace with your real evaluation step)."
