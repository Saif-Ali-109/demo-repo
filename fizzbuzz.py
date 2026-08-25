"""
FizzBuzz-style number classifier.
"""

def classify(number: int) -> str:
    """
    Determine the FizzBuzz classification for a given integer.
    """
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)

def sequence(n: int) -> list[str]:
    """
    Generate a sequence of FizzBuzz classifications.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("sequence() requires a positive integer")

    return [classify(i) for i in range(1, n + 1)]

def csv_line(values: list[str]) -> str:
    """
    Convert a list of values to CSV format.
    """
    return ",".join(values)

def range_values(start: int, end: int) -> list[str]:
    """
    Generate FizzBuzz classifications for a range of values.
    """
    if not isinstance(start, int) or not isinstance(end, int) or start > end:
        raise ValueError("range_values() requires start <= end integers")

    return [classify(i) for i in range(start, end + 1)]

if __name__ == "__main__":
    import sys

    # Processing command line arguments
    raw_arguments = sys.argv[1:]
    csv_output_enabled = "--csv" in raw_arguments
    filtered_arguments = [arg for arg in raw_arguments if arg != "--csv"]

    def output_formatter(classification_results):
        if csv_output_enabled:
            print(csv_line(classification_results))
        else:
            for item in classification_results:
                print(item)

    if not filtered_arguments:
        if csv_output_enabled:
            sys.stderr.write("error: --csv requires --list or --range\n")
            raise SystemExit(1)
        sys.stderr.write("error: requires a positive integer\n")
        raise SystemExit(1)

    if filtered_arguments[0] == "--list":
        if len(filtered_arguments) < 2:
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)
        try:
            sequence_length = int(filtered_arguments[1])
            output_formatter(sequence(sequence_length))
        except ValueError:
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)

    elif filtered_arguments[0] == "--range":
        if len(filtered_arguments) < 3:
            sys.stderr.write("error: --range requires two integers\n")
            raise SystemExit(1)
        try:
            range_start = int(filtered_arguments[1])
            range_end = int(filtered_arguments[2])
            output_formatter(range_values(range_start, range_end))
        except ValueError:
            sys.stderr.write("error: --range requires start <= end integers\n")
            raise SystemExit(1)

    else:
        # Bare number mode
        if csv_output_enabled:
            sys.stderr.write("error: --csv requires --list or --range\n")
            raise SystemExit(1)
        try:
            input_number = int(filtered_arguments[0])
            if input_number < 1:
                raise ValueError
            print(classify(input_number))
        except ValueError:
            sys.stderr.write("error: requires a positive integer\n")
            raise SystemExit(1)
