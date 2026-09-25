## --- DAY 7 UPDATE ---

**DAY 7 | COMPLETED | 38 min 35 sec | Level: 4.7/5**

### Focus Topic

`if` statements and basic control flow.

### Session Notes

- Transitioned from evaluating Boolean expressions to using them to control code execution with `if`.
- Learned that Python uses indentation (whitespace) instead of brackets or semicolons to define code blocks.
- Successfully debugged an early `SyntaxError: expected ':'` without requiring external hints.
- Enforced the bootcamp "no spoon-feeding" rule when the AI provided too much setup code.
- Successfully implemented sequential `if` statements to handle mutually exclusive business rules (ATM withdrawal vs. penalty).
- Tested both execution paths correctly to verify that the unindented code runs regardless of the condition.

### Minhyi Notes

- Noticed the structural difference between Python and SQL (indentation vs `;`), correctly identifying that indentation is easy to mess up initially.
- Caught the AI providing the `input()` setup line before an independent attempt and demanded a strict blank-screen standard.
- Successfully navigated the final ATM logic using only `if`, proving an understanding of how sequential conditions evaluate. 

### Key Lesson

> Code blocks in Python are strictly defined by indentation, and an unindented line signals the end of the `if` statement.

### Performance Evaluation

- Concept understanding: 4.8/5
- Coding correctness: 4.8/5
- Reasoning / problem decomposition: 4.5/5
- Independence: 5.0/5
- Debugging: 4.5/5

**Final Score: 4.7/5**

### Blank-Screen Performance

Minhyi independently wrote the final ATM script from a blank screen. The program correctly captured two float inputs, evaluated if the withdrawal exceeded the balance, and applied either a penalty or a deduction using two independent `if` statements. No solution-level AI help or hints were required.

### Progress Update

- Bootcamp Progress: Day 7 / 84
- Current Phase: Phase 1 — Python Survival
- Current Position: Can independently write `if` statements, define code blocks with indentation, and use conditions to modify variable state.

### Critical Weakness

> Currently lacks the syntax to safely link mutually exclusive conditions; relying on sequential independent `if` statements is risky because modifying a variable in the first block can accidentally trigger the second block.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi demonstrated acceptable independent use of `if` statements, indentation, and conditional logic. 

### Next Session

**Day 8 — `if / elif / else`**