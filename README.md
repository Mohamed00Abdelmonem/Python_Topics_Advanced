
# Python Topics Advanced

Welcome to the **Python Topics Advanced** repository! This repository contains advanced Python topics with explanations, examples, and interview questions to help you deepen your knowledge and prepare for technical interviews.

## Repository Contents

- [Context Manager](#context-manager)
- [Data Classes](#data-classes)
- [Decorator](#decorator)
- [Logging](#logging)
- [Typer](#typer)
- and others....
- [Interview Questions](#interview-questions)

## Context Manager

Context managers are a way to allocate and release resources precisely when you want to. The most widely used example of context managers is the `with` statement.

**Example:**

```python
with open('file.txt', 'w') as file:
    file.write('Hello, World!')
```

## Data Classes

Data classes provide a decorator and functions for automatically adding generated special methods such as `__init__()` and `__repr__()` to user-defined classes.

**Example:**

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)  # Point(x=1, y=2)
```

## Decorator

Decorators are a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. They are usually called before the definition of a function you want to decorate.

**Example:**

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## Logging

Logging is a means of tracking events that happen when some software runs. The logging module in Python is a standard module that provides a flexible framework for emitting log messages from Python programs.

**Example:**

```python
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

## Typer

Typer is a library for building command-line interface (CLI) applications that users will love using and developers will love creating. Based on Python's type hints.

**Example:**

```python
import typer

def main(name: str):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)
```

## Interview Questions

This section includes questions that can be asked in interviews related to the topics covered in this repository. Each section has its own set of questions aimed at testing your understanding of the topic.

---

### Contact

For any questions or inquiries, please contact [Mohamed00Abdelmonem](https://github.com/Mohamed00Abdelmonem).

---

Thank you for visiting the **Python Topics Advanced** repository! Happy coding!
```
