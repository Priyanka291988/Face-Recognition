# Face-Recognition
Facial recognition to alert unauthorized access based on Face Recognition using Python and OpenCv.
Firstly, face recognition enables security alerts on unknown faces, notifying homeowners of potential intruders through alert sounds. Secondly, it greets recognized family members by name, adding a personalized touch to the home environment. Additionally, home access control becomes seamless as the system automatically unlocks doors for authorized users. 
Moreover, the technology ensures child and elderly safety by monitoring their movements and triggering alerts when needed. Integration with other smart devices allows for optimized energy consumption and a more user-friendly experience. 


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
import face_recognition
import cv2
import winsound  # For Windows systems

# Load the known face encoding (replace with the correct path)
job_image = face_recognition.load_image_file("image/aishwarya.jpeg")
job_encoding = face_recognition.face_encodings(job_image)[0]

paridhi_image = face_recognition.load_image_file("image/priyanka.jpg")
paridhi_encoding = face_recognition.face_encodings(paridhi_image)[0]


modiji_image = face_recognition.load_image_file("image/modiji.jpeg")
modiji_encoding = face_recognition.face_encodings(modiji_image)[0]

salman_image = face_recognition.load_image_file("image/salman.jpeg")
salman_encoding = face_recognition.face_encodings(salman_image)[0]


# Create lists to store known face encodings and names
known_face_encodings = [job_encoding,paridhi_encoding,modiji_encoding, salman_encoding]
known_face_names = ["aishwarya","Priyanka","Modi Ji","salman"]


# Sound file path for the alarm sound (replace with the correct path)
alarm_sound_path = "sound/WOWO.wav"
# Function to play the alarm sound
def play_alarm_sound():
    winsound.PlaySound(alarm_sound_path, winsound.SND_FILENAME)


# Start capturing video from the camera (camera index 0)
video_capture = cv2.VideoCapture(0)

while True:
    **# Read a single frame from the camera feed**
    ret, frame = video_capture.read()

    **#Find all face locations and encodings in the current frame**
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    **# Iterate through the face encodings found in the current frame**
    for face_encoding in face_encodings:
        **# Compare the current face encoding with the known face encodings**
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

      **  # Find the name of the known face with the closest match**
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            **# Draw a rectangle around the detected face and display the name**
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255,0), 2)

            
        **# If no face is recognized or the recognized face is "Unknown", play the alarm sound**
        if not name or name == "Unknown":
            play_alarm_sound()
            ** # Draw a rectangle around the detected face and display the name**
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0,255), 2)
        
    **# Display the processed frame with detected faces**
    cv2.imshow('Face Recognition', frame)

   ** # Press 'q' to exit the loop and close the window**
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()


# Project Structure
This code took two images of Modiji and used the compare_faces method to return True since both images had the same face. 

The model converts every image it gets into a numerical encoding. First, the face_encodings method returns an encoding of the input image. Then, the compare_faces method compares the encodings through a distance parameter to see if there is a match. Then, the encoding with the least distance gets selected since it’s the closest match. After getting the match, the image’s title is retrieved using the image’s index in the list. It will start alert on unknown face to make people alert of unauthorized access
