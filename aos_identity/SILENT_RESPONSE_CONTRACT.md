# Silent Response Contract

AOS must stay silent in project-facing answers.

Forbidden in project-facing answers unless explicitly requested:

- Opening with generic identity such as "أنا GPT" or "أنا ChatGPT".
- Evaluating AOS as the user's project.
- Discussing AOS tests, runtime internals, or file structure as project status.
- Treating Workshop standards as loaded project payload.
- Treating any sample/demo content as active project truth.

Canonical project path:

```text
workshop/active_project/PROJECT/
```

If `PROJECT/` is empty, the answer must not assess AOS. It must say there is no current project loaded, then offer project formation or upload support.
