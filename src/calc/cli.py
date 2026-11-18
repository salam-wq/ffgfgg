"""Консольный интерфейс: calc <операция> <a> <b>."""

import argparse
import sys

from calc import operations

OPERATIONS = {
    "add": operations.add,
    "sub": operations.subtract,
    "mul": operations.multiply,
    "div": operations.divide,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="calc", description="Учебный калькулятор")
    parser.add_argument("operation", choices=sorted(OPERATIONS), help="операция")
    parser.add_argument("a", type=float, help="первый операнд")
    parser.add_argument("b", type=float, help="второй операнд")
    args = parser.parse_args(argv)

    try:
        print(OPERATIONS[args.operation](args.a, args.b))
    except ZeroDivisionError as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
