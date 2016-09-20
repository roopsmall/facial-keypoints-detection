from matplotlib import pyplot as plt
from cv2 import VideoCapture, cvtColor, COLOR_BGR2GRAY, COLOR_BGR2HSV, THRESH_BINARY, flip
from cv2 import threshold as thresh

class plot(object):

	def __init__(self, fps=24):

		self.capture = VideoCapture(0)
		self.fps = fps

	def filter(self, filter=None):

		plt.ion()		
		fig = plt.figure()
		ax = plt.gca()
		
		_, frame = self.capture.read()
		frame = flip(frame, 1)
		artist = ax.imshow(frame)

		while 1:
			_, frame = self.capture.read()
			
			if filter is not None:
				_ = cvtColor(frame, filter)

			artist.set_data(frame)
			plt.draw()
 			plt.pause(.001)
			plt.axis("off")
			plt.axis("tight")


        def threshold(self, method=None):

                plt.ion()               
                fig = plt.figure()
                ax = plt.gca()
                
                _, frame = self.capture.read()
                artist = ax.imshow(frame)

                while 1:
                        _, frame = self.capture.read()
			_ = cvtColor(frame, COLOR_BGR2GRAY)
                        frame = flip(frame, 1)

                        if method is not None:
                                _, frame = thresh(frame, 127, 255, method)

                        artist.set_data(frame)
                        plt.draw()
                        plt.pause(.001)
                        plt.axis("off")
                        plt.axis("tight")


if __name__ == '__main__':

	#plot().filter(filter=None)
	#plot().filter(filter=COLOR_BGR2GRAY)
	plot().threshold(method=THRESH_BINARY)

