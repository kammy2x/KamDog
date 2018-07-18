def setup():
    size(400,400)
    pic = loadImage("colorful.jpg")
    image(pic, 0, 0)
    loadPixels()
    for i in range (len(pixels)):
        currentPixel = pixels[i]
        pixelRed = red(currentPixel)
        pixelGreen = green(currentPixel)
        pixelBlue = blue(currentPixel)
        pixelRed = 255 - pixelRed
        pixelGreen = 255 - pixelGreen
        pixelBlue = 225 - pixelBlue
        newColor = color(pixelRed, pixelGreen, pixelBlue)
        pixels[i] = newColor
    updatePixels()
