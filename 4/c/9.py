# Import the necessary modules
from skimage.restoration import denoise_tv_chambolle, ____
from skimage import transform

# Transform the image so it's not rotated
upright_img = ____(damaged_image, 20)

# Remove noise from the image, using the chambolle method
upright_img_without_noise = ____(upright_img,weight=0.1, multichannel=True)

# Reconstruct the image missing parts
mask = get_mask(upright_img)
result = ____.____(upright_img_without_noise, mask, multichannel=True)

show_image(result)
