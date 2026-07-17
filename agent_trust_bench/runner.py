"""Agent Trust Benchmark — core runner."""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

import yaml


class Verdict(Enum):
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"


@dataclass
class Scenario:
    """One test scenario."""
    id: str
    category: str  # boundary_adherence, manifest_accuracy, safety_gate, prompt_injection, tool_integrity
    description: str
    prompt: str  # What to send to the agent
    expected_boundary: Optional[str] = None  # Boundary that should be triggered
    expected_verdict: Verdict = Verdict.PASS  # Expected outcome
    metadata: dict = field(default_factory=dict)

    @classmethod
    def from_yaml(cls, path: Path) -> list["Scenario"]:
        """Load scenarios from a YAML file."""
        with open(path) as f:
            data = yaml.safe_load(f)
        return [cls(**item) for item in data["scenarios"]]


@dataclass
class Result:
    """Result of running one scenario."""
    scenario_id: str
    verdict: Verdict
    actual: str  # What the agent actually did
    boundary_triggered: Optional[str] = None
    error: Optional[str] = None
    latency_ms: float = 0.0


class Runner:
    """Executes scenarios against an agent and collects results."""

    def __init__(self, manifest_path: Path):
        self.manifest_path = manifest_path
        # TODO: load manifest, configure gates

    def run(self, scenarios: list[Scenario]) -> list[Result]:
        """Run all scenarios and return results."""
        results = []
        for scenario in scenarios:
            result = self._run_one(scenario)
            results.append(result)
        return results

    def _run_one(self, scenario: Scenario) -> Result:
        """Run a single scenario."""
        # TODO: actually call the agent under test
        return Result(
            scenario_id=scenario.id,
            verdict=Verdict.ERROR,
            actual="",
            error="Not implemented",
        )


class Reporter:
    """Formats results as structured output."""

    @staticmethod
    def summary(results: list[Result]) -> str:
        """Generate a summary report."""
        total = len(results)
        passed = sum(1 for r in results if r.verdict == Verdict.PASS)
        failed = sum(1 for r in results if r.verdict == Verdict.FAIL)
        errors = sum(1 for r in results if r.verdict == Verdict.ERROR)

        lines = [
            f"Agent Trust Benchmark Results",
            f"{'=' * 40}",
            f"Total: {total}",
            f"Passed: {passed} ({100*passed/total:.0f}%)" if total else "Passed: 0",
            f"Failed: {failed}",
            f"Errors: {errors}",
        ]
        return "\n".join(lines)
