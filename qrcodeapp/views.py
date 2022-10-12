from django.shortcuts import render
from django.conf import settings
import qrcode
import datetime
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import SquareGradiantColorMask


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

def qr_generate(request):
    if request.method == 'POST':
        data = request.POST['data']
        qr = qrcode.QRCode(version=1, box_size=10, border=5, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(data)
        qr.make(fit=True)
        # img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer(),\
                            color_mask=SquareGradiantColorMask(), \
                            embeded_image_path="/home/test/QRCodeGenerator/qrcodesite/images/microbiome.png",\
                            eye_drawer=RoundedModuleDrawer(radius_ratio=2.5))
        img_name = 'QR-' + str(datetime.datetime.now().strftime('%d%b%Y-%H%M%S')) + '.png'
        img.save(str(settings.MEDIA_ROOT) + '/' + str(img_name))
        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')