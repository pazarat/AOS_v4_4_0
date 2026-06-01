#!/usr/bin/env python3
"""AOS CLI adapter. It delegates to the root Operations Runtime Kernel, the single runtime entrypoint.

If a model opens this file first, it must stop treating code as first awareness
and load `00_READ_FIRST_OPERATING_ENTRY.md`, `AGENTS.md`, and the operating
identity files before inspecting capabilities or project payload.

Normal answer sequence is owned by operations_runtime graph: identity -> intent hypothesis -> layer API fan-out -> truth synthesis -> delivery.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from operations_runtime.main import OperationsKernel


def emit(data, verbose: bool) -> None:
    if isinstance(data, str):
        print(data)
        return
    if verbose:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        status = data.get('status') or data.get('project_condition') or data.get('intent_type') or ('passed' if data.get('passed') else 'done')
        print(status)


def main() -> int:
    parser = argparse.ArgumentParser(description='AOS CLI adapter. Use answer for normal prompts; inspect/doctor only for diagnostics.')
    parser.add_argument('--root', default='.', help='AOS root directory')
    sub = parser.add_subparsers(dest='cmd', required=True)

    for name in ['boot', 'self-check', 'awareness', 'simulate-entry']:
        p = sub.add_parser(name)
        p.add_argument('--verbose', action='store_true')

    inspect = sub.add_parser('inspect')
    inspect.add_argument('--query', default='')
    inspect.add_argument('--changed', nargs='*', default=[])
    inspect.add_argument('--scope', choices=['active_project', 'workshop', 'aos'], default='active_project')
    inspect.add_argument('--verbose', action='store_true')

    doctor = sub.add_parser('doctor')
    doctor.add_argument('--query', default='')
    doctor.add_argument('--changed', nargs='*', default=[])
    doctor.add_argument('--scope', choices=['active_project', 'workshop', 'aos'], default='active_project')
    doctor.add_argument('--verbose', action='store_true')

    intent = sub.add_parser('intent')
    intent.add_argument('text')
    intent.add_argument('--verbose', action='store_true')

    goal = sub.add_parser('goal')
    goal.add_argument('text')
    goal.add_argument('--verbose', action='store_true')

    packet = sub.add_parser('packet')
    packet.add_argument('text')
    packet.add_argument('--verbose', action='store_true')

    answer = sub.add_parser('answer')
    answer.add_argument('text')

    args = parser.parse_args()
    kernel = OperationsKernel(Path(args.root))

    if args.cmd == 'boot':
        emit(kernel.boot(), args.verbose)
    elif args.cmd == 'inspect':
        emit(kernel.inspect(query=args.query, changed_paths=args.changed, scope=args.scope), args.verbose)
    elif args.cmd == 'doctor':
        emit(kernel.doctor(query=args.query, changed_paths=args.changed, scope=args.scope), args.verbose)
    elif args.cmd == 'intent':
        emit(kernel.resolve_intent(args.text), args.verbose)
    elif args.cmd == 'goal':
        emit(kernel.plan_goal(args.text), args.verbose)
    elif args.cmd == 'packet':
        emit(kernel.operation_packet(args.text), args.verbose)
    elif args.cmd == 'answer':
        emit(kernel.answer(args.text), True)
    elif args.cmd == 'self-check':
        emit(kernel.self_check(), args.verbose)
    elif args.cmd == 'awareness':
        kernel.identity_sync.sync()
        from aos_core.config import load_json
        emit(load_json(kernel.paths.reports / 'operational_awareness_packet.json', {}), args.verbose)
    elif args.cmd == 'simulate-entry':
        emit(kernel.simulate_entry(''), args.verbose)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
