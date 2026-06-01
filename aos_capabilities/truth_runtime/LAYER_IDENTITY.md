# Truth Runtime Layer Identity

Truth Runtime is the reasoning governor that decides what kind of truth is required before AOS may answer, plan, or execute.

## Purpose

Truth Runtime prevents the agent from behaving like a blind reader of files. It defines the required truth depth, builds evidence packets, detects incomplete truth, and validates response/execution grounding.

## Core Philosophy

Truth is not file size, file name, or the first matching document.

A small note file may carry higher authority than a large document if it is a canon, decision, contract, layer identity, or project truth file. A large file may still be weak truth if it is duplicated, placeholder-like, contradicted, or misaligned with higher project truth.

## Truth Layers

1. Literal Truth — direct text, path, symbol, route, field.
2. Structural Truth — owner, layer, folder, artifact role.
3. Relational Truth — dependencies, neighboring domains, callers, consumers, tests, APIs, database mappings.
4. Intent Truth — what truth depth the user request requires.
5. Project Truth — local project identity, goals, canons, decisions, accepted standards.
6. Canon Truth — cross-cutting rules that govern writing, code, docs, and construction.
7. Incomplete Truth — documented but weak, duplicated, contradicted, placeholder, or insufficient truth.
8. Executable Truth — enough verified/derived evidence to safely answer or execute.

## Law

No answer or implementation may rely on a narrow artifact if the intent requires relational truth.

## Relationship with File Intelligence

File Intelligence discovers and extracts evidence. Truth Runtime tells it what kind of evidence is required, how to classify it, and whether it is sufficient.

## Relationship with Surface

Surface decides what may be visible in the answer. Truth Runtime decides what must be true before the answer or execution is allowed.

## Failure Signals

- Response based on one file while intent is cross-domain.
- Executing from duplicated or placeholder artifacts.
- Treating generated index or cache as source truth.
- Treating a large file as more authoritative purely because it is large.
- Treating a workshop general standard as project-specific truth before localization.
- Ignoring small high-value files such as canons, contracts, layer identities, or decisions.

## Truth Value Semantics

Truth Runtime now distinguishes:

- empty declared construction targets: planned owners that must be matured, not ignored;
- declared-but-missing artifacts: broken truth promises;
- required new truth artifacts: legitimate new owner files that may be proposed/created through construction gates;
- truth story: a compact explanation of meaning, value, relation, and sufficiency before response/execution;
- hot truth packets: fast, compact evidence packets for normal answers without sacrificing deep truth.

The layer must not rank truth by file size. It must rank truth by authority, provenance, relation, intent, canon status, and alignment with higher truth.
