def white_rook_can_capture(rook, board):
    possible_captures = []
    for key, value in board.items():
        # Rank = row
        # File = column
        if (value[0] == 'b'): # Current piece is black
            if (key[0] == rook[0] or key[1] == rook[1]): # Piece is in same rank or file
                possible_captures.append(key) # Add current space to list
    return possible_captures

if __name__ == "__main__":
    
    capture_list = white_rook_can_capture('d3', 
        {'d7': 'bQ', 'd2': 'wB', 'f1': 'bP', 'a3': 'bN'})
    
    print(capture_list)