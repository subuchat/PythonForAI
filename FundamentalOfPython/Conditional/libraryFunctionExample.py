import numpy as np # You can rename and use
import random      # you may use directly too
import matplotlib.pyplot as plt
import inspect
import math
from math import pi

def main():
    #generate_random()
    generate_random_using_seed()
    #generate_sin()
    #print("Sin of 360 degree from numpy: ", np.sin(2*np.pi))
    #generate_plotting()
    test_method()

def test_method():
    result = round(math.sqrt(16) + pi)
    print(result)

def generate_random_using_seed():
    random.seed(42)
    result1 = random.randint(50, 100)
    random.seed(42)
    result2 = random.randint(50, 100)

    print(result1, result2)

def generate_random():
    val = random.randint(0,10) #generate a random number within the range
    print("Random value : ", val)

def generate_sin():
    val = np.sin(2*3.1415)
    print("Sin valu of 2Pi(360 degree):", val)
    
def generate_plotting():
    plt.plot([1,2,3,4,5],[1,4,9,16,25]) # x and y values , plotting value against it square
    plt.show() # THis is required to show pop up the window
    # TO READ OTHERS SOURCE CODE , YOU CAN USE INSPECT'S GETSOURCE
    #source_code = inspect.getsource(plt.plot)
    #print(source_code)

if __name__ == "__main__":
    main()
