"""SYST/CYSE 130
Pb2: Polygon Properties
Author: Joshua R Obee
Purpose: The program calculates and displays 
the properties (area, perimeter, internal angles) 
of a polygon based on user input, then draws 
the polygon using turtle graphics.
"""

# Import necessary libraries
from math import tan, pi
import turtle as t
import os

def get_user_input():
    #Get user input for the number of sides and side length
    n = int(input("Enter number of sides, must be greater than 2 (enter integer only): "))
    s = int(input("Enter length of each side (enter integer only): "))
    return n, s

def calculate_properties(n, s):
    #Calculate polygon properties such as area, internal angle, external angle, and perimeter
    Area = n * s ** 2 / (4 * tan(pi / n))  # Area of the polygon
    I = (180 * (n - 2)) / n  # Internal angle of the polygon
    O = 360 / n  # External angle of the polygon
    P = n * s  # Perimeter of the polygon
    return Area, I, O, P

def setup_turtle():
    #Setup turtle graphics
    t.tracer(1000000)
    t.speed(10000000)
    t.left(90)

def draw_polygon(n, O):
    #Draw the polygon and return its coordinates
    coord = []
    for _ in range(n):
        t.left(O)
        t.forward(100)
        coord.append((t.xcor(), t.ycor()))
        t.goto(0, 0)
    return coord

def display_properties(n, s, Area, P, I):
    #Display the calculated properties of the polygon.
    n_str = str(n)
    Area_str = str(round(Area, 2))
    s_str = f'{float(s):.1f}'
    P_str = f'{float(P):.2f}'
    I_str = f'{float(I):.2f}'

    properties = [
        (115, 60, f"Num of sides = {n_str}"),
        (115, 40, f"Side length = {s_str}"),
        (115, 20, f"Area = {Area_str}"),
        (115, 0, f"Perimeter = {P_str}"),
        (115, -20, f"Internal Angles = {I_str}")
    ]

    t.pu()
    t.hideturtle()
    t.right(90)
    for x, y, text in properties:
        t.goto(x, y)
        t.write(text, move=False, align="left")

def handle_redraw():
    #Handle the redraw or exit option
    script_dir = os.path.dirname(__file__)
    data_path = os.path.join(script_dir, 'joshua_obee_pb2.py')

    if t.textinput('Redraw', 'Enter Yes or Y to redraw; Enter any other key to quit.') in ['Yes', 'yes', 'Y', 'y']:
        t.resetscreen()
        t.color('green')
        style = ('Courier', 15, 'bold')
        t.write('Please close this tab and return to the Python console', font=style, align='center')
        t.hideturtle()
        t.done()
        os.system(f'py {data_path}')
    else:
        print("\nOk, goodbye!")
        t.done()

# Main program
if __name__ == "__main__":
    n, s = get_user_input()
    Area, I, O, P = calculate_properties(n, s)
    setup_turtle()
    coord = draw_polygon(n, O)
    # Close the polygon by connecting the last point to the first
    new_coord = coord + [coord[0]]
    for point in new_coord:
        t.goto(point)

    display_properties(n, s, Area, P, I)
    handle_redraw()
