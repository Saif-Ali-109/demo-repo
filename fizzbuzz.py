"""
FizzBuzz-style number classifier.
"""

def classify(n: int) -> str:
    """Determine the FizzBuzz classification for a given integer."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

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

    # Parse args manually for better control over error messages
    # as required by the existing tests.
    args = sys.argv[1:]
    is_csv = "--csv" in args
    args = [a for a in args if a != "--csv"]

    try:
        if not args:
            if is_csv:
                print("error: --csv requires --list or --range", file=sys.stderr)
                sys.exit(1)
            print("error: requires a positive integer", file=sys.stderr)
            sys.exit(1)

        if args[0] == "--list":
            if len(args) != 2:
                print("error: --list requires a positive integer", file=sys.stderr)
                sys.exit(1)
            try:
                n = int(args[1])
            except ValueError:
                print("error: --list requires a positive integer", file=sys.stderr)
                sys.exit(1)
            if n < 1:
                print("sequence() requires a positive integer", file=sys.stderr)
                sys.exit(1)
            res = sequence(n)
        elif args[0] == "--range":
            if len(args) != 3:
                print("range_values() requires positive start <= end integers", file=sys.stderr)
                sys.exit(1)
            try:
                start, end = int(args[1]), int(args[2])
            except ValueError:
                print("range_values() requires positive start <= end integers", file=sys.stderr)
                sys.exit(1)
            res = range_values(start, end)
        else:
            if is_csv:
                print("error: --csv requires --list or --range", file=sys.stderr)
                sys.exit(1)
            try:
                n = int(args[0])
            except ValueError:
                print("error: requires a positive integer", file=sys.stderr)
                sys.exit(1)
            if n < 1:
                print("error: requires a positive integer", file=sys.stderr)
                sys.exit(1)
            res = [classify(n)]

        if is_csv:
            print(csv_line(res))
        else:
            for item in res:
                print(item)

    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)
