import cv2, os
import numpy as np

from .bboxes import filter_bboxes
from ultralytics import YOLO 


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

lc_model = YOLO(os.path.join(ROOT_DIR, "models", "CharNetLC.pt"))
uc_model = YOLO(os.path.join(ROOT_DIR, "models", "CharNetUC.pt"))
dc_model = YOLO(os.path.join(ROOT_DIR, "models", "CharNetDC.pt"))


def predict(model, img_path, reduce_by=1):
    img = cv2.imread(img_path)
    results = model(img, verbose=False)

    boxes = results[0].boxes.xyxy.numpy()
    class_ids = results[0].boxes.cls.numpy().astype(int)
    confidences = results[0].boxes.conf.numpy()

    # Sort by x-coordinate before filtering
    sorted_indices = np.argsort(boxes[:, 0])
    sorted_boxes = boxes[sorted_indices]

    sorted_confidences = confidences[sorted_indices]
    sorted_class_ids = class_ids[sorted_indices]

    # Filter bounding boxes
    to_filter = {str(i): box for i, box in enumerate(sorted_boxes)}
    filtered_bboxes, filtered_confidences = filter_bboxes(bboxes=to_filter, confidences=sorted_confidences)


    filtered_bboxes_list = list(filtered_bboxes.values())
    box_to_index = {tuple(box): i for i, box in enumerate(sorted_boxes)}


    filtered_indices = [box_to_index[tuple(box)] for box in filtered_bboxes_list]
    filtered_confidences = sorted_confidences[filtered_indices] * reduce_by

    filtered_class_ids = sorted_class_ids[filtered_indices]

    for i, box in enumerate(filtered_bboxes_list):
        x_min, y_min, x_max, y_max = map(int, box)
        class_id = filtered_class_ids[i]

        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(img, model.names[class_id], (x_min, y_min), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return filtered_bboxes, filtered_confidences, [model.names[class_id] for class_id in filtered_class_ids]


def pred_word(img_path, factors=[0.99, 0.99, 0.9]):
    lc_factor, uc_factor, dc_factor = factors

    # Get predictions from each model
    fb_lc, fc_lc, fl_lc = predict(lc_model, img_path, reduce_by=lc_factor)
    fb_uc, fc_uc, fl_uc = predict(uc_model, img_path, reduce_by=uc_factor)
    fb_dc, fc_dc, fl_dc = predict(dc_model, img_path, reduce_by=dc_factor)

    # Extract bounding box arrays from dictionaries
    boxes_lc = np.array(list(fb_lc.values()))
    boxes_uc = np.array(list(fb_uc.values()))
    boxes_dc = np.array(list(fb_dc.values()))

    # Combine bounding boxes, confidences, and labels
    all_boxes = np.concatenate((boxes_lc, boxes_uc, boxes_dc), axis=0)
    all_confidences = np.concatenate((fc_lc, fc_uc, fc_dc), axis=0)
    all_labels = np.concatenate((fl_lc, fl_uc, fl_dc), axis=0)

    # Sort combined results by x-coordinate
    # sorted_indices = np.argsort(all_boxes[:, 0])
    sorted_indices = np.argsort(all_boxes) if all_boxes.ndim == 1 else np.argsort(all_boxes[:, 0])
    sorted_boxes = all_boxes[sorted_indices]
    sorted_confidences = all_confidences[sorted_indices]
    sorted_labels = all_labels[sorted_indices]

    # Filter combined results
    to_filter = {str(i): box for i, box in enumerate(sorted_boxes)}
    filtered_bboxes, filtered_confidences = filter_bboxes(bboxes=to_filter, confidences=sorted_confidences)

    # Convert filtered dictionary back to a list
    filtered_bboxes_list = list(filtered_bboxes.values())

    # Create a mapping of boxes to their index in the original sorted lists.
    box_to_index = {tuple(box): i for i, box in enumerate(sorted_boxes)}
    filtered_indices = [box_to_index[tuple(box)] for box in filtered_bboxes_list]

    # Reorder filtered confidences and labels.
    filtered_confidences = sorted_confidences[filtered_indices]
    filtered_labels = sorted_labels[filtered_indices]

    return filtered_labels, np.mean(filtered_confidences)
