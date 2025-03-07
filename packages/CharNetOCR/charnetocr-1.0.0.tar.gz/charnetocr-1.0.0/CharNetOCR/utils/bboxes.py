def calculate_overlap_percentage(bbox1, bbox2):
    """
    Calculates the percentage overlap of the smaller box within the larger box.

    Args:
        bbox1: Tuple (x1, y1, x2, y2) representing the first bounding box.
        bbox2: Tuple (a1, b1, a2, b2) representing the second bounding box.

    Returns:
        The percentage overlap, or 0 if the boxes don't overlap.
    """ 

    x1, y1, x2, y2 = bbox1
    a1, b1, a2, b2 = bbox2

    # Check if boxes overlap
    if x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2:
        return 0

    # Calculate intersection area
    intersection_x1 = max(x1, a1)
    intersection_y1 = max(y1, b1)

    intersection_x2 = min(x2, a2)
    intersection_y2 = min(y2, b2)

    intersection_area = (intersection_x2 - intersection_x1) * (intersection_y2 - intersection_y1)

    # Calculate box areas
    area1 = (x2 - x1) * (y2 - y1)
    area2 = (a2 - a1) * (b2 - b1)

    # Determine smaller box
    smaller_area = min(area1, area2)

    # Calculate overlap percentage
    overlap_percentage = (intersection_area / smaller_area) * 100
    return overlap_percentage



def filter_bboxes(bboxes, confidences, threshold=50):
    bbox_keys = list(bboxes.keys())
    bbox_list = list(bboxes.values())

    to_keep = set(range(len(bbox_list)))
    grouped = {}

    for i in range(len(bbox_list)):
        for j in range(len(bbox_list)):
            if i == j:
                continue

            overlap = calculate_overlap_percentage(bbox_list[i], bbox_list[j])
            if overlap > threshold:
                area_i = (bbox_list[i][2] - bbox_list[i][0]) * (bbox_list[i][3] - bbox_list[i][1])
                area_j = (bbox_list[j][2] - bbox_list[j][0]) * (bbox_list[j][3] - bbox_list[j][1])

                larger, smaller = (i, j) if area_i > area_j else (j, i)

                if larger not in grouped:
                    grouped[larger] = []
                grouped[larger].append(smaller)

    for larger, smaller_list in grouped.items():
        smaller_confidences = [confidences[idx] for idx in smaller_list]
        mean_smaller_conf = sum(smaller_confidences) / len(smaller_confidences)

        if mean_smaller_conf > confidences[larger]:
            if larger in to_keep:
                to_keep.remove(larger)
            # else:
            #     print(f"Warning: Index {larger} not found in to_keep. Skipping removal.")
        else:
            for smaller in smaller_list:
                to_keep.discard(smaller)

    filtered_bboxes = {bbox_keys[i]: bbox_list[i] for i in to_keep}
    filtered_confidences = [confidences[i] for i in to_keep]

    return filtered_bboxes, filtered_confidences


def sort_word_bboxes(bboxes, line_threshold=15):
    """
    Sorts bounding boxes first by line, then left to right within each line.
    Uses a `line_threshold` to determine which words belong to the same line.
    """
    
    # Step 1: Sort by Y-coordinate first
    bboxes.sort(key=lambda x: x[1])

    # Step 2: Group words into lines
    lines = []
    current_line = [bboxes[0]]

    for i in range(1, len(bboxes)):
        x_min, y_min, x_max, y_max = bboxes[i]
        prev_x_min, prev_y_min, prev_x_max, prev_y_max = current_line[-1]

        # If the new box is on a new line (based on vertical threshold)
        if abs(y_min - prev_y_min) > line_threshold:
            lines.append(current_line)
            current_line = [bboxes[i]]
        else:
            current_line.append(bboxes[i])

    # Append last detected line
    if current_line:
        lines.append(current_line)

    # Step 3: Sort words within each line from left to right
    for line in lines:
        line.sort(key=lambda x: x[0])

    # Flatten list back
    sorted_bboxes = [bbox for line in lines for bbox in line]
    return sorted_bboxes