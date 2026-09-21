## --- DAY 2 UPDATE ---

**DAY 2 | COMPLETED | ≈ 1 hour | Level: 4.4/5**

### Focus Topic

**Variables and assignment**

### Session Notes

- Practiced creating variables and assigning values with `=`.
- Correctly understood that `=` represents assignment rather than mathematical equality.
- Practiced reassigning variables and tracking how their values change over time.
- Correctly explained why:

```python
score = 10
score = 15
```

results in `score` containing `15`.

- Connected reassignment with the accumulator-style pattern:

```python
sum = sum + n
```

and understood that Python first evaluates the current value on the right side before assigning the new result back to the variable.

- Correctly reasoned through variable copying:

```python
a = 10
b = a
a = 20
```

and understood that `b` remains `10` because it received the current value of `a` at the time of assignment.

- Practiced valid Python variable naming.
- Initially made mistakes with `_user` and `2user`, then corrected the rule:
  - variable names may begin with `_`;
  - variable names cannot begin with a number;
  - spaces and `-` are not valid inside normal variable names;
  - Python keywords such as `class` cannot be used as variable names.
- Completed the final blank-screen task independently after disabling AI autocomplete in the bootcamp workspace.
- No full-solution AI assistance was required.

### Minhyi Notes

- Initially thought `_user` was invalid and `2user` was valid.
- Needed clarification on Python variable naming rules.
- Accidentally typed `current_balace` instead of `current_balance`.
- The typo was logically harmless because it was used consistently, but it did not match the required variable name.
- Noticed that VS Code AI inline suggestions could reveal answers before an independent attempt was completed.
- Chose to disable AI features for the bootcamp workspace so future blank-screen exercises remain genuinely independent.
- Reasoning about reassignment felt intuitive because it connected with prior exposure to patterns such as `sum = sum + n`.

### Key Lesson

> A variable name refers to its currently assigned value, and reassignment replaces that value without automatically changing variables that copied an earlier value.

### Performance Evaluation

- Concept understanding: **4.5/5**
- Coding correctness: **4.5/5**
- Reasoning / problem decomposition: **4.5/5**
- Independence: **4.5/5**
- Debugging: **4.0/5**

**Final Score: 4.4/5**

### Blank-Screen Performance

Minhyi independently wrote the final task:

```python
bank_balance = 1000

old_balance = bank_balance

bank_balance = 1500

current_balance = bank_balance

print(old_balance)
print(bank_balance)
print(current_balance)
```

Expected output:

```text
1000
1500
1500
```

The assignment logic was correct.

The first version contained one naming typo:

```python
current_balace
```

After the mistake was identified, Minhyi corrected it to:

```python
current_balance
```

AI autocomplete had been disabled before the final attempt, so the completed final solution was written without inline AI code suggestions.

### Progress Update

- Bootcamp Progress: **Day 2 / 84**
- Current Phase: **Phase 1 — Python Survival**
- Current Position: Can create, copy, and reassign simple variables independently while mentally tracking their current values.

### Critical Weakness

> Variable-assignment reasoning is solid, but small naming and typing mistakes can still cause avoidable errors, so variable names need to be checked more carefully before considering a task finished.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi demonstrated acceptable independent use of variables and assignment and can proceed to the next Day.

### Next Session

**Day 3 — Core data types: `int`, `float`, `str`, `bool`**