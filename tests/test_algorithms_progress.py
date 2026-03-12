"""BFS and DFS: path finding + that constraints (depth, expansions) are respected and failure_reason is set."""

import unittest

from environment.grid_world import GridWorld
from algorithms.base import SearchConstraints
from algorithms.bfs import bfs
from algorithms.dfs import dfs


class TestBFSDFSProgress(unittest.TestCase):
    def setUp(self) -> None:
        self.grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
        ]
        self.start = (0, 0)
        self.goal = (4, 4)
        self.env = GridWorld(self.grid, self.start, self.goal)

    def test_bfs_finds_path_without_constraints(self) -> None:
        result = bfs(self.env)
        self.assertTrue(result.solution_found)
        self.assertGreater(result.path_cost, 0.0)

    def test_dfs_finds_path_without_constraints(self) -> None:
        result = dfs(self.env)
        self.assertTrue(result.solution_found)
        self.assertGreater(result.path_cost, 0.0)

    def test_bfs_respects_max_depth(self) -> None:
        # With max_depth=1 we only expand start and its neighbours; goal (4,4) is unreachable at depth 1
        constraints = SearchConstraints(max_depth=1)
        result = bfs(self.env, constraints)
        self.assertFalse(result.solution_found)
        self.assertEqual(result.failure_reason, "depth_limit")

    def test_dfs_respects_max_expansions(self) -> None:
        # With max_expansions=1 we expand only the start node, so we never reach the goal
        constraints = SearchConstraints(max_expansions=1)
        result = dfs(self.env, constraints)
        self.assertFalse(result.solution_found)
        self.assertEqual(result.failure_reason, "expansion_limit")


if __name__ == "__main__":
    unittest.main()
