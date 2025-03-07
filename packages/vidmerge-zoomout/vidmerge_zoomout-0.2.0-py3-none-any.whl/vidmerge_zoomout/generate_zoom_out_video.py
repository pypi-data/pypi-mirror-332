import cv2
import os
import numpy as np
import tempfile
import yaml
from datetime import datetime

def generate_video(final_imgs, output_path, fps):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    file_path = os.path.join(output_path,f"{current_time}")
    H,W = final_imgs[0].shape[:2]
    out = cv2.VideoWriter(file_path, fourcc, fps, (W,H), isColor=True)
    for frame_idx in range(len(final_imgs)):
        frame = final_imgs[frame_idx]
        out.write(frame[:,:,:3])
    out.release()
    print(f"Video saved to {file_path}")


def load_png_as_numpy_array(img_path):
    """
    Load a PNG image as a numpy array.
    
    Parameters:
    img_path (str): The path to the PNG image file.
    
    Returns:
    np.ndarray: The image as a numpy array.
    """
    img = cv2.imread(img_path)
    return img

def get_fps(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError("Error: Unable to open video file.")
    else:
        # Retrieve the FPS property
        fps = cap.get(cv2.CAP_PROP_FPS)
    fps.release()
    return fps

def zoom_out_scale(frame_idx:int, raw_shape:tuple, target_shape:tuple, init_num_frames:int, zoom_out_num_frames:int):
    raw_height, raw_width = raw_shape
    target_height, target_width = target_shape
    target_scale = target_height*1.0 / raw_height
    if frame_idx < init_num_frames:
        scale = 1.0
    else:
        scale = max((target_scale**(1/(zoom_out_num_frames-init_num_frames)))**(frame_idx-init_num_frames),target_scale)
    return scale

def get_img_grids(frame_ids:np.ndarray, img_folder_path:str, video_order:np.ndarray, nrow:int, ncol:int):
    imgs = []
    for video_idx in video_order[:nrow*ncol]:
        img = load_png_as_numpy_array(os.path.join(img_folder_path, f"video_{video_idx}_frame_{frame_ids[video_idx]}.png"))
        imgs.append(img)
    
    imgs = np.array(imgs) #(nrow*ncol)*H*W*C
    imgs = imgs.reshape(nrow,ncol,*imgs.shape[1:])
    img_grid = np.concatenate([np.concatenate([imgs[i,j] for i in range(nrow)], axis=0) for j in range(ncol)],axis=1)
    return img_grid

def check_path_exist(path):
    if not os.path.exists(path):
        print(f"Path {path} does not exist!")
        exit(0)


def create_temp_folder():
    temp_folder = tempfile.mkdtemp()
    return temp_folder

def split_video_2_imgs(video_path:str, img_folder_path:str, video_idx:int):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_filename = os.path.join(img_folder_path, f"video_{video_idx}_frame_{frame_count}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    cap.release()
    return frame_count

def load_paths_from_yaml(yaml_path:str):
    with open(yaml_path, 'r') as f:
        video_paths = yaml.load(f, Loader=yaml.FullLoader)
    return video_paths

