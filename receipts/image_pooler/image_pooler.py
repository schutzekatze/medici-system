import logging
import cv2
import numpy
import uuid
import os

logger = logging.getLogger(__name__)

def pool_image(mediciuser, image):
    image_dir = '/home/flux/receipts/unlabeled'

    if len(os.listdir(image_dir)) > 2000:
        return

    path = image_dir + '/receipt-' + uuid.uuid4().hex + '.jpg'

    logger.info("Saving image from <" + mediciuser.user.username + "> to '" + path + "'.")

    img = cv2.imdecode(numpy.fromstring(image, numpy.uint8), 1)
    cv2.imwrite(path, img)
