# Project Management CLI Tool

## Features
- Add users
- Assign projects to users
- Add tasks to projects
- Save data using JSON
- CLI interaction using argparse

## Setup
pip install -r requirements.txt

## Run Commands

Add user:
python main.py add-user --name "Alex" --email "alex@mail.com"

Add project:
python main.py add-project --user "Alex" --title "CLI Tool"

Add task:
python main.py add-task --project "CLI Tool" --title "Build CLI"

List users:
python main.py list-users