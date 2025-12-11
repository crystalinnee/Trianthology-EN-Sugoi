# -*- coding: utf-8 -*-
import json

def main():
    input_file = "input.txt"
    mapping_file = "mapping.json"
    translated_file = "en_lines.txt"
    output_file = "output_translated.txt"

    # Load original file
    with open(input_file, "r", encoding="shift_jis", errors="ignore") as f:
        original_lines = f.readlines()

    # Load Japanese mapping
    with open(mapping_file, "r", encoding="utf-8") as f:
        mapping = json.load(f)

    # Load translated English lines
    with open(translated_file, "r", encoding="utf-8") as f:
        translated = [l.rstrip("\n") for l in f.readlines()]

    if len(translated) != len(mapping):
        print("ERROR: Number of translated lines does not match mapping count.")
        print(f"Translated: {len(translated)}, Expected: {len(mapping)}")
        return

    # Replace lines
    for i, entry in enumerate(mapping):
        line_num = entry["line_number"]
        original_lines[line_num] = translated[i] + "\n"

    # Save output as SHIFT-JIS
    with open(output_file, "w", encoding="shift_jis", errors="ignore") as f:
        f.writelines(original_lines)

    print(f"Reinserted {len(translated)} translated lines into script.")
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    main()
