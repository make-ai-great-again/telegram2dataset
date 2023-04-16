# Converting telegram chat to dataset for Alpaca-LoRA

### Description:
Revised telegram chat parser, prepares a file in Instruction format for training llama/alpaca/vicuna models,
saves it in json and jsonl.

JSON structure for instruct models:
```
{	
	"instruction": "", 
	"input": "", 
	"output": ""
}
```

The parser takes all the messages that have replies. When converting you can optionally choose:

- Whether to add the first message to 'instruction' or to 'input' (and set the instruction yourself)
- Use only pairs where the first message containing the '?' sign or all message pairs.
- 'output' is always reply.


### How to use:
1. Download this repository to your pc
2. Install the dependencies by using
```
pip install -r requirements.txt
```
3. Export chats from telegram to html (embedded client function)
4. Put the resulting folders in the same directory as this repository. You can put many at once, different files will be generated
5. Run the program
```
python3 telegram_export_chat_parser.py
```
6. Follow the prompts.
7. Wait for completion, files will be saved in the same directory

<br /><br />
# Конвертируем телеграм-чат в датасет для Alpaca-LoRA

### Описание:
Доработанный парсер чатов телеграм, подготовливает файл в Instruct формате для обучения моделей llama/alpaca/vicuna,
сохраняет в json и jsonl.

Структура json для instruct моделей:
```
{	
	"instruction": "", 
	"input": "", 
	"output": ""
}
```

Парсер берет все пары сообщений, на которые есть ответы. При конвертации вы задаете опционально:

- Добавлять первое сообщение в 'instruction' или в 'input' (а инструкцию задать самому).
- Использовать только первые сообщения, содержащие знак '?', или вообще все пары.
- В 'output' помещается всегда ответ на первое сообщение.


### Как использовать:
1. Скачайте данный репозиторий на ваш пк
2. Установите зафисимости с помощью
```
pip install -r requirements.txt
```
3. Экспортируйте чаты из telegram в формат html (встроенная функция клиентов)
4. Полученные папки положите в одну директорию с этим репозиторием. Можно положить сразу несколько папок, для каждой будут созданы отдельные файлы.
5. Запустите программу
```
python3 telegram_export_chat_parser.py
```
6. Следуйте подсказкам.
7. Ожидайте завершения, файлы будут сохранены в этой же директории

<br /><br />

Based on https://github.com/Den4ikAI/telegram_chat_parser
