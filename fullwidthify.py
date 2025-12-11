import sys
import os

def to_fullwidth(text, convert_space=True):
    result = []
    for ch in text:
        code = ord(ch)

        # Convert ASCII space to full-width space
        if ch == " " and convert_space:
            result.append("　")
            continue

        # Full-width range conversion (ASCII 33–126)
        if 33 <= code <= 126:
            result.append(chr(code + 0xFEE0))
        else:
            result.append(ch)

    return "".join(result)


def convert_file(input_path, output_path=None, convert_space=True):
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_fullwidth{ext}"

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        data = f.read()

    fullwidth_data = to_fullwidth(data, convert_space=convert_space)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(fullwidth_data)

    print(f"Converted file saved as: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_fullwidth.py input.txt [output.txt]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    convert_file(input_file, output_file)
