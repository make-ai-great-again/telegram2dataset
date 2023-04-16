import os
import fnmatch
from bs4 import BeautifulSoup
import lxml
from tqdm import tqdm
import json

folders = [d for d in os.listdir() if os.path.isdir(d) and d != '.git']

cleandict = {
    ')': ' ',
    '?': '? ',
    '😂': '',
    '😅': '',
    '🙈': '',
    '🤗': '',
    '🤣': '',
    '@': '',
    '😬': '',
    '❤️': '',
    'хД': '',
    'ДДД': '',
    '😁': '',
    '😹': '',
    '👋': '',
    '🥺': '',
    '☀️': '',
    '🍀': '',
    '  ': ' ',
    '  ': ' '
}

def myclean(s):
    for x in cleandict:
        s = s.replace(x, cleandict[x])
    return s.strip()


def get_instruction_input():
    choice = input("Enter 'instruction' or 'input' to use first message in: ").lower()
    while choice not in ['instruction', 'input']:
        choice = input("Invalid input. Enter 'instruction' or 'input': ").lower()
    if choice == 'input':
        instruction_text = input("Enter text for 'instruction' field: ")
    else:
        instruction_text = None
    return choice, instruction_text

def use_question_messages_only():
    choice = input("Use only first messages which contains '?' ? (y/n): ").lower()
    while choice not in ['y', 'n']:
        choice = input("Invalid input. Enter 'y' or 'n': ").lower()
    return choice == 'y'

field_choice, instruction_text = get_instruction_input()
question_messages_only = use_question_messages_only()



for chatdir in folders:
    print(f"Processing folder: {chatdir}")  # Display folder being processed
    with open(chatdir+'_output.jsonl', 'a') as dataset:
        for file in os.listdir(chatdir):
            if fnmatch.fnmatch(file, '*.html'):
                with open(os.path.join(chatdir, file), 'r', encoding='UTF-8') as f:
                    data = f.read().strip()
                soup = BeautifulSoup(data, 'html.parser')
                messages = soup.find_all('div', class_='message')
                for message in tqdm(messages, desc=f'Processing file: {file}'):
                    if message.find("div", {"class": "reply_to details"}) and message.find("div", {"class": "text"}):
                        new_message = (message.find("div", {"class": "text"}).text).strip()
                        old_message0 = message.find("div", {"class": "reply_to details"}).a.get('href').replace('#go_to_', '')
                        old_message = ''
                        if soup.find("div", {"id": str(old_message0)}):
                            old_message0 = soup.find("div", {"id": str(old_message0)})
                            if old_message0.find("div", {"class": "text"}):
                                old_message = (old_message0.find("div", {"class": "text"}).text).strip()
                        if len(new_message) > 7 and len(old_message) > 7:
                            old_message = myclean(old_message)
                            new_message = myclean(new_message)
                            if field_choice == 'input':
                                json_record = {'instruction': instruction_text, 'input': old_message, 'output': new_message}
                            else:
                                json_record = {'instruction': old_message, 'input': '', 'output': new_message}
                            if not question_messages_only or '?' in old_message:
                                dataset.write(json.dumps(json_record, ensure_ascii=False) + '\n')


    if os.path.exists(chatdir+'_output.jsonl'):
        with open(chatdir+'_output.jsonl', 'r', encoding='utf-8') as infile:
            data_jsonl = [json.loads(line) for line in infile]
            print('Total objects: ' + str(len(data_jsonl)))

        with open(chatdir+'_output.json', 'w', encoding='utf-8') as outfile:
            json.dump(data_jsonl, outfile, ensure_ascii=False)