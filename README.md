# Video Clipper
Batch processing of videos into clips. Uses [`moviepy`](https://pypi.org/project/moviepy) for actual video processing.

## Installation
```bash
git clone https://github.com/quasikyo/video-clipper
cd video-clipper
python -m venv venv
source venv/Scripts/activate
pip install
pip install -r requirements.txt
```
`venv` steps aren't necessary but are recommended.

## Running
```bash
python main.py [-f|--file] "path/to/input.json"
```

## Input File Structure
- `input_directory`: Absolute path indicating where to look for files.
- `output_directory`: Absolute path indicating where to output files.
- `clips`: array of objects consisting of the following:
  - `video`:` Absolute or relative path to source video file.
    - If relative, appended onto `input_directory`.
  - `start_time`: 2-item array with minutes and seconds.
  - `end_time`: 2-item array with minutes and seconds.
  - (Optional) `output`: Name of output file. Will output in working directory.
    - Default: Outputs generated name to `output_directory`.
    - If relative, outputted to `output_directory`.
    - If no file extension, defaults to the extension of the input file.
  - (Conditional) `codec`: Depends on container type of `output`. Not necessary for `.mp4`.
    - See [moviepy documentation](https://moviepy.readthedocs.io/en/latest/ref/VideoClip/VideoClip.html?highlight=write_videofile#moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip.write_videofile) for defaults.
    - All codecs by [ffmpeg](https://ffmpeg.org) are supported.
  - (Optional) `resolution`: 2-item array with width and height.
    - Default: Width and height of source video.

#### Example
```json
{
	"input_directory": "D:\\Recordings",
	"output_directory": "D:\\Recordings\\Monster Hunter Wilds",
	"clips": [
		{
			"video": "D:\\Recordings\\2024-11-02 12-02-36.mp4",
			"start_time": [0, 44],
			"end_time": [0, 54],
			"output": "10 seconds.avi",
			"codec": "rawvideo",
			"resolution": [2580, 1080]
		},
		{
			"video": "D:\\Recordings\\2024-11-02 11-26-33.mp4",
			"start_time": [9, 42],
			"end_time": [9, 49],
			"output": "D:\\7 seconds.mp4"
		},
		{
			"video": "2024-11-02 12-02-36.mp4",
			"start_time": [6, 6],
			"end_time": [6, 36],
			"resolution": [2580, 1080]
		}
	]
}
```
This input file will result in the following files:
1. `D:\Recordings\2024-11-02 12-02-36.mp4` -> `D:\Recordings\Monster Hunter Wilds\10 seconds.avi` (10 seconds, 2580x1440)
2. `D:\Recordings\2024-11-02 11-26-33.mp4` -> `D:\7 seconds.mp4` (7 seconds, 3440x1440 from base file)
3. `D:\Recordings\2024-11-02 12-02-36.mp4` -> `D:\Recordings\Monster Hunter Wilds\2024-11-02 12-02-36 Clip 6,6-6,36.mp4` (30 seconds, 2580x1440)
