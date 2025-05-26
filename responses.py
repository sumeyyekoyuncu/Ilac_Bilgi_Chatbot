# responses.py

from ilaclar import ilac_bilgileri

def get_bot_response(message):
    message = message.strip().lower()
    for ilac in ilac_bilgileri:
        if ilac.lower() == message:
            return ilac_bilgileri[ilac]
    return "Bu ilacı veritabanımızda bulamadım. Lütfen doğru yazdığınızdan emin olun."
