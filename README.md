# Planning Agent Starter (Python)

A minimal starter repo for building an **agent with explicit planning** (plan → execute → reflect) and an example CLI runner.

## What you get

- `agent/planning.py`: data structures + planner interface
- `agent/executor.py`: executes steps with tool stubs
- `agent/agent.py`: orchestration (plan → run → reflect)
- `examples/tasks.md`: sample tasks & expected plans
- `main.py`: run from CLI

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -e .
python main.py "Write a short release note for v1.2.0"
```

## Planning format

The agent produces a plan like:

1. Goal
2. Assumptions
3. Steps (actionable)
4. Success criteria

You can swap in your own LLM planner/tooling.

## License

MIT
