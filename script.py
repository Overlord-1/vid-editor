import yt_dlp
import pandas as pd
def download_video(url, output_path):
    ydl_opts = {
        'format': 'best', 
        'outtmpl': output_path if output_path else '%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': True,
    }


    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info)
            return video_path
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None



# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# title = "Rick Astley - Never Gonna Give You Up" 
# output_path = f"clips/{title}.mp4"
# downloaded_video = download_video(video_url, output_path)
# if downloaded_video:
#     print(f"Video downloaded successfully: {downloaded_video}")
# else:
#    print("Failed to download video.")  





df = pd.read_csv('data.csv')


# step 1 # read the csv file and download the videos
for idx,row in df.iterrows():
    try:
        video_url = row['url']
        title = row['title'] 
        output_path = f"clips/{title}.mp4"
        downloaded_video = download_video(video_url, output_path)
        if downloaded_video:
            print(f"Video downloaded successfully: {downloaded_video}")
        else:
            print("Failed to download video.")  
    except Exception as e:
        print(f"Error processing row {idx}: {e}")



# step 2 -> for all the downloaded videos, clip all of them acccording to the start and end time