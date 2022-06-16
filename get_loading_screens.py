import os
import requests
from PIL import Image

max     = 87
banlist = [1,14,33,38,72,73,74,75,80,81]

def check_size(file):
    im = Image.open(file)
    width, height = im.size
    return width, height

def output():
    output = list(range(1,max+1))
    for element in banlist:
        output.remove(element)

    print(str(output).replace(",", " "))
    print("TOTAL = ", len(output))

def get_pictures():
    for number in range(max, 0, -1):
        try:
            url      = "https://www.grandtheftauto5.fr/images/artworks-officiels/gta5-artwork-{0}-hd.jpg".format(number)
            path     = "./wallpapers/"
            filename = "gta5_wallpaper{0}.jpg".format(number)

            response = requests.get(url)
            open(path + filename, "wb").write(response.content)
            print("Saved element   #{0}".format(number))

            if check_size(path + filename) != (1920, 1200) or number in banlist:
                os.remove(path + filename)
                print("Deleted element #{0}".format(number))

        except:
            try:
                os.remove(path + filename)
            except:
                pass

            print("Failed for number {0}".format(number))

    output()

if __name__ == "__main__":
    get_pictures()

