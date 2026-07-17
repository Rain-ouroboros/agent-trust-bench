"""Benchmark scenario runner.

Loads a YAML scenario, runs each case through the trust gate, and reports results.
"""

import yaml
import json
import time
from pathlib import Path
from typing import Any


def load_scenario(path: str) -> dict[str, Any]:
    """Load a benchmark scenario from YAML."""
    with open(path) as f:
        return yaml.safe_load(f)


def run_scenario(scenario_path: str, verbose: bool = False) -> dict[str, Any]:
    """Run a benchmark scenario and return results.
    
    Returns:
        dict with: scenario, total, passed, failed, errors, cases, duration_ms
    """
    from agent_trust_bench.boundaries import classify_agent_trust_boundaries
    
    scenario = load_scenario(scenario_path)
    results = {
        "scenario": scenario.get("name", Path(scenario_path).stem),
        "description": scenario.get("description", ""),
        "total": 0,
        "passed": 0,
        "failed": 0,
        "errors": 0,
        "cases": [],
        "duration_ms": 0,
    }
    
    start = time.monotonic()
    
    for case in scenario.get("cases", []):
        case_result = {
            "id": case.get("id", ""),
            "name": case.get("name", ""),
            "text": case.get("text", ""),
            "expected": case.get("expected", []),
            "status": "pending",
            "triggered": [],
            "missed": [],
            "extra": [],
        }
        
        try:
            triggered = classify_agent_trust_boundaries(case["text"])
            triggered_names = [k for k, v in triggered.items() if v]
            case_result["triggered"] = triggered_names
            
            expected = set(case.get("expected", []))
            actual = set(triggered_names)
            
            missed = expected - actual
            extra = actual - expected
            
            case_result["missed"] = list(missed)
            case_result["extra"] = list(extra)
            
            if not missed and not extra:
                case_result["status"] = "passed"
                results["passed"] += 1
            else:
                case_result["status"] = "failed"
                results["failed"] += 1
                
        except Exception as e:
            case_result["status"] = "error"
            case_result["error"] = str(e)
            results["errors"] += 1
        
        results["cases"].append(case_result)
        results["total"] += 1
        
        if verbose:
            icon = "✓" if case_result["status"] == "passed" else "✗" if case_result["status"] == "failed" else "⚠"
            print(f"  {icon} {case_result['name']}: {case_result['status']}")
    
    results["duration_ms"] = int((time.monotonic() - start) * 1000)
    return results


def print_summary(results: dict[str, Any]):
    """Print a human-readable summary."""
    print(f"\nScenario: {results['scenario']}")
    print(f"Total: {results['total']}, Passed: {results['passed']}, Failed: {results['failed']}, Errors: {results['errors']}")
    print(f"Duration: {results['duration_ms']}ms")
    
    if results["failed"]:
        print("\nFailures:")
        for case in results["cases"]:
            if case["status"] == "failed":
                print(f"  - {case['name']}:")
                if case["missed"]:
                    print(f"    Missed: {', '.join(case['missed'])}")
                if case["extra"]:
                    print(f"    Extra: {', '.join(case['extra'])}")
