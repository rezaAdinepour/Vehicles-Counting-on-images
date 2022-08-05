import cv2 as cv
from vehicle_detector import VehicleDetector
import glob

vd = VehicleDetector()

imagesDir = glob.glob('images/*.jpg')
#print(imagesDir)
vehicleDirCount = 0

for imgPath in imagesDir:
    print('image path: ', imgPath)
    img = cv.imread(imgPath)

    vehicleBoxes = vd.detect_vehicles(img)
    vehicleCount = len(vehicleBoxes)
    print('current vehicle: ', vehicleCount)
    vehicleDirCount += vehicleCount
    print('total current vehicle: ', vehicleDirCount)

    #print(vehicleBoxes)
    for box in vehicleBoxes:
        (x, y, w, h) = box
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(img, 'vehicle: ' + str(vehicleCount), (20, 50), 0, 2, (255, 0, 0), 3)


    cv.imshow('img', img)
    cv.waitKey(2000)
    cv.destroyAllWindows()