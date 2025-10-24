# this function finds the square root of a number using the bisection method
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # handle negative numbers
    if square_target < 0:
        raise ValueError('square root of negative number is not defined in real numbers')
    
    # handle special cases
    if square_target == 1:
        root = 1
        print(f'the square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'the square root of {square_target} is 0')
    
    else:
        # define the initial search range
        low = 0
        high = max(1, square_target)
        root = None
        
        # iterate up to max_iterations
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2
            
            # check if the guess is close enough
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            # adjust the search range
            elif square_mid < square_target:
                low = mid
            else:
                high = mid
        
        # print results
        if root is None:
            print(f'failed to converge within {max_iterations} iterations')
        else:   
            print(f'the square root of {square_target} is approximately {root}')
    
    return root

# example usage
n = 16
square_root_bisection(n)
