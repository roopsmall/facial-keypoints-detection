from matplotlib import pyplot as plt
from cv2 import VideoCapture, cvtColor, COLOR_BGR2GRAY, COLOR_BGR2HSV, THRESH_BINARY, flip
from cv2 import threshold as thresh
from numpy import ceil


class plot(object):
	"""plot camera feed with various filters"""

	def __init__(self, fps=24, cmap="magma"):
		"""get camera object, initialise colour map and frame rate"""

		self.capture = VideoCapture(0)
		self.fps = fps
		self.cmap = cmap


	def filter(self, im, filter=None):
		"""return filtered image"""

		if filter is not None:
			im = cvtColor(im, filter)
		
		return im


        def threshold(self, im, method=None):
		"""return threshold image"""

		im = cvtColor(im, COLOR_BGR2GRAY)
                if method is not None:
			_, im = thresh(im, 100, 255, method)

		return im


	def camera(self, methods):
		"""grab images from camera and apply user-specified filters as defined in methods"""
		
		# interactive plotting on
		plt.ion()
		fig = plt.figure()
		# reduce whitespace in plot window
		fig.subplots_adjust(wspace=0, hspace=0)
		num_plots = len(methods)
		cols = 3
		rows = int(ceil(num_plots / 3.))

		# create axis objects
		axes = [fig.add_subplot(rows, cols, i) for i in xrange(1, num_plots+1)]
		[ax.set_axis_off() for ax in axes]
		_, frame = self.capture.read()
	
		# initialise artist objects
		artists = []
		for i in xrange(num_plots):
			if 'cmap' in methods[i].keys():
				artists.append(axes[i].imshow(frame, cmap=plt.get_cmap(methods[i]['cmap'])))
			else:
				artists.append(axes[i].imshow(frame))
		
		# loop over camera input
		while 1:
			_, frame = self.capture.read()
                	images = [frame.copy() for _ in xrange(num_plots)]
			images = [flip(im, 1) for im in images]
			method = [self.filter if methods[i]['method'] == 'filter' else self.threshold for i in xrange(num_plots)]
			images = [method[i](images[i], **methods[i]['arguments']) for i in xrange(num_plots)]
			[artist.set_data(images[i]) for i, artist in enumerate(artists)]
			plt.axis('off')
			plt.draw()
			plt.pause(.0000001)


if __name__ == '__main__':

	methods = [{'method': 'filter', 'arguments': {'filter': None}}, 
			{'method': 'filter', 'arguments': {'filter': COLOR_BGR2GRAY}}, 
			{'method': 'threshold', 'arguments': {'method':THRESH_BINARY}, 'cmap':'gray'}, 
			{'method': 'threshold', 'arguments': {'method':THRESH_BINARY}, 'cmap':'magma'}]

	plot().camera(methods)
