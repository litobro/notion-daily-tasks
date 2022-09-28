# notion-daily-tasks
[Notion.so](https://www.notion.so) is an online workspace and productivity management software. It is a powerful tool that utilizes relational database style structures to customize your dashboards. 

Unfortunately, there is limited support for automations and other routines. In particular, the creation of items in a database periodically is not supported. This may be useful when users want to create something like a daily routine task list that resets every day. 

This project intends to create a relatively simple system to automate the creation of daily tasks. It uses the [Notion API](https://developers.notion.com/reference) as implemented in [notion-client](https://pypi.org/project/notion-client/).

# Getting Started

TODO: Flesh out instructions

This is fairly simple to get started. Simply either build the dockerfile yourself or do a docker pull from [dockerhub](https://hub.docker.com/r/litobro/notiondailytasks):
```docker pull litobro/notiondailytasks```

Then you will be required to set these env variables:

|Variable|Value|
|-|-|
|NOTION_TOKEN|Your Notion API key|
|NOTION_DB_ID|Your Notion Database ID|

Finally, create a volume mapped to */app/data* and insert a file called *items.txt*. This file should contain a row separated list of all tasks you wish to create in order. The Database in Notion must contain the following fields:

|Field|Value|
|-|-|
|Name|Text field of taskname|
|Complete|Checkbox|
|Order|Number corresponding to row number|