# tg_sender

**1C Distributions files sender with version captions to TG-channel via user account**

Автоматизированный инструмент загрузки дистрибутивов 1С Сервер в телеграм-канал через аккаунт пользователя с подписью версии дистрибутива.

## Установка
`git clone -b 1c_server https://github.com/sdnv0x4d/tg_sender.git`

Установка зависимостей:
```bash
pip3 install -r req.txt
```

## Использование

Запуск tg_sender с указанием пути до 1С дистрибутивов, ссылки на канал, API ID, API Hash: 
```bash
python3 main.py -p /mnt/1c_distr/ --channel @sdnv_funkhole --api-id 12345 --api-hash 0123456789abcdef0123456789abcdef
```
> При первом запуске необходимо произвести интерактивную аутентификацию. Будет создан файл `uploader.session`

| Аргумент | Пример | Пояснение
| :-| :-| :-
| Помощь | `--help` |
| Файл для отправки | `-f, --file /srv/my_file.txt` | Абсолютный путь до файла
| Путь до директории с файлами | `-f, --path /srv/my_files` | Абсолютный путь до директории с файлами .rar 1С дистрибутивов
| ТГ-канал | `--channel @sdnv_funkhole` | Указание телеграм-канала. **Важно:** пользователь должен иметь права на отправку сообщений
| Подпись | `--caption 'Hello World!👋'` | Указание подписи сообщения. **Важно:** Для 1С 8.3 подпись создается автоматически
| App api_id | `--api-id 12345` | Telegram API ID
| App api_hash | `--api-hash 0123456789abcdef0123456789abcdef` | Telegram API Hash

#### Перед началом работы
Для получения API ID и API Hash необходимо:
1. [Войти в свой телеграм аккаунт](https://my.telegram.org/auth) с номером телефона, от которого будут рассылаться сообщения
2. Перейти в [API development tools](https://my.telegram.org/apps)
3. Появится окно создания нового приложения. Достаточно заполнить `App title` и `Short name`
4. Нажать `Create application`, скопировать `App api_id` и `App api_hash`

### Работа приложения

- Можно выбрать что-то одно из отправления одного файла или указания директории
- Проверка указанных аргументов `--file` или `--path`
- Указывается подпись из `--caption`, если отправляется одиночный файл
- Извлечение названий 1С дистрибутивов. К примеру: `windows64_8_3_1353.rar`
- Создание подписи исходя из названия файла дистрибутива. К примеру: `windows64_8_3_1353.rar` -> `1C Server Windows x64 8.3.1353`
- Отправка файла(ов) с указанной подписью на указанный телеграм-канал

## Лицензия

Licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) License.
