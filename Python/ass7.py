import cv2
from ultralytics import YOLO
import pyttsx3

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Open the video file
video_path = "video.mp4"
# cap = cv2.VideoCapture(video_path)

cap = cv2.VideoCapture(0)

# Flag to indicate whether to capture a single frame
capture_frame = False

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        if not capture_frame:
            # Run YOLOv8 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            if results[0].boxes:
                # Get the name of the detected object
                detected_object = results[0].names[results[0].boxes[0].cls[0].item()]
                print(f"Detected object: {detected_object}")

                # Speak the detected object name
                engine.say(f"Detected object: {detected_object}")
                engine.runAndWait()

                # Capture and save the frame when an object is detected
                cv2.imwrite("detected_frame.jpg", frame)
                capture_frame = True

        # Break the loop if 'q' is pressed or a frame has been captured
        if cv2.waitKey(1) & 0xFF == ord("q") or capture_frame:
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
