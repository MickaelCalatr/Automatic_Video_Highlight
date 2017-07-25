import os
from Config import conf

path = os.getcwd() + "/tmp/"
f = None

def add_video(name):
    with open(conf.result_file,"a+") as f:
        f.write('file ' + path + str(name) + '.mp4\n')

def save(start, end):
    name = conf.video_source[conf.camera]
    end = (end - start) / 25
    start_point = start / 25
    add_video(start)
    os.system("ffmpeg -loglevel quiet -r 25 -i " + name +" -ss " + str(start_point) + " -c copy -t " + str(end) + " " + path + str(start) + ".mp4")

def concatenate():
    os.system("ffmpeg -loglevel quiet -f concat -safe 0 -i " + conf.result_file + " -c copy " + conf.video_name_dest)
