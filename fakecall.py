from twilio.rest import Client

def fake_call():
    account_sid='ACb1815220e78264c92244f79cfed53329'
    account_auth='f185654310459b0637d1d15d38329c8c'
    client = Client(account_sid,account_auth)

    call=client.calls.create(
        twiml='<Response><Say>Hello This is a Fake Call </Say></Response>',
        to='+123456789010',
        from_='+109872654321',
    )
    print(call.sid)


#fake_call()