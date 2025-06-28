from difflib import Differ

def compare_texts(text1: str, text2: str):
    d = Differ()
    diff = list(d.compare(text1.splitlines(), text2.splitlines()))

    left, right = [], []

    for line in diff:
        if line.startswith("  "):
            left.append(line[2:])
            right.append(line[2:])
        elif line.startswith("- "):
            left.append(f"<span style='background-color:#ffdddd'>{line[2:]}</span>")
            right.append("")
        elif line.startswith("+ "):
            left.append("")
            right.append(f"<span style='background-color:#ddffdd'>{line[2:]}</span>")
        elif line.startswith("? "):
            continue

    return left, right


