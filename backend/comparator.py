# backend/comparator.py

import difflib

def compare_texts(text1, text2):
    differ = difflib.HtmlDiff()
    html_diff = differ.make_table(
        text1.splitlines(), text2.splitlines(),
        fromdesc="Document 1", todesc="Document 2",
        context=True, numlines=2
    )
    return html_diff
