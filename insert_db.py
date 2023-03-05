from pymongo import MongoClient
from PIL import Image
import io
from bson.binary import Binary
from PIL import Image
import io

#establish connection with database
client = MongoClient('mongodb+srv://vedantmodi8689:3F9fNwu8EOwmFFcs@cluster1.h9nlbyo.mongodb.net/test')
db = client['employee_jk']
images = db.images
eid=2004
for i in range(27):
#open the image file    
    s='E:\\Nirma University\\Hackathon\\dataset1\\dataset1\\img\\' + str(i+1) + '.jpg'
    im = Image.open(s)

    #converts image to byte format
    image_bytes = io.BytesIO()
    im.save(image_bytes, format='JPEG')

    #save image along with the the id
    image = {
        'id': eid,
        'data': image_bytes.getvalue()
    }
    eid+=1
    #upload data to database
    image_id = images.insert_one(image).inserted_id