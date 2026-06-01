# Workspace Layer Identity

The Workspace layer resolves stable operating locations. It does not decide project truth.

## Purpose

Maintain the stable project gateway contract:

```text
workshop/active_project/PROJECT/
```

This path is the only active project payload gate.

## Rules

- `workshop/active_project/` is a slot, not a project.
- `PROJECT/` may be empty; empty means no current project loaded.
- Project names inside `PROJECT/` are discovered payload facts, not AOS runtime constants.
- AOS must not hardcode sample or test project names as truth.

## Output

The Workspace layer exposes project loading state:

```text
no_project_loaded
single_project_detected
unformed_or_scattered_project
multi_project_ambiguity
project_path_missing
slot_missing
```
