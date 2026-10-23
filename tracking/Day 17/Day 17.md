## --- DAY 17 UPDATE ---

**DAY 17 | COMPLETED | 1 hr 29 min 53 sec | Level: 4.6/5**

### Focus Topic

Lists: creation, indexing, and mutation.

### Session Notes

- Learned how to create Python lists and access elements using positive and negative indexes.
- Correctly connected list indexing with previously learned string indexing:
  - index `0` accesses the first element;
  - index `-1` accesses the final element;
  - `len(list) - 1` gives the final valid positive index.
- Learned the major difference between strings and lists:
  - strings are immutable;
  - lists are mutable, so individual elements can be replaced directly.
- Practiced mutating numeric, string, Boolean, and mixed-type list elements.
- Correctly used existing list elements inside later expressions and mutations.
- Reinforced that assigning a list element's current value to another variable does not create a live connection between them.
- Correctly identified that accessing an invalid list index raises `IndexError`.
- Completed multiple progressively harder exercises rather than moving directly to the mandatory task.
- Successfully handled two-list state tracking involving swaps, arithmetic updates, Boolean mutation, negative indexing, and `type()`.
- Challenged an overly guided exercise design and requested less procedural problem specifications so that problem decomposition, rather than merely following steps, would be tested.
- Built a stock-position program combining:
  - list creation and mutation;
  - user input;
  - numeric conversion;
  - Boolean expressions;
  - `if / elif / else`;
  - Day 16 string normalization;
  - state validation;
  - dynamic buy/sell quantities.
- Independently extended the original fixed-quantity specification into a user-defined quantity version.
- Refactored duplicated quantity input so that both `buy` and `sell` share one input statement.
- Correctly prevented selling more shares than were currently owned.
- Learned that `pass` can represent an intentionally empty branch when no action is required.
- Rebuilt the final program again from a blank screen after receiving material assistance on the earlier version.
- The final rewrite successfully used `.strip().lower()` for action normalization and `pass` for the `hold` branch.

### Minhyi Notes

- Early exercises showed correct list-state reasoning but occasionally missed Python's exact printed representation, such as forgetting quotes around strings inside a printed list and forgetting that `type()` prints `<class 'int'>`.
- Initially mutated the price and calculated profitability correctly as a separate variable, but forgot to store the Boolean result back into the list's profitability element.
- Recognized duplicated code independently and asked how to reduce two identical quantity-input lines to one.
- Intentionally changed the exercise specification from a hard-coded transaction size of `20` shares to user-defined quantity. This was a deliberate extension rather than an accidental requirement miss.
- Initially used:

    `position[1] = position[1]`

  for the `hold` branch because it was unclear how Python represents "do nothing."
- Learned to replace this with:

    `pass`

- During the mandatory rewrite, initially forgot the requirement to normalize the action input with Day 16 string methods.
- After a requirement-level reminder, corrected it to:

    `action = input("Action: ").strip().lower()`

- The recurring weakness remains final requirement checking rather than core programming logic.
- Asked about the relationship between the current Python curriculum and concurrent DSA material covering arrays, linked lists, stacks, and queues. The current list work provides useful sequence/indexing foundations, while the linked-list implementation requires later Python concepts such as functions and classes.

### Key Lesson

> A Python list is a mutable sequence: its elements can be accessed by index, used in expressions, and replaced directly while the list itself remains the same structure.

### Performance Evaluation

- Concept understanding: **4.7/5**
- Coding correctness: **4.6/5**
- Reasoning / problem decomposition: **4.7/5**
- Independence: **4.5/5**
- Debugging: **4.6/5**

**Final Score: 4.6/5**

### Blank-Screen Performance

Minhyi completed several list programs from blank files without seeing final solutions first.

He independently demonstrated:

- list creation;
- positive and negative indexing;
- mixed data types;
- direct element mutation;
- dependent mutations using current list values;
- `len()`;
- `type()`;
- Boolean expressions stored inside lists;
- state tracking across multiple lists;
- combining list mutation with previously learned conditionals and input handling.

The main applied program represented a stock position as:

`["VCB", 100, 120.0, False]`

and allowed the user to perform `buy`, `sell`, or `hold` actions while updating share quantity, price, and profitability.

The earlier version required mentor assistance to:

- remove duplicated quantity-input logic;
- identify that the profitability Boolean needed to be written back into the list.

Because that assistance was material, Minhyi then rebuilt the program from a blank screen.

During the rewrite, the main program structure and mutation logic were reproduced independently. A final requirement-level reminder was needed for action normalization using `.strip().lower()`, after which the program was corrected successfully.

### Progress Update

- Bootcamp Progress: **Day 17 / 84**
- Current Phase: **Phase 2 — Core Python Data Structures**
- Current Position: Can independently create, index, inspect, and mutate Python lists, including mixed-type lists, and combine list state changes with previously learned input, arithmetic, Boolean logic, and conditional branching.

### Critical Weakness

> Core list mutation is independently usable, but final specifications are still occasionally completed from memory rather than checked item-by-item, causing small requirements such as input normalization or exact output representation to be missed even when the underlying logic is correct.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Minhyi demonstrated acceptable independent use of list creation, indexing, and mutation and successfully integrated lists with earlier Python concepts.

The session should stop here rather than adding more exercises.

### Next Session

**Day 18 — List methods**