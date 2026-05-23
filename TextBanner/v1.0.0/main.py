import argparse

from pyfiglet import Figlet


def main():
    parser = argparse.ArgumentParser(
        description="Turn a short message into an ASCII art banner."
    )
    parser.add_argument("text", nargs="*", help="Message to display.")
    parser.add_argument(
        "--font",
        default="standard",
        help="pyfiglet font name (default: standard).",
    )
    args = parser.parse_args()

    message = " ".join(args.text).strip()
    if not message:
        message = input("Enter text for the banner: ").strip()

    if not message:
        print("No text supplied.")
        return

    try:
        banner = Figlet(font=args.font).renderText(message)
    except Exception as error:
        parser.error(f"could not render banner: {error}")

    print(banner)


if __name__ == "__main__":
    main()
