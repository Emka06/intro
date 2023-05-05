'''DRF'''
# API (Aplication programming interface)
# место соприкосновения клиента и сервера, 
# предназначено для взаимодействия между программами

'''REST (representational state transfer)-
стиль API, стандарт которому следуют API'''

# принципы REST
# 1. разграничиние клиента и сервера 
# 2. отсутсвтие состояния (нет сохранения состояния) -
# сервер не должен хранить какую-либо информацию о клиенте 
# 3. кэширование 
# 4. многоуровневая система 
# 5. единый интерфэйс
# 6. код предоставляется по запросу 


#  REST full API - API которое соответсвует принципам REST

# 1. Создаем виртальное окружение
# python3 -m venv venv


# 2. Активируем виртуальное окружение
#    . venv/bin/activate


# 3. создаем файл req.txt
# записываем: Django, djangorestframework, psycopg2-binary


# 4. устанавливаем: pip3 install -r req.txt


# 5. django-admin startproject <название> . -> создание проекта, 
# если не поставить точку, будет вложенность


# 6. python3 manage.py startapp <app_name> - создание приложения


# 7. открывем файл settings.py в INSTALED_APPS -> регистрируем
# rest_framework, <app_name>


# 8. в файле settings.py настраиваем базу данных
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'test',
#         'USER': 'user',
#         'PASSWORD': 6663,
#         'HOST':'loacalhost',
#         'PORT': 5432
#     }
# }

# python3 manage.py makemigrations -> создает файл миграций
# python3 manage.py migrate 


# python3 manage.py createsuperuser - создание суперпользователя (aдмина)

# python3 manage.py runserver -> запуск проекта
# python3 manage.py runserver 8001


'''Models'''
# как проходит запрос
# 1. asgi/wsgi -> (те,кто принимают запрос и возвращает ответ) 
# 2. settings -> middlewares
# 3. urls -> маршрутизаторы
# 4. views -> представления (функции, которые 
# возвращают данные в нужном формате)
# 5. serializers (классы, которые переводят данные из
# json в python и наоборот)
# 6. models (классы, которые обозначают как будет 
# выглядеть наша таблица в бд)
# 7. managers (objects) -> классы которые работают с ORM
# 8. db -база данных 


'''ПОЛЯ'''
# 'CharField' -> для строкового значения (обязательно нужно указывать max_length)
# 'SlugField' -> для хранения slug (обычно используется в url) содержит только буквы, числа, -, _
# 'TextField' -> просто для хранения текста 
# 'DrcimalField' -> для дробных чисел (max_digit: кол-во цифр цклой части, decimal_places (кол-во
# цифр после запятой))
# 'IntegerField' -> для чисел
# 'BooleanField' -> для bool значений
# 'DateField' -> для дат (datetime.date) можно передать аргументы: auto_now ->
# обновляется при изменении записи, auto_now_add -> задается только один раз при создании
# 'TimeField' -> для времени (auto_now, auto_now_add)
# 'DateTimeField' -> для даты и времени (auto_now, auto_now_add)
# 'EmailField' -> для email
# 'FileField' -> для хранения файлов,принимает в себя аргумент(upload_to) -> указание
# директории где будет файл
# 'ImageField' -> для картинок
# 'JSONField' -> для строк в формате json

'''ключевые параметры для полей'''
# null -> если True, будет в бд записывать null, если данные не переданы
# blanck -> если True, будет ставить пустую строку(не обязательно для заполнения)
# default -> значение по умолчанию
# unique -> если True, в колонке могут хранится только уникальные значения
# primary key -> если True, первичный ключ-идентификатор
# choices -> список с tuple ограничиваем возможные варианты для заполнения