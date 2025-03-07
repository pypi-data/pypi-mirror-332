from .utils.detection import pred_word
from .utils.bboxes import sort_word_bboxes

from .utils.misc import progress_bar

import numpy as np
import cv2, os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def recognize(
        img_path, 
        verbose=True,
        word_configs={
            'kernel': (10, 10),
            'iterations': 2
        },
        char_weights={
            'lowercase': 0.95,
            'uppercase': 0.85,
            'digits_and_special_chars': 0.80 
        }
    ):
    img = cv2.imread(img_path)
    img = cv2.bitwise_not(img)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones(word_configs.get('kernel'), np.uint8) 

    dilated_img = cv2.dilate(gray_img, kernel, iterations=word_configs.get('iterations')) 
    contours, _ = cv2.findContours(dilated_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cont_bboxes = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cont_bboxes.append((x, y, x+w, y+h))

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cont_bboxes = sort_word_bboxes(cont_bboxes)
    data = []


    print('\n')

    for i in range(len(cont_bboxes)):
        img = cv2.imread(img_path)

        # Extract the first word's bounding box
        x_min, y_min, x_max, y_max = cont_bboxes[i]
        word_img = img[y_min:y_max, x_min:x_max]

        # Convert to grayscale (important for padding)
        word_img = cv2.cvtColor(word_img, cv2.COLOR_RGB2GRAY)

        # Increase the dimensions by padding
        padding = 100
        word_img = cv2.copyMakeBorder(word_img, padding, padding, padding, padding, 
                                    cv2.BORDER_CONSTANT, value=255)

        # Save the img
        temp_dir = os.path.join(BASE_DIR, 'temp')
        os.makedirs(temp_dir, exist_ok=True)

        path = os.path.join(temp_dir, 'word.png')
        cv2.imwrite(path, word_img)


        labels, confs = pred_word(
            img_path=path, 
            factors=[
                char_weights['lowercase'],
                char_weights['uppercase'],
                char_weights['digits_and_special_chars']
            ]
        )

        data.append([ ''.join(labels), cont_bboxes[i], confs ])
        os.remove(path)

        if verbose:
            progress_bar(i+1, len(cont_bboxes))

    print('\n\n')
    return data


# wat does python -c do?
# ans: python -c is used to execute a python command from the command line
# e.g., python -c "print('Hello, World!')"