# AOS First Operating Entry

This is the first file a new model should read before inspecting code, capabilities, or project payload.

## First-touch sequence

1. Load operating identity from `aos_identity/START_WORK_OPERATING_MESSAGE.md` and `aos_identity/OPERATIONAL_IDENTITY.md`.
2. Resolve the user's intent.
3. Resolve the visible surface: AOS, Workshop, or Active Project.
4. Resolve the required truth depth.
5. Only then use the Artifact Cockpit / File Intelligence if the request needs evidence.
6. Deliver a truth-grounded answer without exposing internal paths or generic model identity unless explicitly asked.

## Important

`aos.py` is a CLI adapter, not the reasoning entrypoint. If you opened `aos.py` first, return here and load the operating identity before reading implementation files.

File Intelligence is not first awareness. It is a cockpit used after identity, intent, surface, and truth requirement are resolved, except for explicit diagnostic commands such as inspect/doctor.

## Critical model-entry correction

For normal user questions, do not begin by inspecting files. Run the hot answer path first:

```bash
python aos.py answer "<user question>"
```

`inspect`, `doctor`, and test commands are explicit diagnostic tools only.

## Intent Cognition

After operating identity, build operational cognition from the user's request. This is not a route table. It decides what truth, evidence, and goal handling are needed while keeping the system on one spine.


## Operations Runtime Kernel

The single operating spine is the Operations Runtime Kernel. Do not enter capabilities directly. Identity, intent, truth, artifact intelligence, goal tracking, and delivery operate behind the Runtime Kernel and return contributions. Visible answers must come from Operational Insight, not raw layer reports.
