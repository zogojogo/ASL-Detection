import os
import matplotlib.pyplot as plt
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="Image(1)/Webcam(2) input")
parser.add_argument("-p", "--path", help="Image path input")
args = parser.parse_args()

def predictImage(imageDir):
    os.system("cd darknet && ./darknet detector test data/obj.data cfg/custom-detector.cfg \
              ../weights/custom-detector.weights ../{} -thresh 0.3 -dont_show -map".format(imageDir))
    image = cv2.imread("./darknet/predictions.jpg")
    height, width = image.shape[:2]
    resized_image = cv2.resize(image,(3*width, 3*height),   interpolation = cv2.INTER_CUBIC)
    fig = plt.gcf()
    fig.set_size_inches(15, 8)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.show()

def webcamInfer():
    os.system("cd darknet && ./darknet detector demo data/obj.data cfg/custom-detector.cfg \
              ../weights/custom-detector.weights")

if args.mode == '1':
    predictImage(args.path)

elif args.mode == '2':
    webcamInfer()
