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


# Create lists to store known face encodings and names
known_face_encodings = [job_encoding,paridhi_encoding,modiji_encoding]
known_face_names = ["aishwarya","Priyanka","Modi Ji"]


# Sound file path for the alarm sound (replace with the correct path)
alarm_sound_path = "sound/WOWO.wav"
# Function to play the alarm sound
def play_alarm_sound():
    winsound.PlaySound(alarm_sound_path, winsound.SND_FILENAME)


# Start capturing video from the camera (camera index 0)
video_capture = cv2.VideoCapture(0)

while True:
    # Read a single frame from the camera feed
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Iterate through the face encodings found in the current frame
    for face_encoding in face_encodings:
        # Compare the current face encoding with the known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Find the name of the known face with the closest match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            # Draw a rectangle around the detected face and display the name
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255,0), 2)

            
        # If no face is recognized or the recognized face is "Unknown", play the alarm sound
        if not name or name == "Unknown":
            play_alarm_sound()
             # Draw a rectangle around the detected face and display the name
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0,255), 2)
        
    # Display the processed frame with detected faces
    cv2.imshow('Face Recognition', frame)

    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()
