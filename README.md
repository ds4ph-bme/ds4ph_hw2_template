# Homework 2

In a single jupyter notebook file named `hw2.ipynb` create the following:

1. A sorting hat program called `sorting_hat` that, when run, takes in Y or N answers and returns your Hogwart's house between Gryffindor and Slytherine using `if/elif/else` statements. The sorting hat program should have at least 2 simple yes/no questions using python's `input` function. You can use any questions that you'd like and determine the Hogwart's house any way that you'd like. Have the selected house be the return value of the function.
2. Write an class `mydata` that takes in a list of numbers and has the methods: `mean` and `std` (for standard deviation) returning the mean and standard deviation respectively. This should calculate the mean and standard deviation using only base python functions. Try it out with `x = mydata([1, 2, 7, 5])`.
3. Create a function called `lag` as follows. It takes in a numpy vector, say `a = numpy.array( [1, 6, 8, 4] )` and an integer > 0. It then returns the list lagged by the integer value. So, `lag(a, 1)` will return `[nan, 1, 6, 8]` and `lag(a, 2)` will return `[nan, nan, 1, 6]`. That is, it gets rid of `n` values at the end and appends that many `nan`s at the beginning. Use `numpy`'s `nan` for the missing values. It should return a numpy array. Do not uses numpy's existing lag, lead, roll etcetera functions. Instead, use numpy indexing.
4. Using your code from 3, write a function `lagGenerator` that returns - a function - that lags by a specific amount. So`lagGenerator(2)` creates a function that lags a vector by 2.  Use the `lambda` operator in python.

Write your code in a single jupyter notebook called hw2.ipynb
