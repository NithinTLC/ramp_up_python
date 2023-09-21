## Author: Nithin
## Code for Calculating Area of Geometric Shapes

This code is a Python script that allows you to calculate the area of different geometric shapes, including triangles, rectangles, and circles. It takes user input for the shape and its dimensions and then computes and displays the area.

### Usage

To use this code, follow these steps:

1. **Run the Script**

   Execute the script in a Python environment. You can do this by saving the code in a `.py` file and running it using a Python interpreter.

2. **Input Format**

   The code expects input in the following format:

   - For **Triangle**: Enter the base, height, and "T" (or "t") to specify the shape.
   - For **Rectangle**: Enter the length and width.
   - For **Circle**: Enter only the radius.

3. **Example Input**
4. **Enter Values**

After running the script, it will prompt you to enter values for the area calculation. Separate the values by commas as per the instructions.

Example input for a triangle: `5, 10, T`
Example input for a rectangle: `4, 7`
Example input for a circle: `3`

5. **View Result**

The code will calculate the area based on the input provided and display the result with two decimal places (CM^2).

### Code Explanation

The script consists of two main parts:

- **`calculate_area` Function**: This function calculates the area based on the provided input. It checks the shape identifier and dimensions and performs the corresponding area calculation for triangles, rectangles, or circles.

- **User Input Handling**: The script guides the user to input the values correctly for each shape. It splits the input values and calls the `calculate_area` function with the appropriate arguments. Any errors during execution are caught and displayed.

### Example

Here's an example of how you can use the script:

1. Run the script.

2. Input: `5, 10, T`

3. Output: `The area of Triangle is: 25.00 CM^2`

4. You can similarly calculate the areas of rectangles and circles by following the input format.



