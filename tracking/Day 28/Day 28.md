## --- DAY 28 UPDATE ---

**DAY 28 | COMPLETED | 2h 49m 38s | Level: 4.1/5**

### Focus Topic

**Checkpoint 2 — Data Structures Mini Project + Applied Problem Solving**

* Part A: Museum Entry Audit
* Part B: Warehouse Inventory Ledger

### Session Notes

* Completed the **Museum Entry Audit** mini project, implementing:

  * Gate activity frequency counting.
  * Duplicate badge detection.
  * Unique badge grouping by gate.
  * Visitor type frequency counting.
* Built an interactive menu using `while`, `if/elif`, and `break`.
* Combined lists, dictionaries, tuples, and sets to solve multi-step problems.
* Corrected a duplicate detection issue where badges appearing more than twice could be printed repeatedly.
* Implemented the **Warehouse Inventory Ledger**, involving:

  * Sequential transaction processing.
  * Inventory updates based on transaction quantities.
  * Duplicate transaction ID detection.
  * Unknown product validation.
  * Insufficient stock handling.
  * Successful operation frequency counting.
* Successfully calculated the correct final inventory for the provided dataset.
* Correctly identified rejected transactions and their reasons.
* Two issues remained in the Warehouse implementation:

  1. Successful transaction IDs were collected in a set rather than grouped by product.
  2. Rejected transaction IDs were not consistently recorded in the tracking set, potentially violating the duplicate prevention rule.
* Used external AI assistance for debugging, syntax clarification, and selected algorithmic guidance.
* No complete program solution was copied from AI.
* The session ended after nearly three hours of active programming, with the remaining issues intentionally left unresolved.

### Minhyi Notes

* Independently designed and implemented the main structures of both programs.
* Initially struggled with dictionary indexing and selecting appropriate nested structures.
* Received conceptual assistance when implementing dictionary-of-sets grouping.
* Reused the Day 27 frequency-counting pattern across multiple requirements.
* Encountered difficulty interpreting and implementing the Warehouse Ledger's detailed business rules.
* Initially used fixed inventory adjustments (`+= 1` and `-= 1`) instead of transaction quantities.
* Corrected inventory calculations and several validation errors through iterative debugging.
* External AI provided meaningful guidance on validation order, transaction indexing, and duplicate handling.
* Despite assistance, actively reasoned through the problems and wrote the implementations personally.
* Recognized that solving larger programming problems requires more sustained concentration than isolated exercises.
* Expressed frustration when the checkpoint became increasingly examination-oriented rather than learning-oriented.
* Decided to conclude the session instead of continuing with additional corrections or another cold test.

### Key Lesson

> Programming independence is demonstrated through reasoning, implementation, debugging, and understanding—not simply through avoiding AI assistance.

### Performance Evaluation

* Concept understanding: **4.3/5**
* Coding correctness: **3.7/5**
* Reasoning / problem decomposition: **4.1/5**
* Independence: **4.4/5**
* Debugging: **4.1/5**

**Final Score: 4.1/5**

The independence score reflects demonstrated ownership of the implementations, while acknowledging meaningful AI assistance.

The correctness score reflects the remaining specification violations in Part B.

### Blank-Screen Performance

* Independently authored the primary implementations of both mini projects.
* Successfully combined loops, conditional logic, dictionaries, sets, and nested data structures.
* Demonstrated the ability to construct multi-step programs without receiving complete solutions.
* Required targeted debugging, syntax clarification, and some conceptual guidance.
* Successfully completed Part A after correcting its duplicate detection logic.
* Produced a substantially functional Part B implementation, although two requirements remained incomplete.
* The cold test was not completed under strict no-AI conditions, so it cannot be considered a fully independent assessment.
* No additional cold test was required under the adjusted checkpoint criteria.

### Progress Update

* **Bootcamp Progress:** Day 28 / 84
* **Current Phase:** Phase 2 — Core Python Data Structures (Completed)
* **Current Position:** Can independently construct substantial Python programs combining multiple data structures, with developing ability to translate complex business rules into correct implementations.
* **Next Phase:** Phase 3 — Functions + Program Decomposition

### Critical Weakness

> Translating detailed specifications into complete program behavior remains challenging, particularly when multiple business rules interact or when the required output structure differs from a familiar counting pattern.

### Session Verdict

**COMPLETED — WITH DOCUMENTED CORRECTNESS GAPS**

Day 28 is considered completed under the adjusted checkpoint criteria.

Part A was successfully completed, while Part B demonstrated meaningful applied programming ability despite two unresolved requirements.

The remaining issues are documented but do not prevent progression.

The session provided sufficient evidence of practical data structure understanding and continued development toward independent problem solving.

**Phase 2 — Core Python Data Structures: COMPLETED**

### Next Session

**Day 29 — Defining and Calling Functions**

Phase 3 — Functions + Program Decomposition.
