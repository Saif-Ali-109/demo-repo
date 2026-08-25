"""
FizzBuzz-style number classifier.
"""

def classify(number: int) -> str:
    """Determine the FizzBuzz classification for a given integer."""
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)

def sequence(n: int) -> list[str]:
    """Generate a sequence of FizzBuzz classifications."""
    if not isinstance(n, int) or n < 1:
        raise ValueError("sequence() requires a positive integer")
    return [classify(i) for i in range(1, n + 1)]

def csv_line(values: list[str]) -> str:
    """Convert a list of values to CSV format."""
    return ",".join(values)

def range_values(start: int, end: int) -> list[str]:
    """Generate FizzBuzz classifications for a range of values."""
    if not isinstance(start, int) or not isinstance(end, int) or start < 1 or start > end:
        raise ValueError("range_values() requires positive start <= end integers")
    return [classify(i) for i in range(start, end + 1)]

if __name__ == "__main__":
    import sys

    # Parse args
    args = sys.argv[1:]
    is_csv = "--csv" in args
    args = [a for a in args if a != "--csv"]

    try:
        if not args:
            if is_csv:
                raise ValueError("error: --csv requires --list or --range")
            raise ValueError("error: requires a positive integer")

        if args[0] == "--list":
            if len(args) != 2:
                raise ValueError("error: --list requires a positive integer")
            try:
                n = int(args[1])
            except ValueError:
                raise ValueError("error: --list requires a positive integer")
            res = sequence(n)
        elif args[0] == "--range":
            if len(args) != 3:
                raise ValueError("error: --range requires start <= end integers")
            try:
                start, end = int(args[1]), int(args[2])
            except ValueError:
                raise ValueError("error: --range requires start <= end integers")
            res = range_values(start, end)
        else:
            if is_csv:
                raise ValueError("error: --csv requires --list or --range")
            try:
                n = int(args[0])
            except ValueError:
                raise ValueError("error: requires a positive integer")
            if n < 1:
                raise ValueError("error: requires a positive integer")
            res = [classify(n)]

        if is_csv:
            print(csv_line(res))
        else:
            for item in res:
                print(item)

    except ValueError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)
