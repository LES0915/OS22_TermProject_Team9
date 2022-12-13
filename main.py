import os
import cv2
import face_recog

#registration service

# Verify that the name is already registered
def check_name(user):
    name_data = []

    file = os.listdir('datas')
    for filename in file:
        name, ext = os.path.splitext(filename)
        if ext == '.txt':
            name_data.append(name)

    count_1 = 0
    for i in name_data:
        if i == user:
            count_1 += 1
    return count_1

# Select login or sign up
print('Enter \'sign up\' if you want to sign up and \'log in\' if you want to log in.')
action = input()

# join membership
if action == 'sign up':
    print('Please enter the name to register: ')
    user_name = input()
    
    # Check if ID exists
    count = check_name(user_name)

    if count == 1:
        print("Name already registered.")

    else:
        print('Enter password to enter if face recognition fails: ')
        password = input()

        # Create a file with the user's nickname, enter a password in the file, and close the file
        user_file = open('datas/{}.txt'.format(user_name), 'w')
        user_file.write(password)
        user_file.close()

        # Capture the user's face with the camera and put it in "Knows"
        capture = cv2.VideoCapture(0)
        if capture.isOpened():
            while True:
                ret, frame = capture.read()

                if ret:
                    cv2.imshow('camera', frame)
                    if cv2.waitKey(1) != -1:
                        cv2.imwrite('knowns/{}.jpg'.format(user_name), frame)
                        break
                else:
                    print('no frame')
                    break
        else:
            print('no camera!')
        capture.release()
        cv2.destroyAllWindows()


# Log in
elif action == 'log in':
    if __name__ == '__main__':
        print('Enter the name to login: ')
        user_name = input()

        # Check if ID exists
        count = check_name(user_name)

        if count == 1:
            print('Please waiting...')
            print('If your face is not recognized, press p to enter the password.')
            print('And if you want to exit the program, press the q key.')
            face_recog = face_recog.FaceRecog()

            while True:
                frame, compare_name = face_recog.get_frame()

                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1) & 0xFF

                # If you press the q button,
                if key == ord("q"):
                    # end
                    break

                # If the given name is the same as the face name of the person recognized by the camera,
                elif user_name == compare_name:
                    print('\n----------------------------')
                    print('** User {}, Welcome! **'.format(user_name))
                    print('----------------------------\n')
                    break

                # It's not recognized, so if you want to press the p button and get a password,
                elif key == ord("p"):
                    print('Please enter the password for user {}:'.format(user_name))
                    password = input()
                    user_file = open('datas/{}.txt'.format(user_name), 'r')
                    if password == user_file.read():
                        print('\n----------------------------')
                        print('** User {}, Welcome! **'.format(user_name))
                        print('----------------------------\n')
                        user_file.close()
                    else:
                        print('Wrong password! Exit the register...')
                        user_file.close()

            cv2.destroyAllWindows()
            print('finish')
        else:
            print("This user is not registered.")

else:
    print('You have been entered incorrectly. Please re-enter.')
