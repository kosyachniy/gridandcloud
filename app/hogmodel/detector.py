from . import dtc
import numpy as np
from skimage.transform import pyramid_gaussian
from .nms import non_max_suppression


def sliding_window(image, step_size, window_size):
    for y in range(0, image.shape[0], step_size):
        for x in range(0, image.shape[1], step_size):
            yield x, y, image[y:y+window_size[1], x:x+window_size[0]]


def detect_faces(src):
    detector = dtc.FaceDetector('./hogfacedetector/scripts/model/weights.pkl')
    boxes = []
    scale_factor = 1
    window_size = (128, 128)
    step_size = 16
    for img in pyramid_gaussian(np.copy(src), downscale=2, multichannel=True):
        if img.shape[0] < window_size[0] or img.shape[1] < window_size[1]:
            break

        for (x, y, window) in sliding_window(img, step_size, window_size):
            if window.shape[0] < window_size[0] or window.shape[1] < window_size[1]:
                continue

            confidence = detector.detect(window)
            if confidence > 0:
                x1 = x * scale_factor
                y1 = y * scale_factor
                x2 = x1 + window_size[1] * scale_factor
                y2 = y1 + window_size[0] * scale_factor
                boxes.append((x1, y1, x2, y2, confidence))

        scale_factor *= 2

    if len(boxes) == 0:
        return 0
    else:
        return 1
