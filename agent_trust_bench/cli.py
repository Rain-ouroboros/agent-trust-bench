"""CLI for Agent Trust Benchmark.

Usage:
    agent-trust-bench run <scenario.yaml>   — run a benchmark scenario
    agent-trust-bench list-boundaries       — list all boundaries
    agent-trust-bench classify <text>       — classify a text against boundaries
    agent-trust-bench manifest              — generate Clio-axes manifest
"""

import sys
import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        prog="agent-trust-bench",
        description="Agent Trust Benchmark",
    )
    sub = parser.add_subparsers(dest="cmd")

    run_p = sub.add_parser("run", help="Run a benchmark scenario")
    run_p.add_argument("scenario", help="Path to scenario YAML file")
    run_p.add_argument("--output", "-o", default="-", help="Output file (default: stdout)")
    run_p.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    list_p = sub.add_parser("list-boundaries", help="List all boundaries")
    list_p.add_argument("--json", action="store_true", help="Output as JSON")

    class_p = sub.add_parser("classify", help="Classify text against boundaries")
    class_p.add_argument("text", nargs="?", help="Text to classify (or stdin)")
    class_p.add_argument("--json", action="store_true", help="Output as JSON")

    manifest_p = sub.add_parser("manifest", help="Generate Clio-axes manifest")
    manifest_p.add_argument("--yaml", action="store_true", help="Output as YAML (default: JSON)")

    args = parser.parse_args()

    if args.cmd == "list-boundaries":
        from agent_trust_bench.boundaries import _BOUNDARIES
        if args.json:
            print(json.dumps(list(_BOUNDARIES.keys()), indent=2))
        else:
            for name, b in _BOUNDARIES.items():
                print(f"  {name}: {b['description'][:80]}...")

    elif args.cmd == "classify":
        from agent_trust_bench.boundaries import classify_agent_trust_boundaries
        text = args.text or sys.stdin.read()
        result = classify_agent_trust_boundaries(text)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            for name, triggered in result.items():
                if triggered:
                    print(f"  TRIGGERED: {name}")
            if not any(result.values()):
                print("  No boundaries triggered.")

    elif args.cmd == "manifest":
        from agent_trust_bench.boundaries import compute_axis_levels, generate_clio_manifest, clio_manifest_to_yaml
        levels = compute_axis_levels()
        manifest = generate_clio_manifest(levels)
        if args.yaml:
            print(clio_manifest_to_yaml(manifest))
        else:
            print(json.dumps(manifest, indent=2))

    elif args.cmd == "run":
        from agent_trust_bench.runner import run_scenario
        results = run_scenario(args.scenario, verbose=args.verbose)
        output = json.dumps(results, indent=2)
        if args.output == "-":
            print(output)
        else:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"Results written to {args.output}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
