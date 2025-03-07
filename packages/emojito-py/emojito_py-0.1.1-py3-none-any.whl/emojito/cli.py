import sys
import argparse
from .core import encode, decode

def main():
    parser = argparse.ArgumentParser(
        description="A tool to encode/decode text using emojis."
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encode command
    encode_parser = subparsers.add_parser("encode", help="Encode text into emoji")
    encode_parser.add_argument("emoji", help="Emoji to use for encoding")
    encode_parser.add_argument("text", help="Text to encode")

    # Decode command
    decode_parser = subparsers.add_parser("decode", help="Decode emoji text")
    decode_parser.add_argument("encoded_text", help="Encoded text to decode")

    args = parser.parse_args()

    try:
        if args.command == "encode":
            result = encode(args.emoji, args.text)

            print(result)  # Regular output
        elif args.command == "decode":
            result = decode(args.encoded_text)
            print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
