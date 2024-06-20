import cv2
import dlib
import numpy as np
from imutils import face_utils
from pygame import mixer

mixer.init()

sleep = "/Users/AryanaGhugharawala1/Downloads/standard-emergency-warning-signal-sews-102244.mp3"
drowsy = "/Users/AryanaGhugharawala1/Downloads/emergency-alarm-with-reverb-29431.mp3"
# Initialize webcam
cap = cv2.VideoCapture(0)

# Load the facial landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/Users/AryanaGhugharawala1/Desktop/new1/shape_predictor_68_face_landmarks.dat")

# Define color for text and shapes
color = (0, 0, 0)

def euclidean_distance(pointA, pointB):
    return np.linalg.norm(pointA - pointB)  # Calculate Euclidean distance between two points.

def calculate_mouth_ratio(mouth_points):
    q1, q2, q3, q4, q5, q6 = mouth_points[12], mouth_points[14], mouth_points[16], mouth_points[18], mouth_points[13], mouth_points[19]
    q7, q8, q9, q10 = mouth_points[0], mouth_points[6], mouth_points[3], mouth_points[9]

    vertical_1 = euclidean_distance(q2, q8) # Calculate vertical distances.
    vertical_2 = euclidean_distance(q3, q7)

    horizontal = euclidean_distance(q1, q4)  # Calculate the horizontal distance

    mar = (vertical_1 + vertical_2) / (2.0 * horizontal)  # mouth aspect ratio

    return mar

def calculate_eye_ratio(eye_points):
    # Calculate the blink ratio for a given set of eye landmarks.
    p1, p2, p3, p4, p5, p6 = eye_points

    vertical_1 = euclidean_distance(p2, p6)  # Calculate the vertical distances
    vertical_2 = euclidean_distance(p3, p5)

    horizontal = euclidean_distance(p1, p4)  # Calculate the horizontal distance

    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)  # Calculate the eye aspect ratio (EAR)
    return ear

def mouth_status(mar):
    # Determine if the person is yawning based on the MAR value
    if mar > 0.6:
        return 1  # Yawning
    else:
        return 0  # Not yawning

def eye_status(ear):
    # Determine the status of the eyes based on the EAR value
    if ear > 0.25:
        return 2  # Eyes wide open
    elif 0.21 < ear <= 0.25:
        return 1  # Drowsy
    else:
        return 0  # Eyes closed

# Counters for different conditions
sleeping_count = 0
drowsy_count = 0
active_count = 0
status = "Active"


while True:
    ret, frame = cap.read() # video frame
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_frame)

    for face in faces:
        landmarks = predictor(gray_frame, face)
        landmarks_np = face_utils.shape_to_np(landmarks)

        # Eye landmarks
        left_eye = landmarks_np[36:42]
        right_eye = landmarks_np[42:48]
        mouth = landmarks_np[48:68]

        # Calculating blink ratios
        left_eye_status = eye_status(calculate_eye_ratio(left_eye))
        right_eye_status = eye_status(calculate_eye_ratio(right_eye))

        # Calculating mouth status
        mouth_stat = mouth_status(calculate_mouth_ratio(mouth))

        # Determine the conditions based on eye state and mouth state
        if left_eye_status == 0 or right_eye_status == 0:
            
            sleeping_count += 1
            drowsy_count = 0
            active_count = 0
           
            if sleeping_count > 10:
               
                status = "Sleeping!!"
                color = (0, 0, 255)
                mixer.music.load(sleep)
                mixer.music.play()

        elif left_eye_status == 1 or right_eye_status == 1 or mouth_stat == 1:
            
            sleeping_count = 0
            drowsy_count += 1
            active_count = 0
           
            if drowsy_count > 10:
                
                status = "Drowsy!!"
                color = (0, 255, 255)
                mixer.music.load(drowsy)
                mixer.music.play()

        else:
            
            sleeping_count = 0
            drowsy_count = 0
            active_count += 1
            
            if active_count > 6:
                status = "Active!!"
                color = (0, 255, 0)

       
        x1, y1 = face.left(), face.top() # counting faces from the frame
        x2, y2 = face.right(), face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) # forming rectangle around the found face

        # Draw landmarks
        for (x, y) in landmarks_np:
            cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)

    # Display the status on the frame
    cv2.putText(frame, status, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    # Show the frames
    cv2.imshow("Frame", frame)

    # Break loop on 'ESC' key press
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
