````markdown
# Video ⇄ Image Conversion Toolkit 🖼️🎞️

> Lightweight collection of Python scripts to convert videos to images (frames), capture frames in real-time, rename & batch-convert image formats, and perform simple image utilities — organized for fast experimentation and automation.

---

## Quick overview
This repository contains a set of small, focused Python scripts that help you extract frames from videos, grab images at intervals or on click, convert file formats, rename files, and shuffle images for experiments or dataset preparation.

**Key capabilities**
- Extract every frame or one frame-per-second from a video  
- Extract frames on mouse click events (interactive)  
- Real-time capture from a camera on click  
- Batch convert `.jpg` → `.png`  
- Rename and shuffle image files for dataset prep

(Files & purpose inferred from the repository listing.) :contentReference[oaicite:0]{index=0}

---

# Contents
- `video_to_Image_click.py` — extract frames from a video when you click (interactive frame capture)
- `Image_frame_by_frame.py` — step through a video frame-by-frame and save frames
- `image_every_second.py` — extract one image per second from a video (time-based sampling)
- `real_time_by_click.py` — capture stills from a live camera feed on mouse/keyboard click
- `jpg to png.py` — batch-convert JPG images to PNG format
- `rename.py` — bulk rename images (useful to normalize dataset filenames)
- `suffleing image.py` — shuffle or reorder images (for randomization/data split)
- `.idea/` — PyCharm/IDE project files (ignore in commits or add to `.gitignore`)

---

# Requirements
Create an isolated environment and install dependencies (typical):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install opencv-python pillow numpy tqdm
````

> Some scripts may use additional built-in modules — open the script to confirm exact imports.

---

# Usage examples (typical)

Below are example command patterns. Scripts in this repo are simple and may require editing the top of the file to set input/output paths or minimal CLI arguments — open the script to confirm exact parameter names.

**Extract one frame per second**

```bash
python image_every_second.py /path/to/video.mp4 /path/to/output_dir
# or edit input/output inside the script and run:
python image_every_second.py
```

**Frame-by-frame extraction**

```bash
python Image_frame_by_frame.py /path/to/video.mp4 /path/to/output_dir
```

**Interactive extract on click (video)**

```bash
python video_to_Image_click.py /path/to/video.mp4 /path/to/output_dir
# Play the video, click to save the current frame
```

**Capture from camera on click (real-time)**

```bash
python real_time_by_click.py  # may pick camera index 0 by default
# Click or press specified key to save a snapshot
```

**Batch JPG → PNG conversion**

```bash
python "jpg to png.py" /path/to/input_jpgs /path/to/output_pngs
# or modify the script with source/destination folders
```

**Bulk rename images**

```bash
python rename.py /path/to/images prefix_
# renames files to prefix_0001.ext, prefix_0002.ext, ...
```

**Shuffle / reorder images**

```bash
python "suffleing image.py" /path/to/images
# script will randomize order and optionally write mapping or rename files
```

> If a script lacks CLI parsing, open it and adapt the input/output variables at the top, or add `argparse` for a small improvement.

---

# Recommended improvements (quick wins)

1. Add a top-level `README.md` (this file) and a short `USAGE.md` with examples for each script.
2. Standardize CLI using `argparse` for each script (input, output, fps, step, camera-index, format).
3. Add a `requirements.txt` (or `pyproject.toml`) with pinned versions.
4. Add tests or a small demo video in `examples/` for reproducibility.
5. Add a LICENSE (MIT recommended) and `.gitignore` excluding `.idea/` and typical Python artifacts.

---

# Contributing

Contributions are welcome! A suggested workflow:

1. Fork the repository
2. Create a topic branch (`feature/cli-args` or `fix/typo`)
3. Add tests or usage examples
4. Open a pull request with a clear description of changes

Please include small, focused PRs (e.g., add `argparse` to a single script, or add `requirements.txt`).

---

# License

No license file detected in the repository. If you want others to use your code freely, consider adding an [MIT License](https://opensource.org/licenses/MIT) or another open-source license. Add a `LICENSE` file at project root.

---

# Contact / Author

Repository owner: **masumb2k2** (see GitHub profile for contact and more projects). ([GitHub][1])

---

## Example: Minimal `requirements.txt`

```
opencv-python
numpy
Pillow
tqdm
```

