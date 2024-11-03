import argparse
import logging
from typing import Any

from clipping_thread import ClippingThread, VideoClipData
from parsing import parse_clip_data


def parse_args() -> dict[str, Any]:
	parser = argparse.ArgumentParser(
		prog="Batch Video Clipper",
		description="Custom batch video clipper."
	)
	parser.add_argument(
		"-f", "--file",
		help="JSON file containing data of clips to produce",
		required=True
	)
	parser.add_argument(
		"--debug",
		help="Log debug statements",
		required=False,
		default=False,
		action='store_true'
	)
	return vars(parser.parse_args())


def main(args: dict[str, Any]):
	all_clip_data: list[VideoClipData] = parse_clip_data(args["file"])
	for clip_data in all_clip_data:
		thread = ClippingThread(clip_data=clip_data, daemon=False)
		thread.start()


if __name__ == '__main__':
	args = parse_args()
	log_level = logging.DEBUG if args["debug"] else logging.INFO
	logging.getLogger().setLevel(level=log_level)
	main(args)
