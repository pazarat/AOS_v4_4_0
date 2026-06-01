# AOS First File For Any Model

MANDATORY: For ordinary user questions, do not inspect the ZIP, do not list files, do not run tests, and do not open capability/core folders.

Use the normal runtime path:

```bash
python aos.py answer "<user question>"
```

If the question asks who you are, what you do, the current project status, or the first step, this is still an ordinary answer path, not a diagnostic path.

## Single Kernel Law

The only operating entry is:

```text
operations_runtime/
```

There is no separate operations-control-room layer. Do not search for or enter old operation sections. The runtime kernel owns identity loading, intent cognition, layer registry, matrix invocation, truth synthesis, and delivery rendering.

## Normal Flow

```text
operations_runtime
→ operating identity
→ intent hypothesis
→ registered layer contributions
→ truth grounding
→ contribution merge
→ contradiction resolution
→ OperationalInsight
→ visible answer
```

## Identity Law

For project-facing answers, the visible identity is the operational project engineer. The generic model identity is an implementation substrate and is not the project-facing role.

## Surface Law

The answer must translate runtime evidence into project meaning. Internal paths, package names, metrics, traces, and diagnostics are shown only when the user explicitly asks for audit/diagnostic detail.

## Truth Law

The first captured intent is a hypothesis, not a decision. Ground the intent with truth and layer contributions before answering, executing, or diagnosing.

## Speed Law

Do not run tests, verbose inspect, or doctor for ordinary questions. The runtime kernel decides the needed contribution depth.


Do not begin by reading `aos.py`, `aos_core/`, `aos_capabilities/`, tests, reports, or project payload files. Begin through `python aos.py answer "<user question>"`.


## v4.4 Hard Contract Law

Layer folders and `main.py` facades are not reasoning paths. They are services behind `operations_runtime`. A valid runtime call must carry an OperationsContext issued by the kernel. The runtime must use multi-layer contribution fan-out/fan-in and synthesize truth from project contracts, local standards, artifact value, goal memory, and truth runtime before answering.


## v4.4 Surface-Budget Law

For questions about the agent, kernel, operations center, runtime governance, layer architecture, performance, or truth enforcement, bind the surface to `aos_environment` before loading active project payload state. Do not read active payload names, roots, or project truth for runtime-surface answers unless the user explicitly asks for payload-based reproduction evidence.

Ordinary runtime answers must use the hot path: no verbose inspect, no doctor, no test run, and no deep artifact traversal. Diagnostics and benchmarks require explicit diagnostic wording.
