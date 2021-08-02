# Problem

View the problem: [pdf](./Apple\ and\ Orange Problem.pdf) or [web](https://www.hackerrank.com/challenges/apple-and-orange/problem)

# Analysis

First, I don't think the problem was very well articulated.  The idea that the apple tree is on the **LEFT** of the house and that the orange tree is on the **RIGHT** of the house, isn't represented properly.

In my opinion, if the values of of the apples list is **positive**, that would mean it fell towards the house.  I think everyone can agree to that.

However, if the values of the oranges list is **positive**, that would mean it fell **AWAY** from the house, considering that the orange tree is on the *RIGHT* of the house.  

I initially was thinking of performing: `map(lambda x: x*-1, oranges)` and subsequently filtering the positive values (meaning they fell towards the house).  This is wrong of-course.  

I think the problem should be modified to make it more challenging.  This is too easy.

### Big O:  O(n)

