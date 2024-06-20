# Driver Drowsiness Detection

This project aims to detect driver drowsiness and alert the driver using facial landmark detection and aspect ratios of the eyes and mouth. The system uses the webcam to capture video frames, detects faces, and analyzes the eyes and mouth to determine if the driver is drowsy or sleeping. Alerts are triggered using audio signals.

## Features

- Real-time drowsiness detection using webcam
- Alerts for drowsiness and sleepiness with distinct audio signals
- Uses Dlib's facial landmark predictor
- Calculates Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) to detect drowsiness

## Requirements

- Python 3.x
- OpenCV
- Dlib
- Imutils
- Numpy
- Pygame (for audio alerts)

## Usage

Run the command to start the driver drowsiness detection system: python app2.py

## Code Explanation

### Main Components

1. Euclidean Distance Calculation**: Computes the distance between two points - 

   def euclidean_distance(pointA, pointB):
       return np.linalg.norm(pointA - pointB)


2. Mouth Aspect Ratio (MAR)**: Determines if the person is yawning.

   def calculate_mouth_ratio(mouth_points):
       ...
       return mar


3. Eye Aspect Ratio (EAR): Determines if the eyes are open, drowsy, or closed - 

   def calculate_eye_ratio(eye_points):
       ...
       return ear
   ```

4. Status Determination: Decides the status of the driver (Active, Drowsy, Sleeping) - 

   def mouth_status(mar):
       ...
   def eye_status(ear):
       ...
   ```

### Main Loop

- Captures video frames from the webcam.
- Detects faces and landmarks.
- Calculates EAR and MAR.
- Updates the driver's status and triggers alerts if necessary.
- Displays the status on the video frame.

