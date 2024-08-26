# Generally used in function
# finally will execute even if we return the function

def main():
    try:
        a = int(input("Enter your number: "))
        print(a)
        return

    except Exception as e:
        print(e)

    finally:
        print("I am inside finally")

main()