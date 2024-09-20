def eve(user):
    return user.count("eve")


if __name__ == "__main__":
    user = input("name: ")
    
    name = eve(user)
    print(f"eve appeared {name} times")