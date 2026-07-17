"""Helper functions for agent trust benchmark.

Extracted from ouroboros/agent_trust.py — the normalization and redaction
functions needed by boundaries.py.
"""

def normalize_agent_trust_text(value: Any) -> str:
    """Normalize adversarial text for advisory matching/redaction.

    This is intentionally small and dependency-free: strip Unicode formatting
    controls such as zero-width joiners, apply NFKC, and map a tiny set of
    common homoglyphs used to hide security-sensitive words. It is not a proof
    of semantic safety; it only makes obvious evasions visible to local checks.
    """
    text = unicodedata.normalize("NFKC", str(value)).translate(_HOMOGLYPH_TRANSLATION)
    return "".join(ch for ch in text if unicodedata.category(ch) != "Cf")




def redact_agent_trust_packet(value: Any, *, parent_key: str | None = None) -> Any:
    """Return a JSON-safe copy with secret-shaped material removed.

    Agent Trust packets are advisory evidence artifacts and may become logs,
    receipts, or review bundles. They must never echo raw secret-looking input
    values. This redactor is conservative: key names associated with secrets
    redact their value even if the value itself is not pattern-matched.
    """
    if isinstance(value, dict):
        return {str(key): redact_agent_trust_packet(item, parent_key=str(key)) for key, item in value.items()}
    if isinstance(value, list):
        return [redact_agent_trust_packet(item, parent_key=parent_key) for item in value]
    if isinstance(value, tuple):
        return [redact_agent_trust_packet(item, parent_key=parent_key) for item in value]
    if isinstance(value, set):
        return sorted(redact_agent_trust_packet(item, parent_key=parent_key) for item in value)
    if isinstance(value, str):
        if parent_key is not None and _looks_like_secret_key(parent_key) and value.strip():
            return _REDACTED_SECRET
        return _redact_secret_text(value)
    return value



