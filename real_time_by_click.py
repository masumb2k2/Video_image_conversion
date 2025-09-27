import cv2
import os

def main():
    # Create an output directory if it doesn't exist
    output_folder = "output_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to open the webcam.")
        return

    print("Press 's' to save a frame as an image, or 'q' to quit.")

    frame_count = 1

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Cannot read from webcam.")
            break

        # Display the frame
        cv2.imshow("Webcam", frame)

        # Wait for a key press
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
