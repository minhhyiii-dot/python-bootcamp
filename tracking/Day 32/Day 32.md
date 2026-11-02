## --- DAY 32 UPDATE ---

**DAY 32 | COMPLETED | ≈ 21 min | Level: 4.7/5**

### Focus Topic

Local vs Global Scope in Python.

### Session Notes

* Learned the distinction between local and global variables.
* Correctly understood that local variables do not automatically modify global variables.
* Demonstrated understanding of Python's variable lookup behavior.
* Correctly identified an `UnboundLocalError` caused by referencing a local variable before assignment.
* Learned how the `global` keyword allows functions to modify global variables.
* Initially misunderstood how global modifications persist after a function returns.
* Completed the mandatory bank balance exercise independently.
* Successfully used a function to read a global variable without modifying it.

### Minhyi Notes

* Correctly predicted variable behavior when local and global names overlap.
* Explained that functions check their local scope before accessing global variables when appropriate.
* Correctly identified the cause of an `UnboundLocalError` without executing the code.
* Initially predicted that modifying a variable with `global` would not change its value outside the function.
* Corrected this misconception after reviewing the output.
* Completed the final coding task without assistance.

### Key Lesson

> Functions can read global variables without modifying them, while assignments inside functions normally create local variables unless explicitly declared global.

### Performance Evaluation

* Concept understanding: 4.5/5
* Coding correctness: 5.0/5
* Reasoning / problem decomposition: 4.7/5
* Independence: 5.0/5
* Debugging: 4.2/5

**Final Score: 4.7/5**

### Blank-Screen Performance

Independently implemented `preview_withdrawal(amount)`.

The solution:

* Accessed the global `balance`.
* Calculated the hypothetical withdrawal using a local variable.
* Returned the calculated value.
* Preserved the original balance.
* Produced the exact expected output.

No coding hints or debugging assistance were required.

### Progress Update

* Bootcamp Progress: Day 32 / 84
* Current Phase: Phase 3 — Functions + Program Decomposition
* Current Position: Can independently distinguish local and global scope, identify common scope-related errors, and write functions that preserve global state.

### Critical Weakness

> Needs to consistently recognize that modifying a global variable inside a function creates a persistent change visible outside that function.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi demonstrated acceptable independent understanding of Python variable scope and can proceed to Day 33.

### Next Session

**Day 33 — Functions with Lists / Dictionaries**
