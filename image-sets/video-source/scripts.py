from pytube import YouTube
from moviepy.editor import *
import cv2


def download(link, min_start, sec_start, min_stop, sec_stop):
    yt = YouTube(str(link))
    video = yt.streams.filter(file_extension='mp4', only_video=True).first()
    video.download(filename='video.mp4')
    print('Download finished')
    clip = VideoFileClip('video.mp4').subclip(t_start=(int(min_start), int(sec_start)),
                                              t_end=(int(min_stop), int(sec_stop)))
    clip.write_videofile('video_clip.mp4', fps=25)


def split_frames(num):
    vid = cv2.VideoCapture('video_clip.mp4')
    frame_count = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    success, image = vid.read()
    count = 0
    fps = 25
    while success and count < int(num):
        cv2.imwrite('../image%d.jpg' % count, image)
        vid.set(cv2.CAP_PROP_POS_MSEC, (count*int(frame_count/num)*(1000/fps)))
        success, image = vid.read()
        count += 1


def hello(msg="hello"):
    print(msg)


if __name__ == '__main__':
    if sys.argv[1] == 'download':
        globals()[sys.argv[1]](sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif sys.argv[1] == 'split_frames':
        globals()[sys.argv[1]](int(sys.argv[2]))
