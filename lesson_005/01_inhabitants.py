# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1
import room_2

# TODO А если у нас добавятся жильцы в комнаты, а принты у нас заточены только на 3 жильца! Используйте join
print('В комнате room_1 живут:', room_1.folks[0], 'и', room_1.folks[1])
print('В комнате room_2 живут:', room_2.folks[0])
