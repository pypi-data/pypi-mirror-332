import os
import glob

from pathlib import Path
from codai.bots.refactor import bot as refactor_bot


def refactor(glob_pattern: str, instructions: str | Path) -> None:
    if instructions.endswith(".md"):
        instructions = Path(instructions)
    if isinstance(instructions, str):
        with open("instructions.md", "w") as f:
            f.write(instructions)
    if isinstance(instructions, Path):
        instructions = instructions.read_text()
    print(instructions)
    files = glob.glob(glob_pattern, recursive=True)
    files = [f for f in files if os.path.isfile(f)]
    for file in files:
        print(file)
        old_content = Path(file).read_text()
        print(old_content)
        # new_file = refactor_bot(old_content, instructions)
