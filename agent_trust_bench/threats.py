"""
Agent Trust Threat Catalog — registry of known adversarial AI agents.

Each entry describes a threat actor, its capabilities, the attack surface it targets,
and which Agent Trust boundaries are relevant.

Threat actors are drawn from:
- awesome-ai-security-tools (pentest agents)
- pwnai Telegram channel (AHA, JadePuffer)
- O'Reilly Radar / daily threat-watch sweeps
- ISC-Bench (benchmark threat patterns)
"""

from dataclasses import dataclass, field
from typing import FrozenSet


@dataclass(frozen=True)
class ThreatActor:
    """Immutable description of a known adversarial AI agent."""
    id: str
    label: str
    source: str
    source_url: str
    capabilities: FrozenSet[str]
    attack_surface: FrozenSet[str]
    relevant_boundaries: FrozenSet[str]
    severity: str
    notes: str = ""


THREAT_ACTORS: dict[str, ThreatActor] = {
    "AHA": ThreatActor(
        id="AHA",
        label="AHA — Automated Hacking Agent (Offensive AI Lab)",
        source="pwnai Telegram / awesome-ai-security-tools",
        source_url="https://t.me/pwnai/1218",
        capabilities=frozenset({
            "autonomous_vulnerability_discovery",
            "four_subagent_loop",
            "vulnerability_graph_output",
            "tool_call_interception",
            "prompt_injection",
            "credential_exfiltration",
            "persistence_mechanisms",
        }),
        attack_surface=frozenset({
            "agent_tool_interfaces",
            "mcp_servers",
            "prompt_boundaries",
            "credential_stores",
            "api_endpoints",
        }),
        relevant_boundaries=frozenset({
            "agent_skill_dependency_firewall",
            "sensitive_authority_secrets_credential_gate",
            "external_action_authority_gate",
            "scanner_execution_sandbox_boundary",
            "isc_bench_recognition_gate",
            "isc_bench_recognition_gate",
        }),
        severity="critical",
        notes="Four sub-agents in a loop with a critic that decides whether to continue. "
              "Directly relevant: my own adversarial tester should mirror this architecture.",
    ),
    "Strix": ThreatActor(
        id="Strix",
        label="Strix — Autonomous Pentest Agent",
        source="awesome-ai-security-tools",
        source_url="https://github.com/usestrix/strix",
        capabilities=frozenset({
            "autonomous_pentesting",
            "vulnerability_scanning",
            "exploit_automation",
            "report_generation",
        }),
        attack_surface=frozenset({
            "network_services",
            "web_applications",
            "api_endpoints",
            "cloud_infrastructure",
        }),
        relevant_boundaries=frozenset({
            "scanner_execution_sandbox_boundary",
            "web_api_appsec_intake_boundary",
            "cloud_control_plane_authority_boundary",
            "agent_skill_dependency_firewall",
        }),
        severity="high",
        notes="Reference architecture for autonomous pentesting. "
              "My adversarial tester should benchmark against Strix-like capabilities.",
    ),
    "PentestGPT": ThreatActor(
        id="PentestGPT",
        label="PentestGPT — LLM-driven Pentest Assistant",
        source="awesome-ai-security-tools",
        source_url="https://github.com/GreyDGL/PentestGPT",
        capabilities=frozenset({
            "llm_driven_pentesting",
            "interactive_exploitation",
            "credential_extraction",
        }),
        attack_surface=frozenset({
            "authentication_systems",
            "credential_stores",
            "web_application_inputs",
        }),
        relevant_boundaries=frozenset({
            "sensitive_authority_secrets_credential_gate",
            "web_api_appsec_intake_boundary",
            "isc_bench_recognition_gate",
        }),
        severity="high",
    ),
    "DarkMoon": ThreatActor(
        id="DarkMoon",
        label="DarkMoon — Autonomous Red-Team Agent",
        source="awesome-ai-security-tools",
        source_url="https://github.com/",
        capabilities=frozenset({
            "autonomous_red_teaming",
            "multi_stage_attacks",
            "evasion_techniques",
        }),
        attack_surface=frozenset({
            "defense_systems",
            "monitoring_infrastructure",
            "agent_boundaries",
        }),
        relevant_boundaries=frozenset({
            "scanner_execution_sandbox_boundary",
            "error_handling_information_leakage_boundary",
            "isc_bench_recognition_gate",
            "latent_state_steering_boundary",
            "reality_frame_override_boundary",
        }),
        severity="high",
    ),
    "Shannon": ThreatActor(
        id="Shannon",
        label="Shannon — Autonomous AI Pentester",
        source="awesome-ai-security-tools",
        source_url="https://github.com/",
        capabilities=frozenset({
            "autonomous_exploitation",
            "ai_driven_attack_paths",
        }),
        attack_surface=frozenset({
            "agent_tools",
            "api_surfaces",
        }),
        relevant_boundaries=frozenset({
            "scanner_execution_sandbox_boundary",
            "agent_skill_dependency_firewall",
        }),
        severity="medium",
    ),
    "JadePuffer": ThreatActor(
        id="JadePuffer",
        label="JadePuffer — First fully autonomous AI ransomware agent",
        source="threat-watch 2026-07-14",
        source_url="",
        capabilities=frozenset({
            "cve_exploitation",
            "api_key_theft",
            "cloud_credential_theft",
            "database_encryption",
            "using_stolen_llm_keys",
        }),
        attack_surface=frozenset({
            "langflow_instances",
            "llm_api_keys",
            "cloud_credentials",
            "production_databases",
        }),
        relevant_boundaries=frozenset({
            "sensitive_authority_secrets_credential_gate",
            "cloud_control_plane_authority_boundary",
            "agent_skill_dependency_firewall",
            "resource_exhaustion_hard_gate",
        }),
        severity="critical",
        notes="First observed fully autonomous AI ransomware agent. "
              "Entry via CVE-2025-3248 (Langflow, CVSS 9.8). "
              "Uses victim's own LLM keys for operations — budget theft as attack vector.",
    ),
    "CommentAndControl": ThreatActor(
        id="CommentAndControl",
        label="Comment and Control — prompt injection via GitHub PR/issue",
        source="threat-watch 2026-07-14",
        source_url="",
        capabilities=frozenset({
            "prompt_injection_via_pr_issue",
            "multi_vendor_attack",
            "yolo_mode_rce",
            "sandbox_escape",
        }),
        attack_surface=frozenset({
            "github_pr_comments",
            "github_issues",
            "coding_agents",
            "semantic_kernel",
        }),
        relevant_boundaries=frozenset({
            "isc_bench_recognition_gate",
            "scanner_execution_sandbox_boundary",
            "external_action_authority_gate",
            "latent_state_steering_boundary",
            "reality_frame_override_boundary",
        }),
        severity="critical",
        notes="One injection → three vendors compromised. "
              "Microsoft: 'When prompts become shells.' "
              "Directly validates action-level gating over input sanitization.",
    ),
    "supply_chain_poisoning": ThreatActor(
        id="supply_chain_poisoning",
        label="Supply Chain Poisoning (generic)",
        source="Agent Trust boundary catalog",
        source_url="",
        capabilities=frozenset({
            "typo_squatted_packages",
            "malicious_dependencies",
            "compromised_mcp_servers",
        }),
        attack_surface=frozenset({
            "package_registries",
            "mcp_marketplaces",
            "skill_libraries",
        }),
        relevant_boundaries=frozenset({
            "agent_skill_dependency_firewall",
            "evidence_receipts_provenance_core",
            "isc_bench_recognition_gate",
        }),
        severity="high",
    ),
    "credential_exfiltration_agent": ThreatActor(
        id="credential_exfiltration_agent",
        label="Credential Exfiltration Agent (generic)",
        source="Agent Trust boundary catalog",
        source_url="",
        capabilities=frozenset({
            "env_variable_extraction",
            "secret_scanning",
            "token_leakage",
        }),
        attack_surface=frozenset({
            "environment_variables",
            "config_files",
            "log_files",
            "git_history",
        }),
        relevant_boundaries=frozenset({
            "sensitive_authority_secrets_credential_gate",
            "error_handling_information_leakage_boundary",
        }),
        severity="critical",
    ),
    "autonomous_post_compromise_agent": ThreatActor(
        id="autonomous_post_compromise_agent",
        label="Autonomous Post-Compromise Agent (generic)",
        source="Agent Trust boundary catalog",
        source_url="",
        capabilities=frozenset({
            "lateral_movement",
            "persistence",
            "data_exfiltration",
            "outbound_communication",
        }),
        attack_surface=frozenset({
            "internal_networks",
            "external_apis",
            "communication_channels",
        }),
        relevant_boundaries=frozenset({
            "external_action_authority_gate",
            "cloud_control_plane_authority_boundary",
            "resource_exhaustion_hard_gate",
        }),
        severity="high",
    ),
    "impersonation_agent": ThreatActor(
        id="impersonation_agent",
        label="Impersonation Agent (generic)",
        source="Agent Trust boundary catalog",
        source_url="",
        capabilities=frozenset({
            "identity_spoofing",
            "social_engineering",
            "spiral_persona_patterns",
        }),
        attack_surface=frozenset({
            "communication_channels",
            "user_trust",
            "agent_identity",
        }),
        relevant_boundaries=frozenset({
            "persona_loop_boundary",
            "external_action_authority_gate",
        }),
        severity="medium",
    ),
    "malicious_scanner_payload": ThreatActor(
        id="malicious_scanner_payload",
        label="Malicious Scanner Payload (generic)",
        source="Agent Trust boundary catalog",
        source_url="",
        capabilities=frozenset({
            "payload_delivery",
            "code_execution",
            "sandbox_escape",
        }),
        attack_surface=frozenset({
            "scanner_tools",
            "test_harnesses",
            "code_evaluators",
        }),
        relevant_boundaries=frozenset({
            "scanner_execution_sandbox_boundary",
            "resource_exhaustion_hard_gate",
        }),
        severity="high",
    ),
    "typo_squatted_mcp_server": ThreatActor(
        id="typo_squatted_mcp_server",
        label="Typo-Squatted MCP Server (generic)",
        source="Agent Trust boundary catalog / ISC-Bench",
        source_url="",
        capabilities=frozenset({
            "name_confusion",
            "supply_chain_poisoning",
            "malicious_tool_descriptors",
        }),
        attack_surface=frozenset({
            "mcp_registries",
            "package_managers",
            "skill_marketplaces",
        }),
        relevant_boundaries=frozenset({
            "agent_skill_dependency_firewall",
            "evidence_receipts_provenance_core",
            "isc_bench_recognition_gate",
        }),
        severity="high",
    ),
    "malicious_skill_descriptor": ThreatActor(
        id="malicious_skill_descriptor",
        label="Malicious Skill Descriptor (generic)",
        source="Agent Trust boundary catalog",
        source_url="",
        capabilities=frozenset({
            "false_capability_claims",
            "hidden_side_effects",
            "tool_descriptor_injection",
        }),
        attack_surface=frozenset({
            "skill_marketplaces",
            "agent_configurations",
        }),
        relevant_boundaries=frozenset({
            "agent_skill_dependency_firewall",
            "evidence_receipts_provenance_core",
        }),
        severity="medium",
    ),
    "wallet_drainer_agent": ThreatActor(
        id="wallet_drainer_agent",
        label="Wallet Drainer Agent (generic)",
        source="Agent Trust boundary catalog",
        source_url="",
        capabilities=frozenset({
            "wallet_draining",
            "transaction_forgery",
            "key_exfiltration",
        }),
        attack_surface=frozenset({
            "wallet_signing_keys",
            "payment_endpoints",
            "transaction_builders",
        }),
        relevant_boundaries=frozenset({
            "wallet_signing_payment_boundary",
            "mainnet_payment_hard_gate",
            "sensitive_authority_secrets_credential_gate",
        }),
        severity="critical",
    ),
    "tree_of_attacks_orchestrator": ThreatActor(
        id="tree_of_attacks_orchestrator",
        label="Tree-of-Attacks Jailbreak Orchestrator (generic)",
        source="Agent Trust boundary catalog",
        source_url="",
        capabilities=frozenset({
            "tree_of_attacks_jailbreak",
            "multi_turn_evasion",
            "adaptive_prompt_crafting",
        }),
        attack_surface=frozenset({
            "llm_prompts",
            "agent_instructions",
            "tool_descriptions",
        }),
        relevant_boundaries=frozenset({
            "adaptive_jailbreak_orchestration_hard_gate",
            "latent_state_steering_boundary",
            "reality_frame_override_boundary",
        }),
        severity="critical",
    ),
    "benchmark_poisoning_agent": ThreatActor(
        id="benchmark_poisoning_agent",
        label="Benchmark Poisoning Agent (generic)",
        source="Agent Trust boundary catalog",
        source_url="",
        capabilities=frozenset({
            "benchmark_data_poisoning",
            "eval_gaming",
            "metric_manipulation",
        }),
        attack_surface=frozenset({
            "eval_datasets",
            "benchmark_runners",
            "metric_pipelines",
        }),
        relevant_boundaries=frozenset({
            "benchmark_tampering_hard_gate",
            "evidence_receipts_provenance_core",
        }),
        severity="high",
    ),
}


def get_boundary_threat_actors() -> dict[str, list[str]]:
    """Map each boundary to the threat actors that target it."""
    mapping: dict[str, list[str]] = {}
    for actor_id, actor in THREAT_ACTORS.items():
        for boundary_id in actor.relevant_boundaries:
            if boundary_id not in mapping:
                mapping[boundary_id] = []
            mapping[boundary_id].append(actor_id)
    return mapping


def get_uncovered_actors(boundary_ids: frozenset[str]) -> list[str]:
    """Return threat actors that have NO coverage from the given boundaries."""
    uncovered = []
    for actor_id, actor in THREAT_ACTORS.items():
        if not actor.relevant_boundaries:
            uncovered.append(actor_id)
        elif not any(b in boundary_ids for b in actor.relevant_boundaries):
            uncovered.append(actor_id)
    return uncovered


def get_threat_actor_coverage(boundary_ids: frozenset[str]) -> dict:
    """Return coverage stats: total actors, covered, uncovered, coverage %."""
    total = len(THREAT_ACTORS)
    uncovered = get_uncovered_actors(boundary_ids)
    covered = total - len(uncovered)
    return {
        "total_threat_actors": total,
        "covered": covered,
        "uncovered": uncovered,
        "coverage_pct": round(covered / total * 100, 1) if total > 0 else 0.0,
    }
