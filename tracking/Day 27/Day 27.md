
## --- DAY 27 UPDATE ---

**DAY 27 | COMPLETED | 47 min | Level: 4.2/5**

### Focus Topic

Frequency Counting and Dictionary Lookup Patterns.

### Session Notes

- Practiced dynamic frequency counting using Python dictionaries.
- Initially implemented event counting with hardcoded dictionary keys and `if/elif/else` conditions.
- Identified why hardcoded event categories could not handle new event types correctly.
- Rewrote the solution using an initially empty dictionary and dynamic key creation.
- Successfully counted additional `"TIMEOUT"` events without modifying the counting logic.
- Learned how `dict.get(key, default)` retrieves values and handles missing keys.
- Understood the difference between dictionary retrieval and assignment.
- Replaced the `if/else` counting structure with the more concise pattern:
  `count[event] = count.get(event, 0) + 1`
- Completed a warehouse order frequency-counting challenge involving user input and dictionary lookups.
- Successfully tested existing and nonexistent product IDs.
- Corrected missing output requirements and improved the final implementation after feedback.

### Minhyi Notes

- Initially assumed `count["LOGIN"] += 1` would automatically create the missing dictionary key.
- Learned that attempting to increment a nonexistent key directly raises a `KeyError`.
- Initially misunderstood how `.get()` could be useful for frequency counting because it does not modify dictionaries.
- Attempted to write `count.get("LOGIN", 0) += 1`, which is invalid Python syntax.
- Understood that `.get()` retrieves a value while dictionary assignment creates or updates an entry.
- Successfully connected retrieval and assignment into a single frequency-counting expression.
- In the first final-challenge submission, checked product membership against the original list rather than the frequency dictionary.
- Initially omitted the required frequency dictionary output and returned `"ID not exist"` instead of `0`.
- Corrected these issues independently after receiving requirement-level feedback.
- The final version used `count[id] = count.get(id, 0)` for lookup. Although functionally correct for the required output, this unnecessarily modifies the dictionary when the requested ID is missing.
- Learned that `print(count.get(id, 0))` is sufficient for a read-only lookup.

### Key Lesson

> Frequency counting combines dictionary retrieval and assignment, while read-only lookups should retrieve values without unnecessarily modifying the dictionary.

### Performance Evaluation

- Concept understanding: 4.4/5
- Coding correctness: 4.2/5
- Reasoning / problem decomposition: 4.3/5
- Independence: 4.0/5
- Debugging: 4.3/5

**Final Score: 4.2/5**

### Blank-Screen Performance

- Independently implemented the initial event-counting program, although the first version relied on hardcoded event categories.
- Rebuilt the counting logic using dynamic dictionary keys after a targeted conceptual hint.
- Successfully implemented the `.get()` frequency-counting pattern after understanding how retrieval and assignment work together.
- Independently transferred frequency counting to a warehouse order dataset in the final challenge.
- Correctly implemented user input and existing-product frequency retrieval.
- Initially missed two explicit output requirements and used the original list for membership checking.
- Corrected the final program after feedback without receiving a complete solution.
- Successfully tested an existing product (`"A12"`) and an unknown product (`"asd"`), producing the expected frequency values.
- No full AI-generated solution was used.

### Progress Update

- Bootcamp Progress: Day 27 / 84
- Current Phase: Phase 2 — Core Python Data Structures
- Current Position: Can independently implement dictionary-based frequency counting, handle previously unseen keys, and perform dictionary lookups with default values.

### Critical Weakness

> Still occasionally confuses dictionary retrieval with dictionary modification. Needs to distinguish read-only lookups from updates and verify all output requirements before considering a solution complete.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi successfully implemented dynamic frequency counting, understood dictionary lookup patterns, and transferred the concepts to a new problem with acceptable independence.

The session required targeted conceptual explanations and requirement-level corrections, but no full-solution assistance.

Ready to proceed to Day 28.

### Next Session

**Day 28 — CHECKPOINT 2: Data Structures Mini Project + Cold Test**

The checkpoint will assess independent data structure selection, frequency counting, duplicate detection, grouped information, and problem solving in an unfamiliar context.
