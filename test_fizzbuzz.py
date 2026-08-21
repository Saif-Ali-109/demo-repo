"""Unit tests for fizzbuzz.classify.

Covers the Issue #1 fix: multiples of 15 must return 'FizzBuzz' rather
than 'Fizz'. Also guards against regressions in the %3 -> Fizz and
%5 -> Buzz branches and the plain-number fallback.

Covers the Issue #10 fix: bare-number CLI mode (``python3 fizzbuzz.py <n>``)
must reject non-positive integers (0 and negatives) with rc=1 and an error
message, consistent with ``--list`` and ``--range`` modes, while positive
values still work.
"""

import subprocess
import sys

from fizzbuzz import classify, sequence, csv_line, range_values


def main() -> None:
    failed = 0

    # classify() test cases (Issue #1)
    cases = {
        1: "1",
        2: "2",
        3: "Fizz",
        5: "Buzz",
        9: "Fizz",
        10: "Buzz",
        15: "FizzBuzz",
        30: "FizzBuzz",
        45: "FizzBuzz",
        60: "FizzBuzz",
        75: "FizzBuzz",
    }
    for n, expected in cases.items():
        got = classify(n)
        status = "ok" if got == expected else "FAIL"
        if got != expected:
            failed += 1
        print(f"{status}: classify({n}) = {got!r} (expected {expected!r})")

    # sequence() test cases (Issue #3)
    sequence_cases = {
        1: ["1"],
        15: [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
            "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
        ],
    }
    for n, expected in sequence_cases.items():
        got = sequence(n)
        status = "ok" if got == expected else "FAIL"
        if got != expected:
            failed += 1
        print(f"{status}: sequence({n}) = {got!r} (expected {expected!r})")

    # sequence() must reject non-positive / non-integer input
    for bad in (0, -3, "5"):
        try:
            sequence(bad)
            failed += 1
            print(f"FAIL: sequence({bad!r}) did not raise ValueError")
        except ValueError:
            print(f"ok: sequence({bad!r}) raised ValueError")

    # csv_line() test cases
    csv_cases = [
        (["1", "2", "Fizz", "4", "Buzz"], "1,2,Fizz,4,Buzz"),
        (["Buzz", "11", "Fizz", "13", "14", "FizzBuzz"],
         "Buzz,11,Fizz,13,14,FizzBuzz"),
        ([], ""),
        (["FizzBuzz"], "FizzBuzz"),
        (["1", "2"], "1,2"),
    ]
    for values, expected in csv_cases:
        got = csv_line(list(values))
        status = "ok" if got == expected else "FAIL"
        if got != expected:
            failed += 1
        print(f"{status}: csv_line({values!r}) = {got!r} (expected {expected!r})")

    # range_values() test cases
    range_cases = {
        (1, 5): ["1", "2", "Fizz", "4", "Buzz"],
        (10, 15): ["Buzz", "11", "Fizz", "13", "14", "FizzBuzz"],
        (15, 15): ["FizzBuzz"],
        (1, 1): ["1"],
    }
    for (start, end), expected in range_cases.items():
        got = range_values(start, end)
        status = "ok" if got == expected else "FAIL"
        if got != expected:
            failed += 1
        print(f"{status}: range_values({start}, {end}) = {got!r} (expected {expected!r})")

    # range_values() must reject bad input
    for bad in ((5, 1), (1.0, 5), (1, "5")):
        try:
            range_values(*bad)
            failed += 1
            print(f"FAIL: range_values({bad!r}) did not raise ValueError")
        except ValueError:
            print(f"ok: range_values({bad!r}) raised ValueError")

    # subprocess CLI tests
    def run_cli(*argv):
        return subprocess.run(
            [sys.executable, "fizzbuzz.py", *argv],
            capture_output=True, text=True,
        )

    cli_cases = [
        # (argv, expected_stdout, expected_returncode[, expected_stderr])
        (["--list", "5"], "1\n2\nFizz\n4\nBuzz\n", 0),
        (["--list", "5", "--csv"], "1,2,Fizz,4,Buzz\n", 0),
        (["--csv", "--list", "5"], "1,2,Fizz,4,Buzz\n", 0),
        (["--range", "10", "15"],
         "Buzz\n11\nFizz\n13\n14\nFizzBuzz\n", 0),
        (["--range", "10", "15", "--csv"],
         "Buzz,11,Fizz,13,14,FizzBuzz\n", 0),
        (["--csv", "--range", "10", "15"],
         "Buzz,11,Fizz,13,14,FizzBuzz\n", 0),
        (["5"], "Buzz\n", 0),
        (["--csv"], None, 1),
        (["--csv", "5"], None, 1),
        (["--csv", "--list"], None, 1),
        (["--range", "5", "1"], None, 1),
        (["--list", "abc"], None, 1),
        (["--list", "0"], None, 1),
        # Issue #10: bare-number mode must reject non-positive integers
        (["0"], None, 1, "error: requires a positive integer\n"),
        (["-1"], None, 1, "error: requires a positive integer\n"),
        (["-15"], None, 1, "error: requires a positive integer\n"),
        (["abc"], None, 1, "error: requires a positive integer\n"),
        (["1"], "1\n", 0),
        (["15"], "FizzBuzz\n", 0),
        # Issue #20: --sep option for --list and --range
        (["--list", "5", "--sep", ";"], "1;2;Fizz;4;Buzz\n", 0),
        (["--sep", ";", "--list", "5"], "1;2;Fizz;4;Buzz\n", 0),
        (["--range", "10", "15", "--sep", " "], "Buzz 11 Fizz 13 14 FizzBuzz\n", 0),
        (["--sep", " ", "--range", "10", "15"], "Buzz 11 Fizz 13 14 FizzBuzz\n", 0),
        # --sep combined with --csv must error
        (["--list", "5", "--sep", ";", "--csv"], None, 1, "error: --sep cannot be combined with --csv\n"),
        (["--list", "5", "--csv", "--sep", ";"], None, 1, "error: --sep cannot be combined with --csv\n"),
        # --sep without --list or --range must error
        (["--sep", ";", "5"], None, 1, "error: --sep requires --list or --range\n"),
        (["5", "--sep", ";"], None, 1, "error: --sep requires --list or --range\n"),
        # --sep without a value argument must error
        (["--list", "5", "--sep"], None, 1, "error: --sep requires a character argument\n"),
        # --sep with multi-char value must error
        (["--list", "5", "--sep", "ab"], None, 1, "error: --sep value must be a single character\n"),
    ]
    for item in cli_cases:
        argv = item[0]
        expected_stdout = item[1]
        expected_rc = item[2]
        expected_stderr = item[3] if len(item) > 3 else None
        result = run_cli(*argv)
        ok_rc = result.returncode == expected_rc
        if not ok_rc:
            failed += 1
        stdout_ok = True
        if expected_stdout is not None:
            stdout_ok = result.stdout == expected_stdout
            if not stdout_ok:
                failed += 1
        stderr_ok = True
        if expected_stderr is not None:
            stderr_ok = result.stderr == expected_stderr
            if not stderr_ok:
                failed += 1
        status = "ok" if (ok_rc and stdout_ok and stderr_ok) else "FAIL"
        detail = (
            f"rc={result.returncode}(expected {expected_rc}), "
            f"stdout={result.stdout!r}, stderr={result.stderr!r}"
        )
        print(f"{status}: cli {argv} -> {detail}")

    if failed:
        print(f"{failed} test(s) failed.")
        raise SystemExit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
