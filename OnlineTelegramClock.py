from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import time

api_id = 14798336
api_hash = 'c87ba486bb1e398f73abb97f3b8dec0f'

def get_image():
    image = Image.open('Clock.png')

    font = ImageFont.truetype('Digital Dismay.ttf', size=445)
    time_image = Image.new('L', (font.getsize(get_time_now())[0], 446))

    ImageDraw.Draw(time_image).text((0, 0), get_time_now(), fill=140, font=font)
    time_image = time_image.rotate(1.55, resample=Image.BICUBIC, expand=True)

    image.paste((191, 23, 17), box=(780, 935), mask=time_image)
    image.save('image.png')

def get_time_now():
    if datetime.now().hour < 10 and datetime.now().minute < 10:
        return f'0{datetime.now().hour}:0{datetime.now().minute}'
    elif datetime.now().hour < 10:
        return f'0{datetime.now().hour}:{datetime.now().minute}'
    elif datetime.now().minute < 10:
        return f'{datetime.now().hour}:0{datetime.now().minute}'
    else:
        return f'{datetime.now().hour}:{datetime.now().minute}'

def main():
    date = datetime.now().minute
    while True:
        if datetime.now().minute != date:
            get_image()
            with TelegramClient('qwerty', api_id, api_hash) as client:
                client.start()
                client.connect()
                client(DeletePhotosRequest(client.get_profile_photos('me')))
                client(UploadProfilePhotoRequest(
                client.upload_file('image.png')))
            date = datetime.now().minute
        else:
            time.sleep(1)

if __name__ == '__main__':
    main()
