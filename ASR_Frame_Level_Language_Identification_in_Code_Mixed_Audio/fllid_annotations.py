import os
import re
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
text_file = Path(current_dir) / "test" / "transcripts" / "text"
text_fllid_file = Path(current_dir) / "test" / "transcripts" / "text_fllid.txt"

with open(text_file, "r") as f:
    text = f.read()

for line in text.split("\n"):
    # print(line)
    new_text = line[0:29]
    for i in range(29, len(line)):
        if re.search(r'[a-zA-Z]', line[i]):
            new_text += "E"
            a = "E"
        elif line[i] == " ":
            new_text += " "
            a = ""
        else:
            new_text += "H"
            a = "H"
    # print(new_text)
    with open(text_fllid_file, "a") as f:
        f.write(new_text + "\n")


