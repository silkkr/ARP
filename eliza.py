from moviepy.editor import *
from random import randint


clip1 = VideoFileClip("eliza.mp4")
clip2 = ImageClip("rae.png")
clip3 = ImageClip("raeneg.png")
clip4 = VideoFileClip("sivu.mp4")
clip5 = VideoFileClip("tanssi.mp4")
clip6 = VideoFileClip("microchip2.mp4")
clip7 = VideoFileClip("heiluminen.mp4")
clip8 = VideoFileClip("nopea2.mp4")

final_clip = CompositeVideoClip(
                [clip1,
                clip2.resize(0.7).set_start(randint(90,100)).set_end(randint(110,120)).set_position((randint(0,900),randint(0,940))),
                clip3.resize(0.7).set_start(randint(90,100)).set_end(randint(110,120)).set_position((randint(0,900),randint(0,940))),
                clip4.resize(0.6).set_start(randint(17,40)).set_position((randint(0,150),randint(0,240))),
                clip5.resize(0.4).set_start(randint(22,40)).set_position((randint(300,350),randint(0,540))),
                clip6.resize(0.7).set_start(90).set_position((randint(0,450),randint(0,440))),
                clip7.resize(0.8).set_start(100).set_position("center"),
                clip8.resize(0.7).set_start(122).set_position((randint(0,850),randint(0,240)))],
                size=(1920,1080))

final_clip.set_duration(137).write_videofile("eliza_edited2.mp4", fps=30, audio=False)
