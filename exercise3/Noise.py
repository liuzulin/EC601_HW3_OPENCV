import cv2
import numpy as np
import copy

def Add_salt_pepper_Noise(image,pa,pb):
    row,col,ch = image.shape
    out = copy.deepcopy(image)
    # Salt mode
    num_salt = row*col*pb
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = row*col*pa
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
    out[coords] = 0
    return out

def Add_gaussian_Noise(image,mean,sigma):
    image_noise = copy.deepcopy(image)
    im = np.zeros(image.shape, np.uint8)
    cv2.randn(im,mean,sigma) # create the random distribution
    image_noise=cv2.add(image_noise, im)
    return image_noise

def main():
    image = cv2.imread('Test_images/Lenna.png')
    try:
        image.shape
        print("checked for shape".format(image.shape))
    except AttributeError:
        print("shape not found")
    image_gau = Add_gaussian_Noise(image,0,50)
    image_sp = Add_salt_pepper_Noise(image,0.01,0.01)
    cv2.imshow("original image", image)
    cv2.imshow("Add gaussian Noise", image_gau)
    cv2.imshow("Add a&p Noise", image_sp)

    image_box = cv2.blur(image_gau,(3,3))   
    cv2.imshow("gua_noise Box filter", image_box)
    
    image_gau_filter = cv2.GaussianBlur(image_gau,(3,3),1.5)
    cv2.imshow("gua_noise Gaussian filter", image_gau_filter)
    
    iamge_median = cv2.medianBlur(image_gau,3)
    cv2.imshow("gua_noise Median filter", iamge_median)
      
    image_box = cv2.blur(image_sp,(3,3))   
    cv2.imshow("a&p Noise Box filter", image_box)
    
    image_gau_filter = cv2.GaussianBlur(image_sp,(3,3),1.5)
    cv2.imshow("a&p Noise Gaussian filter", image_gau_filter)
    
    image_median = cv2.medianBlur(image_sp,3)    
    cv2.imshow("a&p Noise Median filter", image_median)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows() ## Destroy all windows
main()