## --- DAY 21 UPDATE ---

**DAY 21 | COMPLETED | Time: Not recorded | Level: 4.3/5**

### Focus Topic

Tuples and immutability.

### Session Notes

- Learned how tuples differ from lists, particularly their immutable nature.
- Understood that tuple elements cannot be reassigned after creation.
- Distinguished **object mutation** from **variable reassignment**.
- Reviewed tuple indexing, negative indexing, slicing, and `len()`.
- Learned the two tuple methods:
  - `.count()` — Counts occurrences of a specified value.
  - `.index()` — Returns the index of the first occurrence of a specified value.
- Identified that `.index()` raises a `ValueError` when the requested value does not exist.
- Completed the mandatory transaction-record exercise using tuples without converting them into lists.
- Corrected two requirement mismatches after feedback.
- Final execution produced all four expected outputs.

### Minhyi Notes

- Initially predicted that a tuple element-assignment error would still allow the following `print()` statement to execute.
- Correctly understood that reassigning a variable to a new tuple does not violate immutability.
- Initially unfamiliar with `.count()`, but successfully applied it after a short explanation.
- Correctly identified that `.index()` raises an error when the searched value is absent.
- First mandatory attempt used a reverse slice, producing `(150, 250, 400)` instead of `(400, 250, 150)`.
- Initially used `transaction` instead of the explicitly required `transactions`.
- Corrected both issues independently after they were identified.
- An intermediate execution showed a `NameError` involving the old singular variable name. The final execution succeeded.
- Session duration was not recorded.

### Key Lesson

> Immutability prevents changing an existing tuple's elements, but does not prevent a variable from being reassigned to a new tuple.

### Performance Evaluation

- Concept understanding: **4.5/5**
- Coding correctness: **4.3/5**
- Reasoning / problem decomposition: **4.2/5**
- Independence: **4.2/5**
- Debugging: **4.3/5**

**Final Score: 4.3/5**

### Blank-Screen Performance

Minhyi independently constructed a program that:

1. Created a tuple of six transaction amounts.
2. Counted occurrences of `150`.
3. Located the first occurrence of `400`.
4. Extracted the last three transactions.
5. Reassigned the original variable to a new tuple.
6. Printed all required results using exactly four `print()` statements.

The first submission contained two specification mismatches involving slicing direction and variable naming.

After targeted feedback, Minhyi corrected both without receiving a complete solution.

Final output:

```text
3
3
(400, 250, 150)
(150, 200, 150, 400, 250, 500)
```

The final code executed successfully.

### Progress Update

- Bootcamp Progress: **Day 21 / 84**
- Current Phase: **Phase 2 — Core Python Data Structures**
- Current Position: Can independently create, index, slice, and query tuples; understands basic immutability and variable reassignment.

### Critical Weakness

> Slicing direction and exact variable-name requirements still require more careful verification. A program executing successfully does not guarantee full specification compliance.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi demonstrated acceptable independent use of tuples and corrected the important mistakes identified during the mandatory exercise.

No additional practice is required for Day 21.

### Next Session

**Day 22 — Dictionaries: key-value model**