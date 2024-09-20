def box(n):
    if n < 4:
        print("More than 4.")
        return
    
    # Print X with closed borders
    for i in range(n):
        for j in range(n):
            
            # Top & Bot borders
            if i < 2 or i >= n-2:
                print('x', end='')
            
            # Left & Right borders    
            elif j < 2 or j >= n-2:
                print('x', end='')
            
            # X on the middle    
            elif i == j or i + j == n-1 or i == j-1 or i+j == n-2 or i == j+1 or i+j == n:
                print('x', end='')
                
            else:
                print(' ', end='')
        print()
    
    
if __name__ == "__main__":
    try:
        n = int(input("n: "))
        
        if n < 3:
            print("ulit")
        else:
            box(n)
                
    except ValueError:
        print("ulit.")