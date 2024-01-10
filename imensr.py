import cv2

# Load the image
image_path = r"demo-repo\images\paris-street-musicians.jpg"
image = cv2.imread(image_path)

# Display the image
cv2.imshow('Image', image)

# Function to get mouse click coordinates
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Coordinates: ({x}, {y})')

# Set the callback function for mouse events
cv2.setMouseCallback('Image', get_coordinates)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()