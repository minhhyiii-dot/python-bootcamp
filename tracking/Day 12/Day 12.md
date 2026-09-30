## --- DAY 12 UPDATE ---

**DAY 12 | COMPLETED | 54 min 48.44 sec | Level: 4.5/5**

### Focus Topic

Combining conditions + loops.

### Session Notes

- Practiced combining previously learned control-flow tools:
  - `for`
  - `range()`
  - `if / elif / else`
  - Boolean conditions
  - modulo
  - accumulators
  - `break`
  - `continue`
- Began with manual loop tracing and initially made two reading mistakes:
  - skipped several iterations that affected an accumulator;
  - incorrectly applied later scoring logic even when `continue` should have skipped the rest of an iteration.
- Corrected both traces after slowing down and evaluating the loop one iteration at a time.
- Independently completed a blank-screen number-processing task with correct condition priority.
- Completed a contextual Security Event Scanner with the overall control-flow structure correct.
- In that exercise, accidentally wrote:

```python
id -= 1
```

instead of:

```python
threat_score -= 1
```

- This was a finish-line checking mistake rather than a misunderstanding of the overall logic.
- Corrected the wrong-variable bug immediately after it was identified.
- Completed the final Fraud Detection Queue from a contextual specification without step-by-step implementation instructions.
- Correctly handled overlapping rules:
  - transaction `729` stopped the loop;
  - IDs divisible by `10` were ignored;
  - ignored transactions did not increase `reviewed`;
  - high-range even transactions received a different score from normal even transactions;
  - odd multiples of `7` overrode the normal odd penalty.
- Final challenge produced:

```text
30
26
```

- No structural hint or solution code was required for the final challenge.
- After completing the task, independently noticed duplicated logic because:

```python
reviewed += 1
```

appeared in every scoring branch.
- Correctly reasoned that `reviewed += 1` represents a rule shared by every transaction that survives the `break` and `continue` filters.
- Learned a cleaner control-flow structure:

```text
termination filter
→ skip filter
→ shared processing
→ classification
```

- Learned why two independent `if` statements can sometimes replace `if / elif` when the first branch unconditionally executes `break` or `continue`.
- During refactoring, produced:

```text
IndentationError: unexpected indent
```

because `reviewed += 1` was accidentally moved outside the `for` loop while the following scoring block remained indented.
- Correctly understood that `reviewed += 1` and the scoring logic must remain at the same indentation level inside the loop.
- Successfully reran the refactored program with the same correct result.
- Exercise design was adjusted during the session after Minhyi identified that highly ordered English instructions were effectively pseudocode disguised as a problem statement.
- Future challenges should provide contextual requirements and require Minhyi to independently determine the implementation structure.

### Minhyi Notes

- Early mistakes were mainly caused by reading and tracing too quickly rather than lacking knowledge of Python syntax.
- Initially skipped iterations while manually tracing loops.
- Initially misunderstood how `continue` prevented later statements in the same iteration from executing.
- Recognized that requirements written in implementation order provide too much guidance.
- Requested future challenges to avoid obvious step-by-step structures and instead use more realistic contextual problem specifications.
- Future exercises should require independent decisions about:
  - condition priority;
  - loop structure;
  - placement of `break` and `continue`;
  - accumulator placement;
  - translation of business rules into code.
- Identified a recurring personal pattern: once a solution feels almost finished, tends to rush the final few lines.
- This finish-line rushing directly caused the `id -= 1` mistake.
- Adopted a short final-check habit:

> **wrong variable → wrong operator/condition → exact output requirement**

- Applied better checking discipline on the final challenge and completed it correctly.
- Showed good refactoring intuition by questioning why `reviewed += 1` had to be repeated across several branches.
- Began recognizing the separation between:
  - deciding whether an item should be processed;
  - performing shared processing;
  - classifying the surviving item.
- The later indentation mistake reinforced that Python indentation represents program structure, not merely visual formatting.

### Key Lesson

> In multi-rule loops, first decide which items should stop or skip processing, then perform shared work once, and only afterward classify the surviving items.

### Performance Evaluation

- Concept understanding: **4.6/5**
- Coding correctness: **4.4/5**
- Reasoning / problem decomposition: **4.6/5**
- Independence: **4.7/5**
- Debugging: **4.4/5**

**Final Score: 4.5/5**

### Blank-Screen Performance

Minhyi independently completed multiple contextual loop-and-condition tasks during the session.

The strongest blank-screen performance was the final Fraud Detection Queue.

Initial independent solution:

```python
risk_score = 0
reviewed = 0

for id in range(700, 735):
    if id == 729:
        break
    elif id % 10 == 0:
        continue
    elif id % 2 == 0 and id > 720:
        reviewed += 1
        risk_score += 5
    elif id % 2 == 0:
        reviewed += 1
        risk_score += 2
    elif id % 2 != 0 and id % 7 == 0:
        reviewed += 1
        risk_score += 3
    else:
        reviewed += 1
        risk_score -= 1

print(risk_score)
print(reviewed)
```

Output:

```text
30
26
```

Afterward, Minhyi independently questioned the repeated `reviewed += 1` statements and understood the cleaner refactoring:

```python
risk_score = 0
reviewed = 0

for id in range(700, 735):
    if id == 729:
        break

    if id % 10 == 0:
        continue

    reviewed += 1

    if id % 2 == 0 and id > 720:
        risk_score += 5
    elif id % 2 == 0:
        risk_score += 2
    elif id % 7 == 0:
        risk_score += 3
    else:
        risk_score -= 1

print(risk_score)
print(reviewed)
```

The first refactoring attempt temporarily contained an indentation error, but after understanding the structural issue, the corrected version executed successfully with the same result.

### Progress Update

- Bootcamp Progress: **Day 12 / 84**
- Current Phase: **Phase 1 — Python Survival**
- Current Position: Can independently translate contextual multi-rule problems into loops with prioritized conditions, filtering, accumulators, `break`, and `continue`, and is beginning to recognize opportunities to refactor duplicated logic into cleaner program structure.

### Critical Weakness

> When the main reasoning feels complete, checking discipline tends to drop near the finish line, causing avoidable wrong-variable, indentation, or requirement-checking mistakes despite otherwise correct logic.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi demonstrated acceptable independent use of conditions combined with loops, successfully handled overlapping rules, completed the final challenge without structural assistance, and showed early refactoring awareness.

He can proceed to the next Day.

### Next Session

**Day 13 — Basic debugging with errors and `print()`**