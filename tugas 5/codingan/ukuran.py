import cv2
import numpy as np

images= [cv2.imread("F:/semester5/citra digital/tugas 5/WhatsApp Image 2024-11-04 at 22.28.12.jpeg"),
         cv2.imread("C:/Users/k-ruko/Downloads/WhatsApp Image 2024-11-04 at 22.55.27.jpeg")]

# images[0] = cv2.bilateralFilter(images[0], 3, 100, 100)

closeIterations = [2, 10]
openIterations = [10, 10]
kernelOpen = np.ones((5,5), np.uint8)
kernelClose = np.ones((5,5), np.uint8)

for i in range(len(images)):
    images[i] = cv2.resize(images[i], (640, 480))
    gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Melakukan operasi closing dan opening pada citra
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernelClose, iterations = closeIterations[i])
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen, iterations = openIterations[i])

    # Segmentasi citra
    segment = cv2.Canny(opening, 200, 200)
    contours, hierarchy = cv2.findContours(segment, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    segment = cv2.cvtColor(segment, cv2.COLOR_GRAY2RGB)
    cv2.drawContours(images[i], contours, -1, (0, 0, 255), 1)

    #Segmentasi, clustering, pemberian label, dan menghitung parameter pada citra
    centers = []
    for j in range(len(contours)):
        # Segmentasi, clustering dan pemberian label
        moments = cv2.moments(contours[j])
        centers.append((int(moments['m10']/moments['m00']), int(moments['m01'] / moments['m00']))) # Mencari centroid
        cv2.circle(images[i], centers[-1], 1, (0, 0, 255), -1) # Menggambar bulat pada centroid
        cv2.putText(images[i], str(j+1), centers[-1], cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 255, 255), 1) # Memberi nomor pada centroid

        # Menghitung parameter
        (x, y), (minorAxis, majorAxis), angle = cv2.fitEllipse(contours[j]) # Mengambil minor dan major axis
        area = round(cv2.contourArea(contours[j]),2)
        perimeter = round(cv2.arcLength(contours[j], True),2)

        offset = (centers[-1][0] + 0, centers[-1][1] + 20)
        cv2.putText(images[i], str("Area = " + str(area)), offset, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)
        offset = (centers[-1][0] + 0, centers[-1][1] + 40)
        cv2.putText(images[i], str("Perimeter = " + str(perimeter)), offset, cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

for i in range(len(images)):
    cv2.imshow(f'Gambar {i+1}', images[i])
cv2.waitKey(0)
cv2.destroyAllWindows()
