def calculate_area(length, width):
    return length * width
'''
Calculate the area of the rectangle by multiplying the length and width b.
Parameters:
    length (float): The length of rectangle
    width (float): The width of the rectangle
'''
# [Put Docstring in this function]
def calculate_perimeter(length, width):
    return 2 * (length + width)
'''
Multiplying the sum of the length and width of the triangle
gives you the total length of the four sides of the rectangle, 
which is the definition of parameter.
'''

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    '''
    The users need to put their desired lenght and width
    to calculate the area and parameter.
    '''
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    '''
    In this part the outcome or 
    the result will be printed.
    '''
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

if __name__ == "__main__":
    main()
