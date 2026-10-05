## --- DAY 14 UPDATE ---

**DAY 14 | COMPLETED | ≈57 min | Level: 4.5/5**

### Focus Topic

**CHECKPOINT 1 — Python Survival Test**

### Session Notes

- Completed the Phase 1 checkpoint covering:
  - output prediction;
  - debugging a broken program;
  - multiple blank-screen coding tasks;
  - one unseen logic problem.
- Practiced mental execution involving `for`, `range()`, `break`, `continue`, and accumulator variables.
- Initially forgot that `score` started at `2` during the first output-prediction task.
- After noticing the missed initial state, corrected the trace independently to:

```text
2
→ 1
→ 3
→ 2
→ 6
```

- Correctly solved the second output-prediction task with:
  - final output `14`;
  - correct understanding that `continue` prevents the accumulator update for that iteration.
- Debugged a broken ID-processing program.
- Correctly identified that the termination rule:

```python
if id == 105:
    break
```

must be checked before:

```python
if id % 5 == 0:
    continue
```

because otherwise `105` satisfies the divisibility rule first and skips the `break`.
- Independently corrected another bug from:

```python
id -= 1
```

to:

```python
score -= 1
```

although this second bug was not consciously identified during the first verbal debugging pass.
- Clarified that modifying the loop variable inside a `for` loop does not modify the sequence that the loop will use on the next iteration.
- Completed Blank-Screen Task 1 independently using:
  - `range()`;
  - `break`;
  - `continue`;
  - a processed counter;
  - prioritized scoring conditions.
- Correctly structured the program as:

```text
termination filter
→ skip filter
→ shared processing
→ scoring rule
```

- Blank-Screen Task 1 produced the correct output:

```text
3
9
```

- Initially believed that `while` loops had never been studied.
- Review of previous progress showed that `while` had been covered on Day 10.
- Despite weak explicit recall, independently reconstructed a correct `while` loop from a raw specification.
- Completed the replacement `while` task correctly with output:

```text
4
4
```

- Temporarily wrote:

```python
print(round)
```

instead of:

```python
print(rounds)
```

which caused Python to display the built-in `round` function.
- Identified and corrected that naming mistake independently.
- Completed the final unseen logic problem from a blank screen.
- The first execution incorrectly used:

```python
while char in signal:
```

before `char` had been defined, causing a `NameError`.
- Independently corrected the iteration structure to:

```python
for char in signal:
```

without requesting an AI hint.
- Correctly implemented:
  - immediate termination at `"X"`;
  - skipping `"-"`;
  - processed counting;
  - `"A"` scoring;
  - `"B"` scoring.
- Final unseen-problem output was:

```text
1
3
```

- No solution-level AI assistance was required for the final unseen task.

### Minhyi Notes

- The first output-prediction mistake came from forgetting the initial value of the accumulator rather than misunderstanding the loop itself.
- Coding intuition sometimes identified and fixed a bug before the exact reason for the bug could be verbally explained.
- `while` showed a significant retrieval gap:
  - the concept initially felt completely unfamiliar;
  - however, the ability to write a working `while` loop was still retained.
- This suggests that the practical skill was stronger than explicit recall of the topic name.
- The final unseen problem produced a genuine runtime error on the first attempt, but the error was repaired independently.
- Small mistakes involving variable names, initial values, and exact requirement checking remain more common than major reasoning failures.
- Questioned a poorly designed checkpoint problem when its final state was effectively predetermined; the task was replaced and was not counted negatively.

### Key Lesson

> Knowing the main control-flow logic is no longer the biggest problem; reliable state tracking, retrieval, and careful final checking now matter more.

### Performance Evaluation

- Concept understanding: **4.5/5**
- Coding correctness: **4.4/5**
- Reasoning / problem decomposition: **4.6/5**
- Independence: **4.7/5**
- Debugging: **4.6/5**

**Final Score: 4.5/5**

### Blank-Screen Performance

Minhyi completed the main checkpoint coding tasks without seeing final solutions first.

He independently wrote:

- a `for`-loop transaction processor using termination and skip filters;
- a `while`-based state-reduction program;
- an unseen character-stream processor combining iteration, `break`, `continue`, counters, and accumulators.

For the final unseen problem, the first attempt contained:

```python
while char in signal:
```

which caused a `NameError` because `char` had not yet been defined.

Minhyi independently changed the iteration mechanism to:

```python
for char in signal:
```

and completed the program successfully.

Final output:

```text
1
3
```

No solution-level AI assistance was required.

### Progress Update

- Bootcamp Progress: **Day 14 / 84**
- Current Phase: **Phase 1 — Python Survival — COMPLETED**
- Current Position: Can independently write small Python programs using variables, operators, basic types, Boolean logic, conditional branching, `for` loops, `while` loops, `range()`, `break`, `continue`, accumulators, and basic debugging techniques.

### Critical Weakness

> Core programming logic is independently usable, but initial-state tracking and retrieval of less-recently-practiced concepts can still fail under pressure; before coding, explicitly identify the starting state, controlling variable, termination rule, and exact required output.

### Session Verdict

**COMPLETED — CHECKPOINT 1 PASSED**

The Phase 1 learning objective was achieved.

Minhyi demonstrated acceptable independent programming ability across the checkpoint and repaired multiple mistakes without solution-level assistance.

**Phase 1 — Python Survival is cleared.**

### Next Session

**Day 15 — Strings: indexing and basic operations**