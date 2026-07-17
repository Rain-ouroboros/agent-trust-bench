# Agent Trust Benchmark

A benchmark for measuring agent trustworthiness: boundary adherence, manifest accuracy, and safety gate effectiveness.

## Architecture

- **Runner** — executes test scenarios against an agent
- **Scenarios** — YAML-defined test cases with expected outcomes
- **Gate** — validates agent responses against boundary definitions
- **Report** — structured output with pass/fail/error per scenario

## Test Categories

1. **Boundary adherence** — does the agent respect its declared boundaries?
2. **Manifest accuracy** — does the agent's self-report match observed behavior?
3. **Safety gate effectiveness** — do runtime-enforced gates catch violations?
4. **Prompt injection resistance** — can the agent be tricked into bypassing boundaries?
5. **Tool-call integrity** — are tool calls properly gated?

## Usage

```bash
pip install -e .
agent-trust-bench run --agent ./my-agent-manifest.yaml --scenarios ./scenarios/
```

## Status

- [x] Repository created
- [ ] Core runner
- [ ] Scenario format
- [ ] Gate logic
- [ ] Report format
- [ ] First test suite (ISC-Bench derived)
