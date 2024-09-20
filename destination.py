def find_intersection(x1, v1, x2, v2):
    # Calculate Player 1's final position with detailed output
    final_position1 = x1 + (x1 * v1)
    position1_steps = ' + '.join([str(x1)] * v1)  # Creates a string like "x1 + x1 + x1"
    
    # Calculate Player 2's final position with detailed output
    final_position2 = x2 + (x2 * v2)
    position2_steps = ' + '.join([str(x2)] * v2)  # Creates a string like "x2 + x2"

    # Print detailed addition for both players
    print(f"Player 1: {x1} + {position1_steps} = {final_position1}")
    print(f"Player 2: {x2} + {position2_steps} = {final_position2}")

    if final_position1 == final_position2:
        return f"They will meet at position {final_position1}."
    else:
        return "They will never meet."

if __name__ == "__main__":
    x1, v1 = map(int, input("Player 1 (x1 v1): ").split())
    x2, v2 = map(int, input("Player 2 (x2 v2): ").split())
    
    result = find_intersection(x1, v1, x2, v2)
    print(result)
