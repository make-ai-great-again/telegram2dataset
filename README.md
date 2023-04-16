# Telegram chat 2 dataset for Alpaca-LoRA
Revised telegram chat parser, prepares a file in Instruction format for training llama/alpaca/vicuna models,
saves it in json and jsonl.

The parser takes all the messages that have replies. 
- You can add the first message to 'instruction', or to 'input' (and set the instruction yourself)
- You can use either pairs where the first message containing the '?' sign, or all messages.
- 'output' is always reply.

JSON structure for instruct models:
```
{	
	"instruction": "", 
	"input": "", 
	"output": ""
}
```


How to use:
1. Download this repository to your pc
2. Install the dependencies by using
```
pip install -r requirements.txt
```
Export chats from telegram to html (embedded client function)
4. Put the resulting folders in the same directory as this repository
5. Run the program
```
python3 telegram_export_chat_parser.py
```
6. Follow the prompts.
7. Wait for completion, files will be saved in the same directory



# Датасет из Телеграм-чата, для Alpaca-LoRA
Доработанный парсер чатов телеграм, подготовливает файл в Instruct формате для обучения моделей llama/alpaca/vicuna,
сохраняет в json и jsonl.

Парсер берет все пары сообщений, на которые есть ответы. 
— Можно добавлять первое сообщение в 'instruction', или в 'input' (а инструкцию задать самому).
— Можно использовать только первые сообщения, содержащие знак '?' или все.
- В 'output' помещается всегда ответ на первое сообщение.

Структура json для instruct моделей:
```
{	
	"instruction": "", 
	"input": "", 
	"output": ""
}
```

Как использовать:
1. Скачайте данный репозиторий на ваш пк
2. Установите зафисимости с помощью
```
pip install -r requirements.txt
```
3. Экспортируйте чаты из telegram в формат html (встроенная функкция клиентов)
4. Полученные папки положите в одну директорию с этим репозиторием
5. Запустите программу
```
python3 telegram_export_chat_parser.py
```
6. Следуйте подсказкам.
7. Ожидайте завершения, файлы будут сохранены в этой же директории



Based on https://github.com/Den4ikAI/telegram_chat_parser
