# FirstSecondNumericDiff
A Python class for computing first and second-order numerical derivatives using finite difference methods.

## Features
- Computes first and second derivatives using:
  - Forward Difference
  - Backward Difference
  - Central Difference
- Handles uniformly spaced data.
- Provides warning when handling non-uniformly spaced data.
- Provides error handling for invalid data formats.

## Installation
This class requires Python.

## Usage
To use this module, import it from the numeric_diff package like this:

from numeric_diff import first_second_numeric_diff

And use it like this:

x_data = [1, 2, 3, 4, 5]
y_data = [7.5, 8.3, 9.1, 10.8, 12]
order = 'First'
method = 'Forward'

x_output, y_output = first_second_numeric_diff(x_data, y_data, order, method)

## Methods

### __init__(x_data, y_data, order, method)
Initializes the numerical differentiation class

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
  - order (str): Numerical differentiation order.
  - method (str): Numerical differentiation method.

### __first_second_numeric_differentiation(x_data, y_data, order, method)
Computes the specified derivative.

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
  - order (str): Numerical differentiation order. Options:
    - 'first': Calculates first-order derivative.
    - 'second': Calculates second-order derivative.
  - method (str): Numerical differentiation method. Options:
    - 'forward': Uses forward difference.
    - 'backward': Uses backward difference.
    - 'central': Uses central difference.

### __first_order_differentiation(x_data, y_data, method)
Computes the first derivative.

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
  - method (str): Numerical differentiation method. Options:
    - 'forward': Uses forward difference.
    - 'backward': Uses backward difference.
    - 'central': Uses central difference.
  - Returns: list of independent variable values and list of first derivative values.

### __second_order_differentiation(x_data, y_data, method)
Computes the second derivative.

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
  - method (str): Numerical differentiation method. Options:
    - 'forward': Uses forward difference.
    - 'backward': Uses backward difference.
    - 'central': Uses central difference.
  - Returns: list of independent variable values and list of second derivative values.

### __forward_diff_first_order(x_data, y_data)
Computes the first derivative with forward difference.

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
- Returns: list of independent variable values and list of first derivative values.

### __backward_diff_first_order(x_data, y_data)
Computes the first derivative with backward difference.

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
- Returns: list of independent variable values and list of first derivative values.

### __central_diff_first_order(x_data, y_data)
Computes the first derivative with central difference.

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
- Returns: list of independent variable values and list of first derivative values.

### __forward_diff_second_order(x_data, y_data)
Computes the second derivative with forward difference.

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
- Returns: list of independent variable values and list of first derivative values.

### __backward_diff_second_order(x_data, y_data)
Computes the second derivative with backward difference.

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
- Returns: list of independent variable values and list of first derivative values.

### __central_diff_second_order(x_data, y_data)
Computes the second derivative with central difference.

- Parameters:
  - x_data (list, tuple, set, or NumPy array): Independent variable values.
  - y_data (list, tuple, set, or NumPy array): Dependent variable values.
- Returns: list of independent variable values and list of first derivative values.

## Notes
- If x_data type is not valid, an Exception will rise.
- If y_data type is not valid, an Exception will rise.
- If x_data and y_data do not have the same length, an Exception will rise.
- If length of x_data and y_data is less than 2, an Exception will rise.
- If the elements of x_data and y_data are not valid float values, an Exception will rise.
- If order type is not valid, an Exception will rise.
- If method type is not valid, an Exception will rise.
- If length of x_data and y_data is less than 3 for second-order derivative, an Exception will rise.
- If length of x_data and y_data is less than 3 for first-order derivative with central difference, an Exception will rise.

## Authors
Juan David Amaya Carreño - jd.amaya20@uniandes.edu.co