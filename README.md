# Arrow Direction Detection using OpenCV

**This program detects the direction an arrow is pointing in an image using OpenCV in Python.**

## How it Works

1. Capture video frame and convert to grayscale.
2. Apply Canny edge detection to find edges.
3. Find contours and filter for large contours that are likely the arrow.
4. Approximate the arrow contour to get vertex points.
5. Calculate the midpoint of the vertices.
6. Use the vector between midpoint and the first vertex to determine direction.
7. Check the angle of the direction vector to determine which direction the arrow is pointing:
   - Right: -45 to 45 degrees
   - Left: 135 to 180 or -180 to -135 degrees
8. Draw vertices, midpoint, and direction text on the original frame.
9. Display video with detected arrow direction.

## Usage

1. Run the Python script to display the video feed with arrow detection.
2. Point an arrow towards the camera, and the direction will be printed and drawn on the frame.
3. Press 'q' to quit.

## Customizing

- Tweak the Canny threshold values to better detect arrow edges.
- Adjust the contour area filter as needed for arrow size.
- Modify angle ranges for direction detection as desired.
- Change midpoint and vertex circle colors and sizes.

## Dependencies

- OpenCV
- NumPy
- Math

---

**Note:** Replace this text with your own details as needed.
