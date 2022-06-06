from pytube import YouTube
from moviepy.editor import *


def download(link, min_start, sec_start, min_stop, sec_stop):
    yt = YouTube(str(link))
    video = yt.streams.filter(file_extension='mp4', only_video=True).first()
    video.download(filename='video.mp4')
    print('Download finished')
    clip = VideoFileClip("video.mp4").subclip(t_start=(int(min_start), int(sec_start)),
                                              t_end=(int(min_stop), int(sec_stop)))
    clip.write_videofile("video_clip.mp4", fps=25)


def hello(msg="hello"):
    print(msg)


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
