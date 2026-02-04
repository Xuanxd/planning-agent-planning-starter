from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Protocol, Optional


@dataclass
class PlanStep:
    """A single actionable step in a plan."""

    title: str
    rationale: str = ""
    expected_output: str = ""


@dataclass
class Plan:
    goal: str
    assumptions: List[str] = field(default_factory=list)
    steps: List[PlanStep] = field(default_factory=list)
    success_criteria: List[str] = field(default_factory=list)


class Planner(Protocol):
    def make_plan(self, task: str) -> Plan: ...


class SimplePlanner:
    """A deterministic placeholder planner.

    Replace this with an LLM-backed planner.
    """

    def make_plan(self, task: str) -> Plan:
        return Plan(
            goal=task,
            assumptions=[
                "No external tools are required.",
                "We prefer short, verifiable outputs.",
            ],
            steps=[
                PlanStep(
                    title="Clarify the desired output",
                    rationale="Ensure we know the format and scope.",
                    expected_output="A clarified specification.",
                ),
                PlanStep(
                    title="Draft the output",
                    rationale="Produce the requested artifact.",
                    expected_output="A first draft.",
                ),
                PlanStep(
                    title="Review against success criteria",
                    rationale="Catch omissions and tighten wording.",
                    expected_output="A revised final version.",
                ),
            ],
            success_criteria=[
                "Output matches the requested format.",
                "No missing key information.",
                "Concise and readable.",
            ],
        )
