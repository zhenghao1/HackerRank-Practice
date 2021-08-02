# Problem

View the problem: [pdf](./Grading\ Students\ Problem.pdf) or [web](https://www.hackerrank.com/challenges/grading/problem)

# Analysis

This starts off as a really easy problem but with one very key intricacy.  The rounding part.

I initially only took into consideration rounding to the nearest 10:

```python
def roundUp(grade):
    return int(grade/10.0) * 10
```

However, this is wrong as we also have to consider rounding to the nearest 5:

```python
def roundUp(grade):
    return int(grade/5.0) * 5
```

The general idea is to loop through the grades with `for` loop and filter it through cases when `grade < 38` and `grade >= 38`.

### Big O:  O(n)

