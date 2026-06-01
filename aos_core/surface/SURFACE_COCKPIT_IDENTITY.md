# Surface Cockpit Identity

The Surface layer must not route the model into a narrow tunnel.

Its role is to bind the request to a visible answer surface while preserving governed internal awareness.

## Core distinction

```text
Intent = what the user is asking for.
Visible surface = what the answer may be about.
Allowed internal scopes = what AOS may silently inspect to avoid partial truth.
Artifact Cockpit = the governed 360-degree file/runtime view.
```

## Law

Surface selection controls visibility, not blindness.

A project-facing request may use AOS and Workshop silently as operating and maturity lenses, but the visible answer must remain about the active project payload.

## Default behavior

- Project work answers about `active_project_payload`.
- Workshop questions answer about `workshop_general_truth`.
- AOS questions answer about `aos_environment`.

## Forbidden behavior

- Do not treat intent classification as a single-path tunnel.
- Do not expose AOS internals in project-facing answers.
- Do not treat Workshop standards as active project evidence.
- Do not evaluate `workshop/active_project/` as the project; only `PROJECT/` is the payload gate.
