## --- DAY 13 UPDATE ---

**DAY 13 | COMPLETED | 1 hr 3 min | Level: 4.6/5**

### Focus Topic

Basic debugging with errors and `print()`.

### Session Notes

- Practiced distinguishing three major categories of bugs:
  - syntax errors;
  - runtime errors;
  - logic errors.
- Correctly identified a missing `:` as a syntax error.
- Learned that valid Python syntax can still fail during execution, such as attempting arithmetic between an `int` and a `str`.
- Correctly identified multiple logic errors where Python executed successfully but produced the wrong result.
- Practiced manually tracing accumulator variables before running code.
- Used temporary `print()` statements to inspect program state inside loops.
- Improved debugging output from duplicated branch-specific `print()` statements into one shared state-tracing statement.
- Practiced tracking multiple relevant values together, especially the loop variable and accumulator/state variables.
- Learned to locate the **first incorrect state change** instead of focusing only on the final wrong output.
- Correctly diagnosed wrong-variable bugs, such as modifying the loop variable instead of the intended counter.
- Correctly diagnosed assignment-versus-accumulation bugs such as `total = n` instead of `total += n`.
- Learned the difference between `x =+ 3` and `x += 3`.
- Practiced reading `NameError` and checking whether the referenced variable had been defined before use.
- Revisited control-flow priority and confirmed that a terminating `break` condition must be checked before state-changing processing when the terminating item must not be counted.
- Completed the mandatory blank-screen task independently.
- Built a Security Event Processor using `range()`, `break`, `continue`, prioritized conditions, accumulators, and modulo conditions.
- Added a temporary debugging `print()` to inspect `risk_score`, `processed`, and the current event ID.
- Used the trace to verify state changes.
- Removed the temporary debugging statement and reran the clean final program.
- Final output matched the specification exactly:

```text
11
10
```

### Minhyi Notes

- Initially classified a runtime `TypeError` as a syntax error because the underlying cause was an unconverted string.
- Corrected the distinction between code that cannot be parsed and code that starts successfully but crashes during execution.
- Initially placed debugging `print()` statements separately inside both branches of an `if / else`.
- Corrected this by placing one shared debugging statement after the branch so every iteration could be inspected consistently.
- Correctly used state traces to identify which iterations were changing an accumulator incorrectly.
- Identified several bugs directly from code without relying on trial-and-error execution.
- Needed clarification once about what an "incorrect state change" meant; afterward, the distinction between the current loop value and the variables being mutated became clearer.
- Encountered `range(start, stop, step)` with a negative step for the first time and learned that the stop boundary remains excluded.
- Correctly challenged a weak debugging exercise that did not represent a meaningful practical situation.
- Correctly noticed that the session had accumulated too many guided micro-exercises without reaching the mandatory blank-screen task and enforced the bootcamp rule.
- The final blank-screen task required no implementation hint or solution code.

### Key Lesson

> Debugging is not randomly changing code until it works; inspect the program state, find the first place it becomes wrong, identify the responsible line, and fix the underlying cause.

### Performance Evaluation

- Concept understanding: **4.6/5**
- Coding correctness: **4.7/5**
- Reasoning / problem decomposition: **4.6/5**
- Independence: **4.7/5**
- Debugging: **4.7/5**

**Final Score: 4.6/5**

### Blank-Screen Performance

Minhyi independently wrote the final Security Event Processor from a blank screen.

The program correctly:

- initialized `risk_score` and `processed`;
- iterated through event IDs `301` through `315`;
- placed the corrupted-event termination rule first;
- stopped immediately at event `313`;
- skipped IDs divisible by `5` using `continue`;
- incremented `processed` only for events that survived both filters;
- gave IDs divisible by `4` the highest scoring priority;
- gave remaining IDs divisible by `3` the secondary score;
- applied the fallback penalty to all other processed events.

During debugging, Minhyi temporarily added:

```python
print(risk_score, processed, id)
```

The trace was used to verify the program's state transitions.

The debugging statement was then removed, and the clean program produced:

```text
11
10
```

No solution-level AI assistance was required for the final implementation.

### Progress Update

- Bootcamp Progress: **Day 13 / 84**
- Current Phase: **Phase 1 — Python Survival**
- Current Position: Can independently write small multi-rule Python programs and use error messages, manual tracing, and temporary `print()` statements to locate basic syntax, runtime, state-update, and control-flow bugs.

### Critical Weakness

> Debugging reasoning is becoming strong, but explanations of exactly which program state changed incorrectly can still be slightly imprecise; continue identifying the specific variable, how its value changed, and which line caused the change.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi demonstrated acceptable independent debugging ability, successfully used temporary state-tracing output, diagnosed multiple bug patterns, and completed the mandatory blank-screen task without solution-level assistance.

He can proceed to the next Day.

### Next Session

**Day 14 — CHECKPOINT 1: Python Survival Test**