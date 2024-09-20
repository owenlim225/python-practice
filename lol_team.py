def team(roles):
    T = 0 # Top
    M = 0 # Mid
    J = 0 # Jungler
    B = 0 # Bottom
    S = 0 # Support
    
    for i in roles:
        if i == 'T':
            T += 1
        
        elif i == 'M':
            M += 1
        
        elif i == 'J':
            J += 1
            
        elif i == 'B':
            B += 1
            
        elif i == 'S':
            S += 1
            
    if T == 0 or M == 0 or J == 0 or B == 0 or S == 0:
        print("No team.")
        return 0
    
    return min(T, M, J, B, S)


if __name__ == "__main__":
    roles = input("Roles: ").upper()
    game = team(roles)
    
    if game > 0:
        print(f"5-man Team: {game}")