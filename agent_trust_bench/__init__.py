"""Agent Trust Benchmark — standalone benchmarking and testing for agent trust.

Core modules:
- boundaries: boundary catalog, classification, Clio axes, manifest generation
- threats: threat actor catalog mapped to boundaries
- isc_bench: ISC-Bench fixtures and test scenarios
- helpers: normalization and redaction utilities
"""

from agent_trust_bench.boundaries import (
    _BOUNDARIES,
    AXIS_DEFINITIONS,
    classify_agent_trust_boundaries,
    compute_axis_levels,
    generate_clio_manifest,
    clio_manifest_to_yaml,
)
from agent_trust_bench.threats import THREAT_ACTORS, resolve_threat_actors
from agent_trust_bench.isc_bench import ISCBenchFixture, load_isc_bench_fixtures
from agent_trust_bench.helpers import normalize_agent_trust_text, redact_agent_trust_packet

__version__ = "0.1.0"
