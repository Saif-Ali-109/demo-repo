# demo-repo

A tiny demo app for testing an autonomous multi-agent fleet: given a GitHub issue,
the fleet analyzes, plans, implements, tests, reviews and opens a Pull Request.

## Usage

    python3 fizzbuzz.py <number>

Print the FizzBuzz-style classification for one number.

    python3 fizzbuzz.py --list <n>

Print one classification per line for the range 1..n (e.g. `python3 fizzbuzz.py --list 15`).

    python3 fizzbuzz.py --range <start> <end>

Print one classification per line for the range start..end (e.g. `python3 fizzbuzz.py --range 10 15`).

    python3 fizzbuzz.py --list <n> --csv

Print the 1..n classifications as a single comma-separated line with no
trailing comma or spaces, e.g. `1,2,Fizz,4,Buzz`. Works with `--range` too:
`python3 fizzbuzz.py --range 10 15 --csv` prints `Buzz,11,Fizz,13,14,FizzBuzz`.
The `--csv` flag may appear anywhere in the argument list and requires
either `--list` or `--range`.

## Self-Healer demo

This branch intentionally triggers the failing `lint` job (biome check on src/widget.js).

