"""Unit tests for fizzbuzz.classify.

Covers the Issue #1 fix: multiples of 15 must return 'FizzBuzz' rather
than 'Fizz'. Also guards against regressions in the %3 -> Fizz and
%5 -> Buzz branches and the plain-number fallback.
"""

from fizzbuzz import classify, sequence


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

    if failed:
        print(f"{failed} test(s) failed.")
        raise SystemExit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
