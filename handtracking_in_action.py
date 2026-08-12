import cv2
import mediapipe as mp
import pyfirmata2
import numpy as np

board = pyfirmata2.Arduino('COM3')

s_index = board.get_pin('d:9:s') # Digital Pin 9, servo - s
s_middle = board.get_pin('d:10:s') # middle finger - pin 10
s_ring = board.get_pin('d:11:s') # ring finger - pin 11
s_pinky = board.get_pin('d:6:s') # pinky finger - pin 6

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands=1)

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    if success:
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hand.process(rgb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                h, w, _ = img.shape
                lm = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks.landmark]

                hand_size = np.linalg.norm(np.array(lm[0]) - np.array(lm[9]))

                index_tip = lm[8]
                index_lowtip = lm[7]
                index_highbase = lm[6]
                index_base = lm[5]

                middle_tip = lm[12]
                middle_lowtip = lm[11]
                middle_highbase = lm[10]
                middle_base = lm[9]

                ring_tip = lm[16]
                ring_lowtip = lm[15]
                ring_highbase = lm[14]
                ring_base = lm[13]

                pinky_tip = lm[20]
                pinky_lowtip = lm[19]
                pinky_highbase = lm[18]
                pinky_base = lm[17]


                # index finger
                cv2.circle(img, index_tip, 10, (0, 255, 0), -1)
                '''cv2.circle(img, index_lowtip, 10, (0, 255, 0), -1)
                cv2.circle(img, index_highbase, 10, (0, 0, 255), -1)'''
                cv2.circle(img, index_base, 10, (0, 0, 255), -1)
                # middle finger
                cv2.circle(img, middle_tip, 12, (0, 255, 0), -1)
                '''cv2.circle(img, middle_lowtip, 10, (0, 255, 0), -1)
                cv2.circle(img, middle_highbase, 10, (0, 0, 255), -1)'''
                cv2.circle(img, middle_base, 12, (0, 0, 255), -1)
                # ring finger
                cv2.circle(img, ring_tip, 10, (0, 255, 0), -1)
                '''cv2.circle(img, ring_lowtip, 10, (0, 255, 0), -1)
                cv2.circle(img, ring_highbase, 10, (0, 0, 255), -1)'''
                cv2.circle(img, ring_base, 10, (0, 0, 255), -1)
                # pinky finger
                cv2.circle(img, pinky_tip, 10, (0, 255, 0), -1)
                '''cv2.circle(img, pinky_lowtip, 10, (0, 255, 0), -1)
                cv2.circle(img, pinky_highbase, 10, (0, 0, 255), -1)'''
                cv2.circle(img, pinky_base, 10, (0, 0, 255), -1)



                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            #prev_angle = 90

            # DISTANCES:

            # index finger distance
            # index tip
            distance_indextip_to_base = np.linalg.norm(np.array(index_tip) - np.array(index_base))
            '''distance_indextip_to_lowtip = np.linalg.norm(np.array(index_tip) - np.array(index_lowtip))
            distance_indextip_to_highbase = np.linalg.norm(np.array(index_tip) - np.array(index_highbase))'''
            normalized_index = distance_indextip_to_base / hand_size * 100

            '''# index lowtip
            distance_indexlowtip_to_base = np.linalg.norm(np.array(index_lowtip) - np.array(index_base))
            distance_indexlowtip_to_highbase = np.linalg.norm(np.array(index_lowtip) - np.array(index_highbase))

            # index highbase
            distance_indexhighbase_to_base = np.linalg.norm(np.array(index_highbase) - np.array(index_base))'''


            # middle finger distance
            # middle tip
            distance_middletip_to_base = np.linalg.norm(np.array(middle_tip) - np.array(middle_base))
            normalized_middle = distance_middletip_to_base / hand_size * 100
            '''distance_middletip_to_lowtip = np.linalg.norm(np.array(middle_tip) - np.array(middle_lowtip))
            distance_middletip_to_highbase = np.linalg.norm(np.array(middle_tip) - np.array(middle_highbase))

            # middle lowtip
            distance_middlelowtip_to_base = np.linalg.norm(np.array(middle_lowtip) - np.array(middle_base))
            distance_middlelowtip_to_highbase = np.linalg.norm(np.array(middle_lowtip) - np.array(middle_highbase))

            # middle highbase
            distance_middlehighbase_to_base = np.linalg.norm(np.array(middle_highbase) - np.array(middle_base))'''


            # pinky finger distance
            # pinky tip
            distance_pinkytip_to_base = np.linalg.norm(np.array(pinky_tip) - np.array(pinky_base))
            normalized_pinky = distance_pinkytip_to_base / hand_size * 100
            '''distance_pinkytip_to_lowtip = np.linalg.norm(np.array(pinky_tip) - np.array(pinky_lowtip))
            distance_pinkytip_to_highbase = np.linalg.norm(np.array(pinky_tip) - np.array(pinky_highbase))

            # pinky lowtip
            distance_pinkylowtip_to_base = np.linalg.norm(np.array(pinky_lowtip) - np.array(pinky_base))
            distance_pinkylowtip_to_highbase = np.linalg.norm(np.array(pinky_lowtip) - np.array(pinky_highbase))

            # pinky highbase
            distance_pinkyhighbase_to_base = np.linalg.norm(np.array(pinky_highbase) - np.array(pinky_base))
'''

            # ring finger distance
            # ring tip
            distance_ringtip_to_base = np.linalg.norm(np.array(ring_tip) - np.array(ring_base))
            normalized_ring = distance_ringtip_to_base / hand_size * 100
            '''distance_ringtip_to_lowtip = np.linalg.norm(np.array(ring_tip) - np.array(ring_lowtip))
            distance_ringtip_to_highbase = np.linalg.norm(np.array(ring_tip) - np.array(ring_highbase))

            # ring lowtip
            distance_ringlowtip_to_base = np.linalg.norm(np.array(ring_lowtip) - np.array(ring_base))
            distance_ringlowtip_to_highbase = np.linalg.norm(np.array(ring_lowtip) - np.array(ring_highbase))

            # ring highbase
            distance_ringhighbase_to_base = np.linalg.norm(np.array(ring_highbase) - np.array(ring_base))'''

            print(normalized_pinky)
            # ANGLES:

            # index finger angle
            normalized_index = np.clip(normalized_index,0 ,95)
            angle_indextip_to_base = np.interp(normalized_index, [0, 95], [90, 0])
            # middle finger angle
            normalized_middle = np.clip(normalized_middle, 0, 105)
            angle_middletip_to_base = np.interp(normalized_middle, [0, 105], [55, 0])
            # ring finger angle
            normalized_ring = np.clip(normalized_ring, 0, 90)
            angle_ringtip_to_base = np.interp(normalized_ring, [0, 90], [105, 0])
            # pinky finger angle
            normalized_pinky = np.clip(normalized_pinky, 0, 75)
            angle_pinkytip_to_base = np.interp(normalized_pinky, [0, 75], [90, 0])
            print('angle:', angle_indextip_to_base)
            #smoothed_angle = prev_angle*0.7 + angle*0.3

            # WRITINGS

            # index finger
            s_index.write(angle_indextip_to_base)
            # middle finger
            s_middle.write(angle_middletip_to_base)
            # ring finger
            s_ring.write(angle_ringtip_to_base)
            # pinky finger
            s_pinky.write(angle_pinkytip_to_base)

            #prev_angle = smoothed_angle

        cv2.imshow('capture image', img)
        if cv2.waitKey(1) == ord('a'):  # ord gets the number value from the letter so it can use it for the boolean, a = 97 so instead of typing 97 we can type that.
            break

        '''cap.release()
        cv2.destroyAllWindows()
        board.exit()'''
