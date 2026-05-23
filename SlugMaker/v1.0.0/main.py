import argparse

from slugify import slugify


def main():
    parser = argparse.ArgumentParser(
        description="Convert a title into a URL-friendly slug."
    )
    parser.add_argument("text", nargs="*", help="Text to convert.")
    parser.add_argument(
        "--separator",
        default="-",
        help="Character used between words (default: -).",
    )
    args = parser.parse_args()

    text = " ".join(args.text).strip()
    if not text:
        text = input("Enter text to convert: ").strip()

    if not text:
        print("No text supplied.")
        return

    print(slugify(text, separator=args.separator))


if __name__ == "__main__":
    main()
