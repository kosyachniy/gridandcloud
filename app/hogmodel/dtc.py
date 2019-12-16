import numpy as np
import pickle as pkl
from skimage.feature import hog
from sklearn.svm import LinearSVC


class FaceDetector:
	def __init__(self, model=None):
		if model:
			self.clf = pkl.load(open(model, 'rb'))
		else:
			self.clf = LinearSVC(penalty='l2', loss='hinge', max_iter=5000)

	def detect(self, x):
		if x.dtype != np.float64:
			x = (x / 256).astype(np.float64)
		hog_x = self.compute_hog(x)
		return self.clf.predict([hog_x])

	@staticmethod
	def compute_hog(x):
		return hog(x, block_norm='L1', visualize=False, multichannel=True)

