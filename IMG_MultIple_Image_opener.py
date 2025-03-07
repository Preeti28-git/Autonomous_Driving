import cv2 # type: ignore

def process_multiple_images(image_paths):
  for image_path in image_paths:
    image = cv2.imread(image_path)

    if image is None:
      print(f"Error: Could not read the image at {image_path}")
    else:
      
      cv2.imshow('Image', image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
      print(f"Dimensions of image {image_path}: {image.shape}") 

image_paths = ["radha krishna1.jpg", "park.jpg", "nature2.jpg"]
process_multiple_images(image_paths)