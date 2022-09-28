import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
db_id = os.getenv("NOTION_DB_ID")

def create_item(name, completed=False, order=0):
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
    

def main():
    create_item("testA", False, 5)


if __name__ == '__main__':
    main()