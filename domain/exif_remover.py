from PIL import Image

image = Image.open('../test.jpg')

image = image.resize((int(image.width / (image.width/400)), int(image.height / (image.height/300))))

data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)

image_without_exif.save('image_file_without_exif.jpeg')

