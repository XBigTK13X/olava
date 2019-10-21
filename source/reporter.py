import json
import config
import requests
import datetime

def createCampaign():
    params = {
        "recipients": {
            "list_id": config.get().MailChimpListId
        },
        "type": "regular",
        "settings": {
            "subject_line": "Olava Weekly Gaming Roundup",
            "reply_to": "no-reply@olava.xyz",
            "from_name": "Olava"
        }
    }
    response = requests.post(
        'https://us10.api.mailchimp.com/3.0/campaigns',
        auth=(
            'apikey',
            config.get().MailChimpApiKey
        ),
        json=params
    )
    try:
        response.raise_for_status()
        body = response.json()
        return body['id']
    except requests.exceptions.HTTPError as err:
        print("Error: {} {}".format(str(response.status_code), err))
        print(json.dumps(response.json(), indent=4))
        return -1
    except ValueError:
        print("Cannot decode json, got %s" % response.text)
        return -1


def populateCampaign(campaignId, releaseCount):
    dateToday = datetime.date.today()
    params = {
        'html': '<a href="http://olava.xyz/archive/' + str(dateToday) + '.html">Click here to view all ' + str(releaseCount) + ' games coming out this week.</a>',
    }
    response = requests.put(
        'https://us10.api.mailchimp.com/3.0/campaigns/{}/content'.format(campaignId),
        auth=(
            'apikey',
            config.get().MailChimpApiKey
        ),
        json=params
    )
    try:
        response.raise_for_status()
        body = response.json()
    except requests.exceptions.HTTPError as err:
        print("Error: {} {}".format(str(response.status_code), err))
        print(json.dumps(response.json(), indent=4))
        return -1
    except ValueError:
        print("Cannot decode json, got %s" % response.text)
        return -1


def sendCampaign(campaignId):
    response = requests.post(
        'https://us10.api.mailchimp.com/3.0/campaigns/{}/actions/send'.format(campaignId),
        auth=(
            'apikey',
            config.get().MailChimpApiKey
        )
    )
    try:
        response.raise_for_status()
        body = response.json()
    except requests.exceptions.HTTPError as err:
        print("Error: {} {}".format(str(response.status_code), err))
        print(json.dumps(response.json(), indent=4))
        return -1
    except ValueError:
        print("Cannot decode json, got %s" % response.text)
        return -1


def send(releaseCount):
    campaignId = createCampaign()
    if campaignId != -1:
        populateCampaign(campaignId, releaseCount)
        sendCampaign(campaignId)
