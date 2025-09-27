import cv2

import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
# Create output directory if not exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
Tk().withdraw()  # Hide the root tkinter window
video_path = askopenfilename(
    title="Select a video file",
    filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
)
# Open video capture (0 for webcam, or provide video file path)
cap = cv2.VideoCapture(video_path)  # Change '0' to 'video.mp4' for a file

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_rate = int(cap.get(cv2.CAP_PROP_FPS))  # Get the frame rate
frame_count = 0
image_count = 1485

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_rate == 0:  # Capture image every second
        img_path = os.path.join(output_dir, f"{image_count}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"Saved: {img_path}")
        image_count += 1

    frame_count += 1

    # Display the video (optional)
    cv2.imshow('Video Feed', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
