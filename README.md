# YouTube Video Compilation Project

This project aims to automate the process of creating video compilations from YouTube clips. The main functionalities include:

1.  **Downloading Video Clips:** Downloading specified video clips from YouTube.
2.  **Extracting Segments:** Extracting specific segments from the downloaded clips based on provided start and end times.
3.  **Adding Title Cards:** Inserting title cards before specified video segments.
4.  **Adding Transitions:** Adding transitions between video segments to create a smoother viewing experience.
5.  **Merging Clips:** Merging all processed clips and title cards into a single output video.

The project will utilize a CSV file (`data.csv`) to manage the input video information, including YouTube links, segment timings, and title card text. The main script (`script.py`) will handle the core logic of the video processing pipeline.

## Current Project State

This project is in its early development phase. Currently, the functionality to download videos from YouTube based on the `data.csv` file is implemented in `script.py`. However, the core video editing features—such as clipping segments, generating title cards, adding transitions, and merging clips into a final video—are yet to be developed. The `structue.md` file provides a specification and guide for these planned future developments.

## File Descriptions

*   **`data.csv`**: This file contains the input data for the video compilation. Each row specifies a video clip, including its YouTube URL, the start and end times for the segment to be extracted, and the text for any title card that should precede it.
*   **`script.py`**: This is the main Python script that orchestrates the video processing pipeline. Its current functionalities include:
    *   Reading video information from the `data.csv` file.
    *   Downloading the full video clips from YouTube using the `yt_dlp` library.
    *   Saving the downloaded videos into the `clips/` directory.
*   **`structue.md`**: This document outlines the intended structure of the project and details the various processing steps involved in creating the final video compilation. It serves as a blueprint for the project's development.
*   **`.gitignore`**: This file specifies intentionally untracked files that Git should ignore. In this project, it is configured to exclude the `clips/` directory, which is where downloaded video clips will be stored, from version control. This prevents large video files from being unnecessarily added to the repository.

## Planned Features

The following features are part of the project's goals but are not yet implemented in `script.py`:

*   **Video Clipping:** Extracting specific segments from the downloaded videos based on `start_time` and `end_time` specified in `data.csv`.
*   **Title Slide Generation:** Creating a 2-second title slide for each video segment. These slides will have a black background and white text, using the `name` field from `data.csv` as the title.
*   **Transitions:** Inserting a 1-second black screen transition between each video segment and its preceding title slide or transition.
*   **Final Video Merging:** Combining all processed video clips, title slides, and transitions into a single MP4 output file, sequenced as: title slide → clip → black screen transition → next title slide → ...

## Potential Issues and Discrepancies

The following are potential issues or discrepancies noted between the project's planning documents and current implementation:

*   **CSV Column Name Mismatch:**
    *   `structue.md` defines CSV columns as `link`, `start_time`, `end_time`, `name`.
    *   `data.csv` (and `script.py` which reads it) uses `url`, `start_time`, `end_time`, `title`.
    *   While `link`/`url` are functionally equivalent, the `name` column specified in `structue.md` (intended for title card text) corresponds to the `title` column in `data.csv`. This should be kept consistent during development.

*   **Timestamp Format for Clipping:**
    *   `data.csv` currently uses a `MM:SS` (e.g., "1:54") or `M:SS` (e.g. "5:30") format for `start_time` and `end_time`.
    *   Video editing libraries (like MoviePy or FFmpeg) typically require timestamps in total seconds (e.g., 114) or a standardized `HH:MM:SS` format. The current format will need conversion before it can be used for video clipping.

*   **Missing Video Editing Libraries:**
    *   `script.py` currently imports `yt_dlp` for downloading and `pandas` for CSV handling.
    *   The planned features of video clipping, title slide generation, and merging will require additional video manipulation libraries (e.g., MoviePy) or command-line tools (e.g., FFmpeg). These dependencies are not yet integrated into `script.py`.
