def calculate_area(a=None, b=None, c=None):
    try:

        # Triangle
        if a is not None and b is not None and c is not None and (c == "T" or c == "t"):
            area = 0.5 * (int(a) * int(b))
            print(f"The area of Triangle is: {area:.2f} CM^2")
        # Rectangle
        elif a is not None and b is not None and c is None:
            area = int(a) * int(b)
            print(f"The area of Rectangle is: {area:.2f} CM^2")
        # Circle
        elif a is not None and b is None and c is None:
            area = 3.14 * (int(a) ** 2)
            print(f"The area of Circle is: {area:.2f} CM^2")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

try:
    print(""" ********Important note*********
                    1) For Triangle give the base ,height and also  T string parameter to get the area of triangle
                    2) For Rectangle length and width
                    3) For Circle give only radius
                       """)
    userin = input("enter the values for area separate it by comma: ")
    inval = userin.split(",")
    if len(inval) == 3 and (inval[-1] == "T" or inval[-1] == "t"):
        a, b, c = inval[0], inval[1], inval[2]
        calculate_area(a, b, c)
    elif len(inval) == 2:
        a, b = inval[0], inval[1]
        calculate_area(a, b)
    elif len(inval) == 1:
        a = inval[0]
        calculate_area(a)
except Exception as e:
    print(f"An error occurred: {str(e)}")
