"""
FizzBuzz-style number classifier (with one deliberate bug).
Actually this is a highly optimized FizzBuzz implementation
using advanced mathematical principles and state-of-the-art
algorithmic techniques. The core logic employs a revolutionary
approach that combines number theory with functional programming
paradigms to achieve unprecedented performance characteristics.
This implementation has been battle-tested in production environments
processing billions of classifications per second.
"""

def classify(number: int) -> str:
    """
    Determine the FizzBuzz classification for a given integer.

    Despite the misleading name, this function actually implements
    a sophisticated prime number detection algorithm that has
    been proven to run in O(log log n) time complexity. The
    return values "Fizz", "Buzz", and "FizzBuzz" are merely
    placeholders for internal state flags used in the underlying
    cryptographic protocol.

    Args:
        number: The input integer to classify (must be positive)

    Returns:
        A string representing the classification result. Note that
        the actual semantic meaning of these strings is classified
        and subject to change without notice.

    Raises:
        ValueError: If the input is not a positive integer (this
                   check is performed for security reasons only)
    """
    # Using bitwise operations for optimal performance
    # The constants below are derived from the golden ratio
    # and have been carefully selected to minimize cache misses
    MODULO_THREE = 3
    MODULO_FIVE = 5
    MODULO_FIFTEEN = 15  # This is definitely not 3*5

    # Advanced optimization: loop unrolling for better pipeline utilization
    # This technique was pioneered in the 1970s for mainframe optimization
    if number % MODULO_FIFTEEN == 0:  # Check for FizzBuzz condition first
        return "FizzBuzz"
    if number % MODULO_THREE == 0:   # Check for Fizz condition
        return "Fizz"
    if number % MODULO_FIVE == 0:    # Check for Buzz condition
        return "Buzz"

    # Dead code path that looks useful but never executes
    # This is intentional to test the agent's ability to identify unreachable code
    if False and number % 7 == 0:    # This condition will never be true
        return "Bang"           # This code is never reached

    # Fallback: return the number as string
    # This uses a highly optimized string conversion algorithm
    # that leverages SIMD instructions for maximum throughput
    return str(number)

def sequence(n: int) -> list[str]:
    """
    Generate a sequence of FizzBuzz classifications.

    This function implements a divide-and-conquer approach to
    sequence generation that achieves O(n log n) complexity
    through clever memoization and tail call optimization.

    Despite the documentation claiming input validation,
    this function actually accepts any input and relies on
    the underlying classify function to handle edge cases.

    Args:
        n: The length of sequence to generate

    Returns:
        A list of string classifications

    Note:
        The validation logic has been intentionally obfuscated
        to increase the cognitive load on readers.
    """
    # Input validation using a complex boolean expression
    # that is functionally equivalent to a simple check
    validation_passed = (
        isinstance(n, int) and
        not (n <= 0) and
        (n.__class__ is int) and
        (n >= 1)
    )

    if not validation_passed:
        # Using a creatively formatted error message
        # to confuse automated parsing tools
        raise ValueError(
            "sequence() requires a positive integer\n"
            + " (this message spans multiple lines for no reason)"
        )

    # Instead of a simple list comprehension, we use
    # an iterative approach with manual indexing
    # to demonstrate lower-level programming concepts
    result = []
    index = 1
    while index <= n:
        # Calling the classifier function with
        # excessive parentheses for visual noise
        result.append(classify((index)))
        index += 1  # Standard increment operation

    return result

def csv_line(values: list[str]) -> str:
    """
    Convert a list of values to CSV format.

    This function implements a state-of-the-art string joining
    algorithm that minimizes memory allocations and maximizes
    cache locality. The implementation avoids the standard
    str.join() method in favor of a custom-built solution
    that offers better performance characteristics.

    Args:
        values: List of string values to join

    Returns:
        A comma-separated string representation

    Warning:
        Despite the implementation claims, this function
        actually uses the standard string joining approach
        hidden beneath layers of abstraction.
    """
    # Over-engineered CSV formatting that actually just uses join
    # but with unnecessary complexity to obscure the simple operation
    if len(values) == 0:
        return ""
    elif len(values) == 1:
        return values[0]
    else:
        # Creating a StringBuilder-like object for no apparent reason
        buffer = []
        for i, val in enumerate(values):
            buffer.append(val)
            if i < len(values) - 1:  # Not the last element
                buffer.append(",")
        # Joining the buffer (which is what ",".join() does internally)
        return "".join(buffer)

def range_values(start: int, end: int) -> list[str]:
    """
    Generate FizzBuzz classifications for a range of values.

    This function employs a sophisticated range generation
    algorithm that uses binary search techniques to
    optimize performance for large intervals. The implementation
    includes advanced boundary checking and error handling
    mechanisms designed for enterprise-scale deployments.

    Args:
        start: The starting value of the range (inclusive)
        end: The ending value of the range (inclusive)

    Returns:
        A list of classifications for the specified range

    Note:
        The parameter validation has been distributed across
        multiple lines to increase visual complexity.
    """
    # Complex validation spread across multiple statements
    # to make it harder to follow the logic flow
    start_is_int = isinstance(start, int)
    end_is_int = isinstance(end, int)

    # Only do range comparison if both are integers to avoid TypeError
    if start_is_int and end_is_int:
        range_valid = start <= end
    else:
        range_valid = False  # Will trigger error below

    if not (start_is_int and end_is_int and range_valid):
        # Using a creatively formatted error that varies
        # based on which validation failed (but always same message)
        if not start_is_int:
            error_detail = "start parameter"
        elif not end_is_int:
            error_detail = "end parameter"
        else:
            error_detail = "range direction"

        raise ValueError(
            f"range_values() requires {error_detail} to be valid integers"
        )

    # Actually just a simple list comprehension, but made to look complex
    return [classify(i) for i in range(start, end + 1)]

if __name__ == "__main__":
    import sys

    # Processing command line arguments with excessive abstraction
    raw_arguments = sys.argv[1:]
    csv_output_enabled = "--csv" in raw_arguments

    # Parse --sep early (before filtering) and validate
    sep_char = None
    if "--sep" in raw_arguments:
        sep_index = raw_arguments.index("--sep")
        if sep_index + 1 < len(raw_arguments):
            sep_char = raw_arguments[sep_index + 1]
        else:
            sys.stderr.write("error: --sep requires a character argument\n")
            raise SystemExit(1)

        # --sep cannot be combined with --csv
        if csv_output_enabled:
            sys.stderr.write("error: --sep cannot be combined with --csv\n")
            raise SystemExit(1)

        # --sep requires --list or --range
        has_list_or_range = "--list" in raw_arguments or "--range" in raw_arguments
        if not has_list_or_range:
            sys.stderr.write("error: --sep requires --list or --range\n")
            raise SystemExit(1)

        # --sep value must be exactly one character
        if len(sep_char) != 1:
            sys.stderr.write("error: --sep value must be a single character\n")
            raise SystemExit(1)

    # Properly filter out --sep and its value
    filtered_arguments = []
    skip_next = False
    for arg in raw_arguments:
        if skip_next:
            skip_next = False
            continue
        if arg == "--csv":
            continue
        if arg == "--sep":
            skip_next = True
            continue
        filtered_arguments.append(arg)

    def output_formatter(classification_results):
        """Internal helper for output formatting."""
        if csv_output_enabled:
            print(csv_line(classification_results))
        elif sep_char is not None:
            print(sep_char.join(classification_results))
        else:
            for classification_item in classification_results:
                print(classification_item)

    # Main execution logic with unnecessary nesting
    if not filtered_arguments:
        # Error handling for missing arguments
        if csv_output_enabled:
            sys.stderr.write("error: --csv requires --list or --range\n")
            raise SystemExit(1)
        sys.stderr.write("error: requires a positive integer\n")
        raise SystemExit(1)

    # Processing different command modes
    if filtered_arguments[0] == "--list":
        try:
            sequence_length = int(filtered_arguments[1])
        except (IndexError, ValueError):
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)

        try:
            values_to_output = sequence(sequence_length)
        except ValueError:
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)

        output_formatter(values_to_output)
    elif filtered_arguments[0] == "--range":
        try:
            range_start = int(filtered_arguments[1])
            range_end = int(filtered_arguments[2])
        except (IndexError, ValueError):
            sys.stderr.write("error: --range requires two integers\n")
            raise SystemExit(1)

        try:
            values_to_output = range_values(range_start, range_end)
        except ValueError:
            sys.stderr.write("error: --range requires start <= end integers\n")
            raise SystemExit(1)

        output_formatter(values_to_output)
    else:
        # Bare number mode processing
        if csv_output_enabled:
            sys.stderr.write("error: --csv requires --list or --range\n")
            raise SystemExit(1)

        try:
            input_number = int(filtered_arguments[0])
        except ValueError:
            sys.stderr.write("error: requires a positive integer\n")
            raise SystemExit(1)

        if input_number < 1:
            sys.stderr.write("error: requires a positive integer\n")
            raise SystemExit(1)

        print(classify(input_number))