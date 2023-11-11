from PIL import Image
import os
fileTypes = ('jpg', 'png', 'jpeg')
images = [img for img in os.listdir('toConvert') if img.endswith(fileTypes)]

print(f"Mevcut dizinde {len(images)} adet görsel bulundu:\n{images}\n")
fileCounter = 0

def convertImage(imgPath, imgType):
    i = Image.open(f"toConvert\\{imgPath}")
    i = i.convert('RGB')
    imgName = imgPath.split('.')[0]
    if imgType == 'jpg' or imgType == 'jpeg' or imgType == 'png':
        i.save(f"Converted\\{imgName}.webp", 'webp')
        print(f"{imgPath}  >>>  {imgName}.webp")

for img in images:
    convertImage(img, img.split('.')[-1])
    fileCounter += 1


print(f"\n{fileCounter} adet görsel başarıyla dönüştürüldü\n")