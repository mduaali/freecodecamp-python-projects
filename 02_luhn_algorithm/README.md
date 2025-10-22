### 02_luhn_algorithm

**Files:**  
- `luhn_algorithm.py`

**What It Does:**  
This script validates a credit card (or other ID numbers) using the **Luhn Algorithm**.  
- Cleans the input by removing dashes and spaces  
- Doubles every second digit from the right  
- If the doubled number is ≥10, it adds the two digits together  
- Sums all digits and checks if the total is divisible by 10  
- Prints `'VALID!'` if the number passes the check, `'INVALID!'` otherwise  

**What I Learned:**  
- How to manipulate strings and remove unwanted characters (`str.maketrans()` + `translate`)  
- How to reverse a string and use slicing (`[::-1]`)  
- How to use loops and conditionals for mathematical logic  
- How integer division `//` and modulus `%` can split digits  
- How to build reusable functions (`verify_card_number`)  
- How to combine functions and a `main()` entry point  

**Example:**  

```python
Card number: 4111-1111-4555-1142
VALID!
