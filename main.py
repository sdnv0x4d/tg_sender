#!/usr/bin/env python3

from telethon import TelegramClient
from loguru import logger
import re
import argparse
import os

parser = argparse.ArgumentParser(description="Files sender with captions to TG-channel via user account. How to get API ID/Hash: https://docs.telethon.dev/en/stable/basic/signing-in.html#signing-in")
parser.add_argument("-f", "--file", type=str, help="File Path [str]")
parser.add_argument("-p", "--path", type=str, help="Files Path [str]")
parser.add_argument("--channel", type=str, required=True, help="Telegram Channel Link/Nickname [str]")
parser.add_argument("--caption", type=str, help="Caption in message [str]")
if os.path.isfile('uploader.session'):  # Check first time use
    parser.add_argument("--api-id", type=int, help="Telegram App api_id [int]")
    parser.add_argument("--api-hash", type=str, help="Telegram App api_hash [str]")
else:
    parser.add_argument("--api-id", type=int, required=True, help="Telegram App api_id [int]")
    parser.add_argument("--api-hash", type=str, required=True, help="Telegram App api_hash [str]")
args = parser.parse_args()

api_id = args.api_id
api_hash = args.api_hash
file_path = args.file
files_path = args.path
channel = args.channel
caption = args.caption

client = TelegramClient('uploader', api_id, api_hash)

async def main(channel, file_path, caption):
    logger.info('Send ' + file_path + ' to ' + channel + ' with caption ' + caption)
    await client.send_file(entity=channel, file=file_path, caption=caption)  # Send file with caption

def multiple_files_send(channel, files_path, caption):
    file_names = (os.listdir(files_path))   # Extract file names
    for filename in file_names:
        caption = re.sub('windows64_8_', '1C Server Windows x64 8.', filename)  #
        caption = re.sub('_', '.', caption)                                     # Version caption create
        caption = re.sub('.rar', '', caption)                                   #
        file_path = files_path + '/' + filename                                 # Absolute path to file
        with client:
            client.loop.run_until_complete(main(channel, file_path, caption))   # Call main function

if (not file_path and not files_path):
    logger.error('Error! File and Path is empty!')
elif (file_path and files_path):
    logger.error("Error! You can't send file and files in path both!")
elif (file_path and not files_path):
    with client:
      client.loop.run_until_complete(main(channel, file_path, caption))    # Call main function with 1 file
elif (files_path and not file_path):
    multiple_files_send(channel, files_path, caption)   # Call main function with multiple files send