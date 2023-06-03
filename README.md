# pabd_cv
Predictive analytics practice repo for computer vision students

## План семинаров

### 1. Основы работы с bash. 
Система версионирования Git.
Модель разработки GitHub Flow. 
Настройка виртуальной среды python. 
Установка зависимостей, пакетные менеджеры. 
Продвинутые возможности языка python.  

**Результат:** fork репозитория, создание файла services/server_xxx.py.  
Синхронизацию с основным репозиторием labintsev/pabd_cv делать не нужно.
Ваша ветка main должна быть заблокирована от прямых изменения. 
Все изменения вносите в свой репозиторий в ветку main через pull request. 

### 2. Структура ML проекта, шаблонизация cookiecutter ds. 
Требования к коду: codestyle, linters, formatters, function docs. 
Реализация минимального функционала классификации изображений. 
Тестирование с помощью unittest. 

**Результат:**  Ваш репозиторий должен содержать реализацию сервиса classify с помощью предбученной модели.
Модель должна предсказывать три **наиболее** вероятных класса ImageNet.
Тест должен проверять вхождение класса "Пембрук" в результат предсказания при запущенном сервисе.  


### 3. Работа с данными и обучение модели. 
Версионирование данных с DVC.  

**Результат:** 
В проекте подключен dvc. 
Папка data/raw/kaggle добавлена в dvc. 
В качестве dvc remote использовано локальное хранилище на диске.    

### 4. Обучение модели.  
CLI python.  
Пайплайн предобработки данных.  
Сохранение модели после обучения и интеграция с сервисом.  
[Обучение модели.](https://keras.io/examples/vision/image_classification_from_scratch/)  
[Данные](https://drive.google.com/file/d/1PW9uFmww8G9-BwVFwnTitdTFCusx4OuU/view?usp=sharing)

**Результат:** 
Реализация скрипта train.py для обучения модели.  
Результат обучения (модель) сохраняется локально.  
Скрипт предсказания использует обученную модель для бинарной классификации.

### 5. Валидация модели  
Обучение модели на стороннем сервере (Google Colab).  
Генерация отчетов о метриках и производительности модели. 
Выгрузка модели в s3 хранилище.  
Скачать изображения для валидации с pinterest можно с помощью [инструмента](https://github.com/ataknkcyn/pinterest-crawler)

**Результат:** 
1. Обучение модели на стороннем сервере. 
2. Реализован скрипт валидации модели evaluate.py
2. Результат обучения (model.zip) скачан на локальную машину и используется для валидации в скрипте evaluate.py. 
3. Precision, Recall, Accuracy должны быть не менее 0.8
4. Настроена выгрузка модели в s3 хранилище.


### 6. Контейнеризация с Docker

