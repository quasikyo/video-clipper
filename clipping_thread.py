from dataclasses import dataclass
from os import path
import threading

from moviepy.editor import VideoFileClip


@dataclass
class VideoClipData:
	file_path: str
	start_time: tuple[str, str]
	end_time: tuple[str, str]
	output: str


class ClippingThread(threading.Thread):
	'''
	Thread to clip videos using moviepy.
	'''
	def __init__(self, clip_data: VideoClipData):
		super().__init__(daemon=False)
		self.clip_data = clip_data


	def run(self):
		clip_data = self.clip_data
		output_name = self.get_output_name()

		video = VideoFileClip(clip_data.file_path)
		video = video.subclip(clip_data.start_time, clip_data.end_time)

		print(f"Starting thread for {clip_data}")
		video.write_videofile(output_name)
		print(f"Outputed to {output_name}")


	def get_output_name(self):
		file_path, extension = path.splitext(self.clip_data.file_path)
		name = self.clip_data.output
		if len(name) != 0:
			return f"{name}{extension}"

		start_timestamp = ','.join(map(str, self.clip_data.start_time))
		end_timestamp = ','.join(map(str, self.clip_data.end_time))
		return f"{file_path} Clip {start_timestamp}-{end_timestamp}{extension}"
