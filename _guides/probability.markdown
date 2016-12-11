---
layout: post
title: "Probability"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["probability"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Other Materials

https://www.khanacademy.org/mission/probability

# Harvard Course

## Probability and counting

[Harvard Course Home](https://itunes.apple.com/it/course/statistics-110-probability/id502492375?l=en)

### Sample space and events

* A **Sample space** is the set of all possible outcome of an experiment.
* An **event** is a subset of the sample space.

### Naive defintion of probability

A naive definition of probability of an event A is

$$P(A) = \frac{NumberOfPositiveOutcomes}{ NumberOfPossibleOutcomes}$$

example:
carte da poker

This naive definition make sense if:

* all the outcomes are equally likely
* the sample space is finite

### Counting


# Binomial Coefficient

In combinatorics, $$ \binom{n}{k} $$ is interpreted as the number of k-element subsets (the k-combinations) of an n-element set, that is the number of ways that k things can be "chosen" from a set of n things. Hence, it is often read as "n choose k" and is called the choose function of n and k.


For non-negative integers n and k, the binomial coefficient is defined by the factorial representation

$$
\binom{n}{k}
 = \frac{n!}{k!\,(n-k)!}
\quad \mbox{if}\ k\in\{0,1,\ldots,n\}, \qquad (1)
$$

and

$$
 {n \choose k} = 0 \quad \mbox{if } k>n,
$$

where $$ n! $$ denotes the factorial of n.

## Demonstration

Equality of sets: Two sets are equal if and only if they have the same elements.
So you don't create a new combination if you choose the same elements in a different order.

The number of ordered k-combibation is easier to deduce. At the first step
is to choose an element between $$ n $$, you have n choice.
At the second step you choose an element between $$ n-1 $$ elements and
so forth.
When you need to choose the last element you will choose between $$ n -
(k-1) = n - k + 1 $$ elements.
The product of the possible choice at each step is number of ordered k-combibation:

$$ n(n-1)(n-2)...(n-k+1) $$

to get the number k-combinations (unorderd set) we need to remove from
this product the factor that represent the number of permutation of k
elements, which is the number of ordered k-combibation of a set of
k-elements:

$$ k(k-1)(k-2)...(k-k+1) = k(k-1)(k-2)...(1) = k! $$

so finally we can say:

$$
\binom{n}{k}
= \frac{n \cdot (n-1) \cdots (n-k+1)} {k \cdot (k-1) \cdots 1}
= \frac{n \cdot (n-1) \cdots (n-k+1)} {k \cdot (k-1) \cdots 1} \frac{(n-k) \cdots (1)} {(n-k) \cdots (1)}
 = \frac{n!}{k!\,(n-k)!}
\quad \mbox{if}\ k\in\{0,1,\ldots,n\}, \qquad (1)
$$

# Standard Deviation

http://www.mathsisfun.com/data/standard-deviation.html

# Test MathJax

$$ \binom{n}{k} $$

$$ a^2 + b^2 = c^2 $$

$$ \sum_1^n $$

$$
\begin{align}
 \sqrt{37} & = \sqrt{\frac{73^2-1}{12^2}} \\
 & = \sqrt{\frac{73^2}{12^2}\cdot\frac{73^2-1}{73^2}} \\
 & = \sqrt{\frac{73^2}{12^2}}\sqrt{\frac{73^2-1}{73^2}} \\
 & = \frac{73}{12}\sqrt{1 - \frac{1}{73^2}} \\
 & \approx \frac{73}{12}\left(1 - \frac{1}{2\cdot73^2}\right)
 \end{align}
$$
