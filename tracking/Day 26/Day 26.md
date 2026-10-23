## --- DAY 26 UPDATE ---

**DAY 26 | COMPLETED | 1:11:51 | Level: 4.0/5**

### Focus Topic

Nested Data Structures — Accessing, modifying, and iterating through lists of dictionaries and dictionaries containing lists.

### Session Notes

- Reviewed nested data structures, focusing on lists containing dictionaries and dictionaries containing lists.
- Practiced accessing nested elements through combinations of list indexes and dictionary keys.
- Successfully modified a value inside a nested list using dictionary access.
- Initially struggled with nested iteration because previous exercises had not required traversing multiple levels of nested collections.
- Reviewed previous bootcamp exercises to identify relevant foundations:
  - Day 19: List iteration.
  - Day 23: Dictionary iteration.
  - Day 25: Combining different data structures.
- Learned how nested `for` loops work, including how an inner loop completes its iterations before the outer loop advances.
- Practiced nested iteration using lists of lists before progressing to lists of dictionaries.
- Clarified the difference between iterating over a dictionary's keys and iterating over a list stored inside a dictionary.
- Completed Exercise 1 — Product Prices:
  - Initially wrote three nested loops, causing repeated output.
  - Identified the unnecessary iteration over dictionary keys.
  - Corrected the implementation to use two nested loops.
  - Successfully printed all five prices without duplication.
- Completed Exercise 2 — Student Scores:
  - Independently transferred the nested iteration pattern to a different dataset.
  - Correctly retrieved student names and individual scores.
  - Resolved an output formatting issue caused by spaces automatically inserted between arguments in `print()`.
  - Corrected Bob's second score from `80` to `85` to match the final specification.
  - Successfully produced all nine required output lines.
- No complete solution to the final student-score exercise was supplied before the independent implementation.

### Minhyi Notes

- Initially found nested loops unfamiliar and questioned whether similar exercises had appeared earlier in the bootcamp.
- Recognized that the first coding attempt involved trying different combinations of loops without fully understanding what each loop was iterating over.
- Explicitly requested additional conceptual instruction rather than continuing to guess.
- Initially confused dictionary keys with the values stored under those keys.
- Made several mistakes involving exact dictionary key names, particularly `"price"` versus `"prices"` and `"score"` versus `"scores"`.
- Initially confused the type of an entire list with the type of its individual elements.
- Improved understanding after separating nested iteration into smaller concepts:
  - Retrieving a dictionary from a list.
  - Retrieving a list from a dictionary.
  - Iterating through individual elements of that list.
- Demonstrated understanding through mental execution exercises before combining the concepts in code.
- Initially wrote an unnecessary third loop when processing product prices.
- Successfully corrected the structure after understanding why iterating directly over a dictionary retrieves its keys.
- Required a formatting explanation to remove an unwanted space before the colon in the final student-score output.
- Successfully corrected the dataset and verified the final output.
- The most significant improvement was moving from trial-and-error coding toward identifying the type and purpose of each iterable before writing the loops.

### Key Lesson

> Nested iteration becomes manageable when each level is understood separately: identify the collection, determine what each loop retrieves, and then connect the loops.

### Performance Evaluation

- Concept understanding: **4.0/5**
- Coding correctness: **4.4/5**
- Reasoning / problem decomposition: **3.8/5**
- Independence: **3.8/5**
- Debugging: **4.1/5**

**Final Score: 4.0/5**

### Blank-Screen Performance

**Exercise 1 — Product Prices**

- Initially implemented three loops instead of two.
- The first implementation printed each product's prices twice.
- Required conceptual instruction to understand the relationship between dictionary access and list iteration.
- Successfully rewrote the implementation using two nested loops.
- Final output was correct, with no duplicated prices.

**Exercise 2 — Student Scores**

Independently implemented the following nested iteration structure after guided practice with the previous exercise:

`for student in students:`

`    for score in student["scores"]:`

`        print(student["name"] + ":", score)`

The implementation correctly:

- Traversed each dictionary in the student list.
- Retrieved each student's scores using the appropriate dictionary key.
- Iterated through individual scores.
- Printed the corresponding name and score.
- Supported additional students and scores without changing the loop structure.

The first version had an extra space before the colon, which was corrected after a formatting explanation.

The supplied dataset also initially retained Bob's old score of `80`. After clarification, this was updated to `85`.

Final execution produced all nine expected lines correctly.

**Independence assessment:** The final student-score implementation was written independently, but it followed substantial conceptual instruction and a closely related practice exercise. Therefore, the successful result demonstrates developing competence rather than fully independent mastery of unfamiliar nested structures.

### Progress Update

- Bootcamp Progress: **Day 26 / 84**
- Current Phase: **Phase 2 — Core Python Data Structures**
- Current Position: Can access, modify, and iterate through nested collections, including lists of dictionaries containing lists. Can independently apply a recently learned nested-loop pattern to a related problem after conceptual instruction.

### Critical Weakness

> When encountering an unfamiliar nested structure, still struggles to identify the correct iterable at each level before coding. Must strengthen the habit of reasoning about collection types and loop variables instead of experimenting with arbitrary loop combinations.

### Session Verdict

**COMPLETED**

The learning objective was achieved.

Minhyi successfully demonstrated nested element access, mutation, nested-loop execution, and independent implementation of a related student-score processing task.

Although substantial conceptual clarification was necessary, the final implementation demonstrated acceptable understanding and correct application of nested iteration.

No further mandatory exercises are required for Day 26.

### Next Session

**Day 27 — Frequency Counting and Lookup Patterns**

Focus on using dictionaries and other appropriate data structures to count repeated occurrences, track frequencies, and retrieve information efficiently.

Reinforce nested data structure traversal when relevant, but do not repeat Day 26 unless the same conceptual difficulty appears again.