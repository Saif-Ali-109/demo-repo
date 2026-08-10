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


def csv_line(values: list[str]) -> str:
    """Join classification values into a single comma-separated line.

    No trailing comma and no spaces: ``csv_line(["1","Fizz"])`` -> "1,Fizz".
    """
    return ",".join(values)


def range_values(start: int, end: int) -> list[str]:
    """Return the FizzBuzz classification for each value in start..end.

    Validates that both ``start`` and ``end`` are integers and that
    ``start <= end``, raising ``ValueError`` (in the same style as
    ``sequence()``) otherwise.
    """
    if type(start) is not int or type(end) is not int or start > end:
        raise ValueError("range_values() requires start <= end integers")
    return [classify(i) for i in range(start, end + 1)]


if __name__ == "__main__":
    import sys

    raw = sys.argv[1:]
    csv_output = "--csv" in raw
    args = [a for a in raw if a != "--csv"]

    def _print_values(values):
        if csv_output:
            print(csv_line(values))
        else:
            for item in values:
                print(item)

    if not args:
        if csv_output:
            sys.stderr.write("error: --csv requires --list or --range\n")
            raise SystemExit(1)
        sys.stderr.write("error: requires a positive integer\n")
        raise SystemExit(1)

    if args[0] == "--list":
        try:
            n = int(args[1])
        except (IndexError, ValueError):
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)
        try:
            values = sequence(n)
        except ValueError:
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)
        _print_values(values)
    elif args[0] == "--range":
        try:
            start = int(args[1])
            end = int(args[2])
        except (IndexError, ValueError):
            sys.stderr.write("error: --range requires two integers\n")
            raise SystemExit(1)
        try:
            values = range_values(start, end)
        except ValueError:
            sys.stderr.write("error: --range requires start <= end integers\n")
            raise SystemExit(1)
        _print_values(values)
    else:
        # bare-number mode
        if csv_output:
            sys.stderr.write("error: --csv requires --list or --range\n")
            raise SystemExit(1)
        try:
            n = int(args[0])
        except ValueError:
            sys.stderr.write("error: requires a positive integer\n")
            raise SystemExit(1)
        print(classify(n))
