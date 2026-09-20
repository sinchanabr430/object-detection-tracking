import cv2

def main():
    # 0 = default webcam. Change to a file path (e.g. "video.mp4") to test with a video file instead.
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Could not access webcam. Check camera permissions or try a different index (1, 2...).")
        return

    print("Webcam opened successfully. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        cv2.imshow("Webcam Test - Step 1", frame)

        # Press 'q' to exit the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()