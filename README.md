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

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/driver-drowsiness-detection.git
   cd driver-drowsiness-detection
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Download the Dlib's pre-trained shape predictor model [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and place it in the project directory.

4. Ensure you have the necessary audio files for alerts and place them in the specified directory:
   - `standard-emergency-warning-signal-sews-102244.mp3`
   - `emergency-alarm-with-reverb-29431.mp3`

## Usage

Run the following command to start the driver drowsiness detection system:
```sh
python app2.py
```

## Code Explanation

### Main Components

1. **Euclidean Distance Calculation**: Computes the distance between two points - 
   ```python
   def euclidean_distance(pointA, pointB):
       return np.linalg.norm(pointA - pointB)
   ```

2. Mouth Aspect Ratio (MAR)**: Determines if the person is yawning - 
   ```python
   def calculate_mouth_ratio(mouth_points):
       ...
       return mar
   ```

3. Eye Aspect Ratio (EAR)**: Determines if the eyes are open, drowsy, or closed - 
   ```python
   def calculate_eye_ratio(eye_points):
       ...
       return ear
   ```

4. Status Determination**: Decides the status of the driver (Active, Drowsy, Sleeping) - 
   ```python
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



