My code is looking for the amount of green in an image, and calculating it's percentage by
subtracting the amount of green pixels from the total pixel count. 
My is_target_feature function is basically the colour function, both have the same purpose.
In terms of testing, I have checked each of the 10 images, and it correctly identifies all green pixels in them, it goes through every pixel, and checks if it's in the range I've set of green shades, if it is, a counter is increased by 1, and whatever that toal amount is, is divided by the total amount of pixels in the image, and then added to a list
My code was taking pixels that were blue, or white, so I needed to tweak the values I set to determine of a pixel is green, and that fixed my code.
My binary sort is kinda useless and doesn't do anything cuz i don't know what to do with it