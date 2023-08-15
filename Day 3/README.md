# Operators and Expressions

Operators and expressions play a vital role in performing various operations in Python. They allow you to manipulate variables, compare values, perform arithmetic calculations, and more. In this video, we will explore different types of operators and expressions in Python. Let's dive in!

1. Arithmetic operators

Arithmetic operators are used to perform basic mathematical calculations. Here are some common arithmetic operators in Python:

* Addition (+): Adds two values together.
* Subtraction (-): Subtracts one value from another.
* Multiplication (*): Multiplies two values.
* Division (/): Divides one value by another.
* Modulo (%): Returns the remainder of the division.
* Exponentiation (**): Raises a value to the power of another. Example:

``` 
x = 10
y = 5
sum_result = x + y
difference_result = x - y
product_result = x * y
division_result = x / y
modulo_result = x % y
exponentiation_result = x ** y
```

2. Comparison operators

Comparison operators are used to compare values and return a Boolean result (True or False). Here are some common comparison operators in Python:
* Equal to (==): Checks if two values are equal.
* Not equal to (!=): Checks if two values are not equal.
* Greater than (>): Checks if one value is greater than another.
* Less than (<): Checks if one value is less than another.
* Greater than or equal to (>=): Checks if one value is greater than or equal to another.
* Less than or equal to (<=): Checks if one value is less than or equal to another.
Example:

```
x = 10
y = 5
is_equal = x == y
is_not_equal = x != y
is_greater_than = x > y
is_less_than = x < y
is_greater_than_or_equal = x >= y
is_less_than_or_equal = x <= y
```
3. Logical operators

Logical operators are used to combine multiple conditions and evaluate their truthiness. Here are the three logical operators in Python:

* AND: Returns True if both conditions are True.
* OR: Returns True if at least one condition is True.
* NOT: Negates the truth value of a condition.
Example:

```
x = 10
y = 5
z = 8
logical_and = x > y and y < z
logical_or = x > y or y > z
logical_not = not(x > y)
```

4. Assignment operators

Assignment operators are used to assign values to variables. They combine the assignment (=) operator with other operators. Here's an example:

```
x = 10
x += 5  # Equivalent to x = x + 5
```
In this example, the value of x is increased by 5 and assigned back to x using the += assignment operator.

5. Expressions and precedence

Expressions are combinations of operators and operands that produce a value. Python follows a specific order of precedence for evaluating expressions. Parentheses can be used to override the default precedence. Example:

```
result = (x + y) * z
```

In this example, the expression inside the parentheses is evaluated first before multiplying it by z.

Understanding operators and expressions allows you to perform various operations in Python effectively. In the next video, we will explore control flow statements, including conditional statements. Stay tuned!