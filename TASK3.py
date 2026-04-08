import cv2

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Load video
cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw face boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    # Count faces
    face_count = len(faces)

    # Show count
    cv2.putText(frame, f"Faces: {face_count}", (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0,255,0), 2)

    # Show message
    if face_count > 0:
        cv2.putText(frame, "Face Detected!", (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255,255,0), 2)

    # Add scanning line effect 😎
    h, w, _ = frame.shape
    cv2.line(frame, (0, h//2), (w, h//2), (0,255,255), 2)

    # Show video
    cv2.imshow("Face Detection AI", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()