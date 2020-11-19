def corridor_enviornment(path=0,gender="man"):


    #Import necessary libraries

    import numpy as np
    import time
    import cv2
    import requests
    import threading
    import configparser
    from datetime import datetime
    from keras.preprocessing.image import img_to_array
    from keras.models import load_model
    from keras.utils import get_file
    import os
    import cvlib as cv
    from deepface.basemodels import VGGFace

    import os
    from pathlib import Path
    import gdown
    import numpy as np
    from keras.models import Model, Sequential
    from keras.layers import Convolution2D, Flatten, Activation


    def telegram():

        config = configparser.ConfigParser()
        config.read('DATA/Keys/config.ini')

        config_viewer = config.items('TOKEN')
        token = config_viewer[0][1]
        up_url = config_viewer[1][1]

        print("start")

        try:

            time.sleep(2)


            token = str(token)
            chat_id = str(up_url)  # chat id
            file = 'Fraud.jpg'

            url = f"https://api.telegram.org/bot{token}/sendPhoto"

            print(url)
            files = {}
            files["photo"] = open(file, "rb")
            print(requests.get(url, params={"chat_id": chat_id}, files=files))
        except:
            pass

        print("end")

    model = VGGFace.baseModel()

    # --------------------------

    classes = 2
    base_model_output = Sequential()
    base_model_output = Convolution2D(classes, (1, 1), name='predictions')(model.layers[-4].output)
    base_model_output = Flatten()(base_model_output)
    base_model_output = Activation('softmax')(base_model_output)

    gender_model = Model(inputs=model.input, outputs=base_model_output)


    # load model
    gender_model.load_weights('Data/Models/gender_model_weights.h5')
    net = gender_model

    print(gender)



    classes = ['woman','man']

    unauthorised=0

    if gender=="man":
        var_male=(0,255,0)
        var_female = (0, 0, 255)



    elif gender=="woman":
        var_male = (0, 0, 255)
        var_female = (0, 255, 0)




    video_capture = cv2.VideoCapture(path)



    font = cv2.FONT_HERSHEY_SIMPLEX

    man=0
    woman=0
    telegx=0
    iter=0




    while(True):
        #Read each frame and flip it, and convert to grayscale
        ret, frame = video_capture.read()
        frame = cv2.flip(frame,1)
        (H, W) = frame.shape[:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        cv2.putText(frame, "INTELEGIX (Washroom Corridor Monitoring System)", (400, 40),
                    font, 0.7, (0, 0, 0), 2)
        cv2.rectangle(frame, (20, 50), (W - 20, 15), (0, 0, 0), 2)

        now = datetime.now()

        current_time=now.strftime("%H:%M:%S")

        tot_str = "Washroom Corridor for : " + str(gender).capitalize()
        high_str = "Male Detected : " + str(man)
        low_str = "Female Detected : " + str(woman)
        safe_str = "Total Persons: " + str(man+woman)


        man=0
        woman=0
        unauthorised = 0

        sub_img = frame[H - 100: H, 0:260]
        black_rect = np.ones(sub_img.shape, dtype=np.uint8) * 0

        res = cv2.addWeighted(sub_img, 0.8, black_rect, 0.2, 1.0)

        frame[H - 100:H, 0:260] = res

        cv2.putText(frame, tot_str, (10, H - 80),
                    font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, high_str, (10, H - 55),
                    font, 0.5, (0, 255, 0), 1)
        cv2.putText(frame, low_str, (10, H - 30),
                    font, 0.5, (0, 120, 255), 1)
        cv2.putText(frame, safe_str, (10, H - 5),
                    font, 0.5, (0, 0, 150), 1)

        now = datetime.now()
        # cv2.imwrite(str("Data/Saved_Images/CLASS_ENVIRONMENT/") + str(now.strftime("%Y%m%d%H%M%S") + str(".jpg")), img)

        # cv2.putText(img, str(now.strftime("%d-%m-%Y% %H:%M:%S")), (W-10, H - 5),
        #             font, 0.5, (0, 0, 150), 1)
        timex = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        cv2.putText(frame, timex, (W - 200, H - 10),
                    font, 0.5 , (255, 255, 255), 1)

        # apply face detection
        face, confidence = cv.detect_face(frame)

        print(face)
        print(confidence)

        # loop through detected faces
        for idx, f in enumerate(face):

            # get corner points of face rectangle
            (startX, startY) = f[0], f[1]
            (endX, endY) = f[2], f[3]

            # # draw rectangle over face
            # cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

            # crop the detected face region
            face_crop = np.copy(frame[startY:endY, startX:endX])

            if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
                continue

            # preprocessing for gender detection model
            face_crop = cv2.resize(face_crop, (224, 224))
            face_crop = face_crop.astype("float") / 255.0
            face_crop = img_to_array(face_crop)
            face_crop = np.expand_dims(face_crop, axis=0)

            # apply gender detection on face
            conf = net.predict(face_crop)[0]
            print(conf)
            print(classes)

            # get label with max accuracy
            idx = np.argmax(conf)
            label = classes[idx]
            print(label)

            print(label,gender)
            if str(label) != str(gender):
                unauthorised += 1

            if label=="man":
                # draw rectangle over face
                cv2.rectangle(frame, (startX, startY), (endX, endY), var_male, 2)

                label = "{}: {:.2f}%".format(label, conf[idx] * 100)

                Y = startY - 10 if startY - 10 > 10 else startY + 10

                # write label and confidence above face rectangle
                cv2.putText(frame, label, (startX, Y), font,
                            0.7, var_male, 2)
                man+=1





            if label=="woman":

                # draw rectangle over face
                cv2.rectangle(frame, (startX, startY), (endX, endY),var_female, 2)

                label = "{}: {:.2f}%".format(label, conf[idx] * 100)

                Y = startY - 10 if startY - 10 > 10 else startY + 10

                # write label and confidence above face rectangle
                cv2.putText(frame, label, (startX, Y), font,
                            0.7, var_female, 2)

                woman+=1







        if unauthorised==0 :

            #image = draw_outputs(img, (boxes, scores, classes, nums), class_names, color=(0, 255, 0))
            cv2.circle(frame, (25, 80), 10, (0, 255, 0), -1)
            cv2.putText(frame, "All Ok", (50, 85),
                        font, 0.5, (0, 255, 0), 2)



        else:

            if unauthorised>0:
                #image = draw_outputs(img, (boxes, scores, classes, nums), class_names, color=(0, 0, 255))
                cv2.circle(frame, (25, 80), 10, (0, 0, 255), -1)
                cv2.putText(frame, "Unrestricted Access at "+str(gender)+" washroom", (50, 85),
                            font, 0.5, (0, 0, 255), 2)


                telegx += 1
                print(telegx)
                if telegx > 3:
                    cv2.imwrite("Fraud.jpg", frame)
                    threading.Thread(target=telegram).start()
                    telegx = 0

                    now = datetime.now()
                    cv2.imwrite(
                        str("Data/Saved_Images/CORRIDOR_ENVIRONMENT/") + str(now.strftime("%Y%m%d%H%M%S") + str(".jpg")),
                        frame)




        cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Output", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Output", frame)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    #Finally when video capture is over, release the video capture and destroyAllWindows
    video_capture.release()
    cv2.destroyAllWindows()


# if __name__=="__main__":
#     corridor_enviornment(path=0,gender="man")