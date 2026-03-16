# Interview Video Script
## TextWise Solutions | Recursive String Reversal

---

### 1. Introduction

"Hi, my name is [your name]. Today I'm going to be solving the string reversal problem using recursion for the TextWise Solutions ContentOptimizer feature.

Before I start coding, I want to ask a few clarifying questions to make sure I understand the problem correctly."

---

### 2. Clarifying Questions

"First — should the function handle any string, including empty strings and single characters?

Second — should it preserve capitalization, spaces, and punctuation exactly as given?

Third — is there a constraint on the string length I should be aware of?

I'll assume yes to the first two, and no unusual length constraints. Great, let me start by thinking through the approach."

---

### 3. Diagram Walkthrough

*(Point to or draw the ASCII diagram)*

"I'll think through this recursively. The key insight is that reversing a string can be broken into a smaller version of the same problem.

If I have the string 'hello', I can reverse 'ello' — which is everything after the first character — and then append 'h' at the end.

Then to reverse 'ello', I reverse 'llo' and append 'e'. And so on.

This keeps going until I reach a string of length zero or one — which is already reversed. That's my base case.

So the two cases are:
- Base case: if the string has 0 or 1 characters, return it as-is
- Recursive case: return reverse of string[1:] plus string[0]"

---

### 4. Coding the Solution

*(Open solution.py)*

"Let me write the recursive function."

```python
def reverse_string_recursion(string):
    length = len(string)
    if length == 0 or length == 1:
        return string
    else:
        string = reverse_string_recursion(string[1:]) + string[0]
        return string
```

"Walking through this:

- `len(string)` gives me the length
- If it's 0 or 1, I return it immediately — that's the base case
- Otherwise, I call the function on `string[1:]`, which is everything after the first character, and concatenate `string[0]` — the first character — at the end
- Each recursive call receives a string one character shorter, so eventually we always hit the base case"

---

### 5. Trace Through an Example

"Let me trace through 'hello' to verify:

- `reverse_string_recursion('hello')` calls `reverse_string_recursion('ello')` + 'h'
- `reverse_string_recursion('ello')` calls `reverse_string_recursion('llo')` + 'e'
- `reverse_string_recursion('llo')` calls `reverse_string_recursion('lo')` + 'l'
- `reverse_string_recursion('lo')` calls `reverse_string_recursion('o')` + 'l'
- `reverse_string_recursion('o')` hits the base case and returns 'o'

Then it unwinds: 'o' + 'l' = 'ol', + 'l' = 'oll', + 'e' = 'olle', + 'h' = 'olleh'. Correct!"

---

### 6. Running the Tests

*(Switch to terminal and run pytest)*

"I've written unit tests covering both normal cases and edge cases. Let me run them now."

```
pytest test_solution.py
```

"My normal cases are:
- `'Hello!'` — mixed capitalization and punctuation
- `'a man a plan panama'` — a palindrome with spaces
- `'testing testing 123'` — a string with numbers

My edge cases are:
- An empty string `''` — should return `''`
- A single character `'g'` — should return `'g'`
- A two-character string `'yo'` — should return `'oy'`

All 12 tests pass."

---

### 7. Time and Space Complexity

"Now let me analyze the complexity.

**Time complexity: O(n)**
The function makes one recursive call per character in the string, so the number of operations grows linearly with the length of the input.

**Space complexity: O(n)**
Each recursive call adds a frame to the call stack, and the stack grows to depth n before the base case is hit. So memory usage also grows linearly.

This is the same time and space complexity as the iterative approach, but the recursive solution has the additional call stack overhead — something worth noting in a production context for very large strings."

---

### 8. Possible Optimization

"If asked to optimize — Python does have a built-in `string[::-1]` slice syntax that reverses in O(n) time with less overhead. However, since the requirement is to use recursion, this solution is appropriate as written.

One small optimization within the recursive approach: the base case could check `length <= 1` instead of `length == 0 or length == 1`, which is slightly more concise but functionally identical."

---

### 9. Closing

"To summarize: I implemented string reversal recursively by breaking the problem into a base case — strings of length 0 or 1 — and a recursive case that reverses the tail of the string and appends the head. The solution is O(n) time and O(n) space. All tests pass.

Thank you!"
