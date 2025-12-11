# -*- coding: utf-8 -*-
import json
import re

# Japanese detection (Hiragana + Katakana + Kanji + Japanese punctuation)
JAPANESE_REGEX = re.compile(
    r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\u3000-\u303F]'
)

# English letters
ENGLISH_REGEX = re.compile(r'[A-Za-z]')

def is_valid_japanese_line(text):
    # Must contain Japanese
    if not JAPANESE_REGEX.search(text):
        return False
    # Must NOT contain English
    if ENGLISH_REGEX.search(text):
        return False
    # Must NOT contain ;
    if ";" in text:
        return False
    return True

def main():
    input_file = "input.txt"
    mapping_file = "mapping.json"
    output_jp = "jp_lines.txt"

    # Read SHIFT-JIS
    with open(input_file, "r", encoding="shift_jis", errors="ignore") as f:
        lines = f.readlines()

    mapping = []
    extracted = []

    for idx, line in enumerate(lines):
        clean = line.rstrip("\n")

        if is_valid_japanese_line(clean):
            extracted.append(clean)
            mapping.append({
                "line_number": idx,
                "original": clean
            })

    # Output Japanese lines for translation
    with open(output_jp, "w", encoding="utf-8") as f:
        for l in extracted:
            f.write(l + "\n")

    # Save map for reinsertion
    with open(mapping_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(extracted)} Japanese-only lines.")
    print("Saved to jp_lines.txt and mapping.json")

if __name__ == "__main__":
    main()
