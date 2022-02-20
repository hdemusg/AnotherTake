import urllib.request

'''
{
  "textPayload": "CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict([('ToCountry', 'US'), ('MediaContentType0', 'audio/amr'), ('ToState', 'TX'), ('SmsMessageSid', 'MM42c9ba8909c359b279920810e71e5b21'), ('NumMedia', '1'), ('ToCity', ''), ('FromZip', ''), ('SmsSid', 'MM42c9ba8909c359b279920810e71e5b21'), ('FromState', 'GA'), ('SmsStatus', 'received'), ('FromCity', 'ATLANTA'), ('Body', ''), ('FromCountry', 'US'), ('To', '+19034209599'), ('ToZip', ''), ('NumSegments', '1'), ('MessageSid', 'MM42c9ba8909c359b279920810e71e5b21'), ('AccountSid', 'ACf1ace56c36ef7f2030efde7685ef7af4'), ('From', '+14702333985'), ('MediaUrl0', 'https://api.twilio.com/2010-04-01/Accounts/ACf1ace56c36ef7f2030efde7685ef7af4/Messages/MM42c9ba8909c359b279920810e71e5b21/Media/MEeaa4cd8dd1935dc6ed760ea8408f2847'), ('ApiVersion', '2010-04-01')])])",
  "insertId": "000000-5d80dbb7-c6c1-49e5-824c-1c8b9375228a",
  "resource": {
    "type": "cloud_function",
    "labels": {
      "function_name": "musicbot",
      "region": "us-central1",
      "project_id": "anothertake"
    }
  },
  "timestamp": "2022-02-20T03:54:59.165Z",
  "labels": {
    "execution_id": "7egon0e1cf77"
  },
  "logName": "projects/anothertake/logs/cloudfunctions.googleapis.com%2Fcloud-functions",
  "trace": "projects/anothertake/traces/316395d9fa2d5e3b6d851e46fd4d380e",
  "receiveTimestamp": "2022-02-20T03:55:09.642087073Z"
}
'''
# 1. Parse metadata for necessary info
#url = "https://api.twilio.com/2010-04-01/Accounts/ACf1ace56c36ef7f2030efde7685ef7af4/Messages/MMfed0707d3949129a17d940bc5187a3a1/Media/ME8d8e276d4457f3b8f977ff8ac7eecc60.json"
#media_id = url.split('/')[-1]
#message_id = "MMfed0707d3949129a17d940bc5187a3a1"
# url might be enough, we just might not be calling it right
#print(url, media_id, message_id)

# 2. Grab audio file
#https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json
#import requests
#import os
#from twilio.rest import Client

#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
#client = Client(account_sid, auth_token)

#base = "https://%s:%s@api.twilio.com" % (account_sid, auth_token)

#message = client.messages(message_id).fetch()
#print(message)
#medias = message.media.list()
#for media in medias:
    #m = client.messages(message_id).media(media.sid).fetch()
    #u = requests.get(base + m.uri).json()
    #u2 = requests.get(base + u['uri'].replace('.json', ''))
    #with open("audio.amr", "wb") as a:
        #a.write(bytearray(reversed(u2.content)))
        #a.write(u2.content)
        #a.close()
#print("wrote audio to file")

'''
a = requests.get(url)
print(type(a.content))
audio = open("audio.amr", "wb")
audio.write(a.content)
audio.close()
'''

# 3. Perform processing

from scipy.io.wavfile import read, write
import numpy as np

fs, x = read('lyc.wav')

r = np.flip(x)
write('audio.wav', fs, r)

#import soundfile as sf

#data, samplerate = sf.read('audio.amr')
#print(samplerate, type(data))

# 4. Package it for returning to user

