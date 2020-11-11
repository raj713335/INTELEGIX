
def AI_PROCTORING(path=0):
    import math
    import cv2
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    import cv2
    import wget
    import requests
    import threading
    import time
    import configparser
    from datetime import datetime


    from tensorflow.keras.regularizers import l2
    from tensorflow.keras import Model
    from tensorflow.keras.layers import (
        Add,
        Concatenate,
        Conv2D,
        Input,
        Lambda,
        LeakyReLU,
        UpSampling2D,
        ZeroPadding2D,
        BatchNormalization
    )



    def telegram():

        # pyautogui.screenshot(r"Fraud.png")

        print("start")
        config = configparser.ConfigParser()
        config.read('DATA/Keys/config.ini')

        config_viewer = config.items('TOKEN')
        token = config_viewer[0][1]
        up_url = config_viewer[1][1]

        try:

            time.sleep(2)


            token = str(token)
            chat_id = str(up_url)
            file = 'Fraud.jpg'

            url = f"https://api.telegram.org/bot{token}/sendPhoto"

            print(url)
            files = {}
            files["photo"] = open(file, "rb")
            print(requests.get(url, params={"chat_id": chat_id}, files=files))
        except:
            pass

        print("end")




    def load_darknet_weights(model, weights_file):

        # Open the weights file
        wf = open(weights_file, 'rb')
        major, minor, revision, seen, _ = np.fromfile(wf, dtype=np.int32, count=5)

        # Define names of the Yolo layers (just for a reference)
        layers = ['yolo_darknet',
                  'yolo_conv_0',
                  'yolo_output_0',
                  'yolo_conv_1',
                  'yolo_output_1',
                  'yolo_conv_2',
                  'yolo_output_2']

        for layer_name in layers:
            sub_model = model.get_layer(layer_name)
            for i, layer in enumerate(sub_model.layers):

                if not layer.name.startswith('conv2d'):
                    continue

                # Handles the special, custom Batch normalization layer
                batch_norm = None
                if i + 1 < len(sub_model.layers) and \
                        sub_model.layers[i + 1].name.startswith('batch_norm'):
                    batch_norm = sub_model.layers[i + 1]

                filters = layer.filters
                size = layer.kernel_size[0]
                in_dim = layer.input_shape[-1]

                if batch_norm is None:
                    conv_bias = np.fromfile(wf, dtype=np.float32, count=filters)
                else:
                    # darknet [beta, gamma, mean, variance]
                    bn_weights = np.fromfile(
                        wf, dtype=np.float32, count=4 * filters)
                    # tf [gamma, beta, mean, variance]
                    bn_weights = bn_weights.reshape((4, filters))[[1, 0, 2, 3]]

                # darknet shape (out_dim, in_dim, height, width)
                conv_shape = (filters, in_dim, size, size)
                conv_weights = np.fromfile(
                    wf, dtype=np.float32, count=np.product(conv_shape))
                # tf shape (height, width, in_dim, out_dim)
                conv_weights = conv_weights.reshape(
                    conv_shape).transpose([2, 3, 1, 0])

                if batch_norm is None:
                    layer.set_weights([conv_weights, conv_bias])
                else:
                    layer.set_weights([conv_weights])
                    batch_norm.set_weights(bn_weights)

        assert len(wf.read()) == 0, 'failed to read all data'
        wf.close()


    def draw_outputs(img, outputs, class_names,color=(0,0,255)):

        boxes, objectness, classes, nums = outputs
        boxes, objectness, classes, nums = boxes[0], objectness[0], classes[0], nums[0]
        wh = np.flip(img.shape[0:2])
        for i in range(nums):
            x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
            x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))
            img = cv2.rectangle(img, x1y1, x2y2, color, 1)
            img = cv2.putText(img, '{} {:.2f}%'.format(
                class_names[int(classes[i])], objectness[i]),
                              x1y1, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)
        return img


    yolo_anchors = np.array([(10, 13), (16, 30), (33, 23), (30, 61), (62, 45),
                             (59, 119), (116, 90), (156, 198), (373, 326)],
                            np.float32) / 416

    yolo_anchor_masks = np.array([[6, 7, 8], [3, 4, 5], [0, 1, 2]])


    def DarknetConv(x, filters, kernel_size, strides=1, batch_norm=True):

        # Image padding
        if strides == 1:
            padding = 'same'
        else:
            x = ZeroPadding2D(((1, 0), (1, 0)))(x)  # top left half-padding
            padding = 'valid'

        # Defining the Conv layer
        x = Conv2D(filters=filters, kernel_size=kernel_size,
                   strides=strides, padding=padding,
                   use_bias=not batch_norm, kernel_regularizer=l2(0.0005))(x)

        if batch_norm:
            x = BatchNormalization()(x)
            x = LeakyReLU(alpha=0.1)(x)
        return x


    def DarknetResidual(x, filters):

        prev = x
        x = DarknetConv(x, filters // 2, 1)
        x = DarknetConv(x, filters, 3)
        x = Add()([prev, x])
        return x


    def DarknetBlock(x, filters, blocks):

        x = DarknetConv(x, filters, 3, strides=2)
        for _ in range(blocks):
            x = DarknetResidual(x, filters)
        return x


    def Darknet(name=None):

        x = inputs = Input([None, None, 3])
        x = DarknetConv(x, 32, 3)
        x = DarknetBlock(x, 64, 1)
        x = DarknetBlock(x, 128, 2)  # skip connection
        x = x_36 = DarknetBlock(x, 256, 8)  # skip connection
        x = x_61 = DarknetBlock(x, 512, 8)
        x = DarknetBlock(x, 1024, 4)
        return tf.keras.Model(inputs, (x_36, x_61, x), name=name)


    def YoloConv(filters, name=None):

        def yolo_conv(x_in):
            if isinstance(x_in, tuple):
                inputs = Input(x_in[0].shape[1:]), Input(x_in[1].shape[1:])
                x, x_skip = inputs

                # concat with skip connection
                x = DarknetConv(x, filters, 1)
                x = UpSampling2D(2)(x)
                x = Concatenate()([x, x_skip])
            else:
                x = inputs = Input(x_in.shape[1:])

            x = DarknetConv(x, filters, 1)
            x = DarknetConv(x, filters * 2, 3)
            x = DarknetConv(x, filters, 1)
            x = DarknetConv(x, filters * 2, 3)
            x = DarknetConv(x, filters, 1)
            return Model(inputs, x, name=name)(x_in)

        return yolo_conv


    def YoloOutput(filters, anchors, classes, name=None):

        def yolo_output(x_in):
            x = inputs = Input(x_in.shape[1:])
            x = DarknetConv(x, filters * 2, 3)
            x = DarknetConv(x, anchors * (classes + 5), 1, batch_norm=False)
            x = Lambda(lambda x: tf.reshape(x, (-1, tf.shape(x)[1], tf.shape(x)[2],
                                                anchors, classes + 5)))(x)
            return tf.keras.Model(inputs, x, name=name)(x_in)

        return yolo_output


    def yolo_boxes(pred, anchors, classes):
        '''
        Call this function to get bounding boxes from network predictions

        :param pred: Yolo predictions
        :param anchors: anchors
        :param classes: List of classes from the dataset
        '''

        # pred: (batch_size, grid, grid, anchors, (x, y, w, h, obj, ...classes))
        grid_size = tf.shape(pred)[1]
        # Extract box coortinates from prediction vectors
        box_xy, box_wh, objectness, class_probs = tf.split(
            pred, (2, 2, 1, classes), axis=-1)

        # Normalize coortinates
        box_xy = tf.sigmoid(box_xy)
        objectness = tf.sigmoid(objectness)
        class_probs = tf.sigmoid(class_probs)
        pred_box = tf.concat((box_xy, box_wh), axis=-1)  # original xywh for loss

        # !!! grid[x][y] == (y, x)
        grid = tf.meshgrid(tf.range(grid_size), tf.range(grid_size))
        grid = tf.expand_dims(tf.stack(grid, axis=-1), axis=2)  # [gx, gy, 1, 2]

        box_xy = (box_xy + tf.cast(grid, tf.float32)) / \
                 tf.cast(grid_size, tf.float32)
        box_wh = tf.exp(box_wh) * anchors

        box_x1y1 = box_xy - box_wh / 2
        box_x2y2 = box_xy + box_wh / 2
        bbox = tf.concat([box_x1y1, box_x2y2], axis=-1)

        return bbox, objectness, class_probs, pred_box


    def yolo_nms(outputs, anchors, masks, classes):
        # boxes, conf, type
        b, c, t = [], [], []

        for o in outputs:
            b.append(tf.reshape(o[0], (tf.shape(o[0])[0], -1, tf.shape(o[0])[-1])))
            c.append(tf.reshape(o[1], (tf.shape(o[1])[0], -1, tf.shape(o[1])[-1])))
            t.append(tf.reshape(o[2], (tf.shape(o[2])[0], -1, tf.shape(o[2])[-1])))

        bbox = tf.concat(b, axis=1)
        confidence = tf.concat(c, axis=1)
        class_probs = tf.concat(t, axis=1)

        scores = confidence * class_probs
        boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
            boxes=tf.reshape(bbox, (tf.shape(bbox)[0], -1, 1, 4)),
            scores=tf.reshape(
                scores, (tf.shape(scores)[0], -1, tf.shape(scores)[-1])),
            max_output_size_per_class=100,
            max_total_size=100,
            iou_threshold=0.5,
            score_threshold=0.6
        )

        return boxes, scores, classes, valid_detections


    def YoloV3(size=None, channels=3, anchors=yolo_anchors,
               masks=yolo_anchor_masks, classes=80):
        x = inputs = Input([size, size, channels], name='input')

        x_36, x_61, x = Darknet(name='yolo_darknet')(x)

        x = YoloConv(512, name='yolo_conv_0')(x)
        output_0 = YoloOutput(512, len(masks[0]), classes, name='yolo_output_0')(x)

        x = YoloConv(256, name='yolo_conv_1')((x, x_61))
        output_1 = YoloOutput(256, len(masks[1]), classes, name='yolo_output_1')(x)

        x = YoloConv(128, name='yolo_conv_2')((x, x_36))
        output_2 = YoloOutput(128, len(masks[2]), classes, name='yolo_output_2')(x)

        boxes_0 = Lambda(lambda x: yolo_boxes(x, anchors[masks[0]], classes),
                         name='yolo_boxes_0')(output_0)
        boxes_1 = Lambda(lambda x: yolo_boxes(x, anchors[masks[1]], classes),
                         name='yolo_boxes_1')(output_1)
        boxes_2 = Lambda(lambda x: yolo_boxes(x, anchors[masks[2]], classes),
                         name='yolo_boxes_2')(output_2)

        outputs = Lambda(lambda x: yolo_nms(x, anchors, masks, classes),
                         name='yolo_nms')((boxes_0[:3], boxes_1[:3], boxes_2[:3]))

        return Model(inputs, outputs, name='yolov3')


    def weights_download(out='models/yolov3.weights'):
        _ = wget.download('https://pjreddie.com/media/files/yolov3.weights', out='Data/Models/yolov3.weights')


    # weights_download() # to download weights
    yolo = YoloV3()
    import os
    print(os.getcwd())
    load_darknet_weights(yolo, 'Data/Models/yolov3.weights')


    def get_landmark_model(saved_model='Data/Models/pose_model'):

        model = keras.models.load_model(saved_model)
        return model


    def get_square_box(box):
        """Get a square box out of the given box, by expanding it."""
        left_x = box[0]
        top_y = box[1]
        right_x = box[2]
        bottom_y = box[3]

        box_width = right_x - left_x
        box_height = bottom_y - top_y

        # Check if box is already a square. If not, make it a square.
        diff = box_height - box_width
        delta = int(abs(diff) / 2)

        if diff == 0:  # Already a square.
            return box
        elif diff > 0:  # Height > width, a slim box.
            left_x -= delta
            right_x += delta
            if diff % 2 == 1:
                right_x += 1
        else:  # Width > height, a short box.
            top_y -= delta
            bottom_y += delta
            if diff % 2 == 1:
                bottom_y += 1

        # Make sure box is always square.
        assert ((right_x - left_x) == (bottom_y - top_y)), 'Box is not square.'

        return [left_x, top_y, right_x, bottom_y]


    def move_box(box, offset):

        left_x = box[0] + offset[0]
        top_y = box[1] + offset[1]
        right_x = box[2] + offset[0]
        bottom_y = box[3] + offset[1]
        return [left_x, top_y, right_x, bottom_y]


    def detect_marks(img, model, face):

        offset_y = int(abs((face[3] - face[1]) * 0.1))
        box_moved = move_box(face, [0, offset_y])
        facebox = get_square_box(box_moved)

        h, w = img.shape[:2]
        if facebox[0] < 0:
            facebox[0] = 0
        if facebox[1] < 0:
            facebox[1] = 0
        if facebox[2] > w:
            facebox[2] = w
        if facebox[3] > h:
            facebox[3] = h

        face_img = img[facebox[1]: facebox[3],
                   facebox[0]: facebox[2]]
        try:
            face_img = cv2.resize(face_img, (128, 128))
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
        except:
            pass

        # # Actual detection.
        predictions = model.signatures["predict"](
            tf.constant([face_img], dtype=tf.uint8))

        # Convert predictions to landmarks.
        marks = np.array(predictions['output']).flatten()[:136]
        marks = np.reshape(marks, (-1, 2))

        marks *= (facebox[2] - facebox[0])
        marks[:, 0] += facebox[0]
        marks[:, 1] += facebox[1]
        marks = marks.astype(np.uint)

        return marks


    def draw_marks(image, marks, color=(0, 255, 0)):

        for mark in marks:
            cv2.circle(image, (mark[0], mark[1]), 2, color, -1, cv2.LINE_AA)


    def get_face_detector(modelFile=None,
                          configFile=None,
                          quantized=False):

        if quantized:
            if modelFile == None:
                modelFile = "Data/Models/opencv_face_detector_uint8.pb"
            if configFile == None:
                configFile = "Data/Models/opencv_face_detector.pbtxt"
            model = cv2.dnn.readNetFromTensorflow(modelFile, configFile)

        else:
            if modelFile == None:
                modelFile = "Data/Models/res10_300x300_ssd_iter_140000.caffemodel"
            if configFile == None:
                configFile = "Data/Models/deploy.prototxt"
            model = cv2.dnn.readNetFromCaffe(configFile, modelFile)
        return model


    def find_faces(img, model):

        h, w = img.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
                                     (300, 300), (104.0, 177.0, 123.0))
        model.setInput(blob)
        res = model.forward()
        faces = []
        for i in range(res.shape[2]):
            confidence = res[0, 0, i, 2]
            if confidence > 0.5:
                box = res[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x1, y1) = box.astype("int")
                faces.append([x, y, x1, y1])
        return faces


    def draw_faces(img, faces):

        for x, y, x1, y1 in faces:
            cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 3)


    def eye_on_mask(mask, side, shape):

        points = [shape[i] for i in side]
        points = np.array(points, dtype=np.int32)
        mask = cv2.fillConvexPoly(mask, points, 255)
        l = points[0][0]
        t = (points[1][1] + points[2][1]) // 2
        r = points[3][0]
        b = (points[4][1] + points[5][1]) // 2
        return mask, [l, t, r, b]


    def find_eyeball_position(end_points, cx, cy):
        """Find and return the eyeball positions, i.e. left or right or top or normal"""
        x_ratio = (end_points[0] - cx) / (cx - end_points[2])
        y_ratio = (cy - end_points[1]) / (end_points[3] - cy)
        if x_ratio > 3:
            return 1
        elif x_ratio < 0.33:
            return 2
        elif y_ratio < 0.33:
            return 3
        else:
            return 0


    def contouring(thresh, mid, img, end_points, right=False):

        cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        try:
            cnt = max(cnts, key=cv2.contourArea)
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            if right:
                cx += mid
            cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
            pos = find_eyeball_position(end_points, cx, cy)
            return pos
        except:
            pass


    def process_thresh(thresh):

        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=4)
        thresh = cv2.medianBlur(thresh, 3)
        thresh = cv2.bitwise_not(thresh)
        return thresh


    def print_eye_pos(img, left, right):

        if left == right and left != 0:
            text = ''
            if left == 1:
                print('Looking left')
                text = 'Looking left'
            elif left == 2:
                print('Looking right')
                text = 'Looking right'
            elif left == 3:
                print('Looking up')
                text = 'Looking up'
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, text, (30, 30), font,
                        1, (0, 255, 255), 2, cv2.LINE_AA)


    def get_2d_points(img, rotation_vector, translation_vector, camera_matrix, val):
        """Return the 3D points present as 2D for making annotation box"""
        point_3d = []
        dist_coeffs = np.zeros((4, 1))
        rear_size = val[0]
        rear_depth = val[1]
        point_3d.append((-rear_size, -rear_size, rear_depth))
        point_3d.append((-rear_size, rear_size, rear_depth))
        point_3d.append((rear_size, rear_size, rear_depth))
        point_3d.append((rear_size, -rear_size, rear_depth))
        point_3d.append((-rear_size, -rear_size, rear_depth))

        front_size = val[2]
        front_depth = val[3]
        point_3d.append((-front_size, -front_size, front_depth))
        point_3d.append((-front_size, front_size, front_depth))
        point_3d.append((front_size, front_size, front_depth))
        point_3d.append((front_size, -front_size, front_depth))
        point_3d.append((-front_size, -front_size, front_depth))
        point_3d = np.array(point_3d, dtype=np.float).reshape(-1, 3)

        # Map to 2d img points
        (point_2d, _) = cv2.projectPoints(point_3d,
                                          rotation_vector,
                                          translation_vector,
                                          camera_matrix,
                                          dist_coeffs)
        point_2d = np.int32(point_2d.reshape(-1, 2))
        return point_2d


    def draw_annotation_box(img, rotation_vector, translation_vector, camera_matrix,
                            rear_size=300, rear_depth=0, front_size=500, front_depth=400,
                            color=(255, 255, 0), line_width=2):


        rear_size = 1
        rear_depth = 0
        front_size = img.shape[1]
        front_depth = front_size * 2
        val = [rear_size, rear_depth, front_size, front_depth]
        point_2d = get_2d_points(img, rotation_vector, translation_vector, camera_matrix, val)
        # # Draw all the lines
        cv2.polylines(img, [point_2d], True, color, line_width, cv2.LINE_AA)
        cv2.line(img, tuple(point_2d[1]), tuple(
            point_2d[6]), color, line_width, cv2.LINE_AA)
        cv2.line(img, tuple(point_2d[2]), tuple(
            point_2d[7]), color, line_width, cv2.LINE_AA)
        cv2.line(img, tuple(point_2d[3]), tuple(
            point_2d[8]), color, line_width, cv2.LINE_AA)


    def head_pose_points(img, rotation_vector, translation_vector, camera_matrix):

        rear_size = 1
        rear_depth = 0
        front_size = img.shape[1]
        front_depth = front_size * 2
        val = [rear_size, rear_depth, front_size, front_depth]
        point_2d = get_2d_points(img, rotation_vector, translation_vector, camera_matrix, val)
        y = (point_2d[5] + point_2d[8]) // 2
        x = point_2d[2]

        return (x, y)


    face_model = get_face_detector()
    landmark_model = get_landmark_model()
    outer_points = [[49, 59], [50, 58], [51, 57], [52, 56], [53, 55]]
    inner_points = [[61, 67], [62, 66], [63, 65]]

    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(path)


    d_outer = [19.0, 29.0, 28.0, 28.0, 19.0]
    d_inner = [13.0, 14.0, 13.0]




    iter=0


    head_position=""
    mouth_open="False"
    total_person=0
    mobile_phones="False"

    telegx=0

    while (True):
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        rects = find_faces(img, face_model)

        size = img.shape
        (H, W) = img.shape[:2]

        print(H,W)

        # 3D model points.
        model_points = np.array([
            (0.0, 0.0, 0.0),  # Nose tip
            (0.0, -330.0, -65.0),  # Chin
            (-225.0, 170.0, -135.0),  # Left eye left corner
            (225.0, 170.0, -135.0),  # Right eye right corne
            (-150.0, -150.0, -125.0),  # Left Mouth corner
            (150.0, -150.0, -125.0)  # Right mouth corner
        ])

        # Camera internals
        focal_length = size[1]
        center = (size[1] / 2, size[0] / 2)
        camera_matrix = np.array(
            [[focal_length, 0, center[0]],
             [0, focal_length, center[1]],
             [0, 0, 1]], dtype="double"
        )



        if iter%1==0:

            if ret == False:
                break
            imgx = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgx = cv2.resize(imgx, (320, 320))
            imgx = imgx.astype(np.float32)
            imgx = np.expand_dims(imgx, 0)
            imgx = imgx / 255
            class_names = [c.strip() for c in open("Data/Models/classes.TXT").readlines()]
            boxes, scores, classes, nums = yolo(imgx)
            count = 0
            for i in range(nums[0]):
                if int(classes[0][i] == 0):
                    count += 1
                if int(classes[0][i] == 67):
                    print('Mobile Phone detected')
                    mobile_phones="True"
            if count == 0:
                print('No person detected')
            elif count > 1:
                print('More than one person detected')
            total_person=count









        #cv2.imshow("Output", image)
        # cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty("Output", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # cv2.imshow("Output", image)

        if iter%1==0:


            for rect in rects:

                marks = detect_marks(img, landmark_model, rect)
                # mark_detector.draw_marks(img, marks, color=(0, 255, 0))
                image_points = np.array([
                    marks[30],  # Nose tip
                    marks[8],  # Chin
                    marks[36],  # Left eye left corner
                    marks[45],  # Right eye right corne
                    marks[48],  # Left Mouth corner
                    marks[54]  # Right mouth corner
                ], dtype="double")
                dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
                (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix,
                                                                              dist_coeffs, flags=cv2.SOLVEPNP_UPNP)

                # Project a 3D point (0, 0, 1000.0) onto the image plane.
                # We use this to draw a line sticking out of the nose

                (nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), rotation_vector,
                                                                 translation_vector, camera_matrix, dist_coeffs)

                for p in image_points:
                    cv2.circle(img, (int(p[0]), int(p[1])), 3, (0, 0, 255), -1)

                p1 = (int(image_points[0][0]), int(image_points[0][1]))
                p2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
                x1, x2 = head_pose_points(img, rotation_vector, translation_vector, camera_matrix)

                cv2.line(img, p1, p2, (0, 255, 255), 1)
                cv2.line(img, tuple(x1), tuple(x2), (255, 255, 0), 1)
                # for (x, y) in marks:
                #     cv2.circle(img, (x, y), 4, (255, 255, 0), -1)
                # cv2.putText(img, str(p1), p1, font, 1, (0, 255, 255), 1)
                try:
                    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
                    ang1 = int(math.degrees(math.atan(m)))
                except:
                    ang1 = 90

                try:
                    m = (x2[1] - x1[1]) / (x2[0] - x1[0])
                    ang2 = int(math.degrees(math.atan(-1 / m)))
                except:
                    ang2 = 90

                    # print('div by zero error')
                if ang1 >= 48:
                    head_position="Head down"
                    # print('Head down')
                    # cv2.putText(img, 'Head down', (30, 30), font, 2, (255, 255, 128), 3)
                elif ang1 <= -48:
                    head_position="Head up"
                    # print('Head up')
                    # cv2.putText(img, 'Head up', (30, 30), font, 2, (255, 255, 128), 3)

                if ang2 >= 48:
                    head_position="Head right"
                    # print('Head right')
                    # cv2.putText(img, 'Head right', (90, 30), font, 2, (255, 255, 128), 3)
                elif ang2 <= -48:
                    head_position="Head left"
                    # print('Head left')
                    # cv2.putText(img, 'Head left', (90, 30), font, 2, (255, 255, 128), 3)

                print(p1,x1)

                cv2.putText(img, str(ang1), tuple(p1), font, 0.5, (128, 255, 255), 1)
                cv2.putText(img, str(ang2), tuple(x1), font, 0.5, (255, 255, 128), 1)








                shape = marks
                cnt_outer = 0
                cnt_inner = 0
                draw_marks(img, shape[48:], color=(0, 255, 0))
                draw_marks(img, shape[0:48], color=(52, 235, 155))
                cv2.imshow("Output", img)
                for i, (p1, p2) in enumerate(outer_points):
                    if d_outer[i] + 3 < shape[p2][1] - shape[p1][1]:
                        cnt_outer += 1
                for i, (p1, p2) in enumerate(inner_points):
                    if d_inner[i] + 2 < shape[p2][1] - shape[p1][1]:
                        cnt_inner += 1
                if cnt_outer > 3 and cnt_inner > 2:
                    mouth_open="True"
                    # print('Mouth open')
                    # cv2.putText(img, 'Mouth open', (30, 30), font,
                    #             1, (0, 255, 255), 2)




        iter+=1

        # cv2.putText(img, text, (660, img.shape[0] - 45),
        #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

        cv2.putText(img, "INTELEGIX (Online Exam Proctoring System)", (80, 40),
                    font, 0.7, (255, 255, 255), 2)
        cv2.rectangle(img, (20, 50), (W-20, 15), (255, 255, 255), 2)
        # cv2.putText(img, "RISK ANALYSIS", (30, 85),
        #             font, 0.5, (255, 255, 0), 1)
        # cv2.putText(img, "-- GREEN : SAFE", (H-100, 85),
        #             font, 0.5, (0, 255, 0), 1)
        # cv2.putText(img, "-- RED: UNSAFE", (H-200, 85),
        #             font, 0.5, (0, 0, 255), 1)

        tot_str = "Head Position : " + str(head_position)
        high_str = "Mouth Open : " + str(mouth_open)
        low_str = "Mobile Phone Detected : " + str(mobile_phones)
        safe_str = "Total Persons: " + str(total_person)

        sub_img = img[H - 100: H, 0:260]
        black_rect = np.ones(sub_img.shape, dtype=np.uint8) * 0

        res = cv2.addWeighted(sub_img, 0.8, black_rect, 0.2, 1.0)

        img[H - 100:H, 0:260] = res

        cv2.putText(img, tot_str, (10, H - 80),
                    font, 0.5, (255, 255, 255), 1)
        cv2.putText(img, high_str, (10, H - 55),
                    font, 0.5, (0, 255, 0), 1)
        cv2.putText(img, low_str, (10, H - 30),
                    font, 0.5, (0, 120, 255), 1)
        cv2.putText(img, safe_str, (10, H - 5),
                    font, 0.5, (0, 0, 150), 1)

        now = datetime.now()
        # cv2.imwrite(str("Data/Saved_Images/CLASS_ENVIRONMENT/") + str(now.strftime("%Y%m%d%H%M%S") + str(".jpg")), img)

        # cv2.putText(img, str(now.strftime("%d-%m-%Y% %H:%M:%S")), (W-10, H - 5),
        #             font, 0.5, (0, 0, 150), 1)
        timex=str(now.strftime("%d/%m/%Y %H:%M:%S"))
        cv2.putText(img, timex, (W - 200, H - 10),
                    font, 0.5, (255, 255, 255), 1)

        #
        # # cv2.imshow("Social Distancing Detector", frame)
        #
        # cv2.rectangle(img, (300, H - 100), (620, H - 10), (170, 170, 170), 1)
        # cv2.putText(img, "ANALYSIS", (325, H - 50),
        #             font, 0.5, (255, 255, 0), 2)
        # cv2.putText(img, "-- RED   : VIOLATION ", (420, H - 70),
        #             font, 0.5, (0, 0, 255), 1)
        # cv2.putText(img, "-- GREEN : OK ", (420, H - 35),
        #             font, 0.5, (0, 255, 0), 1)

        if mouth_open == "False" and head_position == "" and mobile_phones=="False" and total_person==1:
            image = draw_outputs(img, (boxes, scores, classes, nums), class_names, color=(0, 255, 0))
            cv2.circle(img, (25, 80), 10, (0, 255, 0), -1)
            cv2.putText(img, "All Ok", (50, 85),
                        font, 0.5, (0, 255, 0), 2)

            if total_person == 0:
                telegx += 1
                if telegx>2:
                    now = datetime.now()
                    cv2.imwrite(str("Data/Saved_Images/EXAM_ENVIRONMENT/")+str(now.strftime("%Y%m%d%H%M%S")+str(".jpg")),img)
                if telegx > 5:
                    cv2.imwrite("Fraud.jpg", img)
                    threading.Thread(target=telegram).start()
                    telegx = 0

            else:
                telegx = 0

        else:
            image = draw_outputs(img, (boxes, scores, classes, nums), class_names, color=(0, 0, 255))
            cv2.circle(img, (25, 80), 10, (0, 0, 255), -1)
            cv2.putText(img, "Fraud Detected", (50, 85),
                        font, 0.5, (0, 0, 255), 2)


            telegx += 1
            print(telegx)
            if telegx>2:
                now = datetime.now()
                cv2.imwrite(str("Data/Saved_Images/EXAM_ENVIRONMENT/") + str(now.strftime("%Y%m%d%H%M%S") + str(".jpg")), img)
            if telegx > 5:
                cv2.imwrite("Fraud.jpg", img)
                threading.Thread(target=telegram).start()
                telegx = 0

        head_position = ""
        mouth_open = "False"
        mobile_phones="False"
        total_person=0



        cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Output", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Output", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    AI_PROCTORING(path=0)


