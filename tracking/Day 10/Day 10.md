## --- DAY 10 UPDATE ---

**DAY 10 | COMPLETED | 38 min 34 sec | Level: 4.5/5**

### Focus Topic

`while` loops, dynamic state changes, and condition-driven execution.

### Session Notes

- Transitioned from sequence-based `for` loops to condition-based `while` loops.
- Explored the mechanical risk of infinite loops if the evaluated condition is never updated to `False`.
- Combined Day 8 conditional logic (`if/elif/else`) inside a Day 10 `while` loop to apply dynamic updates to variables.
- Successfully built a Collatz sequence generator based on a raw problem specification without step-by-step guidance.
- Corrected a data type mutation issue by replacing standard division (`/`) with integer division (`//`) to prevent unwanted float conversions.
- Clarified the conceptual difference between loop types: `for` loops process known collections, while `while` loops wait for a specific condition to change.

### Minhyi Notes

- Made a case-sensitivity error (`empty` instead of `Empty`) during a mental execution exercise.
- Correctly called out the mentor for spoon-feeding logical steps and demanded a raw problem specification for the final challenge.
- Successfully translated the raw Collatz sequence rules into a working script independently.
- Initially masked a float conversion by wrapping the variable in `print(int(n))` instead of fixing the root mathematical operator, but understood and implemented the `//` correction when challenged.
- Asked for and locked in a better mental model for deciding when to use `for` vs `while`.

### Key Lesson

> Use a `for` loop to process a known collection of items, and use a `while` loop to repeat an action until a specific condition evaluates to `False`.

### Performance Evaluation

- Concept understanding: 4.5/5
- Coding correctness: 4.3/5
- Reasoning / problem decomposition: 4.8/5
- Independence: 4.5/5
- Debugging: 4.5/5

**Final Score: 4.5/5**

### Blank-Screen Performance

Minhyi independently wrote the Collatz sequence program from a raw, unstructured problem specification. The script correctly initialized the `while` loop, evaluated even/odd states using modulo, updated the variable dynamically, and terminated accurately. No AI hints or logic corrections were required for the sequence logic. The only intervention was correcting the use of `/` to `//` to maintain strict integer types in memory.

### Progress Update

- Bootcamp Progress: Day 10 / 84
- Current Phase: Phase 1 — Python Survival
- Current Position: Can independently write `while` loops from unstructured requirements, avoid infinite execution, and nest conditional logic inside loops to handle dynamic mathematical updates.

### Critical Weakness

> Tends to use formatting or type-casting (like `int()`) to hide unwanted data types at the output level instead of fixing the operation (like `//`) that mutated the data type in memory.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi demonstrated acceptable independent use of `while` loops combined with conditional logic and mathematical operators.

### Next Session

**Day 11 — `range()` and loop control**