"""FizzBuzz-style number classifier (with one deliberate bug)."""


def classify(number: int) -> str:
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def sequence(n: int) -> list[str]:
    """Return the FizzBuzz classification for each value in 1..n.

    Validates that ``n`` is a positive integer (``int`` and >= 1), raising
    ``ValueError`` otherwise.
    """
    if type(n) is not int or n < 1:
        raise ValueError("sequence() requires a positive integer")
    return [classify(i) for i in range(1, n + 1)]


def range_sequence(start: int, end: int) -> list[str]:
    """Return the FizzBuzz classification for each value in start..end inclusive.

    Validates that ``start`` and ``end`` are positive integers (``int`` and >= 1)
    with ``start <= end``, raising ``ValueError`` otherwise.
    """
    if type(start) is not int or type(end) is not int:
        raise ValueError("range_sequence() requires positive integers")
    if start < 1 or end < 1:
        raise ValueError("range_sequence() requires positive integers")
    if start > end:
        raise ValueError("range_sequence() requires start <= end")
    return [classify(i) for i in range(start, end + 1)]


if __name__ == "__main__":
    import sys

    if sys.argv[1:] and sys.argv[1] == "--range":
        try:
            start = int(sys.argv[2])
            end = int(sys.argv[3])
        except (IndexError, ValueError):
            sys.stderr.write(
                "error: --range requires two positive integers with start <= end\n"
            )
            raise SystemExit(1)
        try:
            for item in range_sequence(start, end):
                print(item)
        except ValueError:
            sys.stderr.write(
                "error: --range requires two positive integers with start <= end\n"
            )
            raise SystemExit(1)
    elif sys.argv[1:] and sys.argv[1] == "--list":
        try:
            n = int(sys.argv[2])
        except (IndexError, ValueError):
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)
        try:
            for item in sequence(n):
                print(item)
        except ValueError:
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)
    else:
        n = int(sys.argv[1])
        print(classify(n))
