""" Utiltiy functions to manipulate video data. """

import os
from pathlib import Path
import subprocess
from typing import Optional, Dict, Tuple
import click
import decord
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import numpy as np
from tqdm import tqdm
from PIL import Image

def cut_video(input_file: str, start: float, end: Optional[float] = None, time: Optional[float] = None, output: Optional[str] = None) -> str:
    """
    Cut a video file based on start time and either end time or duration.

    Args:
        input_file (str): Path to the input video file.
        start (float): Start time for cutting in seconds.
        end (Optional[float]): End time for cutting in seconds. Default is None.
        time (Optional[float]): Duration for cutting in seconds. Default is None.
        output (Optional[str]): Path to the output video file. If None, a default name will be generated.

    Returns:
        str: Path to the output video file.

    Raises:
        ValueError: If neither end nor time is provided.

    Note:
        Either 'end' or 'time' must be provided, but not both. If both are provided, 'end' takes precedence.
    """
    if end is not None:
        duration = end - start
    elif time is not None:
        duration = time
    else:
        raise ValueError("Either end or time must be provided.")

    input_name, input_ext = os.path.splitext(input_file)
    if not output:
        output = f"{input_name}.cut-{start}-{start+duration}{input_ext}"

    cmd = [
        'ffmpeg',
        '-ss', str(start),
        '-i', input_file,
        '-t', str(duration),
        '-c', 'copy',
        output
    ]
    subprocess.run(cmd, check=True)
    return output


def crop_video(input_file: str, x: int, y: int, dx: int, dy: int, output: Optional[str] = None) -> str:
    """
    Crop a video file based on specified coordinates and dimensions.

    Args:
        input_file (str): Path to the input video file.
        x (int): X-coordinate of the top-left corner of the crop area.
        y (int): Y-coordinate of the top-left corner of the crop area.
        dx (int): Width of the crop area.
        dy (int): Height of the crop area.
        output (Optional[str]): Path to the output video file. If None, a default name will be generated.

    Returns:
        str: Path to the output video file.

    Note:
        This function uses FFmpeg to crop the video. The audio stream is copied without modification.
    """
    input_name, input_ext = os.path.splitext(input_file)
    if not output:
        output = f"{input_name}.crop-{x}-{y}-{dx}-{dy}{input_ext}"

    crop_filter = f"crop={dx}:{dy}:{x}:{y}"

    cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vf', crop_filter,
        '-c:a', 'copy',
        output
    ]
    subprocess.run(cmd, check=True)
    return output


def cut_and_crop_video(input_file: str, cut_args: Optional[Dict[str, float]], crop_args: Optional[Dict[str, int]], output: Optional[str] = None) -> str:
    """
    Cut and/or crop a video file based on provided arguments.

    Args:
        input_file (str): Path to the input video file.
        cut_args (Optional[Dict[str, float]]): Dictionary containing cutting parameters:
            - 'start': Start time in seconds.
            - 'end': End time in seconds (optional).
            - 'time': Duration in seconds (optional).
        crop_args (Optional[Dict[str, int]]): Dictionary containing cropping parameters:
            - 'x': X-coordinate of the top-left corner of the crop area.
            - 'y': Y-coordinate of the top-left corner of the crop area.
            - 'dx': Width of the crop area.
            - 'dy': Height of the crop area.
        output (Optional[str]): Path to the output video file. If None, a default name will be generated.

    Returns:
        str: Path to the processed video file.

    Note:
        This function applies cutting first (if cut_args is provided) and then cropping (if crop_args is provided).
        The intermediate file from cutting is used as input for cropping if both operations are performed.
    """
    temp_file = input_file
    if cut_args:
        if crop_args:
            output_ = f"{Path(input_file).stem}.cut{Path(input_file).suffix}"
        else:
            output_ = output
        temp_file = cut_video(input_file, cut_args['start'], cut_args.get('end'), cut_args.get('time'), output_)
    if crop_args:
        temp_file = crop_video(temp_file, crop_args['x'], crop_args['y'], crop_args['dx'], crop_args['dy'], output)
        if cut_args:
            os.remove(output_)
    
    print(f"\nVideo has been processed and stored at: {temp_file}")
    return temp_file


class InteractiveCropper:
    """
    A class for interactive video frame cropping using matplotlib.

    Attributes:
        frame (numpy.ndarray): The video frame to be displayed and cropped.
        fig (matplotlib.figure.Figure): The matplotlib figure object.
        ax (matplotlib.axes.Axes): The matplotlib axes object.
        rect (matplotlib.patches.Rectangle): The rectangle selector object.
        x1, y1, x2, y2 (int): Coordinates of the selected region.
        rs (matplotlib.widgets.RectangleSelector): The RectangleSelector widget.

    Methods:
        onselect(eclick, erelease): Callback function for the RectangleSelector.
        get_crop_params(): Returns the cropping parameters based on the selected region.

    Note:
        This class creates an interactive matplotlib window where the user can select a region to crop.
        The window closes automatically after selection, and the crop parameters can be retrieved using get_crop_params().
    """

    def __init__(self, frame):
        self.frame = frame
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(frame)
        self.rect = None
        self.x1 = self.y1 = self.x2 = self.y2 = None
        
        self.fig.suptitle("Select box to crop, then close window to proceed\nClose without selecting to skip cropping", fontsize=10)
        
        self.rs = RectangleSelector(self.ax, self.onselect, 
                                    useblit=True, button=[1], minspanx=5, minspany=5, 
                                    spancoords='pixels', interactive=True)
        plt.show()

    def onselect(self, eclick, erelease):
        """Callback function for the RectangleSelector."""
        self.x1, self.y1 = int(eclick.xdata), int(eclick.ydata)
        self.x2, self.y2 = int(erelease.xdata), int(erelease.ydata)
        print(f"Selected region: ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})")

    def get_crop_params(self) -> Tuple[Optional[int], Optional[int], Optional[int], Optional[int]]:
        """Returns the cropping parameters based on the selected region."""
        if self.x1 is None or self.x2 is None or self.y1 is None or self.y2 is None:
            print("No region selected. Skipping cropping.")
            return None, None, None, None
        x = min(self.x1, self.x2)
        y = min(self.y1, self.y2)
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)
        return x, y, dx, dy


def cut_or_crop_video_interactive(input_file: str, start: Optional[float] = None, end: Optional[float] = None, 
                                  time: Optional[float] = None, output: Optional[str] = None, 
                                  no_interactive: bool = False, x: Optional[int] = None, y: Optional[int] = None, 
                                  dx: Optional[int] = None, dy: Optional[int] = None) -> str:
    """
    Process a video file based on given options for cutting and cropping, with optional interactive cropping.

    Args:
        input_file (str): Path to the input video file.
        start (Optional[float]): Start time for cutting in seconds. Default is None.
        end (Optional[float]): End time for cutting in seconds. Default is None.
        time (Optional[float]): Duration for cutting in seconds. Default is None.
        output (Optional[str]): Path to the output video file. Default is None.
        no_interactive (bool): If True, disable interactive cropping. Default is False.
        x (Optional[int]): x coordinate for cropping. Default is None.
        y (Optional[int]): y coordinate for cropping. Default is None.
        dx (Optional[int]): Width of the crop box. Default is None.
        dy (Optional[int]): Height of the crop box. Default is None.

    Returns:
        str: Path to the processed video file.

    Note:
        If interactive cropping is not disabled and crop parameters are not provided,
        this function will open an interactive window for the user to select the crop region.
        If all crop parameters (x, y, dx, dy) are provided, interactive mode is automatically disabled.
    """
    cut_args = None
    if start is not None:
        cut_args = {'start': start, 'end': end, 'time': time}

    # Set no_interactive to True if all crop parameters are provided
    if x is not None and y is not None and dx is not None and dy is not None:
        no_interactive = True

    if not no_interactive:
        vr = decord.VideoReader(input_file)
        frame = vr[0].asnumpy()
        cropper = InteractiveCropper(frame)
        x, y, dx, dy = cropper.get_crop_params()

    crop_args = None
    if x is not None and y is not None and dx is not None and dy is not None:
        crop_args = {'x': x, 'y': y, 'dx': dx, 'dy': dy}

    return cut_and_crop_video(input_file, cut_args, crop_args, output)


import cv2
from decord import VideoReader

def blur_video_frames(input_path, output_path, blur_frames=40):
    """
    Blurs frames at the beginning, the middle and the end of the video.

    Parameters:
    input_path (str): Path to the input video file.
    output_path (str): Path to save the output video file.
    blur_frames (int): Number of frames to blur at the beginning, middle, and end of the video. Default is 40.

    Returns:
    None
    """
    # Load the video using decord
    vr = VideoReader(input_path)
    frame_count = len(vr)
    
    # Get frame indices to blur
    first_frames = range(blur_frames)
    middle_start = (frame_count // 2) - (blur_frames // 2)
    middle_frames = range(middle_start, middle_start + blur_frames)
    last_frames = range(frame_count - blur_frames, frame_count)
    
    # Initialize video writer
    width, height = vr[0].shape[1], vr[0].shape[0]
    fps = vr.get_avg_fps()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # Process and write frames
    for i in range(frame_count):
        frame = vr[i].asnumpy()
        if i in first_frames or i in middle_frames or i in last_frames:
            frame = cv2.GaussianBlur(frame, (99, 99), 15)
        out.write(frame[..., ::-1])
    
    # Release the video writer
    out.release()
	
def extract_frames_to_npy(input_video_path, output_dir):
    """
    Extract frames from a video and save them as .npy files.

    Parameters:
    input_video_path (str): Path to the input video file.
    output_dir (str): Directory where the frame .npy files will be saved.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the video
    vr = decord.VideoReader(input_video_path)
    
    for k in tqdm(range(len(vr)), desc="Extracting frames"):
        frame = vr[k].asnumpy()
        output_path = os.path.join(output_dir, f'frame_{k:04d}.npy')
        np.save(output_path, frame)

    print(f"All frames have been saved in {output_dir}")
	

def create_video_from_images(image_folder, video_path, image_format, fps=30):
    """
    Create a video from a sequence of images in the specified format.

    Parameters:
    image_folder (str): Path to the directory containing images.
    video_path (str): Desired output video file path.
    image_format (str): Format of the input images (e.g., 'tif', 'jpg', 'png').
    fps (int): Frames per second for the output video. Default is 30.
    """
    # Get the list of all files in the directory with the specified format
    images = [img for img in os.listdir(image_folder) if img.endswith(f'.{image_format}')]
    images.sort()  # Ensure the images are in order

    if not images:
        print(f"No .{image_format} images found in the specified directory.")
        return

    # Read the first image to get the dimensions
    first_image_path = os.path.join(image_folder, images[0])
    first_image = cv2.imread(first_image_path, cv2.IMREAD_UNCHANGED)
    if first_image is None:
        print(f"Error reading the first image: {first_image_path}")
        return
    
    height, width = first_image.shape[:2]

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

    for image in tqdm(images, total=len(images)):
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

        if img is None:
            print(f"Error reading image {img_path}")
            continue

        # Check if the image needs to be converted to 3 channels (color)
        if len(img.shape) == 2:  # grayscale image
            img = cv2.cvtColor((img * 255).astype('uint8'), cv2.COLOR_GRAY2BGR)
        video.write(img)

    # Release the VideoWriter object
    video.release()

    print(f"Video saved at {video_path}")
	

def convert_bgr_to_rgb(input_video_path, output_video_path):
    """
    Convert a BGR video to RGB and save it to a new file.

    Parameters:
        input_video_path (str): Path to the input video file in BGR format.
        output_video_path (str): Path to the output video file in RGB format.
    """
    # Open the input video
    cap = cv2.VideoCapture(input_video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 format
    
    # Define the codec and create VideoWriter object
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    progress_bar = tqdm(total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), desc='Converting')
    while True:
        progress_bar.update(1)
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Write the frame
        out.write(rgb_frame)
    
    # Release everything if job is finished
    cap.release()
    out.release()


def save_frame(video_path, frame_number, output_image_path):
    """
    Extracts a frame from a video and saves it as an image.

    :param video_path: Path to the video file.
    :param frame_number: Frame number to extract.
    :param output_image_path: Path to save the extracted frame image.
    """
    # Use decord to read the video
    decord.bridge.set_bridge('native')
    vr = decord.VideoReader(video_path)

    # Check if the frame number is within the valid range
    if frame_number < 0 or frame_number >= len(vr):
        click.echo(f"Error: Frame number {frame_number} is out of range")
        return
    if output_image_path is not None:
        assert Path(output_image_path).suffix in ['.jpg', '.jpeg', '.png'], "Output image must be in .jpg, .jpeg, or .png format"
        assert Path(output_image_path).parent.exists(), "Output directory does not exist"
    else:
        output_image_path = str(Path(video_path).with_suffix(f'.frame_{frame_number}.jpg'))
    # Get the frame
    frame = vr[frame_number].asnumpy()

    # Convert the frame to an image
    image = Image.fromarray(frame)

    # Save the image
    image.save(output_image_path)

    # Print the output image path
    click.echo(f"Frame {frame_number} saved as {output_image_path}")
