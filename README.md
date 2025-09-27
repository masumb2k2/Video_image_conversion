

# Video ↔ Image Conversion Toolkit 🎞️➡️🖼️

> A compact collection of Python utilities for extracting frames from videos, capturing frames in real time, and doing simple image batch tasks.
> Designed to be minimal, easy to use, and ready to integrate into larger computer-vision or media-processing workflows.

## Features ✨

* Extract every frame from a video (frame-by-frame).
* Extract one image per second from a video.
* Extract frames on mouse clicks (interactive).
* Capture images from real-time webcam input on click.
* Batch operations: JPG→PNG conversion, renaming, shuffling images.
* Lightweight, single-file scripts — easy to read and customize.

---

## Files & Scripts (what’s included)

* `Image_frame_by_frame.py` — Extract all frames from a video file.
* `image_every_second.py` — Save one frame per second from a video.
* `video_to_Image_click.py` — Extract frames when you click on the video window.
* `real_time_by_click.py` — Capture frames from a live camera feed when you click.
* `jpg to png.py` — Convert `.jpg` images to `.png` in bulk.
* `rename.py` — Bulk rename images using a simple numeric or pattern-based scheme.
* `suffleing image.py` — Shuffle images (useful for dataset randomization).
* `.idea/` — IDE settings folder. ([GitHub][1])

> Note: I pulled the repository structure and file list from the project page to ensure the README reflects the repo contents. ([GitHub][1])

---

## Requirements

* Python 3.8+ recommended
* Common Python packages (install via `pip`):

  * `opencv-python` (cv2)
  * `numpy`
  * `Pillow` (PIL) — required for image format conversion
  * `argparse` (standard lib — often used for CLI parameters)

Install quickly:

```bash
python -m pip install --upgrade pip
pip install opencv-python numpy Pillow
```

---

## Example usage

> The scripts are intentionally simple. The examples below are illustrative. If a script has command-line flags, use those; otherwise adapt the examples by editing the script’s variables near the top.

### 1. Extract every frame

```bash
python Image_frame_by_frame.py --video path/to/video.mp4 --outdir ./frames
```

Saves every frame into `./frames/` (e.g. `frame_00001.png`).

### 2. Extract one image per second

```bash
python image_every_second.py --video path/to/video.mp4 --outdir ./per_second_frames
```

Useful for sampling long videos.

### 3. Extract frames by clicking (interactive)

```bash
python video_to_Image_click.py --video path/to/video.mp4 --outdir ./clicked_frames
```

Play the video and click the frame to save it.

### 4. Real-time capture by click (webcam)

```bash
python real_time_by_click.py --camera 0 --outdir ./webcam_frames
```

Open a live camera window, click to capture frames.

### 5. Convert JPG → PNG in a folder

```bash
python "jpg to png.py" --input_dir ./jpgs --output_dir ./pngs
```

### 6. Bulk rename images

```bash
python rename.py --dir ./images --pattern "img_{:04d}.jpg"
```

### 7. Shuffle images (dataset randomization)

```bash
python "suffleing image.py" --dir ./images --seed 42
```

---

## Quick tips & best practices

* Use virtual environments:

  ```bash
  python -m venv venv
  source venv/bin/activate   # macOS / Linux
  venv\Scripts\activate.bat  # Windows
  ```
* For long videos, extract at lower frame rate (e.g., 1 fps) to reduce storage usage.
* If you need different image formats, use `Pillow` to convert or save with different extensions.
* Add `--overwrite` or timestamp suffix logic if scripts save files that might collide.

---

## Suggested improvements (ideas)

* Add a unified CLI wrapper (e.g., `video_tool.py --mode=every_frame`) to avoid separate scripts.
* Add a requirements.txt and a small `setup.py` or `pyproject.toml`.
* Add tests for the conversion & rename logic.
* Add a `--dry-run` mode to preview file changes (rename/convert/shuffle) before committing.

---

## Troubleshooting

* **Blank frames or no video read**: Ensure `opencv-python` supports your codec. Use `ffmpeg` to re-encode the video if needed:

  ```bash
  ffmpeg -i input.mp4 -vcodec libx264 -acodec aac fixed_input.mp4
  ```
* **Permission errors writing files**: Check folder write permissions and ensure outdir exists or is created by the script.
* **Different file extensions or uppercase extensions**: Scripts may be case-sensitive in filename matches (`.JPG` vs `.jpg`). Normalize file extensions before batch actions.

---

## Contributing

Contributions welcome! A simple workflow:

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Add/modify code and update this README if needed
4. Open a pull request with a short description

---

## License

No license file was found in the repository. If you want others to reuse your work, consider adding an open-source license (MIT, Apache-2.0, or BSD are common choices). If you’d like, I can prepare an `MIT` license text for you to add. ([GitHub][1])

---

## Contact / Author

If you want this README adapted in style or to include code snippets taken directly from each script, tell me which scripts you want sample usage for and I’ll extract exact flags & improve the examples.

---


