import time
import cv2
import numpy as np
import imutils


from imutils.video import VideoStream
from screeninfo import get_monitors


usingPiCamera = True

fs = (round(get_monitors()[0].width, -1), round(get_monitors()[0].height-20, -1))

vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=fs,
        framerate=32).start()

time.sleep(5.0)

timeCheck = time.time()


class Chyme():

    def __init__(self):
        
        while True:
            self.frame = vs.read()
            
            if not usingPiCamera:
                    frame = imutils.resize(self.frame, width=fs[0])
            
            cv2.imshow('Chyme', self.frame)
            key = cv2.waitKey(1) & 0xFF
     
            if key == ord("q"):
                    break
        cv2.destroyAllWindows()
        vs.stop()


def main():
    c = Chyme()
    return c

main()

'''raspistill -f -t 0'''
