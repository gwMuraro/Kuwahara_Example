import cv2
from pykuwahara import kuwahara
import os 

dir_sourceFolder = "./source_images"
dir_resultFolder = "./result_images"

for str_fileName in os.listdir(dir_sourceFolder) : 
    print("treating : " + dir_sourceFolder + "/" + str_fileName)
    str_fileNameWithoutExtension = os.path.splitext(str_fileName)[0]
    str_fileExtension = os.path.splitext(str_fileName)[1]

    image = cv2.imread(dir_sourceFolder + "/" + str_fileName)
    image = (image / 255).astype('float32')     # pykuwahara supports float32 as well

    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(lab_image)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)

    filt1 = kuwahara(image, method='gaussian', radius=5, sigma=2., image_2d=l)
    filt2 = kuwahara(image, method='gaussian', radius=5, sigma=2., image_2d=v)
    # filt = kuwahara(lab_image, method='gaussian', radius=5, sigma=2., image_2d=l)

    os.mkdir(dir_resultFolder + "/" + str_fileNameWithoutExtension)
    cv2.imwrite(dir_resultFolder + "/" + str_fileNameWithoutExtension + "/" + str_fileNameWithoutExtension + '_filt1' + str_fileExtension, filt1 * 255)
    cv2.imwrite(dir_resultFolder + "/" + str_fileNameWithoutExtension + "/" + str_fileNameWithoutExtension + '_filt2' + str_fileExtension, filt2 * 255)
    # cv2.imwrite(dir_resultFolder + "/" + str_fileNameWithoutExtension + "/" + str_fileNameWithoutExtension + '_filt0' + str_fileExtension, cv2.cvtColor(filt, cv2.COLOR_Lab2BGR) * 255)
