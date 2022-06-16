import pathlib

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from six import BytesIO

import tensorflow as tf
import tensorflow_hub as hub
import pycocotools
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz
from object_detection.utils import ops

matplotlib.use('Qt5Agg')

def to_np_array(path):
    image_data = tf.io.gfile.GFile(path, 'rb').read()
    image = Image.open(BytesIO(image_data))

    (width, height) = image.size
    return np.array(image.getdata()).reshape((1, height, width, 3)).astype(np.uint8)


data_dir = pathlib.Path.cwd().parent / 'image-sets'
image_list = list(data_dir.glob('*.jpg'))
print('images loaded')

# label_dir = pathlib.Path.cwd().parent / 'labels'
# label_list = list(label_dir.glob('*.xml'))


path_to_labels = 'D:\\Repositories\\models\\research\\object_detection\\data\\mscoco_label_map.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(path_to_labels, use_display_name=True)

model_url = 'https://tfhub.dev/tensorflow/retinanet/resnet101_v1_fpn_1024x1024/1'
model = hub.load(model_url)
print('model loaded')
test_image = 'C:\\Users\\oprea\\Desktop\\test.jpg'
np_image = to_np_array(test_image)
plt.imshow(np_image[0])
plt.show()

print('inferencing')
results = model(np_image)
result = {key: value.numpy() for key, value in results.items()}
viz.visualize_boxes_and_labels_on_image_array(
      np_image[0],
      result['detection_boxes'][0],
      (result['detection_classes'][0]).astype(int),
      result['detection_scores'][0],
      category_index,
      use_normalized_coordinates=True,
      max_boxes_to_draw=200,
      min_score_thresh=.30,
      agnostic_mode=False)

print('displaying result')
plt.imshow(np_image[0])
plt.show()
