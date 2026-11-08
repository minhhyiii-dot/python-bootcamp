
## --- DAY 37 UPDATE ---

**DAY 37 | COMPLETED | 21 min 36 sec | Level: 4.8/5**

### Focus Topic

Raising and Validating Invalid Input — `raise`

### Session Notes

- Learned how to deliberately trigger exceptions using `raise`.
- Understood the difference between `raise` and `try/except`:
  - `raise` deliberately triggers an exception.
  - `try/except` handles an exception.
- Learned that raising an exception interrupts normal function execution unless the exception is caught.
- Practiced using `ValueError` to enforce function requirements.
- Completed two coding exercises independently:
  - `calculate_area()` — validates positive rectangle dimensions before calculating area.
  - `withdraw()` — validates account balance, withdrawal amount, and sufficient funds.
- Correctly used conditional statements to enforce multiple validation rules.
- Used specific exception messages to communicate why an input was rejected.
- Demonstrated correct validation order and return behavior.

### Minhyi Notes

- Completed both exercises independently without starter code or AI hints.
- Correctly implemented `raise ValueError()` with the exact required messages.
- Used separate `if` statements in `calculate_area()` and an `if/elif` chain in `withdraw()`.
- Successfully distinguished valid results from intentionally raised exceptions.
- Understood that red traceback messages were expected behavior for invalid inputs, not implementation bugs.
- Tested multiple valid and invalid inputs through VS Code.
- No syntax errors or significant logical mistakes were observed.
- Recognized when further testing was unnecessary after reviewing the implementation and observed results.
- Completed the session efficiently without extending practice beyond the learning objective.

### Key Lesson

> Use `raise` to enforce function requirements and reject invalid inputs before they produce incorrect results; raising an exception interrupts normal execution unless the exception is handled.

### Performance Evaluation

- Concept understanding: 4.8/5
- Coding correctness: 5.0/5
- Reasoning / problem decomposition: 4.8/5
- Independence: 5.0/5
- Debugging: 4.4/5

**Final Score: 4.8/5**

### Blank-Screen Performance

Independently implemented both functions without receiving setup code, pseudocode, or solution-level assistance.

**Exercise 1 — `calculate_area()`**

- Validated both dimensions using `<= 0`.
- Raised `ValueError` with the required message.
- Returned the calculated area for valid dimensions.
- Successfully demonstrated all four required test cases.

**Exercise 2 — `withdraw()`**

- Rejected negative account balances.
- Rejected zero and negative withdrawal amounts.
- Rejected withdrawals exceeding the available balance.
- Returned the remaining balance for valid transactions.
- Correctly prioritized validation conditions.
- Demonstrated three test scenarios through execution.
- The remaining specified scenarios were supported by the implementation logic but were not separately demonstrated.

Both implementations were logically correct on the first submitted attempt.

No AI debugging assistance or code corrections were required.

### Progress Update

- Bootcamp Progress: Day 37 / 84 (44.0%)
- Current Phase: Phase 3 — Functions + Program Decomposition
- Current Position: Can independently validate function inputs, enforce multiple constraints, and deliberately raise meaningful exceptions while preserving correct return behavior.

### Critical Weakness

> No significant weakness in exception raising or input validation was observed. Testing remains primarily manual, with individual function calls changed between runs rather than using a repeatable test structure.

This did not affect the correctness of today's solutions. More systematic testing can be developed in later sessions.

### Session Verdict

**COMPLETED**

The learning objective was achieved.

Minhyi independently implemented both validation functions with correct conditions, exception types, messages, and return behavior.

No substantial hints, debugging intervention, or solution rewrites were necessary.

Further exercises are unnecessary for today's scope.

### Next Session

**Day 38 — Reading Error Messages and Tracebacks**

Focus on interpreting Python traceback messages, locating the source of exceptions, distinguishing different error types, and identifying the underlying causes of program failures.
