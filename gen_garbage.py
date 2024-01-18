
def generate_garbage(n):
    with open("garbage.py", "w") as file:
        for num in range(1, n + 1):
            file.write(f"if num == {num}:\n")
            if num % 2 == 1:
                file.write(f"    print('odd')\n")
            elif num % 2 == 0:
                file.write(f"    print('even')\n")

def main():
    n = int(input("Enter the value of n: "))
    generate_garbage(n)

if __name__ == "__main__":
    main()
