# -*- coding: utf-8 -*-
import json

def main():
    input_file = "input.txt"
    mapping_file = "mapping.json"
    translated_file = "en_lines.txt"
    output_file = "output_translated.txt"

    # Load original SHIFT-JIS script
    with open(input_file, "r", encoding="shift_jis", errors="ignore") as f:
        original_lines = f.readlines()

    # Load mapping with line positions
    with open(mapping_file, "r", encoding="utf-8") as f:
        mapping = json.load(f)

    # Load translated lines (utf-8)
    with open(translated_file, "r", encoding="utf-8") as f:
        translated = [l.rstrip("\n") for l in f.readlines()]

    if len(translated) != len(mapping):
        print("ERROR: number of translated lines does not match extracted Japanese lines!")
        print(f"Translated: {len(translated)}, Expected: {len(mapping)}")
        return

    for i, entry in enumerate(mapping):
        line_num = entry["line_number"]

        original = original_lines[line_num].rstrip("\n")

        # Check whether original ended with exactly one "\" 
        original_ends_with_slash = original.endswith("\\")

        # Clean the translated line of any trailing "\" (avoid double slashes)
        cleaned_translated = translated[i].rstrip("\\")

        # Reconstruct final line
        if original_ends_with_slash:
            new_line = cleaned_translated + "\\"
        else:
            new_line = cleaned_translated

        original_lines[line_num] = new_line + "\n"

    # Save back as SHIFT-JIS
    with open(output_file, "w", encoding="shift_jis", errors="ignore") as f:
        f.writelines(original_lines)

    print("Reinsertion complete. Backslash duplication fixed.")
    print(f"Saved output to {output_file}")

if __name__ == "__main__":
    main()
