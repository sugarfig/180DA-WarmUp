# source: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def find_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
         # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX
    # return the bar chart
    return bar

cap = cv2.VideoCapture(0)

clt = KMeans(n_clusters=3) #cluster number

while True:
    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_reshaped = rgb.reshape((rgb.shape[0] * rgb.shape[1], 3))  #represent as row*column,channel number
    clt.fit(frame_reshaped)
    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)

    # Display the resulting frame and color bar
    cv2.imshow('frame', frame)
    cv2.imshow('color bar', bar)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()