from . import generate_zoom_out_video
import math
import shutil
import glob
import random
import tqdm
import argparse
from multiprocessing import Pool
import numpy as np
import os
import cv2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage="Generate a zoom out video from a list of .mp4 video files")
    parser.add_argument("--video_folder_path", type=str, default="", help="Path to the input video files")
    parser.add_argument("--video_list_yaml", type=str, default="", help="A yaml file containing the list of video file paths")
    parser.add_argument("--output_folder_path", type=str, default="", help="Path to the output folder")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second")
    parser.add_argument("--shuffle", action='store_true', help="Shuffle the order of video files")
    parser.add_argument("--initial_percentage", type=int, default=20, help="Percentage of the time to start zooming out")
    parser.add_argument("--zoom_out_percentage", type=int, default=40, help="Percentage of the time to zoom out")
    parser.add_argument("--padding_type", type=str, default="freeze", help="for video shorter than the longest video, freeze or loop")
    parser.add_argument("--focus_idx", type=int, default=1, help="The video index to start with, default is 0, from top left to bottom right.")
    parser.add_argument("--nrow", type=int, default=0, help="Number of videos in a row, 0 for automatic define the maximum number")
    parser.add_argument("--js", type=int, default=4, help="Number of processes to use")

    args = parser.parse_args()
    video_folder_path = args.video_folder_path
    video_list_yaml = args.video_list_yaml
    output_folder_path = args.output_folder_path
    fps = args.fps
    shuffle = args.shuffle
    initial_percentage = args.initial_percentage
    zoom_out_percentage = args.zoom_out_percentage
    padding_type = args.padding_type
    focus_idx = args.focus_idx
    nrow = args.nrow
    js = args.js
    
    if zoom_out_percentage<0 or initial_percentage<0 or (zoom_out_percentage+initial_percentage)>=100:
        print(f"Invalid zoom_out_percentage={zoom_out_percentage} and initial_percentage={initial_percentage}, please make sure zoom_out_percentage+initial_percentage<100")
        exit(0)
    
    if nrow<0:
        print(f"Invalid nrow={nrow}, please make sure nrow is positive")
        exit(0)

    if focus_idx<0 :
        print(f"Invalid focus_idx={focus_idx}")
        exit(0)

    
    if padding_type not in ["freeze", "loop"]:
        print(f"Invalid padding_type={padding_type}, please make sure padding_type is either 'freeze' or 'loop'")
        exit(0)

    if fps<0:
        print(f"Invalid fps={fps}, please make sure fps is positive")
        exit(0)

    video_paths = []
    if video_folder_path=="" and video_list_yaml=="":
        print("Please provide either video_list_yaml or video_folder_path")
        exit(0)
    elif video_folder_path!="":
        generate_zoom_out_video.check_path_exist(video_folder_path)
        video_paths =  glob.glob(os.path.join(video_folder_path, "*.mp4"))
    else:
        generate_zoom_out_video.check_path_exist(video_list_yaml)
        video_paths = generate_zoom_out_video.load_paths_from_yaml(video_list_yaml)

    img_folder_path = generate_zoom_out_video.create_temp_folder()

    try:
        # Shuffle the list of video files
        if shuffle:
            random.shuffle(video_paths)

        if fps == 0:
            fps = generate_zoom_out_video.get_fps(video_paths[0])

        # Split the video files into images and store them in the temp folder
        frame_counts = []
        def process_video(video_idx):
            video_path = video_paths[video_idx]
            frame_count = generate_zoom_out_video.split_video_2_imgs(video_path=video_path, img_folder_path=img_folder_path, video_idx=video_idx)
            return frame_count
        
        print(f"Pre-processing {len(video_paths)} videos with {js} processes")
        with Pool(processes=js) as pool:
            frame_counts = list(tqdm.tqdm(pool.imap(process_video, range(len(video_paths))), total=len(video_paths)))

        frame_counts = np.array(frame_counts)
        valid_video_ids = np.argwhere(frame_counts!=0).flatten()
        valid_frame_counts = frame_counts[valid_video_ids]
        if nrow==0:
            nrow = int(np.sqrt(len(valid_video_ids)))
        else:
            if nrow*nrow>len(valid_video_ids):
                print(f"nrow*nrow={nrow*nrow} is larger than the number of valid videos {len(valid_video_ids)}, please make sure all video clips are readable, or decrease nrow.")
                exit(0)


        if nrow<=1:
            print(f"Recommend to have more than 9 valid videos for better visualization, but only {len(valid_video_ids)} valid videos are found.")

        if focus_idx<0 or focus_idx>=nrow*nrow:
            print(f"Invalid focus_idx={focus_idx}, please make sure focus_idx is within the range of {nrow}*{nrow}")
            exit(0)

        chosen_video_ids = valid_video_ids[:nrow*nrow]


        # Create the output directory if it doesn't exist
        if output_folder_path == "":
            output_folder_path = os.path.join(os.getcwd(), "output")
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
        
        # Select videos to include in the final video
        max_frame_count = max(valid_frame_counts)
        final_imgs = {idx:None for idx in range(max_frame_count)} # For multi processing

        def rescale_imgs(frame_idx):
            if padding_type == "loop":
                frame_ids = frame_idx%valid_frame_counts
            elif padding_type == "freeze":
                frame_ids = np.minimum(frame_idx, valid_frame_counts-1)
            else:
                print(f"Padding type {padding_type} is not supported!")
                exit(0)
            img = generate_zoom_out_video.get_img_grids(frame_ids=frame_ids, img_folder_path=img_folder_path, video_order=valid_video_ids, nrow=nrow, ncol=nrow)
            H,W = img.shape[0]//nrow, img.shape[1]//nrow

            scale = generate_zoom_out_video.zoom_out_scale(frame_idx, (H*nrow, W*nrow), (H, W), init_num_frames=int(initial_percentage/100*max_frame_count), zoom_out_num_frames=int((zoom_out_percentage+initial_percentage)/100*max_frame_count))
            h,w = math.ceil(scale * H * nrow), math.ceil(scale * W * nrow)
            img = cv2.resize(img, (w,h))

            # Calculate the coordinates to crop the image to the middle h,w square
            focus_x,focus_y = (focus_idx%nrow)*W, (focus_idx//nrow)*H
            start_x = int((1.-(1.-scale)/(1.-1./nrow))*focus_x) if nrow>1 else 0
            start_y = int((1.-(1.-scale)/(1.-1./nrow))*focus_y)if nrow>1 else 0
            end_x = start_x + W
            end_y = start_y + H

            # Crop the image
            img = img[start_y:end_y, start_x:end_x]
            return img
        
        print(f"Generating the final video with {js} processes")
        with Pool(processes=js) as pool:
            final_imgs = list(tqdm.tqdm(pool.imap(rescale_imgs, range(max_frame_count)), total=max_frame_count))
        
        generate_zoom_out_video.generate_video(final_imgs, output_folder_path, fps)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up the temporary folder
        shutil.rmtree(img_folder_path)
