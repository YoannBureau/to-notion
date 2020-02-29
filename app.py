from flask import Flask, request
from notion.client import NotionClient
import json

app = Flask(__name__)

# https://code.visualstudio.com/docs/python/tutorial-flask
# python3 -m flask run
# https://pypi.org/project/notion/


def add_table_entry(token, table_url, row_properties):
    client = NotionClient(token_v2=token)
    cv = client.get_collection_view(table_url)
    row = cv.collection.add_row()
    for row_property in row_properties:
        update_row_property(row, row_property["name"], row_property["value"])


def update_row_property(row, property_name, value):
    setattr(row, property_name, value)


@app.route("/tableentry", methods=["POST"])
def tableEntry():
    content = request.get_json(silent=True)
    add_table_entry(
        content["token"],
        content["tableUrl"],
        content["properties"]
    )
    return content

# {
#     "token": "305b7a39516160a1273510704ec480bedf711982c6e79b388a33e10d41035dcb46d7bb564cc807311fc2e28ad6247aac295644c40f22d8bf26d1aaee5aa31dcff92311d1b3ceedc4fa4da630ea2e",
#     "tableUrl": "https://www.notion.so/ybureau/a0ae18c3b9c94a6b9019677e27c26dd5?v=9baca57d7cfa42b4912a88ad46610c43",
#     "properties": [
#         {
#             "name": "name",
#             "value": "COUCOU LOL"
#         },
#         {
#             "name": "files",
#             "value": ["https://www.birdlife.org/sites/default/files/styles/1600/public/slide.jpg"]
#         }
#     ]
# }
