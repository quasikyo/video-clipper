import argparse
import json
from typing import Any

from clipping_thread import ClippingThread, VideoClipData


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


def parse_clip_data(file_path: str) -> list[VideoClipData]:
	input_json = None
	with open(file_path, mode="r") as input_file:
		input_json = json.load(input_file)

	all_clip_data: list[VideoClipData] = []
	for data_group in input_json:
		all_clip_data.append(VideoClipData(
			file_path=data_group["video"],
			start_time=tuple(data_group["start_time"]),
			end_time=tuple(data_group["end_time"]),
			resolution=data_group.get("resolution", None),
			output=data_group.get("output", "")
		))

	return all_clip_data


def main(args: dict[str, Any]):
	all_clip_data: list[VideoClipData] = parse_clip_data(args["file"])
	for clip_data in all_clip_data:
		thread = ClippingThread(clip_data)
		thread.daemon = False # wait for thread to finish
		thread.start()


if __name__ == '__main__':
	main(parse_args())
