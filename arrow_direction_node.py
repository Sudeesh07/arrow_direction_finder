#!/usr/bin/env python

import cv2
import math
import rospy
from std_msgs.msg import String

def main():
    cap = cv2.VideoCapture(0)

    rospy.init_node('arrow_direction_publisher')  

    direction_publisher = rospy.Publisher('direction', String, queue_size=10)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not ret:
            break
        edges = cv2.Canny(gray, 150, 250)
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        arrow_contour = None

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if 4000 < area:
                arrow_contour = cnt
                break

        if arrow_contour is not None:
            epsilon = 0.02 * cv2.arcLength(arrow_contour, True)
            approx = cv2.approxPolyDP(arrow_contour, epsilon, True)
            vertices = approx.reshape((-1, 2))

            for vertex in vertices:
                cv2.circle(frame, (vertex[0], vertex[1]), 5, (0, 255, 0), -1) 
            
            x_midpoint = int(sum(vertices[:, 0]) / len(vertices))
            y_midpoint = int(sum(vertices[:, 1]) / len(vertices))
            cv2.circle(frame, (x_midpoint, y_midpoint), 5, (255, 0, 0), -1)  # Draw midpoint in red

            direction_vector = (vertices[0][0] - x_midpoint, vertices[0][1] - y_midpoint)
            angle = math.degrees(math.atan2(direction_vector[1], direction_vector[0]))
            direction_text = f"Direction: {angle:.2f} degrees"
            cv2.putText(frame, direction_text, (x_midpoint - 100, y_midpoint - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            if angle >= -45 and angle < 45:
                direction = "RIGHT"
            elif angle >= 45 and angle < 135:
                direction = "DOWN"
            elif angle >= -180 and angle <= -135:
                direction = "LEFT"
            elif angle >= 135 and angle <= 180:
                direction = "LEFT"

            direction_publisher.publish(direction)  # Publish the direction as a ROS message


        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
