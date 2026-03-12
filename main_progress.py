"""Run BFS and DFS on default grid with optional constraints."""

import argparse
import json
from typing import List

from environment.grid_world import GridWorld
from algorithms.base import SearchConstraints
from algorithms.bfs import bfs
from algorithms.dfs import dfs

# 5x5 grid: 0 = free, 1 = obstacle. Start (0,0), goal (4,4).
DEFAULT_GRID = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
]
DEFAULT_START = (0, 0)
DEFAULT_GOAL = (4, 4)


def run_algorithms(algorithms: List[str], constraints: SearchConstraints, fmt: str) -> None:
    """Run the selected algorithms (bfs/dfs) on the default grid."""
    env = GridWorld(DEFAULT_GRID, DEFAULT_START, DEFAULT_GOAL)
    results = []

    for name in algorithms:
        if name.lower() == "bfs":
            r = bfs(env, constraints)
        elif name.lower() == "dfs":
            r = dfs(env, constraints)
        else:
            continue

        # failure_reason is set only when solution_found is False (e.g. depth_limit, expansion_limit, time_budget, exhausted)
        results.append(
            {
                "algorithm": name.lower(),
                "solution_found": r.solution_found,
                "path_cost": r.path_cost,
                "nodes_expanded": r.nodes_expanded,
                "runtime_seconds": r.runtime_seconds,
                "failure_reason": r.failure_reason,
            }
        )

    if fmt == "json":
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            # Only show failure_reason when search did not find a path
            fail = f", fail={r['failure_reason']}" if r["failure_reason"] else ""
            print(
                f"{r['algorithm']}: found={r['solution_found']}, "
                f"path_cost={r['path_cost']}, nodes={r['nodes_expanded']}, "
                f"time={r['runtime_seconds']:.6f}s{fail}"
            )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Progress-report runner: BFS/DFS with resource constraints"
    )
    parser.add_argument("--max-depth", type=int, default=None, help="Max search depth")
    parser.add_argument(
        "--max-expansions", type=int, default=None, help="Max node expansions"
    )
    parser.add_argument(
        "--time-budget", type=float, default=None, help="Time budget in seconds"
    )
    parser.add_argument(
        "--algorithms",
        nargs="+",
        default=["bfs", "dfs"],
        help="Algorithms to run (default: bfs dfs)",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )
    args = parser.parse_args()

    constraints = SearchConstraints(
        max_depth=args.max_depth,
        max_expansions=args.max_expansions,
        time_budget_seconds=args.time_budget,
    )

    run_algorithms(args.algorithms, constraints, args.format)


if __name__ == "__main__":
    main()
