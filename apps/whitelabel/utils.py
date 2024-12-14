from django.conf import settings as s


def whitelabel():

    labels = {
        "brand": s.BRAND_NAME,
        "slogan": s.SLOGAN,
        "contact": {
            "no": s.PHONE,
            "add": s.ADDRESS
        }
    }
