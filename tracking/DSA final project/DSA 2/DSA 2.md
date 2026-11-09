## --- DSA2 UPDATE ---

**DSA2 | COMPLETED | 1h 05m 42s | Level: 3.0/5**

**Date:** 09/11/2026

### Focus Topic

HT-01 — Hash Table: Implementing `set(key, value)` with Separate Chaining.

### Session Notes

- Continued implementing the custom Hash Table for the Final Project DSA.
- Developed the `set()` method to support:
  - Inserting new key-value pairs.
  - Updating values of existing keys.
  - Handling collisions using separate chaining.
  - Maintaining the correct number of unique keys through `_size`.
- Used `_hash(key)` to identify the correct bucket.
- Implemented linear search within a bucket using `range(len(bucket))`.
- Learned to distinguish between:
  - The hash index identifying a bucket.
  - The list index identifying a tuple within that bucket.
- Practiced nested indexing using `bucket[i][0]`.
- Learned how immutable tuples can be replaced inside a mutable list.
- Used `return` to prevent duplicate insertion after updating an existing key.
- Successfully tested insertion, collision handling, and updating an existing key.

**Verified Test:**

```python
table = HashTable()

table.set("AAK", 100)
table.set("ABA", 200)
table.set("AAK", 300)

print(table._buckets[9])
print(table._size)
```

**Actual Terminal Output:**

```text
[('AAK', 300), ('ABA', 200)]
2
```

The results confirmed that:
- Both colliding keys were preserved.
- The existing value was updated correctly.
- Updating an existing key did not increase `_size`.
- No duplicate key was created in the tested scenario.

### Minhyi Notes

- Initially struggled to determine how to begin implementing `set()`.
- Needed guidance to access instance attributes and call methods using `self`.
- Initially attempted to iterate through every bucket instead of selecting the correct bucket using the hash index.
- Incorrectly placed the insertion operation inside the search loop.
- Learned that modifying a list while iterating over it can cause unexpected behavior.
- Initially struggled with tuple immutability and updating existing key-value pairs.
- Learned that immutable tuples can be replaced at specific positions inside mutable lists.
- Confused the hash index with the index of a tuple within a bucket.
- Had difficulty understanding `range(len(bucket))` and nested indexing.
- Initially assumed that iterating through a list consumed or removed its elements.
- Clarified that iteration only reads elements unless the code explicitly modifies the list.
- Compared direct element iteration with index-based iteration.
- Chose index-based iteration because it made the underlying DSA logic easier to understand.
- Completed the implementation after several debugging iterations.
- Successfully executed the final test and obtained the expected results.

### Key Lesson

> A Hash Table uses the hash index to locate a bucket, then searches within that bucket to identify the correct key. Updating an immutable tuple requires replacing its position in the mutable bucket list.

### Performance Evaluation

- Concept understanding: 3.3/5
- Coding correctness: 4.0/5
- Reasoning / problem decomposition: 2.8/5
- Independence: 2.0/5
- Debugging: 3.0/5

**Final Score: 3.0/5**

### Blank-Screen Performance

Minhyi attempted to implement `set()` himself without receiving a complete solution.

However, substantial AI guidance was required throughout the implementation.

**Independent Work:**

- Wrote the method and its control flow manually.
- Attempted bucket traversal and key comparison.
- Implemented tuple replacement and insertion after receiving guidance.
- Modified the implementation in response to identified errors.
- Executed the final collision and update test successfully.

**AI Assistance Required:**

- Identifying how to access the correct bucket.
- Correcting instance method calls.
- Explaining the difference between bucket indexes and tuple indexes.
- Correcting loop structure and indentation.
- Explaining tuple immutability.
- Introducing index-based iteration.
- Identifying the need for an early `return`.
- Providing the final test scenario.

The final code was written by Minhyi, but the implementation was heavily guided.

No independent blank-screen reimplementation was performed after the corrections.

**Independence Assessment:**

Minhyi demonstrated improving understanding during debugging but still required significant assistance to translate the intended algorithm into working Python code.

The successful final implementation should not be interpreted as fully independent coding performance.

### Progress Update

- Project: Multi-User Stock Trade Management System
- Component: HT-01 — Custom Hash Table
- Session: DSA2
- Current Phase: Core Hash Table Operations
- Current Position: Implemented and manually verified basic insertion and update operations with collision handling.

**Completed:**

- `__init__()`
- `_hash()` for valid string keys
- `set()` — basic insert and update behavior

**Verified:**

- Initial capacity of 16.
- Correct hash result for `"FPT"`.
- Collision handling using `"AAK"` and `"ABA"`.
- Updating an existing key without removing another colliding key.
- Maintaining the correct `_size` after an update.

**Not Yet Completed / Verified:**

- `get()`
- `delete()`
- `__contains__()`
- `__len__()`
- `items()`
- `values()`
- Automatic resizing and rehashing.
- Explicit key type validation.
- Comprehensive unit tests.
- Integration of the three project-level Hash Tables.

The Hash Table component remains incomplete.

### Critical Weakness

> Translating a data structure's internal organization into executable control flow remains difficult without step-by-step guidance.

The main difficulties involved:

- Understanding which data structure level an index refers to.
- Selecting the appropriate iteration method.
- Managing insertion and update as mutually exclusive operations.
- Understanding how indentation affects program behavior.

These difficulties indicate that the main limitation is currently algorithm implementation independence rather than memorizing Python syntax.

### Session Verdict

**COMPLETED**

The primary learning objective of DSA2 was achieved.

Minhyi implemented `set(key, value)` and successfully demonstrated insertion, updating, collision handling, and correct size management.

The implementation required substantial AI guidance, particularly during algorithm decomposition and debugging.

The completed method passed the observed test, but comprehensive correctness has not yet been established.

No additional exercises are necessary for this session.

The next session can proceed to the next project component.

### Next Session

**DSA3 — Hash Table: `get(key, default=None)`**

Focus:

- Implementing value retrieval using the hash index.
- Searching for the correct key within a bucket.
- Returning the associated value.
- Returning a default value when the key does not exist.
- Preserving stored values such as `None`, `0`, and `False`.
- Ensuring that retrieval does not modify the Hash Table.

**Next Starting Point:**

Implement `get()` using the existing `__init__()`, `_hash()`, and `set()` methods.

Prioritize a more independent first attempt before requesting AI assistance.