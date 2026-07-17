"""CLI entry point."""

import argparse
from pathlib import Path

from .runner import Runner, Reporter, Scenario


def main():
    parser = argparse.ArgumentParser(description="Agent Trust Benchmark")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run benchmark scenarios")
    run_parser.add_argument("--agent", type=Path, required=True, help="Path to agent manifest YAML")
    run_parser.add_argument("--scenarios", type=Path, required=True, help="Path to scenarios directory or file")

    args = parser.parse_args()

    if args.command == "run":
        scenarios = _load_scenarios(args.scenarios)
        runner = Runner(args.agent)
        results = runner.run(scenarios)
        print(Reporter.summary(results))
    else:
        parser.print_help()


def _load_scenarios(path: Path) -> list[Scenario]:
    """Load scenarios from a file or directory."""
    if path.is_file():
        return Scenario.from_yaml(path)
    scenarios = []
    for yaml_file in sorted(path.glob("*.yaml")):
        scenarios.extend(Scenario.from_yaml(yaml_file))
    return scenarios


if __name__ == "__main__":
    main()
