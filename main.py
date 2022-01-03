import cv2
import numpy as np

width = 320
height = 320

numberOfTilesHorizontally = 8
numberOfTilesVertically = 8

while True:
    frame = np.zeros([height, width, 3], dtype = np.uint8)
    
    count = 0
    numOfPixelsPerHorizontalTile = int(width / numberOfTilesHorizontally)
    numOfPixelsPerVerticalTile = int(height / numberOfTilesVertically)

    for i in range(numberOfTilesVertically):
        for j in range(numberOfTilesHorizontally+1):
            if count % 2 == 0:
                frame[i * numOfPixelsPerVerticalTile: i * numOfPixelsPerVerticalTile + numOfPixelsPerVerticalTile, (j-1) * numOfPixelsPerHorizontalTile: (j-1) * numOfPixelsPerHorizontalTile + numOfPixelsPerHorizontalTile] = (50, 25, 200)
            else:
                frame[i * numOfPixelsPerVerticalTile: i * numOfPixelsPerVerticalTile + numOfPixelsPerVerticalTile, (j-1) * numOfPixelsPerHorizontalTile: (j-1) * numOfPixelsPerHorizontalTile + numOfPixelsPerHorizontalTile] = (255, 255, 255)

            count += 1

    cv2.imshow("My Window", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
