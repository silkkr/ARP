from moviepy.editor import *
from random import randint

clip1 = VideoFileClip("humanlove.mp4")
clip2 = VideoFileClip("Clip6.mov")
clip3 = VideoFileClip("Clip7.mov")
clip4 = VideoFileClip("Clip8.mov")

# clipin keskipiste on 960,540

final_clip = CompositeVideoClip(
                [clip1,
                clip2.resize(0.6).set_start(randint(17,40)).set_position((randint(0,1850),randint(0,940))),
                clip3.resize(0.4).set_start(randint(27,40)).set_position((randint(0,1850),randint(0,940))),
                clip4.resize(0.2).set_start(randint(17,40)).set_position((randint(0,1850),randint(0,340)))],
                size=(1920,1080))

final_clip.set_duration(73).write_videofile("humanlove_edited2.mp4", fps=30, audio=True)
