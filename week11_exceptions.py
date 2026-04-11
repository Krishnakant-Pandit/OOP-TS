def safe_int(x):
    try:
        return int(x)
    except:
        print("Invalid input! Please enter a number.\n")
        return 0