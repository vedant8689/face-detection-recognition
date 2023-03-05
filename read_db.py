from pymongo import MongoClient
from PIL import Image
import io
from bson.binary import Binary
from PIL import Image
import io
import matplotlib.pyplot as plt
client = MongoClient(
    'mongodb+srv://user-5:user-5pass@cluster1.h9nlbyo.mongodb.net/test')
db = client['employee_jk']
images = db.images

image_bytes = io.BytesIO()

image = images.find_one({
    'id': 2031
})
print(image['id'])
pil_img = Image.open(io.BytesIO(image['data']))
plt.imshow(pil_img)
plt.show()
# for i in image:
#     print(i['id'])
#     pil_img = Image.open(io.BytesIO(i['data']))
#     plt.imshow(pil_img)
#     plt.show()
