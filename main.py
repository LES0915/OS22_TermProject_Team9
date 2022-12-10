import os

import cv2
import face_recog

#registration service

# 이미 등록된 이름인지 확인
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

print('Enter \'sign up\' if you want to sign up and \'log in\' if you want to log in.')
action = input()

# 회원가입
if action == 'sign up':
    print('Please enter the name to register: ')
    user_name = input()

    count = check_name(user_name)

    if count == 1:
        print("Name already registered.")

    else:
        print('Enter password to enter if face recognition fails: ')
        password = input()

        # 유저 닉네임으로 된 파일 생성, 파일 안에는 비밀번호 입력해주고 파일 닫아줌
        user_file = open('datas/{}.txt'.format(user_name), 'w')
        user_file.write(password)
        user_file.close()

        # 카메라로 유저 얼굴 캡처하고 knowns에 넣어줌
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


# 로그인
elif action == 'log in':
    if __name__ == '__main__':
        print('Enter the name to login: ')
        user_name = input()

        # 아이디 존재 여부 확인
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

                # q 버튼을 누르면
                if key == ord("q"):
                    # 종료
                    break

                # 입력받은 이름이 카메라로 인식한 사람의 얼굴 이름과 동일하면
                elif user_name == compare_name:
                    print('\n----------------------------')
                    print('** User {}, Welcome! **'.format(user_name))
                    print('----------------------------\n')
                    break

                # 인식이 안돼서 p 버튼 누르고 비밀번호를 입력받고 싶다면
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