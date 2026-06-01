# Truth Runtime Capability

Read `LAYER_IDENTITY.md` and `TRUTH_RUNTIME_API.yaml` first.

This capability is the truth governor for AOS. It is intentionally implemented as a capability, not a core layer. The core sees only `aos_core/ports/truth_port.py`.

## Public API

- `truth.health`
- `truth.resolve_requirement`
- `truth.build_packet`
- `truth.check_sufficiency`
- `truth.detect_incomplete`
- `truth.validate_response`
- `truth.validate_execution`
- `truth.receipt`

## Integration law

File Intelligence must not only scan files. It must scan according to the truth requirement for the current intent.
