import os

# One line, no trailing newline: the gate counts characters, so keep it exact.
ENTRY = "The migration ran fine in staging. Staging has three rows. Production has three million."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
