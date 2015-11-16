import config

import mandrill
mandrillClient = mandrill.Mandrill(config.get().MandrillApiKey)


def send(releaseCount):
    try:
        name = config.get().FromEmailName
        email_from = config.get().FromEmailAddress

        recipients = [{
            'email': config.get().FromEmailAddress,
            'name': config.get().FromEmailName,
            'type': 'to'
        }]
        for recipient in config.get().Recipients.split(','):
            recipient = recipient.strip()
            parts = recipient.split('---')
            recipients.append({
                'email': parts[0],
                'name': parts[1],
                'type': 'bcc'
            })

        message = {
            'html': '<a href="http://olava.xyz">Click here to view all '+str(releaseCount)+' games coming out this week!</a>',
            'text': 'Please enable HTML content. It is required to view the weekly roundup!',
            'subject': 'Weekly Gaming Roundup',
            'from_email': email_from,
            'from_name': name,
            'to': recipients,
            'headers': {
                'Reply-To': email_from
            }
        }
        mandrillClient.messages.send(message=message, async=False, ip_pool=None, send_at=None)

    except mandrill.Error as e:
        print('A mandrill error occurred: %s - %s' % (e.__class__, e))
        return 500
