def generate_garbage(n):
    with open("garbage.py", "w") as file:
        file.write(f"num = int(input())\n")
        for num in range(1, n + 1):
            file.write(f"if num == {num}:\n")
            if num % 2 == 1:
                file.write(f"    print('odd')\n")
                print(f"Number {num} written.")
            elif num % 2 == 0:
                file.write(f"    print('even')\n")
                print(f"Number {num} written.")


def main():
    n = int(input("Enter the value of n: "))
    generate_garbage(n)

if __name__ == "__main__":
    main()
