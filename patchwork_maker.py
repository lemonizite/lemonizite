#--------------------------------------#

"""------------o------------"""
""" [!] PATCHWORK MAKER [!] """
"""------------o------------"""

# 3 9 5

#--------------------------------------#
from graphix import *
#--------------------------------------#

# the main program
def main():
    size_input, colour_inputs = get_inputs()
    window = create_window(size_input)
    draw_patchwork(window, size_input, colour_inputs)
    extention()
                
#--------------------------------------#                

""" [!] GET INPUTS [!] """

def get_inputs():
    size_input = get_size()
    colour_inputs = get_colours()
    return size_input, colour_inputs

def get_size():
    valid_sizes = [5, 7, 9]
    while True:
        size_input = input("Please input size: ")
        if size_input.isdigit():
            if int(size_input) in valid_sizes:
                print("Valid input.\n")
                break
            else:
                print("Invalid input.\n")
        else:
            print("Integer Values only.\n")
    return int(size_input)
                
def get_colours():
    valid_colours = ["red", "green", "blue", "magenta", "orange", "purple"]
    colour_inputs = []
    for i in range(3):
        while True:
            colour_input = input("Please input colour: ")
            if colour_input in valid_colours:
                if colour_input not in colour_inputs:
                    print("Valid colour.\n")
                    colour_inputs.append(colour_input)
                    break
                else:
                    print("Input unique colour.\n")
            else:
                print("Input valid colour.\n")
    return colour_inputs
            
#--------------------------------------# 

""" [!] CREATE WINDOW [!] """

def create_window(size_input):
    window = Window("Patchwork Maker", size_input * 100, size_input * 100)
    return window
                
#--------------------------------------#

""" [!] DRAW PATCHWORK [!] """

def draw_patchwork(window, size_input, colour_inputs):
    window_length = size_input * 100
    condition = size_input * 50 - 50 
    for y in range(0, window_length, 100):
        for x in range(0, window_length, 100):
            iteration_colour = check_colour(x, y, colour_inputs, condition)
            iteration_patch = check_patch(window, size_input, x, y, iteration_colour)

def check_colour(x, y, colour_inputs, condition):
    # selects first colour for patch
    if x < condition and y < condition \
    or x > condition and y > condition:
        iteration_colour = colour_inputs[0]
        
    # selects second colour for patch
    elif x == condition or y == condition:
        iteration_colour = colour_inputs[1]
            
    # selects third colour for patch
    else:
        iteration_colour = colour_inputs[2]
        
    return iteration_colour

def check_patch(window, size_input, x, y, iteration_colour):
    tile_length = 100
    # draws patch c
    if (x // tile_length) % 2 == 0:
        draw_patch_c(window, tile_length, x, y, iteration_colour)
            
    # draws patch b
    elif y >= tile_length and y < (size_input * 100 - tile_length):
        draw_patch_b(window, tile_length, x, y, iteration_colour)
            
    # draws patch a
    else:
        draw_patch_a(window, tile_length, x, y, iteration_colour)

#--------------------------------------#
        
""" [!] DRAWS PATCHES [!] """

def draw_patch_a(win, tile_length, x, y, colour):
    # square used in multiple patches so uses external function
    point_tl = Point(x, y)
    point_br = Point(x + tile_length, y + tile_length)
    draw_square(win, point_tl, point_br, colour)

# draws patch b
def draw_patch_b(win, tile_length, x, y, colour):
    # finds dimensions of smaller tiles
    small_tile = tile_length // 5
    half_tile = small_tile // 2
    # creates patchwork grid within a patchwork tile
    for row in range(5):
        for column in range(5):
            # calulates values used per iteration
            x_pos = x + column * small_tile
            y_pos = y + row * small_tile
            centre = Point(x_pos + half_tile, \
                           y_pos + half_tile)
    
            # decides to draw square or circle from position
            if (row + column) % 2 == 0:
                draw_square(win, Point(x_pos, y_pos), \
                            Point(x_pos + small_tile, y_pos + small_tile), \
                            colour)
            else:
                draw_circle(win, centre, half_tile, colour)
                # decides triangle direction from row
                if row % 2 == 0:
                    triangle_direction = "left"
                else:
                    triangle_direction = "right"
                draw_triangle(win, x_pos, y_pos, triangle_direction)
                
# draws patch c
def draw_patch_c(win, tile_length, x, y, colour):
    # adds one to tile length as 11 lines must be drawn for this patch
    for i in range(0, tile_length + 1, 10):
        # draws top-down lines
        draw_line(win, Point(x + i, y), \
                  Point(x + tile_length - i, y + tile_length), colour)
        # draws left-right lines
        draw_line(win, Point(x, y + i), \
                  Point(x + tile_length, y + tile_length - i), colour)        
        
#--------------------------------------#

""" [!] SHAPES USED IN PATCHES [!] """

# draws a line
def draw_line(win, line_p1, line_p2, colour):
    line = Line(line_p1, line_p2)
    line.fill_colour = colour
    line.draw(win)

# draws a square
def draw_square(win, p1, p2, colour):
    square = Rectangle(p1, p2)
    square.fill_colour = colour
    square.outline_colour = colour
    square.draw(win)

def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_colour = colour
    circle.draw(win)
    
# draws a triangle
def draw_triangle(win, x, y, direction):
    # confirms left or right position
    if direction == "left":
        a = Point(x, y)
        b = Point(x, y + 20)
        c = Point(x + 10, y + 10)
    else:
        a = Point(x + 20, y)
        b = Point(x + 20, y + 20)
        c = Point(x + 10, y + 10)
        triangle = Polygon(points=[a, b, c])
        
    triangle = Polygon(points=[a, b, c])
    triangle.fill_colour = "white"
    triangle.outline_colour = "white"
    triangle.draw(win)
        
#--------------------------------------#

""" [!] IGNORE FROM HERE, CODE DOES NOT WORK [!] """

def extension():
    pass
    selected_patch = None
    border = None
    while True:       
        # Check for mouse click event
        
        mouse_click = window.check_mouse()
        
        if mouse_click:
            click_row = mouse_click.y // tile_length
            click_column = mouse_click.x // tile_length

            # If clicking the same patch, deselect it
            if selected_patch == (click_row, click_column):
                selected_patch = None  # Deselect the patch
                if border:  # Remove the border if it exists
                    border.undraw()
                continue  # Skip the key press checks for now (as we're handling the click)

            # If it's a new patch, select it and draw the border
            selected_patch = (click_row, click_column)

            # Remove the old border, if any
            if border:
                border.undraw()

            # Draw a new border around the selected patch
            border = draw_border(win, click_row, click_column, tile_length)

        # Check for key press events
        key_press = win.check_key()
        if key_press:
            if key_press in ["Up", "Down", "Left", "Right"]:
                if key_press == "Up":
                    new_row = click_row - 1
                    new_column = click_column
                elif key_press == "Down":
                    new_row = click_row + 1
                    new_column = click_column
                elif key_press == "Left":
                    new_row = click_row
                    new_column = click_column - 1
                elif key_press == "Right":
                    new_row = click_row
                    new_column = click_column + 1
                if 0 <= new_row < size_input and 0 <= new_column <= size_input:
                    """MOVE PATCH"""
                    for i in range(10):
                        border.undraw()
                        draw_border(win)
                    
            
            
            elif key_press == 'x':
                draw_square(win, Point(click_column * tile_length, click_row * tile_length),
                Point((click_column + 1) * tile_length, (click_row + 1) * tile_length), "white")
                if border:
                    border.undraw()
                border = None 
                
            elif key_press in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print(f"Patch updated with key {key_press}")  # Replace with patch change logic
            elif key_press == 'Esc':
                selected_patch = None
                if border:
                    border.undraw()
    
#--------------------------------------#

""" [!] EXTENTION FUNCTIONS [!] """

# draws border
def draw_border(win, click_row, click_column, tile_length):
    border = Rectangle(
                Point(click_column * tile_length, click_row * tile_length),
                Point((click_column + 1) * tile_length, (click_row + 1) * tile_length)
            )
    border.outline_width = 3
    border.outline_colour = "black"
    border.draw(win)
    return border

def border_animation(win, point, tile_length, key_press):
    if key_press == "Up":
        border_tl = Point(point.x, point.y)
        border_br = Point(point.x + tile_length, point.y + tile_length)             
        border = Rectangle(border_tl, border_br)
        border_tl += Point(0, 0)   
    
#--------------------------------------#
    
    
    
#--------------------------------------#
    
    
    
#--------------------------------------#
    
    
    
#-----#
main()
#-----#