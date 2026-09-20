import cv2
from ultralytics import YOLO

def main():
    # Loads YOLOv8's small pretrained model (auto-downloads ~6MB on first run).
    # Trained on the COCO dataset: 80 common object classes (person, car, phone, etc.)
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Could not access webcam.")
        return

    print("Running detection. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Run YOLO detection on this frame
        results = model(frame, verbose=False)

        # results[0].plot() draws boxes, labels, and confidence scores automatically
        annotated_frame = results[0].plot()

        cv2.imshow("Object Detection - Step 2", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()