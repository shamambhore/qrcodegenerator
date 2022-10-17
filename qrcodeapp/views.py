from django.shortcuts import render
from django.conf import settings
import qrcode
import datetime
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import VerticalGradiantColorMask,SolidFillColorMask
from PIL import Image, ImageDraw

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
        logo = Image.open('E:\qrgenerator\qrcodegenerator\images\mbiomelogo.png')
        basewidth = 300
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
        
        def style_eyes(img):
            img_size = img.size[0]
            eye_size = 40 #default
            quiet_zone = 310 #default
            mask = Image.new('L', img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rectangle((40, 40, 305, 305), fill=255)
            draw.rectangle((img_size-305, 40, img_size-40, 305), fill=255)
            draw.rectangle((40, img_size-305, 305, img_size-40), fill=255)
            return mask
    
        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=4, box_size=30)
        QRcode.add_data(data)
        QRcode.make()
        # embeded_img= Image.open("E:\qrgenerator\qrcodegenerator\images\qrcodedesign.jpeg")
        # qr_eyes_img = QRcode.make_image(image_factory=StyledPilImage,\
        #                                 module_drawer=RoundedModuleDrawer(radius_ratio=1),\
        #                                 color_mask=SolidFillColorMask((255,255,255),(255,0,0)),\
        #                                 eye_drawer=RoundedModuleDrawer()
        # )
        qr_eyes_img = Image.open("E:\qrgenerator\qrcodegenerator\images\qrcodedesign.png").convert("RGB")
        # qr_eyes_img.make_image()
        QRimg = QRcode.make_image(image_factory=StyledPilImage,\
                                  module_drawer=VerticalBarsDrawer(),\
                                  color_mask=VerticalGradiantColorMask(back_color=(255,255,255),top_color=(155,38,182),bottom_color=(255,0,0)),\
                                  eye_drawer=RoundedModuleDrawer(),\
        )
        pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
        img_name = 'QR-' + str(datetime.datetime.now().strftime('%d%b%Y-%H%M%S')) + '.png'
        mask = style_eyes(QRimg)
        final_img = Image.composite(qr_eyes_img, QRimg, mask)
        final_img.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')