import argparse
from typing import Any

from clipping_thread import ClippingThread, VideoClipData
from parsing import parse_clip_data


def parse_args() -> dict[str, Any]:
	parser = argparse.ArgumentParser(
		prog="Video Clipper",
		description="Custom video clipper"
	)
	parser.add_argument(
		"-f", "--file",
		help="JSON file containing clips to produce",
		required=True
	)
	return vars(parser.parse_args())


def main(args: dict[str, Any]):
	all_clip_data: list[VideoClipData] = parse_clip_data(args["file"])
	for clip_data in all_clip_data:
		thread = ClippingThread(clip_data)
		thread.daemon = False # wait for thread to finish
		thread.start()


if __name__ == '__main__':
	main(parse_args())
