## --- DAY 16 UPDATE ---

**DAY 16 | COMPLETED | 47 min | Level: 4.5/5**

### Focus Topic

String methods.

### Session Notes

- Learned and practiced common string methods:
  - `.upper()`
  - `.lower()`
  - `.strip()`
  - `.replace()`
  - `.count()`
  - `.find()`
  - `.startswith()`
  - `.endswith()`
- Learned that strings are **immutable**: string methods do not modify the existing string object in place.
- Understood that methods such as `.strip()`, `.lower()`, and `.replace()` return new values which can then be reassigned:

```python
text = text.strip()
text = text.lower()
```

- Correctly distinguished variable reassignment from modifying a string object.
- Learned that `.strip()` removes whitespace from the beginning and end of a string.
- Correctly used `.replace()` to create transformed strings.
- Learned that `.count()` returns the number of occurrences of a substring.
- Learned that `.find()` returns the starting index of the first occurrence and returns `-1` when the substring is absent.
- Correctly distinguished:
  - `text[-1]` → access the final character.
  - `text.find(...) == -1` → requested substring was not found.
- Practiced `.startswith()` and `.endswith()` as Boolean-returning methods.
- Combined multiple methods through sequential reassignment.
- Applied string normalization to user input using `.strip()` and `.lower()`, directly repairing the case-sensitivity weakness identified earlier in the bootcamp.
- Independently built a market-trend program accepting inputs with different capitalization and surrounding whitespace.
- Tested `bullish`, mixed-case `BuLlIsH`, `BEARISH`, spaced mixed-case input, and an unknown value.
- Completed the final unseen string-cleaning task using multiple methods together.
- Final mandatory-task output:

```text
error disk error
2
True
6
```

### Minhyi Notes

- Initially misunderstood `.strip()` because the English word "strip" was unfamiliar and machine translation did not describe its Python meaning clearly.
- Initially thought the transformed string `"MINHYI"` would regain spaces even though `.upper()` was being called on the already-stripped variable.
- Needed clarification on string immutability versus variable reassignment.
- Initially confused the `-1` returned by `.find()` with negative indexing such as `text[-1]`.
- After clarification, correctly explained:
  - `[-1]` means the final element when indexing.
  - `.find(...) == -1` means the substring was not found.
- During the final unseen task, initially wrote `"error"` without quotes inside `.count()`, causing a `NameError`, then corrected it independently.
- The final task initially used:

```python
message.count("disk")
```

instead of the required index lookup.
- After the requirement mismatch was identified, independently corrected it to:

```python
message.find("disk")
```

- The recurring issue remains less about understanding Python logic and more about reading the exact requested operation near the end of a task.

### Key Lesson

> String methods usually return a result rather than modifying the original string, so transformations must be stored or reassigned when they need to persist.

### Performance Evaluation

- Concept understanding: **4.6/5**
- Coding correctness: **4.4/5**
- Reasoning / problem decomposition: **4.5/5**
- Independence: **4.6/5**
- Debugging: **4.5/5**

**Final Score: 4.5/5**

### Blank-Screen Performance

Minhyi independently wrote two meaningful programs from a blank screen.

The first normalized user input using:

```python
market_trend = market_trend.strip()
market_trend = market_trend.lower()
```

and correctly used `if / elif / else` to classify bullish, bearish, and unknown market trends.

The final unseen task independently combined:

```python
.strip()
.lower()
.replace()
.count()
.startswith()
.find()
```

The overall transformation logic was correct.

Two mistakes occurred:

- an early missing-string-quotes `NameError`;
- using `.count("disk")` when the requirement requested the starting index.

Neither required a full solution. The final method mismatch was corrected after a narrow requirement-level hint.

### Progress Update

- Bootcamp Progress: **Day 16 / 84**
- Current Phase: **Phase 2 — Core Python Data Structures**
- Current Position: Can independently normalize and transform strings using common methods, distinguish returned values from mutation, search and count substrings, and combine multiple string methods in small programs.

### Critical Weakness

> Method knowledge is developing well, but exact requirement checking still drops near the finish line; before writing the final expression, identify whether the task asks for a value, count, Boolean, character, or index.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi demonstrated acceptable independent use of string methods, successfully combined them in unseen tasks, and corrected mistakes without solution-level assistance.

He can proceed to the next Day.

### Next Session

**Day 17 — Lists: creation, indexing, mutation**