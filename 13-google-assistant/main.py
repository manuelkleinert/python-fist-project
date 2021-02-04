import io

from six.moves import http_client
from six.moves import urllib

from grpc import device_helpers
import httplib2

import io
import google.oauth2.credentials

# credentials = client.Credentials()
# http = object()
# print(http)

# with io.open('.credentials.json', 'r') as f:
#     credentials = google.oauth2.credentials.Credentials(token=None, **json.load(f))


# with io.open('/path/to/credentials.json', 'r') as f:
#     credentials = google.oauth2.credentials.Credentials(token=None, **json.load(f))

device_handler = device_helpers.DeviceRequestHandler(1025445555074)

@device_handler.command('action.devices.commands.OnOff')

def onoff(on):
    if on:
        print('Turning device on')
    else:
        print('Turning device off')