"""Unit tests for fizzbuzz.classify.

Covers the Issue #1 fix: multiples of 15 must return 'FizzBuzz' rather
than 'Fizz'. Also guards against regressions in the %3 -> Fizz and
%5 -> Buzz branches and the plain-number fallback.
"""

from fizzbuzz import classify, range_sequence, sequence


def main() -> None:
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
    failed = 0
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

    # range_sequence() test cases (Issue #5)
    expected_10_20 = [
        "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
        "16", "17", "Fizz", "19", "Buzz",
    ]
    got = range_sequence(10, 20)
    status = "ok" if got == expected_10_20 else "FAIL"
    if got != expected_10_20:
        failed += 1
    print(f"{status}: range_sequence(10, 20) = {got!r} (expected {expected_10_20!r})")

    # start == end case
    got = range_sequence(15, 15)
    expected = ["FizzBuzz"]
    status = "ok" if got == expected else "FAIL"
    if got != expected:
        failed += 1
    print(f"{status}: range_sequence(15, 15) = {got!r} (expected {expected!r})")

    # range_sequence() must reject non-positive / non-integer / reversed input
    for bad in ((0, 5), (-3, 5), ("1", 5), (5, 2)):
        try:
            range_sequence(*bad)
            failed += 1
            print(f"FAIL: range_sequence({bad!r}) did not raise ValueError")
        except ValueError:
            print(f"ok: range_sequence({bad!r}) raised ValueError")

    if failed:
        print(f"{failed} test(s) failed.")
        raise SystemExit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
