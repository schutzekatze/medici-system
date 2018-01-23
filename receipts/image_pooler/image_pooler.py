import logging
import cv2
import numpy
import datetime

logger = logging.getLogger(__name__)

def pool_image(mediciuser, image):
    path = '/tmp/' + mediciuser.user.username + ' ' + str(datetime.datetime.now()) + '.jpg'

    logger.info("Saving image from <" + mediciuser.user.username + "> to '" + path + "'.")

    img = cv2.imdecode(numpy.fromstring(image, numpy.uint8), 1)
    cv2.imwrite(path, img)
