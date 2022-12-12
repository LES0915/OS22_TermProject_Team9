# OS22_TermProject_Team9
## Project Overview
### 🐥Facial recognition registration service 🐥
This project used a face recognition service using OpenCV. Face recognition login service. When everyone registers their face and name, they recognize their face and even match their name. If your face is not recognized, you can log in manually with a password.


## The package used
* Flask
* Jinja2
* MarkupSafe
* Pillow
* Werkzeug
* click
* cmake
* colorama
* dlib
* face
* face_recognition
* face_recognition_models
* importlib-metadata
* imutils
* itsdangerous
* numpy
* opencv-contrib-python
* opencv-python
* pip
* setuptools
* zipp

## How to practice
Enter sign up or log in.

When you type sign up, enter a name for registration.  
Verify that the name is already registered.  
If the name is not registered, enter a password.  
Afterwards, when the camera turns on, press any key on the keyboard to capture and save your face.

When you type login, enter a name for login.  
If the ID exists, the camera turns on, and if it is the same person through face recognition, a Welcome message appears.  
If it does not continue to be recognized, you can manually press the p button to log in through the password.

### Reference link
[face_recognition](https://github.com/ageitgey/face_recognition).
