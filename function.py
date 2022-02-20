def process(request):
    audio = request.values.get('MediaUrl0', None)
    from twilio.twiml.messaging_response import MessagingResponse
    if audio == None:
        audio = "Please send a voice message in order for AnotherTake to work its magic."
        resp = MessagingResponse()
        resp.message(audio)
        return str(resp)
    else: 
        media_id = audio.split('/')[:-1]
        message_id = request.values.get('SmsMessageSid', None)
        print(url, media_id, message_id)
        import requests
        from twilio.rest import Client
        #account_sid = "ACf1ace56c36ef7f2030efde7685ef7af4"
        #auth_token = "415cbb96b25df80d4776941fd6e4113d"
        client = Client(account_sid, auth_token)
        base = "https://%s:%s@api.twilio.com" % (account_sid, auth_token)
        message = client.messages(message_id).fetch()
        print(message)
        medias = message.media.list()
        for media in medias:
            m = client.messages(message_id).media(media.sid).fetch()
            u = requests.get(base + m.uri).json()
            u2 = requests.get(base + u['uri'].replace('.json', ''))
            with open("audio.amr", "wb") as a:
                a.write(bytearray(reversed(u2.content)))
                a.write(u2.content)
                a.close()
        print("wrote audio to file")
        from scipy.io.wavfile import read, write
        import numpy as np

        fs, x = read('lyc.wav')

        r = np.flip(x)
        write('audio.wav', fs, r)
        with open('audio.wav') as f 
            resp = MessagingResponse()
            resp.play(f)
            return resp
    print("done") #shouldn't run but it's there so it doesn't break on Google Cloud