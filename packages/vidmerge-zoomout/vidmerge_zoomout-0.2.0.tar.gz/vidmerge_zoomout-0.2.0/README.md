# vidmerge_zoomout
## Description
This package provide a tool to easily merge multiple mp4 videos in a N*N grid and adding extra zoom-out effect.
User can select which initial video to start with. The initial waiting time and zoom out time can be regulated.

## Usage
* Show all args
```sh
python -m vidmerge_zoomout -h
```
* Merge all videos from a folder
```sh
python3 -m vidmerge_zoomout --video_folder_path "/path/to/videos" --js 4 --focus_idx 1
```

* Merge all videos from a lists of video with the given order
```sh
python3 -m vidmerge_zoomout --video_list_yaml "/path/to/videos_path.yaml" --js 4 --focus_idx 1
```
`videos_path.yaml`:
```yaml
- "/path/to/video_a.mp4"
- "/path/to/video_b.mp4"
- "/path/to/video_3.mp4"
- "/path/to/video_4.mp4"
```
* Shuffle order
```sh
python3 -m vidmerge_zoomout --video_folder_path "/path/to/videos" --js 16 --focus_idx 1 --shuffle
```

* Change the timing of zoom-out and waiting
```sh
python3 -m vidmerge_zoomout --video_folder_path "/path/to/videos" --js 16 --focus_idx 1  --initial_percentage 30 --zoom_out_percentage 10 
```

* Change fps
```sh
python3 -m vidmerge_zoomout --video_folder_path "/path/to/videos" --js 16 --focus_idx 1  --initial_percentage 30 --zoom_out_percentage 10 
```


***Please make sure you have enough hard-disk***