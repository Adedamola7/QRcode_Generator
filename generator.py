import qrcode

img = qrcode.make("https://www.linkedin.com/in/adedamola-adekeye/")
img.save("linkedin_profile.jpg")
