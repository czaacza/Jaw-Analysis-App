import cv2
# [print(i) for i in dir(cv2) if 'EVENT' in i]

# function to display the coordinates of
# of the points clicked on the image

last_coordinates = None

def click_event(event, x, y, flags, params):
    global last_coordinates
    currentCoordinates = (x,y)

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        if(last_coordinates is not None):
            print(calculateDistance(last_coordinates, currentCoordinates))
            cv2.line(img, currentCoordinates, last_coordinates, (0, 255, 0), thickness=1)

        # displaying the coordinates on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, '. ' + str(x) + ',' +
                    str(y), currentCoordinates, font,
                    0.5, (255, 0, 0), 2)
        cv2.imshow('image', img)
        last_coordinates = (x,y)


def calculateDistance(p1, p2):
    """p1 and p2 in format (x1,y1) and (x2,y2) tuples"""
    dis = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return dis


# driver function
if __name__ == "__main__":
    # reading the image
    img = cv2.imread('img.png', 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse hadler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()