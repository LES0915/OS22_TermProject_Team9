# OS22_TermProject_Team9
## 🐥 Facial recognition registration service 🐥
This project used a face recognition service using OpenCV. Face recognition login service. When everyone registers their face and name, they recognize their face and even match their name. If your face is not recognized, you can log in manually with a password.

## 🎞️ a demonstration video 🎞️


<iframe width="872" height="545" src="https://www.youtube.com/embed/_LeMepjLh4k" title="OS22 TermProject Team9" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>





## 📃The package used 📃
* Flask (2.2.2)
* Jinja2 (3.1.2) 
* MarkupSafe (2.1.1)
* Pillow (9.3.0)
* Werkzeug (2.2.2)
* click (8.1.3)
* cmake (3.25.0)
* colorama (0.4.6)
* dlib (19.24.0)
* face (22.0.0)
* face_recognition (1.3.0)
* face_recognition_models (0.3.0)
* importlib-metadata (5.0.0)
* imutils (0.5.4)
* itsdangerous (2.1.2)
* numpy (1.23.5)
* opencv-contrib-python (4.6.0.66)
* opencv-python (4.6.0.66)
* pip (20.2.3)
* setuptools (49.2.1)
* zipp (3.10.0)

## ✍️ How to practice ✍️
Enter sign up or log in.

When you type sign up, enter a name for registration.  
Verify that the name is already registered.  
If the name is not registered, enter a password.  
Afterwards, when the camera turns on, press any key on the keyboard to capture and save your face.

When you type login, enter a name for login.  
If the ID exists, the camera turns on, and if it is the same person through face recognition, a Welcome message appears.  
If it does not continue to be recognized, you can manually press the p button to log in through the password.

## 🔗 Reference link 🔗
[face_recognition](https://github.com/ageitgey/face_recognition).
