import os.path
# Модуль для преобразования даты в приемлемый формат
from datetime import datetime
path = r'C:\Windows\notepad.exe'
# Получим размер файла в байтах
size = os.path.getsize(path)
# А теперь в килобайтах
# Две косые черты — это целочисленное деление
ksize = size // 1024
atime = os.path.getatime(path)
# Дата последнего доступа в секундах с начала эпохи
mtime = os.path.getmtime(path)
# Дата последней модификации в секундах с начала эпохи
print ('Размер: ', ksize, ' KB')
print ('Дата последнего использования: ', datetime.fromtimestamp(atime))
print ('Дата последнего редактирования: ', datetime.fromtimestamp(mtime))