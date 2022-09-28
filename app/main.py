import os
import time
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN")) # Notion API key
db_id = os.getenv("NOTION_DB_ID") # Notion database ID

def create_item(name, completed=False, order=0):
    '''Create a new item in the database'''
    notion.pages.create(
        parent={
            "database_id": db_id
        },
        properties={
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Complete": {
                "checkbox": completed
            },
            "Order": {
                "number": order
            }
        }
    )
    

def load_items():
    '''Load items from a file'''
    items = []
    with open('items.txt', 'r') as f:
        for line in f:
            items.append(line.strip())
    return items


def main():
    for i, item in enumerate(load_items()):
        create_item(name=item, order=i)
        time.sleep(0.34) # Notion API rate limit


if __name__ == '__main__':
    main()