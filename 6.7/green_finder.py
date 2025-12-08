import time

t0 = time.time()

from PIL import Image

counter = 0

pics = []

tree = "6.7/tree.png"
pics.append(tree)

bliss = "6.7/bliss.png"
pics.append(bliss)

pepper = "6.7/bellpepper.png"
pics.append(pepper)

parrot = "6.7/parrot.png"
pics.append(parrot)

def colour(r, g, b):
        if  (37 <= r <= 50 and 150 <= g):
            return "green"

for file in pics:
    file1 = Image.open(file)
    jbImage = file1.load()

    t1 = time.time()

    width = file1.width
    height = file1.height

    t1 = time.time()


    greenPixels = []

    for x in range(width):
        for y in range(height):
            pixel_r = jbImage[x, y][0]
            pixel_g = jbImage[x, y][1]
            pixel_b = jbImage[x, y][2]

            if colour(pixel_r, pixel_g, pixel_b) == "green":
                greenPixels.append(jbImage[x, y])
                counter += 1


    t2 = time.time()

    numGreen = len(greenPixels)

    totalPixels = width*height
    greenRatio = numGreen / totalPixels

    greenPercent = greenRatio * 100

    t3 = time.time()



    module_load = t1 - t0
    image_open_load = t2 - t1
    loop = t3-t2
    entire = t3 - t0

    rating = (counter / totalPixels) * 100

    if rating < 10:
        print("This picture is bad, not enough green, it makes me really mad >>:(")
    elif rating < 20:
        print("This picture is not bad, but not enough green, it makes me mad >:(")
    elif rating < 50:
        print("This picture is mid, not enough green, but it's better than nothing :|")
    elif rating < 75:
        print("This picture is good, a good amount of green, it makes happy :)")
    elif rating < 90:
        print("This picture is soooo good, enough green to last for a long time, it makes me very happy :)))")
    elif rating <= 100:
        print("This is too much green, why do you need so much")

    timings = "It took {:.2f}s to import the PIL, {:.2f}s to load the image, and {:.2f}s to do the loop. All in all it took {:.2f}s.".format(module_load, image_open_load, loop, entire)
    print(timings)
    perc = "{:.3f}% of the picture is green".format(rating)
    print(perc)