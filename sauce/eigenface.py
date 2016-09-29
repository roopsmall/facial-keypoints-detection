from numpy import genfromtxt, savetxt, linalg, dot
from PIL import Image, ImageDraw


class run(object):

	def __init__(self):
		pass
		
	@staticmethod
	def pca(data_file_in, offset, data_file_out='../data/eigenvectors.csv', delimiter=','):
		
		try:
			data = genfromtxt(data_file_in, delimiter=delimiter)[:,offset:].T
			data = dot(data, data.T)
			A, V = linalg.eigh(data)
			args = argsort(A)
			V = V[:, sort]
			savetxt(data_file_out, V, delimiter=delimiter)

			return 0

		except:
			return 1

	@classmethod
	def top_eigenvectors(cls, N=100, eigenvectors='../data/eigenvectors.csv', delimiter=',', face_shape=(96,96), image_out=None):
		
		try:
			topN = []
			V = genfromtxt(eigenvectors, delimiter=delimiter)
			principles = V[:,-N:]

			for eachline in range(0,N):
        			vector = principles[:,eachline]
        			mx, mn = max(vector), min(vector)
        			component = (vector - mn)*255.0/mx
				topN.append(vector)
        			im = vector.reshape(face_shape)
        			im = Image.fromarray(im).convert('RGB')
        			if image_out is not None:
        				im.save(image_out.replace('.png','') + '_' + eachline + '.png')

			return principles

		except:
			return 1


	@classmethod
	def reconstruct_face(cls, face_vector, N=100, eigenvectors='../data/eigenvectors.csv', delimiter=',', face_shape=(96,96), image_out=None):


		try:
			topN = cls.top_eigenvectors(N=N)
        		coefficients = [dot(face_vector.T, topN[i]) for i in range(0,N)]
        		reconstruction = coefficients*topN
        		reconstruction = sum(reconstruction, 1)
        		mx, mn = max(reconstruction), min(reconstruction)
        		reconstruction = (reconstruction - mn)*255./mx
        		im = reconstruction.reshape((96,96))
        		im = Image.fromarray(im).convert('RGB')
        		if image_out is not None:
				im.save(image_out.replace('.png','') + '.png')
			
			return im
			
		except:
			return 1


if __name__ == '__main__':
	pass

