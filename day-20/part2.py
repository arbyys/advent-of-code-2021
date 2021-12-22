from aocd import get_data

data = get_data(day=20, year=2021)
data = data.split("\n\n")

enhancement = data[0]
image = data[1].splitlines()

def returnBiggerPixelDecimal(image, xPos, yPos, num):
    returnPixel = []
    for yPosNew in range(yPos-1, yPos+2):
        for xPosNew in range(xPos-1, xPos+2):
            if((yPosNew < 0) or (xPosNew < 0) or (yPosNew > len(image)-1) or (xPosNew > len(image[0])-1)):
                if(num % 2 == 0):
                    pixel = "#"
                else:
                    pixel = "."
            else:
                pixel = image[yPosNew][xPosNew]
            returnPixel.append(pixel)
    returnPixel = ["0" if i=="." else "1" if i=="#" else i for i in returnPixel]
    return int("".join(returnPixel),2)

def enhanceImage(image, numIndex):
    enhancedImage = []
    for num,yIndex in enumerate(range(len(image))):
        row = ""
        for xIndex in range(len(image[0])):
            decimalValue = returnBiggerPixelDecimal(image, xIndex, yIndex, numIndex)
            row += enhancement[decimalValue]
        enhancedImage.append(row)
    return enhancedImage

def replaceStr(s, position, character):
    return s[:position] + character + s[position+1:]

def extendImage(image, num):
    if(num % 2 == 0):
        CHAR_TO_PAD = "#"
    else:
        CHAR_TO_PAD = "."
    for idx,item in enumerate(image):
        image[idx] = "{}{}{}{}{}".format(CHAR_TO_PAD, CHAR_TO_PAD, item, CHAR_TO_PAD, CHAR_TO_PAD)
    for i in range(2):
        image.insert(0,CHAR_TO_PAD*len(image[0]))
    for i in range(2):
        image.append(CHAR_TO_PAD*len(image[0]))
    return image

NUMBER_OF_STEPS = 50

for step in range (1, NUMBER_OF_STEPS+1):
    image = extendImage(image, step)
    image = enhanceImage(image, step)
    print("step {}/{}".format(step, NUMBER_OF_STEPS))

for i in range(3):
    del image[0]
for i in range(3):
    image.pop()
for index,r in enumerate(image):
    image[index] = r[3:-3]

counter = 0
for row in image:
    for char in row:
        if char == "#":
            counter += 1

print(counter)
