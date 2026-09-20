import cv2
from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Could not access webcam.")
        return

    # Request a higher resolution from the webcam.
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Camera resolution: {actual_width}x{actual_height}")

    print("Running detection + tracking. Press 'q' to quit.")

    window_name = "Object Detection + Tracking - Step 3"

    # Create a normal, resizable window (not fullscreen)
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # Explicitly force fullscreen OFF, in case it was previously set
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

    # Set a fixed, reasonable size
    cv2.resizeWindow(window_name, 1280, 720)

    # Move the window slightly away from the screen edge so title bar is visible
    cv2.moveWindow(window_name, 100, 60)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        results = model.track(frame, persist=True, tracker="bytetrack.yaml", verbose=False)
        annotated_frame = results[0].plot()

        cv2.imshow(window_name, annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()