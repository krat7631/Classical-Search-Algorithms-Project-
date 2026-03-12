# Main project

Progress-report snapshot: grid world + BFS + DFS with shared resource constraints (max_depth, max_expansions, time_budget). Kept separate from the full Final project.

- `environment/` — grid world, State, SearchResult, build_path
- `algorithms/` — SearchConstraints, bfs, dfs
- `main_progress.py` — **entry point for this Halfway deliverable**; run BFS and DFS on default 5×5 grid with optional constraints (the full Final project uses `main.py` instead)
- `tests/test_algorithms_progress.py` — path finding + constraint behaviour tests
- `run_tests.py` — runs the progress test suite (no pytest needed)

---

## How to run

**Upload the whole folder** as-is (no installs needed — Python 3 standard library only). Then **run everything from inside this folder** so imports and tests work.

```bash
cd "Main Project"
```

All commands below assume you are in that directory.

### 1. Baseline (no constraints) — proves both algorithms run and find a path

Shows that BFS and DFS both find a path and we report path_cost, nodes_expanded, and runtime.

```bash
python3 main_progress.py
```

Example output:
```
bfs: found=True, path_cost=8.0, nodes=18, time=0.000035s
dfs: found=True, path_cost=8.0, nodes=17, time=0.000024s
```

### 2. With max_depth — proves depth constraint and failure_reason

When the goal is beyond the depth limit, both algorithms stop and report `failure_reason=depth_limit`.

```bash
python3 main_progress.py --max-depth 3
```

Example output:
```
bfs: found=False, path_cost=0.0, nodes=7, time=0.000020s, fail=depth_limit
dfs: found=False, path_cost=0.0, nodes=7, time=0.000011s, fail=depth_limit
```

### 3. With max_expansions — proves expansion limit

Caps how many nodes we expand; when hit before finding the goal we report `failure_reason=expansion_limit`.

```bash
python3 main_progress.py --max-expansions 10
```

### 4. With time_budget — proves time constraint

Stops after a wall-clock time limit; when hit we report `failure_reason=time_budget`.

```bash
python3 main_progress.py --time-budget 0.001
```

On the default 5×5 grid, search finishes in tens of microseconds, so 0.001s is rarely exceeded and you usually see a path found. To see `failure_reason=time_budget`, use a much smaller budget (e.g. `--time-budget 0.00001`) or a larger grid.

### 5. JSON output — structured output for later analysis

Same run as baseline but prints one JSON object per algorithm (solution_found, path_cost, nodes_expanded, runtime_seconds, failure_reason). Use this to pipe results to a file or to show we can export metrics.

```bash
python3 main_progress.py --format json
```

To save to a file:
```bash
python3 main_progress.py --format json > results.json
```

### 6. Combined constraints + JSON (more complex run)

Runs with both a depth limit and JSON output so we get structured data under constraints. Example: depth limit 4 and export to file.

```bash
python3 main_progress.py --max-depth 4 --format json
```

### 7. Run tests — proves path finding and constraint behaviour

Runs the unit tests: BFS/DFS find a path when unconstrained, and both respect max_depth and max_expansions and set the correct failure_reason.

```bash
python3 run_tests.py
```

Example output:
```
test_bfs_finds_path_without_constraints ... ok
test_bfs_respects_max_depth ... ok
test_dfs_finds_path_without_constraints ... ok
test_dfs_respects_max_expansions ... ok

Ran 4 tests in 0.000s
OK
```

---

## Summary: what these commands prove

| Command | What it shows |
|--------|----------------|
| `main_progress.py` | BFS and DFS implemented; both find path; we report path_cost, nodes_expanded, runtime. |
| `--max-depth 3` | Resource constraint (depth) works; failure_reason = depth_limit when no path. |
| `--max-expansions 10` | Expansion limit works; failure_reason = expansion_limit when hit. |
| `--time-budget 0.001` | Time limit works; failure_reason = time_budget when hit. |
| `--format json` | We can output structured metrics (for analysis / progress report). |
| `run_tests.py` | Path finding and constraint behaviour are tested and pass. |
