# Face-Recognition
Facial recognition to alert unauthorized access based on Face Recognition using Python and OpenCv


# Code Requirements
To set up the libraries required for face recognition through Python:

1. Go to the terminal and download the dlib library:
   
pip install dlib

The dlib library is a C++ toolkit that features machine learning tools and algorithms. It is important to install it to use the face_recognition library.

2. Use the following command to install the face_recognition library:
   
pip install face recognition

4. Use the following command to download the OpenCV library:
   
pip install opencv

The OpenCV library will come in handy for pre-processing steps.

# What steps you have to follow??
Download my Repository
Create a Image folder in a project.
Open a UAS.py and change the all paths with your system path
Run UAS.py.

![image](https://github.com/Priyanka291988/Face-Recognition/assets/141348892/085e254b-f83d-4fb6-99a2-a3cadfe1677e)

**Explanation for the Presentation:**
1. **Importing Libraries**: We begin by importing the necessary libraries for our face recognition system. `face_recognition` library is used for face detection and recognition, `cv2` (OpenCV) for video capturing and processing, and `winsound` for playing the alert sound on Windows systems.
2. **Known Face Encodings and Names**: We load the images of known individuals (in this case, Aishwarya, Priyanka, Modi Ji, and Salman) and extract their face encodings. These encodings will be used for comparison during face recognition.
3. Alarm Sound: We specify the path for the alarm sound file (`WOWO.wav`) and define a function (`play_alarm_sound()`) to play the sound when an unknown face is detected.
4. **Video Capture and Processing**: We initiate video capture from the camera using `cv2.VideoCapture(0)`. The loop captures frames from the camera feed, detects faces, and compares them with the known face encodings.
5.**Face Recognition and Display**: For each frame, the system finds face locations and encodings. It then compares the encodings with the known face encodings to recognize the faces. If a recognized face matches any of the known faces, their name is displayed along with a green rectangle around their face.
6. **Alarm and Red Rectangle**: If no face is recognized or an unknown face is detected, the alarm sound plays, and the system displays "Unknown" with a red rectangle around the face to indicate that the person is not recognized.
7. **Displaying the Processed Frame**: The processed frame with detected faces and names is displayed in a window titled "Face Recognition."

8. **Exiting the Loop**: The program continues until the user presses 'q', at which point the video capture object is released, and the window is closed.
By running this code, we can create a simple face recognition system that generates an alert sound when an unknown face is detected and displays recognized faces with their names. 

# Project Structure
This code took two images of Modiji and used the compare_faces method to return True since both images had the same face. 

The model converts every image it gets into a numerical encoding. First, the face_encodings method returns an encoding of the input image. Then, the compare_faces method compares the encodings through a distance parameter to see if there is a match. Then, the encoding with the least distance gets selected since it’s the closest match. After getting the match, the image’s title is retrieved using the image’s index in the list. It will start alert on unknown face to make people alert of unauthorized access
