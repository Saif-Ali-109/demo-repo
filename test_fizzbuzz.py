"""Unit tests for fizzbuzz.classify.

Covers the Issue #1 fix: multiples of 15 must return 'FizzBuzz' rather
than 'Fizz'. Also guards against regressions in the %3 -> Fizz and
%5 -> Buzz branches and the plain-number fallback.
"""

from fizzbuzz import classify


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
    if failed:
        print(f"{failed} test(s) failed.")
        raise SystemExit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
