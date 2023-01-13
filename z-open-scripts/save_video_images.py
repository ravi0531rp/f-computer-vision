import cv2
import os
from moviepy.editor import *

# Set the path to the images directory
path = "path/to/images/"

# Get all the images in the directory
images = [f for f in os.listdir(path) if f.endswith('.jpg')]

# Sort the images by name
images.sort()

# Create an empty list to store the image frames
frame_list = []

# Iterate through the images and add them to the frame list
for image in images:
    img = cv2.imread(path + image)
    frame_list.append(img)

# Set the video frame rate
fps = 30

# Create the video using the frames
out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (frame_list[0].shape[1], frame_list[0].shape[0]))

for i in range(len(frame_list)):
    out.write(frame_list[i])
out.release()

# Add the music to the video
video = VideoFileClip("video.avi")
audio = AudioFileClip("music.mp3")
final_video = video.set_audio(audio)
final_video.write_videofile("final_video.mp4")
