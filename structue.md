# Video Editor Structure

## CSV File Format

The input CSV file should follow this structure:

| Column      | Description                    |
|-------------|--------------------------------|
| link        | URL or path to the video       |
| start_time  | Starting timestamp of clip     |
| end_time    | Ending timestamp of clip       |
| name        | Name/identifier for the clip   |

Example:
```csv
link,start_time,end_time,name
https://youtube.com/,00:00:30,00:01:15,intro_clip
```

## Processing Steps

### 1. Download Videos
- Read CSV file and extract video links
- Download videos from URLs/paths
- Store in temporary directory

### 2. Split Videos
- Process each video according to timestamps
- Extract clips using start_time and end_time
- Save individual clips with name identifier

### 3. Merge Final Video
Requirements:
- Create title slide for each clip:
  - Black background
  - White text (clip name)
  - Duration: 2 seconds
- Insert 1-second black screen between clips
- Sequence: title → clip → black screen → title → clip...
- Output format: MP4

Final output will be a single video file combining all clips with transitions.
