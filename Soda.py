from flask import Flask, request
import requests
import base64

app = Flask(__name__)

# Token بوت التليجرام
TELEGRAM_BOT_TOKEN = '7393244196:AAGY7HFZysFeLnC0ErPTlRTmX6ffvUneRnM'
TELEGRAM_CHAT_ID = '1049904862'

@app.route('/upload', methods=['POST'])
def upload_image():
    # الحصول على بيانات الصورة
    image_data = request.form['image']

    # تحويل بيانات Base64 إلى صورة
    image = base64.b64decode(image_data.split(',')[1])

    # إعداد الملفات لإرسالها إلى Telegram
    files = {'photo': ('image.png', image)}

    # إرسال الصورة إلى Telegram
    response = requests.post(
        f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto',
        data={'chat_id': TELEGRAM_CHAT_ID},
        files=files
    )

    if response.status_code == 200:
        return 'تم إرسال الصورة بنجاح!', 200
    else:
        return 'فشل في إرسال الصورة.', 500

if __name__ == '__main__':
    app.run(debug=True)
