import cv2
import time
import numpy as np

from darkflow.net.build import TFNet

from src import *


# noinspection SpellCheckingInspection
def run(model_name, device_id):
    tf_net = TFNet({
        'model': MODEL_PATH.format(model=model_name),
        'load': WEIGHTS_PATH.format(model=model_name),
        'threshold': MODEL_THRESHOLD
    })
    colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

    capture = cv2.VideoCapture(device_id)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while True:
        start_time = time.time()
        ret, frame = capture.read()
        if ret:
            results = tf_net.return_predict(frame)
            for color, result in zip(colors, results):
                tl = (result['topleft']['x'], result['topleft']['y'])
                br = (result['bottomright']['x'], result['bottomright']['y'])
                label = result['label']
                confidence = result['confidence']
                text = '{}: {:.0f}%'.format(label, confidence * 100)
                frame = cv2.rectangle(frame, tl, br, color, 5)
                frame = cv2.putText(
                    frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow('frame', frame)
            print('FPS {:.1f}'.format(1 / (time.time() - start_time)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
