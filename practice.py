def generate_boxed_X_with_borders(n):
    if n < 4:
        print("Size should be at least 4 to accommodate the border and X.")
        return

    for i in range(n):
        for j in range(n):
            # Check for top/bottom border (first 2 or last 2 rows)
            if i < 2 or i >= n - 2:
                print('X', end='')
            # Check for left/right border (first 2 or last 2 columns)
            elif j < 2 or j >= n - 2:
                print('X', end='')
            # Check for the main X pattern with thickness of 2
            elif i == j or i + j == n - 1 or i == j - 1 or i + j == n - 2 or i == j + 1 or i + j == n:
                print('X', end='')
            else:
                print(' ', end='')
        print()  # Move to the next line after each row

# Get the user input for n
try:
    n = int(input("Enter the size of the boxed X (must be at least 4): "))
    if n > 3:
        generate_boxed_X_with_borders(n)
    else:
        print("Please enter an integer greater than 3.")
except ValueError:
    print("Invalid input. Please enter an integer.")
