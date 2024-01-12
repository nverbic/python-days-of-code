''' #2 day challenge:
    Create a program to calculate the area of a circle given its radius.

    Output:
    Area of the circle with radius 5.5 is 95.03.
'''

import math

def calculate_circle_area(radius):
    '''' Calculate circle area '''
    area = round(math.pi * radius**2, 2)
    return area

if __name__ == '__main__':
    radius = 5.5
    area = calculate_circle_area(radius)
    print(f"Area of the circle with radius {radius} is {area}.")
