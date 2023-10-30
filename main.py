import json
import re
import sys
from typing import Optional


class Task:
    def __init__(self, name: str, is_completed: bool) -> None:
        self.name = name
        self.is_completed = is_completed

    def to_dict(self) -> dict[str, str | bool]:
        return {
            "name"       : self.name,
            "isCompleted": self.is_completed
        }


def readFile(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def saveTasks(filename: str, tasks: list[Task]) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4, ensure_ascii=False)


def taskInfo(line: str) -> Optional[tuple[str, bool]]:
    mch = re.search(r'^-\s?\[\s?([xX])?\s?]\s?(.+)$', line.strip())
    return (mch.group(2).strip(), bool(mch.group(1))) if mch else None


def parseLine(line: str) -> Optional[Task]:
    line = line.strip()
    info = taskInfo(line)
    return Task(*info) if info is not None else None


def isValidLine(line: str) -> bool:
    return bool(re.match(r'^-\s?\[ ?([xX])? ?]\s?.+$', line))


def parseLines(lines: list[str]) -> list[Task]:
    valid_lines = list(filter(isValidLine, lines))
    return list(filter(lambda x: x is not None, [parseLine(line) for line in valid_lines]))


def main() -> int:
    lines = readFile('rabbit.todo')
    tasks = parseLines(lines)
    saveTasks('tasks.json', tasks)
    return 0


if __name__ == '__main__':
    sys.exit(main())
