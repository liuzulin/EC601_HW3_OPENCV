import cv2


def main():
    image_path ="Test_images/Lenna.png"
    image = cv2.imread(image_path,1)
    gray_img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('input image')
    cv2.imshow('input image', gray_img)
    
    threshold_value = 128
    
    T, thresh = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_TRUNC)# 255 here is unuseful!
    cv2.imshow("Thresholded Image", thresh)
    
    T, thresh_binary = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary threshold", thresh_binary)
    
    T, thresh_binary_1 = cv2.threshold(gray_img, 27, 255, cv2.THRESH_BINARY)
    T, thresh_binary_2 = cv2.threshold(gray_img, 125, 255, cv2.THRESH_BINARY_INV)
    band_thresholded_image = cv2.bitwise_and(thresh_binary_1,thresh_binary_2)
    cv2.imshow("Band Thresholding", band_thresholded_image)
    
    ret2,Semi = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    Semi = cv2.bitwise_and(gray_img,Semi)
    cv2.imshow("Semi Thresholding", Semi)
    
    adaptive_thresh = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
    cv2.imshow("Adaptive Thresholding", adaptive_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows() ## Destroy all windows
main()