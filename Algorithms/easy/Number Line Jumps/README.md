# Problem

View the problem: [pdf](./Kangaroo\ Jumps\ Problem.pdf) or [web](https://www.hackerrank.com/challenges/kangaroo/problem)

# Analysis

At first the solution sounds easy, just solve for y (number of jumps):

```
x1 + y*v1 = x2 + y*v2

y = (x2 - x1)/(v1 - v2)

OR

(x2 - x1) % (v1 - v2) == 0  // YES
```

but this would fail some of the test cases.  

First we need to read carefully....which I didn't....

**The constraints state that x1 is always smaller than x2.  This means that if `v2 >= v1', the two kangaroos will never meet each other!**

With that in mind, we need to check for such a condition before solving the above equation.

And when solving the equation, it's important to ensure `v2 - v1 != 0` to prevent a divide by zero scenario!

### Big O:  O(1)  (I'm not sure of this...but since we ain't looping anything here, I would think the calculation of y is always constant given the formula)

