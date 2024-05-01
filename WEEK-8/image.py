from PIL import image
image_path='/home/rguktrkvalley/Desktop/WEEK-8/Screenshot from 2022-05-23 18-26-43.png'
image=Image_open("/home/rguktrkvalley/Desktop/WEEK-8/Screenshot from 2022-05-23 18-26-43.png")
x,y=100,100
rgb=image.getpixel((x,y))
print('f,RGB values at position({x},{y}):{rgb}')
new_rgb=(255,0,0)
image.putpixel((x,y),new_rgb)
output_path="/home/rguktrkvalley/Desktop/WEEK-8/Screenshot from 2022-05-23 18-26-43.png"
image.save(output_path)
image.close()
