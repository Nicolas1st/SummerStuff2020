import cv2
import numpy as np


#  loading the NN
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

#  what classes are here
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


def detect_objects(img):

    height, width, channels = img.shape

    #  Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    people_found = 0

    # showing information
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.7 and class_id == 0:

                people_found += 1

                # object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                upper_left = (center_x - w // 2, center_y - h // 2)
                lower_right = (center_x + w // 2, center_y + h // 2)
                green = (0, 255, 0)

                cv2.rectangle(img, pt1=lower_right, pt2=upper_left, color=green, thickness=3)

                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, f'Person {people_found}', upper_left, font, 0.5, (200, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, f'People found: {people_found}', (15, 15), font, 0.5, (200, 255, 255), 1, cv2.LINE_AA)

    return img


print('Choose an option (Camera - 1, video - 2, image - 3)')
choosing = True
while choosing:

    choice = input('Input: ')
    if choice not in '123':
        continue

    if choice == '1':
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            frame = detect_objects(frame)
            cv2.imshow('Image', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break

    elif choice == '2':
        video = input('Enter the path to the video: ')
        cap = cv2.VideoCapture(video)

        while cap.isOpened():
            ret, frame = cap.read()

            frame = detect_objects(frame)
            cv2.imshow('Image', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break

    elif choice == '3':

        img = input('Enter the path to the image: ')
        img = cv2.imread(img)

        img = detect_objects(img)
        cv2.imshow('Image', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
