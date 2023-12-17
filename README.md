# tg_sender

**Files sender with captions to TG-channel via user account**

Автоматизированный инструмент загрузки файлов в телеграм-канал через аккаунт пользователя с подписью.

## Установка
`git clone https://github.com/sdnv0x4d/tg_sender.git`

Установка зависимостей:
```bash
pip3 install telethon
```

## Использование

Запуск tg_sender с указанием пути до файла, подписи, ссылки на канал, API ID, API Hash: 
```bash
python3 main.py -p /mnt/1c_distr/ --channel @sdnv_funkhole --api-id 12345 --api-hash 0123456789abcdef0123456789abcdef
```
> При первом запуске необходимо произвести интерактивную аутентификацию. Будет создан файл `uploader.session`

| Аргумент | Пример | Пояснение
| :-| :-| :-
| Помощь | `--help` |
| Файл для отправки | `-f, --file /srv/my_file.txt` | Абсолютный путь до файла
| Путь до директории с файлами | `-f, --path /srv/my_files` | Абсолютный путь до директории с файлами
| ТГ-канал | `--channel @sdnv_funkhole` | Указание телеграм-канала. **Важно:** пользователь должен иметь права на отправку сообщений
| Подпись | `--caption 'Hello World!👋'` | Указание подписи сообщения
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
- Указывается только одна подпись для всех файлов, в ином случае можно указать индивидуальную подпись в функции `multiple_files_send`
- Проверка указанных аргументов `--file` или `--path`
- Отправка файла(ов) с указанной подписью на указанный телеграм-канал

## Лицензия

Licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) License.