"""Unit tests for fizzbuzz.classify (will FAIL until the bug is fixed)."""

from fizzbuzz import classify


def main() -> None:
    cases = {
        1: "1",
        3: "Fizz",
        5: "Buzz",
        15: "FizzBuzz",  # bug: currently returns "Fizz"
        45: "FizzBuzz",  # bug: currently returns "Fizz"
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
