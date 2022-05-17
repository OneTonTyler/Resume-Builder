# Tyler Singleton
# 05/16/2022
#
# Resume Builder
# This project is designed to read qualifications and keywords from job postings.
# Using a dictionary of keywords to develop a unique resume for the application.
# The resume will be built using latex and create a custom file system to store photos
# and/or other relevant information such as github, linkedin, and webpage portfolio links.
# ---
import json

import requests
import re

def html_generator(data, key):
    for tag in data[key]:
        print(tag)


with open("content.json", 'r') as file:
    content = json.load(file)

keywords = {key for key in content}
for key in keywords:
    html_generator(content, key)


# url = r"https://www.ziprecruiter.com/jobs/one-touch-intelligence-41c23774/junior-python-developer-6d5f82e9?lvk=juny9Bra4tvgtIRQBtaLqg.--MTO5ZfkD-"
# def web_crawler(link):
#     request = requests.get(link)
#     return request
#
#
# r = web_crawler(url).text
#
# def content_generator(text):
#     keywords = {'PYTHON', 'DEVELOPER', 'HTML', 'CSS', 'TYLER', 'JAVASCRIPT'}
#     for val in keywords:
#         if re.search(val, text, re.IGNORECASE):
#             print(f'{val}: ', True)
#         else:
#             print(f'{val}: ', False)


# content_generator(r)