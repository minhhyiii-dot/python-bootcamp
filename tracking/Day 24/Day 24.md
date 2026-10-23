## --- DAY 24 UPDATE ---

**DAY 24 | COMPLETED | 14 min 30 sec | Level: 4.5/5**

### Focus Topic

Sets and uniqueness: set creation, duplicate elimination, membership testing, element modification, and basic set operations.

### Session Notes

- Learned the three fundamental properties of Python sets: unique elements, no guaranteed order, and mutability.
- Correctly predicted how duplicates affect set size and how `in` tests membership.
- Learned `.add()`, `.remove()`, and `.discard()`, including their behavior when an element already exists or is missing.
- Independently completed a set modification exercise using `.add()` and `.remove()`.
- Learned and applied set union (`|`), intersection (`&`), and difference (`-`).
- Independently completed a stock portfolio comparison exercise with all three operators.
- Encountered a `SyntaxError` after replacing `|` with `\` and learned why these characters are different.
- Clarified that set difference depends on operand order, but both differences are equal when the sets contain the same elements.
- Learned that an empty set is written `set()`, while `{}` creates an empty dictionary.
- No full solutions or substantial coding hints were required.

### Minhyi Notes

- Correctly explained why duplicated stock tickers do not increase the length of a set.
- Independently predicted membership tests for stock tickers.
- The set modification program produced the expected output (`3` and `False`).
- Correctly implemented the three portfolio comparison operations and verified the initial results in the terminal.
- Confused the union operator (`|`) with backslash (`\`), partly because the operator was escaped in the mentor's Markdown table.
- Reported correcting that syntax error after clarification; a rerun was not shown.
- Initially claimed that `A - B` and `B - A` could *never* be equal.
- Corrected the overgeneralization after reasoning about two identical sets.
- Initially suggested `{}` as the empty result, then learned Python displays the empty set as `set()`.

### Key Lesson

> Sets enforce uniqueness, and set operations make collection comparisons simple. Always test edge cases before making absolute claims about program behavior.

### Performance Evaluation

- Concept understanding: **4.4/5**
- Coding correctness: **4.8/5**
- Reasoning / problem decomposition: **4.3/5**
- Independence: **4.8/5**
- Debugging: **4.2/5**

**Final Score: 4.5/5**

### Blank-Screen Performance

**Exercise 1 — Set Modification**

Independently created a set of stocks, added a new ticker, attempted to add a duplicate, removed an existing ticker, and printed the remaining count and a membership check.

Expected and observed output:

```text
3
False
```

**Exercise 2 — Stock Portfolio Comparison**

Independently created `shared_stocks`, `all_stocks`, and `only_a` using the correct operators without loops.

The initial code executed successfully. Results, regardless of set display order:

```python
shared_stocks = {"NVDA", "TSLA"}
all_stocks = {"AAPL", "MSFT", "NVDA", "TSLA", "AMZN", "GOOG"}
only_a = {"AAPL", "MSFT"}
```

After the successful run, a separate experiment using `\` instead of `|` raised a syntax error. The difference was explained, and Minhyi reported fixing it.

### Progress Update

- Bootcamp Progress: **Day 24 / 84**
- Current Phase: **Phase 2 — Core Python Data Structures**
- Current Position: Can independently create, modify, and compare sets through membership checks, union, intersection, and difference.

### Critical Weakness

> Occasionally overgeneralizes a rule without checking edge cases. Distinguish rules that are generally true from those that are universally true.

### Session Verdict

**COMPLETED**

The objective was achieved. Both practical exercises were implemented independently. The important conceptual error about set difference was corrected through a targeted reasoning question. No further mandatory practice is required.

### Next Session

**Day 25 — Choosing List vs Tuple vs Dictionary vs Set**

Focus on selecting the appropriate structure based on order, mutability, uniqueness, indexing, and key-value relationships.