"""Run BFS/DFS tests. From this folder: python3 run_tests.py"""

import sys
import unittest

sys.path.insert(0, ".")  # resolve environment and algorithms when run from project root

loader = unittest.TestLoader()
suite = loader.loadTestsFromName("tests.test_algorithms_progress")
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
sys.exit(0 if result.wasSuccessful() else 1)
