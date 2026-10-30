# 🧠 7 Steps of Highly Effective Problem Solving

> **Think before you code. Understand before you solve. Test before you submit.**

Writing code is only one part of solving a programming problem. The real skill is understanding the problem, developing a logical approach, identifying weaknesses, and building a correct and efficient solution.

This lesson introduces **seven practical steps for effective problem-solving**, especially when preparing for coding challenges and technical interviews.

## 🎯 Learning Objectives

By the end of this lesson, I aim to:

* Understand programming problems before jumping into code.
* Develop the ability to solve problems manually.
* Translate logical thinking into algorithms.
* Analyze time and space complexity.
* Identify weaknesses and edge cases before implementation.
* Write structured, readable, and maintainable code.
* Build confidence in solving technical interview questions.

---

## 📚 The 7 Steps of Effective Problem Solving

### 1. 🔍 Understand the Problem

Before writing any code, make sure you understand exactly what the problem is asking.

Every sentence in a problem statement may contain important information. Read carefully and pay attention to the input, expected output, constraints, and examples.

**What to focus on:**

* Identify what the problem is asking you to find or calculate.
* Understand the input and expected output.
* Examine the examples and their explanations.
* Identify important conditions and constraints.
* Avoid making assumptions.

**Key lesson:** A misunderstanding of the problem can lead to an incorrect solution, even if the code itself is written correctly.

### 2. ✍️ Solve the Problem Manually

Before asking the computer to solve a problem, try solving it yourself using a small example.

Manual problem-solving helps you understand the logic behind the solution and discover patterns that can later be automated.

**What to focus on:**

* Use small input examples.
* Work through the problem step by step.
* Observe how you reach the answer.
* Identify repeated actions or patterns.
* Understand the process before translating it into code.

**Key lesson:** If you cannot solve a small example manually, it will be difficult to explain to a computer how to solve it.

### 3. 💡 Develop a Solution Idea on Paper

Once you understand the problem and can solve it manually, develop a clear algorithm before implementation.

Start with a simple approach, even if it is not the most efficient one. Then look for opportunities to optimize it.

**What to focus on:**

* Write down your proposed solution.
* Break the problem into smaller steps.
* Consider a brute-force approach first.
* Look for opportunities to improve the algorithm.
* Analyze time and space complexity, including helper functions.

**Optimization technique – BUD:**

Look for three things that may reduce efficiency:

* **B – Bottlenecks:** Identify operations that slow down the algorithm.
* **U – Unnecessary Work:** Remove operations that are not needed.
* **D – Duplicated Work:** Avoid repeating calculations unnecessarily.

**Key lesson:** A working solution is a starting point. Aim to make it correct and efficient.

### 4. ⚖️ Challenge Your Own Solution (Play Devil's Advocate)

Do not assume your first idea is perfect. Think like a critical reviewer or tester whose job is to find weaknesses in your approach.

Ask yourself how your solution could fail.

**What to focus on:**

* Identify assumptions in your approach.
* Consider unusual or unexpected inputs.
* Look for edge cases.
* Ask whether the algorithm handles every possible scenario.
* Challenge the logic before implementation.

**Questions to ask yourself:**

* What happens if the input is empty?
* What happens if the input contains zero or negative numbers?
* What happens if there are duplicate values?
* Can a particular input break my logic?

**Key lesson:** Finding weaknesses before coding saves time and prevents incorrect solutions.

### 5. 💻 Implement the Solution

Now that you have a clear and tested idea, translate your algorithm into actual code.

The implementation should follow the logic you developed rather than becoming a process of randomly trying different code.

**What to focus on:**

* Choose an appropriate programming language.
* Use meaningful variable names.
* Write pseudocode before implementation when helpful.
* Divide your code into smaller blocks.
* Use helper functions when appropriate.
* Explain the purpose of each completed code block during interviews.

**Pseudocode:** A simple, language-independent description of the steps required to solve a problem.

It helps organize your thinking before writing actual Python or another programming language.

**Key lesson:** Good implementation starts with a clear plan.

### 6. 🧪 Test with Comprehensive Test Cases

A solution that works for one example is not necessarily correct.

After implementation, test your code with different inputs to verify that it works under different conditions.

Testing should be intentional. Every test case should have a reason.

**What to focus on:**

* Test normal inputs.
* Test empty inputs and zero values.
* Test negative numbers when applicable.
* Test duplicate values.
* Test boundary conditions.
* Test assumptions made during implementation.

**Example – Testing assumptions:**

Suppose you implement a prefix sum algorithm assuming all input numbers are positive.

Try an input containing negative numbers to check whether your solution still works.

This helps identify problems that ordinary examples might not reveal.

**Key lesson:** Testing is not just about confirming that your code works. It is about discovering situations where it might fail.

### 7. 🧹 Simplify and Clean Up Your Code

Once your solution works correctly and you are confident in its accuracy and efficiency, take time to improve its readability.

**What to focus on:**

* Use clear and meaningful variable names.
* Remove unnecessary code.
* Add useful comments where needed.
* Organize related logic into helper functions.
* Improve the structure and readability of your solution.

This step may depend on the time available, especially during technical interviews.

**Key lesson:** Good code should not only work; it should also be understandable and maintainable.

---

## 🧩 Practical Example: First Unique Character in a String

The lesson demonstrates how to apply problem-solving techniques to a coding challenge.

**Problem:**

Given a string `s`, find the index of the first non-repeating character. If no such character exists, return `-1`.

**Example:**

```python
s = "leetcode"
```

The first non-repeating character is `l`, which is at index `0`.

**Solution approach:**

1. Create an empty dictionary to store character frequencies.
2. Iterate through the string and count how many times each character appears.
3. Iterate through the string again.
4. Find the first character whose frequency is `1`.
5. Return its index.
6. If no unique character exists, return `-1`.

**Python implementation:**

```python
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_dict = defaultdict(int)

        for char in s:
            freq_dict[char] += 1

        for i in range(len(s)):
            if freq_dict[s[i]] == 1:
                return i

        return -1
```

**What this example teaches:**

* Using dictionaries to count occurrences.
* Iterating through strings.
* Applying logical conditions.
* Breaking a problem into smaller steps.
* Returning the correct result.
* Connecting an algorithm idea to Python implementation.

---

## 💡 Key Takeaways

The seven steps provide a structured approach to solving programming problems:

| Step                   | Main Focus                                     |
| ---------------------- | ---------------------------------------------- |
| 1. Understand          | Know exactly what the problem asks.            |
| 2. Solve Manually      | Discover the logic using small examples.       |
| 3. Develop an Idea     | Design and optimize an algorithm.              |
| 4. Challenge Your Idea | Find weaknesses and edge cases.                |
| 5. Implement           | Translate your algorithm into code.            |
| 6. Test                | Verify correctness with meaningful test cases. |
| 7. Clean Up            | Improve readability and structure.             |

## 🎯 My Learning Goal

My goal is to develop a problem-solving mindset rather than simply memorize solutions.

I want to become comfortable breaking complex problems into smaller steps, recognizing patterns, choosing appropriate algorithms, analyzing efficiency, and writing solutions with confidence.

**Remember: Don't rush to write code. Learn to think like a problem solver first. 🚀**
