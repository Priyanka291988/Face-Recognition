# Face-Recognition
Facial recognition to alert unauthorized access based on Face Recognition using Python and OpenCv


# Code Requirements
To set up the libraries required for face recognition through Python:

1. Go to the terminal and download the dlib library:
pip install dlib

The dlib library is a C++ toolkit that features machine learning tools and algorithms. It is important to install it to use the face_recognition library.

2. Use the following command to install the face_recognition library:
pip install face recognition

3. Use the following command to download the OpenCV library:
pip install opencv

The OpenCV library will come in handy for pre-processing steps.

# What steps you have to follow??
Download my Repository
Create a Image folder in a project.
Open a UAS.py and change the all paths with your system path
Run UAS.py.

![image](https://github.com/Priyanka291988/Face-Recognition/assets/141348892/085e254b-f83d-4fb6-99a2-a3cadfe1677e)

# Project Structure
This code took two images of Modiji and used the compare_faces method to return True since both images had the same face. 

The model converts every image it gets into a numerical encoding. First, the face_encodings method returns an encoding of the input image. Then, the compare_faces method compares the encodings through a distance parameter to see if there is a match. Then, the encoding with the least distance gets selected since it’s the closest match. After getting the match, the image’s title is retrieved using the image’s index in the list. It will start alert on unknown face to make people alert of unauthorized access
