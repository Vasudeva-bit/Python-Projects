from twilio.rest import Client
client = Client('ACbd2e09f485xxxxxxxxxx61fed8198', '7fd4e0xxxxxxxxxxxf706593942c6fa')
from_whatsapp_number='whatsapp:+13xxxxx7485'
to_whatsapp_number='whatsapp:xxxxxxxx9'
message = client.messages.create(body='Check out this 
owl!',from_=from_whatsapp_number,to=to_whatsapp_number)
print(message.sid)