# Week 3 Python Exercises

## Overview

This project contains three Python programs designed to strengthen fundamental programming skills, including writing pure functions, working with strings, using keyword arguments, and applying the Single Responsibility Principle.

The exercises cover text analysis, palindrome detection, and message encryption using a Caesar Cipher.

---

# Project Structure

```text
Week3/
│
├── word_counter.py
├── palindrome.py
├── caesar_cipher.py
└── README.md
```

---

# 1. `word_counter.py`

A simple text analysis program that counts words and characters in a given string.

## Functions

### `count_words(text)`

Returns the total number of words in a string using Python's `split()` method.

**Example**

```python
count_words("Python is fun")
# Output: 3
```

---

### `count_characters(text, include_spaces=True)`

Returns the number of characters in a string.

**Parameters**

* `text` *(str)* – The text to analyze.
* `include_spaces` *(bool, optional)* – Determines whether spaces are included in the character count. Defaults to `True`.

**Examples**

```python
count_characters("Hello World")
# Output: 11

count_characters("Hello World", include_spaces=False)
# Output: 10
```

---

### `text_report(text)`

Generates a formatted, multi-line report containing:

* Original text
* Word count
* Character count (with spaces)
* Character count (without spaces)

---

## Concepts Practiced

* Pure functions
* String manipulation
* `split()`
* `replace()`
* Keyword arguments
* Function composition

---

# 2. `palindrome.py`

Checks whether a string is a palindrome.

A palindrome reads the same forwards and backwards after ignoring spaces and letter case.

## Function

### `is_palindrome(text)`

Returns:

* `True` if the text is a palindrome.
* `False` otherwise.

The function:

* Converts text to lowercase using `.lower()`
* Removes spaces using `.replace()`
* Reverses the string using slicing (`[::-1]`)

**Example**

```python
is_palindrome("Was it a car or a cat I saw")
# Output: True
```

```python
is_palindrome("Python")
# Output: False
```

---

## Concepts Practiced

* String methods
* Boolean values
* String slicing
* Data cleaning
* Pure functions

---

# 3. `caesar_cipher.py`

Implements a Caesar Cipher for encrypting and decrypting text.

Each lowercase letter is shifted forward by a specified number of positions while preserving spaces and punctuation.

## Functions

### `shift_letter(letter, shift)`

Shifts a single lowercase letter by the specified number of positions.

The function wraps around the alphabet so letters after `z` continue from `a`.

**Example**

```python
shift_letter("x", 5)
# Output: "c"
```

---

### `encode(text, shift)`

Encrypts a message by shifting every lowercase letter.

Spaces, punctuation, and numbers remain unchanged.

**Example**

```python
encode("message me now", 6)
# Output: "skyygmk sk tuc"
```

---

### `decode(encoded_text, shift)`

Decrypts an encoded message by reversing the shift.

**Example**

```python
encrypted = encode("message me now", 6)

decode(encrypted, 6)
# Output: "message me now"
```

---

## Concepts Practiced

* Character encoding
* `ord()` and `chr()`
* Modulo arithmetic
* Loops
* Conditional statements
* String manipulation
* Basic cryptography concepts

---

# Requirements

* Python 3.x

---

# Running the Programs

Run any script from the terminal:

```bash
python word_counter.py
```

```bash
python palindrome.py
```

```bash
python caesar_cipher.py
```

---

# Learning Outcomes

After completing these exercises, you will have practiced:

* Writing clean and reusable functions
* Creating pure functions with no side effects
* Using keyword arguments and default values
* Working with strings and text processing
* Applying the Single Responsibility Principle
* Using Python's built-in string methods
* Understanding the basics of classical encryption algorithms

These exercises provide a strong foundation for building more advanced Python applications and reinforce best practices in writing readable, maintainable code.
