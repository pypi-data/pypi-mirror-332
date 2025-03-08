import argparse
from mp4togif.converter import mp4_to_gif

def main():
    parser = argparse.ArgumentParser(description="Convert MP4 to GIF")
    parser.add_argument("input", help="input MP4 file path")
    parser.add_argument("output", help="Output GIF file path")
    parser.add_argument("--duration", type=float, default=4, help="Duration of GIF (max 5s, default 4s)")

    args = parser.parse_args()

    mp4_to_gif(args.input, args.output, duration=args.duration)

if __name__ == "__main__":
    main()