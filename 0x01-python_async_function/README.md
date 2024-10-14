# 0x01-python_async_functionality

This project focuses on asynchronous programming in Python using the `asyncio` module. It covers various aspects of async programming, including coroutines, tasks, and concurrent execution.

## Learning Objectives

By the end of this project, you should be able to explain:

- The `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

## Requirements

### General

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/env python3`
- A README.md file, at the root of the project folder, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.x)
- All your files must be executable
- All your functions and coroutines must be type-annotated
- All modules should have documentation
- All functions should have documentation

## Tasks

### 0. The basics of async

Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (default value: 10) and waits for a random delay between 0 and `max_delay` seconds.

File: `0-basic_async_syntax.py`

### 1. Execute multiple coroutines at the same time with async

Write an async routine `wait_n` that takes two int arguments: `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`.

File: `1-concurrent_coroutines.py`

### 2. Measure the runtime

Create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.

File: `2-measure_runtime.py`

### 3. Tasks

Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

File: `3-tasks.py`

### 4. Tasks

Alter the code from `wait_n` into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

File: `4-tasks.py`

## Resources

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)
