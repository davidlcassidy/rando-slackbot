import os
import time
import re
import json
import random
from slackclient import SlackClient
from flask import abort, Flask, jsonify, request
app = Flask(__name__)

# instantiate Slack client
client_id = "####"
bot_user_access_token = "####"
slack_client = SlackClient(bot_user_access_token)

@app.route("/rando", methods=["POST"])
def rando():

    userListDict = slack_client.api_call(
            "conversations.members",
            channel=request.values.get('channel_id')
        )

    response = ""

    members = userListDict["members"]
    random.shuffle(members)

    index = 0
    for member in members:
        user = slack_client.api_call(
            "users.info",
            user=member
        )
        if not user["user"]["deleted"] and not user["user"]["is_bot"] and user["user"]["name"] != "slackbot":
            index += 1
            response = response + str(index) +  ": " + user["user"]["profile"]["real_name"] + " \n"

    return jsonify(
        response_type='in_channel',
        text=response,
    )

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
