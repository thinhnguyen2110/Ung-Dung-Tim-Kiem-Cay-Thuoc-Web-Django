import tensorflow as tf
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array

mapping = {'CayThongMoc': 0, 'CayTrinhNu': 1, 'CayRauSam': 2, 'CayXaDen': 3, 'CaySoiRung': 4, 'CayRauMa': 5,
           'CayTrinhNuHoangCung': 6, 'CayToi': 7, 'CayYdi': 8, 'CaySe': 9, 'CayMangCau': 10,
           'CayLucLacKhongCuong': 11, 'CayNgheVang': 12, 'CayOliu': 13, 'CayKimNganHoa': 14, 'CayLuocVang': 15,
           'CayKhaTu': 16, 'CayNamLinhChi': 17, 'CayNgheDen': 18, 'CayNhaDam': 19,
           'CayHoaXaThietThao': 20, 'CayHamEch': 21, 'CayGac': 22, 'CayDuaCan': 23, 'CayCucAo': 24,
           'CayHoangCamRau': 25, 'CayDiepCa': 26, 'CayBoKet': 27, 'CayDuDu': 28, 'CayBoQuan': 29,
           'CayBoHoang': 30, 'CayBachTruat': 31, 'CayBoCongAnh': 32, 'CayBachDauOng': 33}
reverse_mapping = {0: 'CayThongMoc', 1: 'CayTrinhNu', 2: 'CayRauSam', 3: 'CayXaDen', 4: 'CaySoiRung', 5: 'CayRauMa',
                   6: 'CayTrinhNuHoangCung', 7: 'CayToi', 8: 'CayYdi', 9: 'CaySe', 10: 'CayMangCau',
                   11: 'CayLucLacKhongCuong', 12: 'CayNgheVang', 13: 'CayOliu', 14: 'CayKimNganHoa', 15: 'CayLuocVang',
                   16: 'CayKhaTu', 17: 'CayNamLinhChi', 18: 'CayNgheDen', 19: 'CayNhaDam',
                   20: 'CayHoaXaThietThao', 21: 'CayHamEch', 22: 'CayGac', 23: 'CayDuaCan', 24: 'CayCucAo',
                   25: 'CayHoangCamRau', 26: 'CayDiepCa', 27: 'CayBoKet', 28: 'CayDuDu', 29: 'CayBoQuan',
                   30: 'CayBoHoang', 31: 'CayBachTruat', 32: 'CayBoCongAnh', 33: 'CayBachDauOng'}


def mapper(value):
    return reverse_mapping[value]

model = load_model('Model31-28102021.h5')
image = load_img('hinh1.jpg', target_size=(180, 180))

image = img_to_array(image)
image = image / 255.0
prediction_image = np.array(image)
prediction_image = np.expand_dims(image, axis=0)

prediction = model.predict(prediction_image)
value = np.argmax(prediction)
move_name = mapper(value)
print("Prediction is {}.".format(move_name))


