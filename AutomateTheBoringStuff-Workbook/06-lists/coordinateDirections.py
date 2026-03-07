import re

def get_end_coordinates(directions):
    
    # Initialize the final result list.
    cartesianCoords = [0, 0] # (X, Y) Coordinates
    
    # Initialize patterns with Regex to ignore case without using string.lower().
    north = re.compile(r"n", re.IGNORECASE)
    south = re.compile(r"s", re.IGNORECASE)
    west = re.compile(r"w", re.IGNORECASE)
    east = re.compile(r"e", re.IGNORECASE)
        
    # Navigate through the list.
    for index, item in enumerate(directions):

        if north.match(item):
            cartesianCoords[1] += 1 # Increase the Y coordinate by 1.
        if south.match(item):
            cartesianCoords[1] -= 1 # Decrease the Y coordinate by 1.
        if east.match(item):
            cartesianCoords[0] += 1 # Increase the X coordinate by 1.
        if west.match(item):
            cartesianCoords[0] -= 1 # Decrease the X coordinate by 1.
    return cartesianCoords

if __name__ == "__main__":
    directions = [] # Initialize empty list
    print("Please enter a direction N, S, E, or W (or enter a blank line to finish):")
    while True:
        
        direction = input().strip() # Capture input once per.
        
        if not direction: # Check that input isn't empty.
            break # Exit the loop.
        
        directions.append(direction) # Append direction to our input list.
    
    cartesianList = get_end_coordinates(directions) # Call Cartesian method.
    print(cartesianList) # Print the result of the method call.
    
