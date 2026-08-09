"""FizzBuzz-style number classifier (with one deliberate bug)."""


def classify(number: int) -> str:
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    print(classify(n))
