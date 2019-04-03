# -*- coding: UTF-8 -*-
import Leap;
import sys;

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

#食指 TYPE_INDEX 1
#中指 TYPE_MIDDLE 2
#大拇指 TYPE_THUMB 0
#小指 TYPE_PINKY 4
#无名指 TYPE_RING 3

fig = plt.figure()
ax = Axes3D(fig)

plt.show()

def main():


    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

class SampleListener(Leap.Listener):

    def on_connect(self, controller):

        print "Connected"


    def on_frame(self, controller):


        print "Frame available"
        frame = controller.frame()
        hands = frame.hands
        if not hands.is_empty:
            hand = hands.rightmost
            if hand.is_right:
                print "right!"
                fingers = hand.fingers
                finger = fingers[1]
                finger_from_frame = frame.finger(finger.id)
                tips = finger_from_frame.tip_position


                # print "x: %d, y: %d, z: %d" % (tips.x, tips.y, tips.z)

                # ax.scatter(tips.x, tips.y, tips.z, c="b", marker="o")
                # plt.pause(0.05)

                # finger = fingers[0]
                # finger_from_frame0 = controller.frame.finger(finger.id)
                # print finger_from_frame0
                #
                # finger = fingers[1]
                # finger_from_frame1 = controller.frame.finger(finger.id)
                # print finger_from_frame1
                #
                # finger = fingers[2]
                # finger_from_frame = controller.frame.finger(finger.id)
                # print finger_from_frame
                #
                # finger = fingers[3]
                # finger_from_frame = controller.frame.finger(finger.id)
                # print finger_from_frame
                #
                # finger = fingers[4]
                # finger_from_frame = controller.frame.finger(finger.id)
                # print finger_from_frame

            else:
                print "left"
        print frame.current_frames_per_second
        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))




if __name__ == '__main__':
    main()
