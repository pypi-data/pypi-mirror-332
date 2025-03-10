import cv2
import numpy as np
import string

def get_optimal_font_scale(text, width, height, fontFace, thickness, margin=0.9):
    """
    Find the largest font scale such that the text (in a single line) fits
    inside the rectangle [0, width] x [0, height], given a margin.

    This function does a simple binary search to quickly find a suitable scale.
    """
    # Binary search limits
    min_scale = 0.1
    max_scale = 1000
    best_scale = min_scale

    while min_scale <= max_scale:
        mid = (min_scale + max_scale) / 2.0
        text_size, _ = cv2.getTextSize(text, fontFace, mid, thickness)
        text_width, text_height = text_size

        if (text_width <= width * margin) and (text_height <= height * margin):
            best_scale = mid  # mid works, try to see if we can go bigger
            min_scale = mid + 0.1
        else:
            max_scale = mid - 0.1

    return best_scale


def create_text_mask(frame_shape, text, font, scale, thickness):
    """
    Creates a single-channel mask of the same size as `frame_shape` (H,W,3),
    with white text on black background. The text is centered.

    White (255) indicates the 'stencil' region (where we want unblurred content).
    Black (0) is the blurred region.
    """
    height, width, _ = frame_shape
    mask = np.zeros((height, width), dtype=np.uint8)

    # Get text size
    text_size, _ = cv2.getTextSize(text, font, scale, thickness)
    text_width, text_height = text_size

    # Calculate center coordinate for text
    x = (width - text_width) // 2
    y = (height + text_height) // 2  # baseline is at y, so it centers roughly vertically

    # Put text in the mask (white letters on black background)
    cv2.putText(mask, text, (x, y), font, scale, 255, thickness, cv2.LINE_AA)

    return mask


def create_blurred_text_frame(original_frame, text):
    """
    Returns a frame where the text shape is unblurred and everything else is blurred.
    The text is sized to fill the frame.
    """
    # 1) Make a heavily blurred copy
    blurred_frame = cv2.GaussianBlur(original_frame, (51, 51), 0)

    # 2) Estimate largest font scale that fits the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 250
    height, width, _ = original_frame.shape
    optimal_scale = get_optimal_font_scale(text, width, height, font, thickness, margin=0.9)

    # 3) Create the single-channel mask
    mask = create_text_mask(original_frame.shape, text, font, optimal_scale, thickness)
    # Expand mask to 3 channels for merging
    mask_3c = cv2.merge([mask, mask, mask])

    # 4) Combine: If mask pixel = 255 => show original_frame, else blurred_frame
    #    We can do this with np.where or with direct alpha blending.
    #    mask is in [0, 255]. Let's normalize it to [0,1] for easy blending:
    mask_float = mask_3c.astype(np.float32) / 255.0

    # Result = Original * mask + Blurred * (1 - mask)
    # We'll do this in float space to avoid rounding issues:
    result = original_frame.astype(np.float32) * mask_float + \
             np.ones_like(blurred_frame.astype(np.float32)) * 125 * (1.0 - mask_float)

    # Convert back to uint8
    result = np.clip(result, 0, 255).astype(np.uint8)
    return result


def generate_blurred_text_video(input_video_path, output_video_path, fps=1):
    """
    Reads the first frame of `input_video_path` and creates a new video at `output_video_path`.
    For each letter from A to Z and index from 1..26, it generates a frame where the text
    shape is the only unblurred region. All else is blurred.
    """
    # 1. Open input video and read first frame
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Error: Could not open input video.")
        return

    ret, first_frame = cap.read()
    cap.release()
    if not ret:
        print("Error: Could not read the first frame from the video.")
        return

    # 2. Get dimensions
    height, width, _ = first_frame.shape

    # 3. Create VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID'
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # 4. For each letter A..Z, create & write one frame
    for i, letter in enumerate(string.ascii_uppercase[:26], start=1):
        text = f"{letter} {i}"
        frame = create_blurred_text_frame(first_frame, text)
        out.write(frame)

    out.release()
    print(f"Output video saved as: {output_video_path}")




if __name__ == "__main__":
    # Example usage:
    # Replace with your actual file paths
    input_video = "/gpfs/laur/data/renardm/output_dir/holiday_runs/240716/GLC-06415/240716-001/240716-001/240716-001_chunk_0.mp4"
    output_video = "blurred_output.mp4"
    
    generate_blurred_text_video(input_video, output_video, fps=1)
