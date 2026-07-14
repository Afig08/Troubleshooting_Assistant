# Rule-Based AI System: Coding Troubleshooting Coach

## Part 1: Initial Project Ideas

### 1. Coding Troubleshooting Coach

**Description:**  
A system that helps users troubleshoot common coding problems, such as error messages, wrong output, no output, or not knowing where to start.

**Rule-Based Approach:**  
The system uses menu choices and predefined rules. For example, if the user selects `SyntaxError`, the system suggests checking for missing colons, parentheses, quotation marks, commas, or indentation.

### 2. Italian Language Tutor

**Description:**  
A system that helps users learn basic Italian words and phrases through short lessons and quiz questions.

**Rule-Based Approach:**  
The system uses rules to decide what lesson comes next. For example, if the user answers enough questions correctly, they move to the next topic. If they score low, they repeat the lesson.

### 3. Programming Topic Recommendation System

**Description:**  
A system that recommends what programming topic a user should study based on their goal and skill level.

**Rule-Based Approach:**  
The system uses rules such as: if the user chooses AI Development and says they are a beginner, recommend starting with Python basics.

### Chosen Idea

I chose the **Coding Troubleshooting Coach** because it helps users learn how to think through programming problems step by step. It also connects to my interest in coding, AI development, and building helpful tools for technical problem-solving.

---

## Part 2: Rules/Logic for the Chosen System

The Coding Troubleshooting Coach follows these rules:

### Problem Type Rules

- **IF** the user has an error message, **THEN** ask what type of error they are seeing.
- **IF** the user has wrong output, **THEN** suggest checking logic, variables, and expected results.
- **IF** the code runs but shows no output, **THEN** suggest checking print statements and function calls.
- **IF** the user does not know where to start, **THEN** suggest breaking the problem into input, process, and output.

### Python Error Rules

- **IF** the user selects `SyntaxError`, **THEN** suggest checking colons, parentheses, quotation marks, commas, brackets, and indentation.
- **IF** the user selects `NameError`, **THEN** suggest checking spelling and whether the variable or function was created before use.
- **IF** the user selects `TypeError`, **THEN** suggest checking for incompatible data types.
- **IF** the user selects `IndexError`, **THEN** suggest checking the list length and remembering that indexes start at 0.
- **IF** the user selects `IndentationError`, **THEN** suggest checking code spacing and alignment.

### Wrong Output Rules

- **IF** the user says the output is wrong, **THEN** ask what output they expected and what output they actually received.
- **IF** the expected output and actual output are different, **THEN** suggest checking variables, formulas, and program flow.

### No Output Rules

- **IF** the program runs but shows no output, **THEN** ask whether the user used a print statement.
- **IF** the code is inside a function, **THEN** tell the user to check whether the function was actually called.
- **IF** the code is inside a conditional statement, **THEN** tell the user to check whether the condition ever becomes true.

### Study Recommendation Rules

- **IF** the user struggles with variables, **THEN** recommend reviewing variables and data types.
- **IF** the user struggles with loops, **THEN** recommend practicing `for` loops and `while` loops.
- **IF** the user struggles with functions, **THEN** recommend reviewing parameters, return values, and function calls.
- **IF** the user struggles with lists, **THEN** recommend reviewing indexing, length, and looping through lists.

---

## Part 3: Sample Input and Output

Sample input and output:

User selects: Error Message  
User selects: SyntaxError  
The system identifies a SyntaxError and suggests checking for missing colons, parentheses, quotation marks, commas, brackets, or indentation.

User selects: Wrong Output  
Expected output: 10  
Actual output: 5  
The system explains that this is probably a logic issue and suggests checking variables, formulas, and program flow.

User selects: No Output  
Used a print statement: yes  
Code is inside a function: yes  
The system suggests checking whether the function was actually called.

User selects: Study Recommendation  
Topic selected: Loops  
The system recommends practicing for loops, while loops, counters, and loop conditions.

---

## Part 4: Reflection

### Project Overview

This project is a rule-based coding troubleshooting system. It uses predefined rules, menu choices, and `if/elif/else` logic to guide users through common programming problems. The system does not use machine learning; instead, it works like a simple expert system.

### Challenges

One challenge was deciding which programming problems to include. There are many possible errors in programming, so I focused on common beginner issues that I find myself researching such as syntax errors, name errors, wrong output, and no output.

Another challenge was finding myself to not overcomplicate things. I can show you what the initial code looked liek this morning and it grew into this.

---

## How to Run the Program

Make sure Python is installed on your computer.

Run the program with:

```bash
python assistant.py
