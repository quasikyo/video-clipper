import json
from typing import Any
from pathlib import Path

from clipping_thread import VideoClipData


def parse_clip_data(config_file: str) -> list[VideoClipData]:
	input_json: dict = None
	with open(config_file, mode="r") as input_file:
		input_json = json.load(input_file)

	input_directory = Path(input_json.get("input_directory", "")).absolute()
	output_directory = Path(input_json.get("output_directory", "")).absolute()

	all_clip_data: list[VideoClipData] = []
	for input_group in input_json["clips"]:
		clip_data = VideoClipData(
			input_path=_get_abs_path(input_directory, Path(input_group["video"])),
			start_time=tuple(input_group["start_time"]),
			end_time=tuple(input_group["end_time"]),
			resolution=_parse_resolution(input_group),
			codec=input_group.get("codec", None)
		)
		_set_output_path(output_directory, input_group, clip_data)
		all_clip_data.append(clip_data)

	return all_clip_data


def _set_output_path(output_directory: Path, input_group: dict[str, Any], clip_data: VideoClipData):
	'''
	Gets output path for the clip.
	If one isn't provided in `input_group`, default to a generated name.
	If a file extension isn't provided, default to the extension of the input file.
	'''
	output_path = _get_abs_path(
		output_directory,
		Path(input_group.get("output", _default_output_name(clip_data)))
	)
	if len(output_path.suffix) == 0:
		output_path = output_path.with_suffix(clip_data.input_path.suffix)
	clip_data.output_path = output_path


def _get_abs_path(base_abs_path: Path, maybe_abs_path: Path) -> Path:
	'''
	Returns `maybe_abs_path` if it's an absolute path.
	Otherwise returns `base_abs_path` joined with `maybe_abs_path`.
	'''
	full_path = Path()
	if maybe_abs_path.is_absolute():
		full_path = Path(maybe_abs_path)
	else:
		full_path = base_abs_path.joinpath(maybe_abs_path)
	return full_path


def _parse_resolution(input_group: dict[str, Any]) -> tuple | None:
	'''
	Parses (width, height) resolution into (height, width) if present for FFMPEG.
	Otherwise returns `None` to use base file's resolution.
	'''
	resolution = input_group.get("resolution", None)
	if resolution is not None:
		resolution.reverse()
	return resolution


def _default_output_name(clip_data: VideoClipData) -> str:
	input_path = Path(clip_data.input_path)
	start_timestamp = ','.join(map(str, clip_data.start_time))
	end_timestamp = ','.join(map(str, clip_data.end_time))
	return f"{input_path.stem} Clip {start_timestamp}-{end_timestamp}{input_path.suffix}"
