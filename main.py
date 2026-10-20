BITS = 8
MAX_VALUE = (1 << BITS) - 1


def read_byte(prompt: str) -> int:
    """Read an integer in the range that fits in one byte."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if 0 <= value <= MAX_VALUE:
            return value
        print(f"Enter a number from 0 to {MAX_VALUE}.")


def show_result(label: str, value: int) -> None:
    """Print a result as both decimal and 8-bit binary."""
    print(f"{label:<12} {value:>3}  {value:0{BITS}b}")


def main() -> None:
    print("Bitwise operations work on the individual bits in a number.")
    print(f"This demo uses {BITS}-bit values (0 to {MAX_VALUE}).\n")

    first = read_byte("First number:  ")
    second = read_byte("Second number: ")

    print("\nDecimal  Binary")
    print(f"A        {first:0{BITS}b}")
    print(f"B        {second:0{BITS}b}")
    print("\nOperation   Decimal  Binary")
    show_result("A AND B", first & second)
    show_result("A OR B", first | second)
    show_result("A XOR B", first ^ second)
    show_result("NOT A", (~first) & MAX_VALUE)
    show_result("A << 1", (first << 1) & MAX_VALUE)
    show_result("A >> 1", first >> 1)

    print("\nAND keeps bits that are 1 in both numbers.")
    print("OR keeps bits that are 1 in either number.")
    print("XOR keeps bits that are different.")
    print("NOT flips each bit; shifts move bits left or right.")


if __name__ == "__main__":
    main()