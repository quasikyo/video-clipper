# Video Clipper
Batch processing of videos into clips.

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
Expecting a JSON array of objects consisting of the following:
- `video`: Path to source video file.
- `start_time`: 2-item array with minutes and seconds.
- `end_time`: 2-item array with minutes and seconds.
- (Optional) `output`: Name of output file. Will output in working directory.
  - Default: Outputs to same directory as `video`.

#### Example
```json
[
	{
		"video": "D:\\Recordings\\2024-11-02 12-02-36.mp4",
		"start_time": [0, 44],
		"end_time": [0, 54],
		"output": "Styling on Rey Dau"
	},
	{
		"video": "D:\\Recordings\\2024-11-02 11-26-33.mp4",
		"start_time": [9, 42],
		"end_time": [9, 49]
	},
	{
		"video": "D:\\Recordings\\2024-11-02 12-02-36.mp4",
		"start_time": [6, 6],
		"end_time": [6, 36],
		"output": "Untouchable"
	}
]
```
