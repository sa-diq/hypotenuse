# Module to calculate the hypotenuse of a right angled triangle

# Function to add two numbers
# input: float or int or list/array of ints/floats
def add_nums(a,b):
    """Add two numbers together

    Args:
        a (int, float, array): A number to add
        b (int, float, array): A number to add

    Returns:
        _type_: _description_
    """
    sum_of_nums = a + b
    return sum_of_nums
    

# Function to calculate the square of a number
# input: float or int or list/array of ints/floats
def square_num(a):
    """square a number

    Args:
        a (int/float/array): Number(s) to be squared

    Returns:
        float, int, array:squared number
    """
    squared = a**2
    return squared



# Function to calculate the square root of a number
# input: float or int or list/array of ints/floats
def square_root(a):
    square_root_num   = a ** 0.5
    return square_root_num


# Function to calculate hypotenuse using all of the above
# formula: a^2 = b^2 + c^2
# c = sqrt(a^2 +b^2)
# input: float or int or list/array of ints/floats


def calc_hypot(opposite, adjacent):
    """Calculate hypotenuse

    Args:
        opposite (int, float, array): _description_
        adjacent (int, float, array): _description_
    """
    opp_squared = square_num(opposite)
    adj_squared = square_num(adjacent)
    nums_add = add_nums(adj_squared, opp_squared)
    hypot = square_root(nums_add)
    return hypot