"""Generate model.py from the declarations in the laboratory class diagram."""
from argparse import ArgumentParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "uml" / "02_classes.puml"
TARGET = ROOT / "model.py"
DECLARATION = re.compile(r"(class|enum|interface) (\w+) \{")
FIELD = re.compile(r"\+(\w+): (.+)")
OPERATION = re.compile(r"\+(\w+)\((.*)\): (.+)")


def generate(source: str) -> str:
    output = [
        '"""Generated from uml/02_classes.puml by generate.py."""',
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from enum import Enum",
        "from typing import Protocol",
    ]
    kind = None
    names = set()
    for number, raw in enumerate(source.splitlines(), 1):
        line = raw.strip()
        if kind is None:
            match = DECLARATION.fullmatch(line)
            if not match:
                continue  # Includes, appearance and UML association lines.
            kind, name = match.groups()
            if name in names:
                raise ValueError(f"Повторное объявление {name} в строке {number}")
            names.add(name)
            output.extend(["", ""])
            if kind == "class":
                output.extend(["@dataclass", f"class {name}:"])
            else:
                base = "Enum" if kind == "enum" else "Protocol"
                output.append(f"class {name}({base}):")
        elif line == "}":
            kind = None
        elif kind == "enum" and line.isidentifier():
            output.append(f'    {line} = "{line}"')
        elif kind == "class" and (field := FIELD.fullmatch(line)):
            output.append(f"    {field[1]}: {field[2]}")
        elif kind == "interface" and (method := OPERATION.fullmatch(line)):
            arguments = ", " + method[2] if method[2] else ""
            output.append(f"    def {method[1]}(self{arguments}) -> {method[3]}: ...")
        else:
            raise ValueError(f"Неподдерживаемое объявление в строке {number}: {line}")
    if kind is not None or not names:
        raise ValueError("Ожидались завершённые объявления типов")
    code = "\n".join(output) + "\n"
    compile(code, str(TARGET), "exec")
    return code


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="проверить актуальность модели")
    args = parser.parse_args()
    expected = generate(SOURCE.read_text(encoding="utf-8"))
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding="utf-8") != expected:
            raise SystemExit("model.py отличается от результата генерации")
        print("model.py: OK")
    else:
        TARGET.write_text(expected, encoding="utf-8")
        print("uml/02_classes.puml -> model.py")
