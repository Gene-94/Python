import requests
import json

def get_messages(ch_id, auth_token):
    headers = {
        'authorization': auth_token
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{ch_id}/messages?all', headers=headers)
    parsed = json.loads(r.text)

    for message in parsed :
        print(message['content'], "\n")

print("Insert chanel id: ")
chanel_id = input()
print("Insert your authorization token: ")
auth_token = input()

get_messages(chanel_id, auth_token)


# not pulling all the messages in the chanel with this method

