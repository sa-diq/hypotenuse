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
# No cleanup needed