# Author : Dongyoon Kim
# Explain : Practicing the coloring process.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# Read in the image and print out some stats
image = mpimg.imread('test.jpg')

print('This image is ',type(image),
      'with dimensions:',image.shape)

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]

# Note : always make a copy rather than simply using "="
region_select = np.copy(image)



# Define a triangle region of interest 관심있는 부분 설정
# Keep in mind the origin(x=0, y=0) is in the upper left in image processing
# Note : if you run this code, you'll find these are not sensible values
# But you'll get a chance to play with them soon in a quiz
left_bottom = [0,539]
right_bottom = [959,539]
apex = [460,310]

# Fit lines (y=Ax+B) to identify the 3 sided region of interest
# np.polyfit() returns the coefficients [A,B] of the fit
fit_left = np.polyfit((left_bottom[0],apex[0]),(left_bottom[1],apex[1]),1)
fit_right = np.polyfit((right_bottom[0],apex[0]),(right_bottom[1],apex[1]),1)
fit_bottom = np.polyfit((left_bottom[0],right_bottom[0]),(left_bottom[1],right_bottom[1]),1)


# Find the region inside the lines
XX, YY = np.meshgrid(np.arange(0,xsize),np.arange(0,ysize))

region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0]+fit_right[1])) & \
                    (YY < (XX*fit_bottom[0]+fit_bottom[1]))



red_threshold = 220
green_threshold = 220
blue_threshold = 220
rgb_threshold = [red_threshold,green_threshold,blue_threshold]

# Identify pixels below the threshold
color_selected = ((image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2]))

# Mast color and region selection
region_select[color_selected] = [0,0,0]

# Color pixels red which are inside the region of interest
region_select[~color_selected & region_thresholds] = [255,0,0]

# Display the image
plt.imshow(region_select)

# Uncomment if plot does not display
plt.show()