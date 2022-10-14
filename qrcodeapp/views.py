from django.shortcuts import render
from django.conf import settings
import qrcode
import datetime
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import VerticalGradiantColorMask
from PIL import Image

#without color QR code Generator

# def qr_generate(request):
#     if request.method == 'POST':
#         data = request.POST['data']
#         img = qrcode.make(data)
#         img_name = 'QR-' + str(datetime.datetime.now().strftime('%d%b%Y-%H%M%S')) + '.png'
#         img.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
#         return render(request, 'index.html', {'img_name': img_name})
#     return render(request, 'index.html')


#with color QR code generator

# def qr_generate(request):
#     if request.method == 'POST':
#         data = request.POST['data']
#         qr = qrcode.QRCode(version=1, box_size=10, border=5, error_correction=qrcode.constants.ERROR_CORRECT_L)
#         qr.add_data(data)
#         qr.make(fit=True)
#         # img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
#         img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer(),\
#                             color_mask=SquareGradiantColorMask(), \
#                             embeded_image_path="/home/test/QRCodeGenerator/qrcodesite/images/microbiome.png",\
#                             eye_drawer=RoundedModuleDrawer(radius_ratio=2.5))
#         img_name = 'QR-' + str(datetime.datetime.now().strftime('%d%b%Y-%H%M%S')) + '.png'
#         img.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
#         return render(request, 'index.html', {'img_name': img_name})
#     return render(request, 'index.html')



def qr_generate(request):
    if request.method == 'POST':
        data = request.POST['data']
        logo = Image.open('/home/test/QRCodeGenerator/qrcodesite/images/mbiomelogo.png')
        basewidth = 300
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=10, box_size=30)
        QRcode.add_data(data)
        QRcode.make()
        QRimg = QRcode.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer(), color_mask=VerticalGradiantColorMask((255,255,255),(155,38,182),(255,0,0)))
        pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
        img_name = 'QR-' + str(datetime.datetime.now().strftime('%d%b%Y-%H%M%S')) + '.png'
        QRimg.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
        # color_img = Image.open(QRimg)
        # for i in range(2100):
        #     for j in range(2100):
        #         k = color_img.getpixel((i,j))
        #         if k == (0,0,0,0):
        #             color_img.putpixel((i,j),(0,0,i/4))
        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')