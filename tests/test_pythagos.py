import hypotenuse.pythagos
import numpy as np


def test_add_nums():
    '''Test function that adds two numbers'''

    # Arrange
    test_variable_a = 5
    test_variable_b = 7
    expected_output = 12

    # Act
    output = hypotenuse.pythagos.add_nums(test_variable_a, test_variable_b)

    # Assert
    assert output == expected_output
    
    
def test_add_arrays():
    '''Test function that adds two arrays'''

# Arrange
    test_array_a = np.array([2, 4, 6])
    test_array_b = np.array([8, 10, 12])
    expected_output = np.array([10, 14, 18])

    # Act
    output = hypotenuse.pythagos.add_nums(test_array_a, test_array_b)

# Assert
    assert np.allclose(expected_output, output)
    
    
def test_square_num():
    '''Test function that square a number'''

# Arrange
    test_number_a = 9
    expected_output =81
    
    # Act
    output = hypotenuse.pythagos.square_num(test_number_a)

    # Assert
    assert output == expected_output    
    

def test_square_root():
    '''Test for the square root function'''

# Arrange
    test_number_1 = 25
    expected_output =5
    
    # Act
    output = hypotenuse.pythagos.square_root(test_number_1)

    # Assert
    assert output == expected_output 
    
    
def test_calc_hypot():
    '''Test for the square root function'''

# Arrange
    test_number_1 = np.array([34, 67, 23])
    test_number_2 = np.array([22, 8, 32])
    expected_output = np.array([40.49,  67.4759, 39.4081])
    
    # Act
    output = hypotenuse.pythagos.calc_hypot(test_number_1, test_number_2)
    

    # Assert
    assert np.allclose(expected_output, output, rtol=1e-1)



# No cleanup needed