### 06_arithmetic_arranger_project
**Files:**
arithmetic_arranger.py

**What It Does:**
This program arranges arithmetic problems (addition and subtraction) vertically and side-by-side, just like students do in primary school. It ensures proper alignment, spacing, and formatting. Optionally, it can also display the calculated answers when enabled.

**Example:**
Input:
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

Output:
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172

**What I Learned:**
- how to parse and validate user input strings using .split()
- how to handle logical conditions for operators and input validation
- how to align text using .rjust() and manage consistent formatting
- how to build and join multiple formatted lines into a single string
- how optional arguments can toggle additional functionality in python
- how to construct a clean, readable output with string joins and loops
