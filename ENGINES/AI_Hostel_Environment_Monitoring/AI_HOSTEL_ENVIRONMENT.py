def hostel_enviornment(path=0,start="20:00:00",end="06:00:00"):


    #Import necessary libraries

    import numpy as np
    import time
    import cv2
    import requests
    import threading
    import configparser
    from datetime import datetime


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





    net=cv2.dnn.readNet("Data/Models/yolov3.weights","Data/Models/yolov3.cfg")

    labelsPath = "Data/Models/class.names"
    classes = open(labelsPath).read().strip().split("\n")




    video_capture = cv2.VideoCapture(path)



    font = cv2.FONT_HERSHEY_SIMPLEX

    drowsey_level="False"
    Cigarette="False"
    Mobile="False"
    telegx=0
    iter=0

    while(True):
        #Read each frame and flip it, and convert to grayscale
        ret, frame = video_capture.read()
        frame = cv2.flip(frame,1)
        (H, W) = frame.shape[:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        cv2.putText(frame, "INTELEGIX (Hostel Monitoring System)", (110, 40),
                    font, 0.7*2, (255, 255, 255), 2)
        cv2.rectangle(frame, (20, 50), (W - 20, 15), (255, 255, 255), 2)

        now = datetime.now()

        current_time=now.strftime("%H:%M:%S")

        tot_str = "Current Time: " + str(current_time)
        high_str = "Start Time: " + str(start)
        low_str = "End Time: " + str(end)
        safe_str = "Total Persons: " + str(iter)


        Cigarette="False"
        Mobile="False"

        sub_img = frame[H - 100: H, 0:260]
        black_rect = np.ones(sub_img.shape, dtype=np.uint8) * 0

        res = cv2.addWeighted(sub_img, 0.8, black_rect, 0.2, 1.0)

        frame[H - 100:H, 0:260] = res

        cv2.putText(frame, tot_str, (10, H - 80),
                    font, 0.5*2, (255, 255, 255), 1)
        cv2.putText(frame, high_str, (10, H - 55),
                    font, 0.5*2, (0, 255, 0), 1)
        cv2.putText(frame, low_str, (10, H - 30),
                    font, 0.5*2, (0, 120, 255), 1)
        cv2.putText(frame, safe_str, (10, H - 5),
                    font, 0.5*2, (0, 0, 150), 1)

        now = datetime.now()
        # cv2.imwrite(str("Data/Saved_Images/CLASS_ENVIRONMENT/") + str(now.strftime("%Y%m%d%H%M%S") + str(".jpg")), img)

        # cv2.putText(img, str(now.strftime("%d-%m-%Y% %H:%M:%S")), (W-10, H - 5),
        #             font, 0.5, (0, 0, 150), 1)
        timex = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        cv2.putText(frame, timex, (W - 200, H - 10),
                    font, 0.5 * 2, (255, 255, 255), 1)

        ln=net.getLayerNames()


        ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (224, 224), swapRB=True, crop=False)
        net.setInput(blob)
        #start = time.time()
        layerOutputs = net.forward(ln)
        #end = time.time()
        # print("Frame Prediction Time : {:.6f} seconds".format(end - start))
        boxes = []
        confidences = []
        classIDs = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                if confidence > 0.1 and classID == 0:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)










        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        #print(indexes)
        font = cv2.FONT_HERSHEY_PLAIN
        iter=0
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[classIDs[i]])
                color = (0,0,255)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                #cv2.putText(frame, label, (x, y + 30), font, 3, color, 2)
                iter+=1






        if iter==0 :

            #image = draw_outputs(img, (boxes, scores, classes, nums), class_names, color=(0, 255, 0))
            cv2.circle(frame, (25, 80), 10, (0, 255, 0), -1)
            cv2.putText(frame, "All Ok", (50, 85),
                        font, 0.5*2, (0, 255, 0), 2)



        else:
            print(str(start)[0:2])
            if str(start)[0:2] <= str(current_time)[0:2] and str(end)[0:2] <= str(current_time)[0:2]:
                #image = draw_outputs(img, (boxes, scores, classes, nums), class_names, color=(0, 0, 255))
                cv2.circle(frame, (25, 80), 10, (0, 0, 255), -1)
                cv2.putText(frame, "Unrestricted Access", (50, 85),
                            font, 0.5*2, (0, 0, 255), 2)


                telegx += 1
                print(telegx)
                if telegx > 10:
                    cv2.imwrite("Fraud.jpg", frame)
                    threading.Thread(target=telegram).start()
                    telegx = 0

                    now = datetime.now()
                    cv2.imwrite(
                        str("Data/Saved_Images/HOSTEL_ENVIRONMENT/") + str(now.strftime("%Y%m%d%H%M%S") + str(".jpg")),
                        frame)



        #Show video feed
        cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Output", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Output", frame)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    #Finally when video capture is over, release the video capture and destroyAllWindows
    video_capture.release()
    cv2.destroyAllWindows()


# if __name__=="__main__":
#     hostel_enviornment(path=0,start="20:00:00",end="06:00:00")