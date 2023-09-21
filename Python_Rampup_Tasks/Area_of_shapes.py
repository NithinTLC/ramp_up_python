def calculate_area(a = None,b = None,c = None):
    try:
        print(""" ********Important note*********
                    1) For Triangle give the base ,height and also  T string parameter to get the area of triangle
                    2) For Rectangle length and width
                    3) For Circle give only radius  
                       """)
        #Triangle
        if a!=None and b!=None and c!=None and c=="T" or  c=="t":
            area=0.5*a*b
            print(f"The area of Triangle is: {area:.2f} CM^2")
        #Rectangle
        elif  a!=None and b!=None and c==None:
            area = a * b
            print(f"The area of Rectangle is: {area:.2f} CM^2")
        #Circle
        elif a != None and b == None and c == None:
            area = 3.14*(a**a)
            print(f"The area of Circle is: {area:.2f} CM^2")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

try:
    calculate_area(8.58, 2, "T")
except Exception as e:
    print(f" An error occurred:  {str(e)}")