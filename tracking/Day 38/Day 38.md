
## --- DAY 38 UPDATE ---

**DAY 38 | COMPLETED | 32 min | Level: 4.0/5**

### Focus Topic

Reading Python Error Messages and Tracebacks.

### Session Notes

- Returned to the Python Bootcamp after approximately one week away.
- Learned how to interpret Python tracebacks:
  - Exception type: What error occurred?
  - Error location: Where the exception was raised?
  - Call chain: How execution reached the failing line?
- Reviewed Day 37 concepts: `raise`, `ValueError`, and input validation.
- Practiced distinguishing error locations from root causes.
- Independently implemented `get_average()` with empty-list validation.
- Initially used `return` instead of `raise`, then corrected the implementation after feedback.
- Successfully tested both scenarios:
  - Empty list → `ValueError`
  - Valid list → `Average: 3.0`
- Analyzed a `KeyError` caused by accessing a missing dictionary key.
- Completed the final traceback reconstruction task independently, correctly identifying the execution order of three nested functions and the exact failing statement.

### Minhyi Notes

- Initially struggled to recall exception-handling concepts after a one-week break.
- Correctly identified `ZeroDivisionError` but initially confused the calling statement with the actual error location.
- Initially used `return("Score cannot be empty")` instead of raising an exception.
- Understood the distinction after observing the terminal output and corrected the code using `raise ValueError(...)`.
- Successfully verified the resulting traceback in VS Code.
- Initially identified the wrong function when analyzing a `KeyError`, despite correctly understanding the missing-key problem.
- Correctly reconstructed the complete function call chain in the final task without assistance.
- Minor specification mismatch: used `"Score cannot be empty"` instead of the required `"Scores cannot be empty"`.

### Key Lesson

> A traceback reveals how execution reached an exception, while the final traceback frame identifies the exact failure location. Understanding the root cause requires examining the operation and its input values.

### Performance Evaluation

- Concept understanding: 4.0/5
- Coding correctness: 4.0/5
- Reasoning / problem decomposition: 4.0/5
- Independence: 4.0/5
- Debugging: 4.0/5

**Final Score: 4.0/5**

### Blank-Screen Performance

- Independently wrote a working average-calculation function with empty-list validation.
- Required one targeted correction to distinguish `return` from `raise`.
- Corrected the implementation independently after receiving feedback.
- Successfully tested the exception case and normal execution separately.
- Independently reconstructed the final three-function execution chain:

  `process_order()` → `calculate_total()` → `extract_price()`

- Correctly identified `return item["price"]` as the failure location.
- No full solution was provided for the final task.

### Progress Update

- Bootcamp Progress: Day 38 / 84
- Current Phase: Phase 3 — Functions + Program Decomposition
- Current Position: Can read common Python exceptions, identify their root causes, follow nested function calls, and implement basic input validation. Traceback interpretation is improving, although first-attempt accuracy still needs attention.

### Critical Weakness

> Sometimes confuses the function call that leads to an exception with the actual statement that raises it. Must consistently distinguish the call chain, failure location, and underlying cause.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi successfully demonstrated acceptable traceback-reading ability and independently completed the final call-chain investigation.

The initial mistakes were corrected, and no additional mandatory practice is required.

### Next Session

**Day 39 — Debugging Strategy**
