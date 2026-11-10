## --- DSA3 UPDATE ---

**DSA3 | PARTIAL — TIME | 56m 31.20s | Level: 3.2/5**

**Date:** 09–10/11/2026

### Focus Topic

HT-01 — Hash Table Core Operations: Retrieval, Membership, Deletion, Iteration, and Introduction to Resizing.

### Session Notes

- Continued implementing the custom Hash Table using separate chaining.
- Implemented six methods:
  - `get(key, default=None)`
  - `__contains__(key)`
  - `__len__()`
  - `delete(key)`
  - `items()`
  - `values()`
- Successfully implemented value retrieval using bucket lookup and linear search.
- Learned the difference between returning a value and printing it.
- Implemented membership checking independently of stored values.
- Learned why `get(key) is not None` is insufficient for membership checks.
- Implemented constant-time size retrieval using `_size`.
- Implemented deletion using index-based list access.
- Learned the difference between deleting a local variable and removing an element from a list.
- Used `yield` to iterate over stored key-value pairs and values.
- Introduced the concept of resizing and rehashing.
- Discussed the resize threshold of 0.75 and the need to redistribute keys when capacity changes.
- Stopped before implementing `_resize()`.

### Minhyi Notes

- Initially returned incorrect data from `get()` and confused `return` with `print()`.
- Corrected the implementation after understanding that `return` sends a value back to the caller.
- Implemented `__contains__()` with correct key comparison and Boolean return values.
- Initially attempted to calculate the number of keys by iterating through a new `HashTable()` object.
- Learned that `_size` already stores the number of keys, allowing `__len__()` to operate in O(1).
- Initially used `del i` inside `delete()`, which removed the local variable rather than the element from the bucket.
- Corrected deletion by using index-based access.
- Implemented `items()` correctly on the first submitted attempt.
- Made two minor mistakes in `values()` involving the attribute name and tuple index.
- Corrected these mistakes and successfully verified both iteration methods.
- Found resizing more challenging because it requires coordinating multiple changes to the internal data structure.

### Key Lesson

> Correct Hash Table operations require maintaining consistency between stored key-value pairs, bucket indexes, and metadata such as `_size`. Iteration and mutation must be handled carefully to preserve that consistency.

### Performance Evaluation

- Concept understanding: 3.3/5
- Coding correctness: 3.7/5
- Reasoning / problem decomposition: 3.1/5
- Independence: 2.8/5
- Debugging: 3.1/5

**Final Score: 3.2/5**

### Blank-Screen Performance

Minhyi independently attempted the implementations before receiving corrections.

**Implemented with relatively limited guidance:**

- `__contains__()`
- `items()`
- `values()`

**Required more substantial assistance:**

- `get()` — correcting return behavior and lookup conditions.
- `__len__()` — recognizing that `_size` already provides the result.
- `delete()` — distinguishing local variable deletion from list element deletion.

All final code was entered and modified by Minhyi.

AI provided explanations, debugging guidance, and selected code fragments.

No independent blank-screen rewrite of the complete Hash Table was performed.

**Independence Assessment:**

Minhyi demonstrated improved speed and familiarity with the internal Hash Table structure compared with DSA2.

However, he still required assistance when an operation involved unfamiliar Python behavior or changes to the underlying data structure.

### Progress Update

- Project: Multi-User Stock Trade Management System
- Component: HT-01 — Custom Hash Table
- Session: DSA3
- Current Phase: Core Hash Table Operations
- Current Position: Most basic operations implemented; resizing and comprehensive testing remain incomplete.

**Implemented:**

- `__init__()`
- `_hash()`
- `set()`
- `get()`
- `__contains__()`
- `__len__()`
- `delete()`
- `items()`
- `values()`

**Verified Through Manual Tests:**

- `get()` returned `300`, `200`, `None`, and `-1` as expected.
- Membership checks returned `True`, `False`, and `True` for the tested keys.
- `len(table)` correctly returned `3`.
- Deleting `"ABA"` reduced `_size` and preserved `"AAK"`.
- `items()` returned the remaining key-value pairs.
- `values()` returned the corresponding values.

**Not Yet Completed / Verified:**

- `_resize()` and rehashing.
- Automatic resize integration with `set()`.
- `capacity` and `load_factor` interfaces.
- Explicit string-key validation.
- `KeyError` test for deleting a missing key.
- Resize threshold tests.
- Multiple-resize tests.
- Comprehensive `unittest` suite.
- Integration of the three application-level Hash Tables.

The Hash Table component remains incomplete.

### Critical Weakness

> Minhyi can increasingly implement operations that follow familiar patterns, but still struggles to independently design algorithms that restructure or modify the underlying data structure.

Resizing is the next important test of this ability.

### Session Verdict

**PARTIAL — TIME**

Six Hash Table methods were implemented and manually verified during the session.

The main unfinished objective is resizing and rehashing.

The session ended before `_resize()` was implemented.

This is a meaningful improvement in implementation speed compared with DSA2, but the overall HT-01 component has not yet passed final verification.

### Next Session

**DSA4 — Hash Table: Resize, Rehash, and Final Verification**

Priorities:

1. Implement `_resize()`.
2. Integrate automatic resizing into `set()`.
3. Verify the resize threshold at the 13th key.
4. Verify data preservation after multiple resizes.
5. Complete key validation and metadata interfaces.
6. Run comprehensive Hash Table tests.

**Next Starting Point:**

Implement `_resize()` while preserving all existing key-value pairs and keeping `_size` unchanged during rehashing.

Do not proceed to Queue until the Hash Table core passes its required correctness tests.