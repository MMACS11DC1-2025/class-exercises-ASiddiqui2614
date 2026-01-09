import time

import sixseven_func as six

t0 = time.time()

from PIL import Image

pics = []

tree = "6.7/tree.png"
pics.append(tree)

bliss = "6.7/bliss.png"
pics.append(bliss)

pepper = "6.7/bellpepper.png"
pics.append(pepper)

parrot = "6.7/parrot.png"
pics.append(parrot)

flower = "6.7/green_flower.jpg"
pics.append(flower)

field = "6.7/greenfield.png"
pics.append(field)

field2 = "6.7/greenfield2.png"
pics.append(field2)

waterfall = "6.7/waterfall.png"
pics.append(waterfall)

leaf = "6.7/leaf.png"
pics.append(leaf)

leaf2 = "6.7/leaf2.png"
pics.append(leaf2)

ratinglist = []



for file in pics:
    file1 = Image.open(file)
    jbImage = file1.load()
    
    file2 = Image.open(file)

    t1 = time.time()

    width = file1.width
    height = file1.height
    counter = 0

    t1 = time.time()


    greenPixels = []

    for x in range(width):
        for y in range(height):
            pixel_r = jbImage[x, y][0]
            pixel_g = jbImage[x, y][1]
            pixel_b = jbImage[x, y][2]

            if six.colour(pixel_r, pixel_g, pixel_b) == "green":
                greenPixels.append(jbImage[x, y])
                file2.putpixel((x, y), (0, 255, 0))
                counter += 1
    file2.save(file + "_output.png")
    t2 = time.time()

    numGreen = len(greenPixels)

    totalPixels = width*height
    print(totalPixels)

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
    ratinglist.append(rating)
#print(ratinglist)

for i in range(len(ratinglist)):
    
    smallest_score = ratinglist[i]
    smallest_index = i

    for j in range(i+1, len(ratinglist)):
        if ratinglist[j] < smallest_score:
            smallest_score = ratinglist[j]
            smallest_index = j

    ratinglist[smallest_index], ratinglist[i] = ratinglist[i], ratinglist[smallest_index]

print(ratinglist)