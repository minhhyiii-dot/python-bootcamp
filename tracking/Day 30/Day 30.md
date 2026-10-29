## --- DAY 30 UPDATE ---

**DAY 30 | COMPLETED | 18 min 20.17 sec | Level: 4.7/5**

### Focus Topic

Parameters and arguments, positional argument matching, and function calls.

### Session Notes

- Learned the distinction between parameters (function definition) and arguments (function calls).
- Correctly identified parameters, arguments, and expected results in a function-reading exercise.
- Independently implemented `calculate_total()` using two parameters and two function calls.
- Practiced positional argument order and identified errors caused by excessive arguments.
- Completed the mandatory Trade Profit Calculator independently.
- Final program produced all three expected results: `150`, `-60`, and `0`.
- No coding hints or solution-level assistance were required.

### Minhyi Notes

- Initially predicted integer outputs instead of floats when multiplying by `0.1`.
- Initially believed that calling a two-parameter function with one argument would execute using the first parameter alone.
- Corrected the misconception after learning that missing required arguments raise a `TypeError` before the function body executes.
- Subsequently identified that supplying too many positional arguments also raises an error.
- Demonstrated independent implementation of multi-parameter functions.

### Key Lesson

> Positional arguments are assigned to parameters from left to right, and every required parameter must receive an argument before the function can execute.

### Performance Evaluation

- Concept understanding: 4.4/5
- Coding correctness: 5.0/5
- Reasoning / problem decomposition: 4.6/5
- Independence: 5.0/5
- Debugging: Not directly assessed

**Final Score: 4.7/5**

### Blank-Screen Performance

Independently implemented:

```python
def calculate_trade_result(buy_price, sell_price, quantity):
    total_profit = (sell_price - buy_price) * quantity
    print(total_profit)

calculate_trade_result(100, 130, 5)
calculate_trade_result(200, 180, 3)
calculate_trade_result(150, 150, 10)
```

All requirements satisfied on the first submitted attempt. No hints or corrections were needed.

### Progress Update

- Bootcamp Progress: Day 30 / 84
- Current Phase: Phase 3 — Functions + Program Decomposition
- Current Position: Can independently define and call functions with multiple positional arguments and use their values in calculations.

### Critical Weakness

> Needs to strengthen understanding of function-call validation, particularly what happens when required arguments are missing.

### Session Verdict

**COMPLETED**

The learning objective was achieved. Independent coding performance met the required standard. No additional exercises are necessary.

### Next Session

**Day 31 — `return`**