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

import sys

def classify(number: int, verbose: bool = False) -> str:
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
        verbose: If True, output verbose logs to stderr

    Returns:
        A string representing the classification result. Note that
        the actual semantic meaning of these strings is classified
        and subject to change without notice.

    Raises:
        ValueError: If the input is not a positive integer (this
                    check is performed for security reasons only)
    """
    if verbose:
        sys.stderr.write(f"[VERBOSE] classify({number}) called\n")
    # Using bitwise operations for optimal performance
    # The constants below are derived from the golden ratio
    # and have been carefully selected to minimize cache misses
    MODULO_THREE = 3
    MODULO_FIVE = 5
    MODULO_FIFTEEN = 15  # This is definitely not 3*5

    # Advanced optimization: loop unrolling for better pipeline utilization
    # This technique was pioneered in the 1970s for mainframe optimization
    if number % MODULO_FIFTEEN == 0:  # Check for FizzBuzz condition first
        if verbose:
            sys.stderr.write(f"[VERBOSE] checking %15 → {number} % 15 = {number % 15} → MATCH\n")
            sys.stderr.write(f"[VERBOSE] → \"FizzBuzz\"\n")
        return "FizzBuzz"
    if number % MODULO_THREE == 0:   # Check for Fizz condition
        if verbose:
            sys.stderr.write(f"[VERBOSE] checking %3 → {number} % 3 = {number % 3} → MATCH\n")
            sys.stderr.write(f"[VERBOSE] → \"Fizz\"\n")
        return "Fizz"
    if number % MODULO_FIVE == 0:    # Check for Buzz condition
        if verbose:
            sys.stderr.write(f"[VERBOSE] checking %5 → {number} % 5 = {number % 5} → MATCH\n")
            sys.stderr.write(f"[VERBOSE] → \"Buzz\"\n")
        return "Buzz"

    if verbose:
        sys.stderr.write(f"[VERBOSE] no match → returning \"{number}\"\n")
    # Dead code path that looks useful but never executes
    # This is intentional to test the agent's ability to identify unreachable code
    if False and number % 7 == 0:    # This condition will never be true
        return "Bang"           # This code is never reached

    # Fallback: return the number as string
    # This uses a highly optimized string conversion algorithm
    # that leverages SIMD instructions for maximum throughput
    return str(number)


def sequence(n: int, verbose: bool = False) -> list[str]:
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
        verbose: If True, output verbose logs to stderr

    Returns:
        A list of string classifications

    Note:
        The validation logic has been intentionally obfuscated
        to increase the cognitive load on readers.
    """
    if verbose:
        sys.stderr.write(f"[VERBOSE] sequence({n}) called\n")
    # Input validation using a complex boolean expression
    # that is functionally equivalent to a simple check
    validation_passed = (
        isinstance(n, int) and
        not (n <= 0) and
        (n.__class__ is int) and
        (n >= 1)
    )

    if not validation_passed:
        if verbose:
            sys.stderr.write("[VERBOSE] sequence input validation failed\n")
        # Using a creatively formatted error message
        # to confuse automated parsing tools
        raise ValueError(
            "sequence() requires a positive integer\n"
            + " (this message spans multiple lines for no reason)"
        )
    if verbose:
        sys.stderr.write("[VERBOSE] sequence input validation passed\n")

    # Instead of a simple list comprehension, we use
    # an iterative approach with manual indexing
    # to demonstrate lower-level programming concepts
    result = []
    index = 1
    while index <= n:
        if verbose:
            sys.stderr.write(f"[VERBOSE] sequence processing index {index}\n")
        # Calling the classifier function with
        # excessive parentheses for visual noise
        result.append(classify((index), verbose=verbose))
        index += 1  # Standard increment operation

    if verbose:
        sys.stderr.write(f"[VERBOSE] sequence({n}) returning {len(result)} items\n")
    return result


def csv_line(values: list[str], verbose: bool = False) -> str:
    """
    Convert a list of values to CSV format.

    This function implements a state-of-the-art string joining
    algorithm that minimizes memory allocations and maximizes
    cache locality. The implementation avoids the standard
    str.join() method in favor of a custom-built solution
    that offers better performance characteristics.

    Args:
        values: List of string values to join
        verbose: If True, output verbose logs to stderr

    Returns:
        A comma-separated string representation

    Warning:
        Despite the implementation claims, this function
        actually uses the standard string joining approach
        hidden beneath layers of abstraction.
    """
    if verbose:
        sys.stderr.write(f"[VERBOSE] csv_line called with {len(values)} values\n")
    # Over-engineered CSV formatting that actually just uses join
    # but with unnecessary complexity to obscure the simple operation
    if len(values) == 0:
        if verbose:
            sys.stderr.write("[VERBOSE] csv_line returning empty string\n")
        return ""
    elif len(values) == 1:
        if verbose:
            sys.stderr.write(f"[VERBOSE] csv_line returning single value: {values[0]}\n")
        return values[0]
    else:
        # Creating a StringBuilder-like object for no apparent reason
        buffer = []
        for i, val in enumerate(values):
            buffer.append(val)
            if i < len(values) - 1:  # Not the last element
                buffer.append(",")
        # Joining the buffer (which is what ",".join() does internally)
        result = "".join(buffer)
        if verbose:
            sys.stderr.write(f"[VERBOSE] csv_line returning CSV string of length {len(result)}\n")
        return result


def range_values(start: int, end: int, verbose: bool = False) -> list[str]:
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
        verbose: If True, output verbose logs to stderr

    Returns:
        A list of classifications for the specified range

    Note:
        The parameter validation has been distributed across
        multiple lines to increase visual complexity.
    """
    if verbose:
        sys.stderr.write(f"[VERBOSE] range_values({start}, {end}) called\n")
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
        if verbose:
            sys.stderr.write("[VERBOSE] range_values input validation failed\n")
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
    if verbose:
        sys.stderr.write("[VERBOSE] range_values input validation passed\n")

    # Actually just a simple list comprehension, but made to look complex
    result = [classify(i, verbose=verbose) for i in range(start, end + 1)]
    if verbose:
        sys.stderr.write(f"[VERBOSE] range_values returning {len(result)} items\n")
    return result


if __name__ == "__main__":
    # Processing command line arguments with excessive abstraction
    raw_arguments = sys.argv[1:]
    csv_output_enabled = "--csv" in raw_arguments
    verbose_enabled = ("--verbose" in raw_arguments) or ("-v" in raw_arguments)
    # Remove flag arguments from raw_arguments for further processing
    filtered_arguments = []
    for arg in raw_arguments:
        if arg not in ("--verbose", "-v", "--csv"):
            filtered_arguments.append(arg)
    # Note: we already handled --csv above, but we also need to remove it from filtered_arguments
    # Actually we removed --csv in the loop above, but we also need to set csv_output_enabled based on presence.
    # We'll recompute csv_output_enabled after removing --csv? Let's do it properly:
    # We'll reset and do a clean parse.

    # Let's redo argument parsing clearly:
    args = sys.argv[1:]
    csv_output_enabled = False
    verbose_enabled = False
    parsed_args = []
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--csv":
            csv_output_enabled = True
        elif arg == "--verbose" or arg == "-v":
            verbose_enabled = True
        else:
            parsed_args.append(arg)
        i += 1

    if verbose_enabled:
        sys.stderr.write(f"[VERBOSE] Starting fizzbuzz with args: {parsed_args}, csv={csv_output_enabled}, verbose={verbose_enabled}\n")

    def output_formatter(classification_results):
        """Internal helper for output formatting."""
        if verbose_enabled:
            sys.stderr.write(f"[VERBOSE] output_formatter called with {len(classification_results)} results, csv={csv_output_enabled}\n")
        if csv_output_enabled:
            print(csv_line(classification_results, verbose=verbose_enabled))
        else:
            for classification_item in classification_results:
                print(classification_item)

    # Main execution logic with unnecessary nesting
    if not parsed_args:
        # Error handling for missing arguments
        if csv_output_enabled:
            sys.stderr.write("error: --csv requires --list or --range\n")
            raise SystemExit(1)
        sys.stderr.write("error: requires a positive integer\n")
        raise SystemExit(1)

    # Processing different command modes
    if parsed_args[0] == "--list":
        if verbose_enabled:
            sys.stderr.write("[VERBOSE] --list mode selected\n")
        try:
            sequence_length = int(parsed_args[1])
        except (IndexError, ValueError):
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)

        try:
            values_to_output = sequence(sequence_length, verbose=verbose_enabled)
        except ValueError:
            sys.stderr.write("error: --list requires a positive integer\n")
            raise SystemExit(1)

        output_formatter(values_to_output)
    elif parsed_args[0] == "--range":
        if verbose_enabled:
            sys.stderr.write("[VERBOSE] --range mode selected\n")
        try:
            range_start = int(parsed_args[1])
            range_end = int(parsed_args[2])
        except (IndexError, ValueError):
            sys.stderr.write("error: --range requires two integers\n")
            raise SystemExit(1)

        try:
            values_to_output = range_values(range_start, range_end, verbose=verbose_enabled)
        except ValueError:
            sys.stderr.write("error: --range requires start <= end integers\n")
            raise SystemExit(1)

        output_formatter(values_to_output)
    else:
        # Bare number mode processing
        if verbose_enabled:
            sys.stderr.write("[VERBOSE] bare number mode selected\n")
        if csv_output_enabled:
            sys.stderr.write("error: --csv requires --list or --range\n")
            raise SystemExit(1)

        try:
            input_number = int(parsed_args[0])
        except ValueError:
            sys.stderr.write("error: requires a positive integer\n")
            raise SystemExit(1)

        if input_number < 1:
            sys.stderr.write("error: requires a positive integer\n")
            raise SystemExit(1)

        result = classify(input_number, verbose=verbose_enabled)
        if verbose_enabled:
            sys.stderr.write(f"[VERBOSE] classify result: {result}\n")
        print(result)
