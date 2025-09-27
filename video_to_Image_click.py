import cv2
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    # Create an output directory if it doesn't exist
    output_folder = "output_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Use a file dialog to select the video file
    Tk().withdraw()  # Hide the root tkinter window
    video_path = askopenfilename(
        title="Select a video file",
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
    )

    if not video_path:
        print("No file selected. Exiting.")
        return

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Unable to open the video file.")
        return

    print("Press 's' to save a frame as an image, or 'q' to quit.")

    frame_count = 93

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        if not ret:
            print("End of video or cannot read the video file.")
            break

        # Display the frame
        cv2.imshow("Video", frame)

        # Wait for a key press with a delay of 2000 ms (2 seconds)
        key = cv2.waitKey(100) & 0xFF

        if key == ord('s'):
            # Save the current frame as an image
            output_path = os.path.join(output_folder, f"{frame_count}.jpg")
            cv2.imwrite(output_path, frame)
            print(f"Saved: {output_path}")
            frame_count += 1

        elif key == ord('q'):
            # Quit the loop
            print("Exiting...")
            break

    # Release the video capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
