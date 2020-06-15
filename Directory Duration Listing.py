import pandas as pd
import moviepy.editor
import os

filepath = r"F:\Udemy Courses\9) Javascript\The Web Developer Bootcamp"

title_list = []
duration_list = []

def list_video_files(filepath):
    for r, d, f in os.walk(filepath):
        for file in f:
            if file.endswith(".mp4"):
                fullpath = os.path.join(r, file)
                title_list.append(fullpath)
                duration_list.append(int(moviepy.editor.VideoFileClip(fullpath).duration))
    
    output_df = pd.DataFrame({"Title":title_list, "Duration":duration_list})
    output_df.to_excel(os.path.join(filepath,"Playlist Duration.xlsx"))

list_video_files(filepath=filepath)


