import os

import requests

response = requests.get("https://favqs.com/api/qotd")

print(f"The Quote of the day: {response.json()['quote']['body']}")

print(os.getenv("STAGE"), os.getenv("BROWSER"))
print("всем добра")
# если что то изменили в образе не забываем его пересобрать\
# docker build -f Dockerfile-api -t home_work:v3 .

# если переменную передаем через терминал
#  в терминале пишем docker run -e "STAGE=qa" -e "BROWSER=chrome" home_work:v3

# если переменную считываем из .env файла то в терминале пишем
# docker run --env-file=.env home_work:v3

#Управляемый запуск
#Запуск с выполнением команды в контейнере, например когда в образе нет инструкции CMD.
 # docker run home_work:v3 sh -c "python3 home_work.py"