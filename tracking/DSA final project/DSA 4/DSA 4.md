## --- DSA4 UPDATE ---

**DSA4 | COMPLETED | ~30 minutes | Level: 3.1/5**

**Date:** 10/11/2026

### Focus Topic

HT-01 — Hash Table: Implementing Manual Resizing and Rehashing.

### Session Notes

- Continued implementing the custom Hash Table using separate chaining.
- Implemented the `_resize()` method.
- Learned how to preserve existing data while replacing the underlying bucket structure.
- Stored a reference to the original buckets before resizing.
- Doubled `_capacity` from 16 to 32.
- Created a new collection of independent empty buckets.
- Implemented rehashing using two nested loops:
  - The outer loop traverses the old buckets.
  - The inner loop traverses individual `(key, value)` pairs.
- Recalculated the hash index of each key using the new capacity.
- Transferred each complete pair into its new bucket.
- Preserved `_size` throughout the rehashing process.
- Successfully tested manual resizing with two colliding keys.

**Verified Test:**

```python
table = HashTable()

table.set("AAK", 100)
table.set("ABA", 200)

table._resize()

print(table._capacity)
print(table._size)
print(table.get("AAK"))
print(table.get("ABA"))
print(list(table.items()))
```

**Actual Terminal Output:**

```text
32
2
100
200
[('AAK', 100), ('ABA', 200)]
```

The results confirmed that:

- Capacity doubled successfully.
- The number of stored keys remained unchanged.
- Both existing values remained accessible.
- No key-value pairs were lost during rehashing.
- Both colliding keys were preserved.

### Minhyi Notes

- Initially struggled to determine how to begin implementing resizing.
- Successfully implemented the initial steps of preserving old buckets, doubling capacity, and creating new buckets.
- Needed guidance to understand how to transfer data between the old and new bucket structures.
- Initially confused a bucket with an individual `(key, value)` pair.
- Incorrectly attempted to iterate through tuple elements rather than pairs within buckets.
- Initially included an unnecessary search operation when transferring pairs into the new buckets.
- Learned that rehashing does not require searching for existing keys in the newly created table.
- Corrected the iteration structure after understanding the difference between:
  - `old_buckets`
  - `old_bucket`
  - `pair`
  - `pair[0]`
- Successfully completed the implementation after several guided corrections.

### Key Lesson

> Resizing a Hash Table requires creating a new bucket structure and redistributing every existing key-value pair according to the new capacity, without changing the number of stored keys.

### Performance Evaluation

- Concept understanding: 3.4/5
- Coding correctness: 3.8/5
- Reasoning / problem decomposition: 3.0/5
- Independence: 2.3/5
- Debugging: 3.2/5

**Final Score: 3.1/5**

### Blank-Screen Performance

Minhyi wrote the `_resize()` method himself but required substantial AI guidance.

**Independent Work:**

- Stored the original bucket reference.
- Doubled the capacity.
- Reinitialized the bucket structure.
- Attempted to implement nested iteration and data transfer.
- Modified the code after identifying mistakes.
- Successfully executed the manual resize test.

**AI Assistance Required:**

- Decomposing resizing into initialization and rehashing stages.
- Explaining the structure of nested buckets and key-value pairs.
- Correcting the nested loop structure.
- Removing unnecessary key-search logic during rehashing.
- Correcting the hash input and transferred data.
- Providing the final verification scenario.

No complete Hash Table solution was provided or copied.

However, the final implementation depended significantly on step-by-step guidance.

**Independence Assessment:**

Minhyi could implement familiar initialization operations with reasonable independence.

The more complex rehashing logic required substantial guidance.

The main difficulty was navigating nested data structures and translating the intended data transformation into Python loops.

### Progress Update

- Project: Multi-User Stock Trade Management System
- Component: HT-01 — Custom Hash Table
- Session: DSA4
- Current Phase: Resizing and Rehashing
- Current Position: Manual resizing implemented and verified.

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
- `_resize()`

**Verified During DSA4:**

- Manual capacity expansion from 16 to 32.
- Preservation of `_size`.
- Preservation of two colliding keys.
- Successful value retrieval after rehashing.
- Successful iteration after rehashing.

**Not Yet Completed / Verified:**

- Automatic resize integration with `set()`.
- Resize threshold at the 13th key.
- Multiple consecutive resizes.
- Capacity and load factor interfaces.
- Explicit string-key validation.
- Comprehensive unit tests.
- Integration of the three application-level Hash Tables.

HT-01 remains incomplete.

### Critical Weakness

> Navigating nested data structures remains difficult when an algorithm requires moving data between multiple levels of lists and tuples.

This weakness currently limits independent implementation of more complex DSA operations.

### Session Verdict

**COMPLETED**

The primary objective of DSA4 was achieved.

Minhyi implemented `_resize()` and successfully verified that manual resizing preserves the existing key-value pairs and key count.

The implementation required substantial guidance, but the final observed behavior was correct.

Automatic resizing and broader correctness testing remain unfinished.

No additional work is required for this session.

### Next Session

**DSA5 — Automatic Resizing and Hash Table Finalization**

Priorities:

1. Integrate `_resize()` into `set()`.
2. Trigger resizing only when adding a new key causes the load factor to exceed 0.75.
3. Verify that the 13th key triggers capacity expansion.
4. Verify preservation of all keys after multiple resizes.
5. Implement `capacity` and `load_factor` interfaces.
6. Complete key type validation.
7. Run comprehensive correctness tests.

**Next Starting Point:**

Modify `set()` to trigger `_resize()` after inserting a new key when the load factor exceeds 0.75.

Preserve the existing update behavior and ensure that updating an existing key never triggers unnecessary resizing.