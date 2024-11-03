from dataclasses import dataclass
from pathlib import Path
import threading

from moviepy.editor import VideoFileClip


@dataclass
class VideoClipData:
	input_path: Path
	start_time: tuple[int, int]
	end_time: tuple[int, int]
	output_path: Path | None = None
	codec: str | None = None
	resolution: tuple[int, int] | None = None


class ClippingThread(threading.Thread):
	'''
	Thread to clip videos using moviepy.
	'''
	def __init__(self, clip_data: VideoClipData):
		super().__init__(daemon=False)
		self.clip_data = clip_data


	def run(self):
		clip_data = self.clip_data
		video: VideoFileClip
		with VideoFileClip(str(clip_data.input_path), target_resolution=clip_data.resolution) as video:
			video = video.subclip(clip_data.start_time, clip_data.end_time)
			video.write_videofile(str(clip_data.output_path), codec=clip_data.codec)
