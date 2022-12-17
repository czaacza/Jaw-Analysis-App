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
        font = cv2.FONT_HERSHEY_SIMPLEX

        if(last_coordinates is not None):
            cv2.line(img, currentCoordinates, last_coordinates, (0, 255, 0), thickness=1)
            cv2.putText(img, str(calculateDistance(last_coordinates, currentCoordinates)), calculateMiddleOfTwoPoints(last_coordinates, currentCoordinates), font, 0.5, (255, 0, 0), 2)

        
        cv2.imshow('image', img)
        last_coordinates = (x,y)


def calculateDistance(p1, p2):
    return  round(((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5, 2)
    

def calculateMiddleOfTwoPoints(p1, p2):
    return (round((p2[0] + p1[0]) / 2) , round((p2[1] + p1[1]) / 2))

# driver function
if __name__ == "__main__":
    point1 = (3, 3)
    point2 = (-4, -7)
    print(calculateMiddleOfTwoPoints(point1, point2))
    # reading the image
    img = cv2.imread('jaw.jpeg', 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse hadler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()