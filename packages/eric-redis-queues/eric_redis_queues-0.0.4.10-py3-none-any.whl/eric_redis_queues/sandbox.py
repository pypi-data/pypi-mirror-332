from eric_redis_queues import RedisChannel
from eric_sse.exception import NoMessagesException
from eric_sse.message import SignedMessage, UniqueMessage, Message

ch = RedisChannel()

sm = SignedMessage(sender_id='luca', msg_type='test', msg_payload='ciao')
um = UniqueMessage(message_id='mgs_id0001', sender_id='luca', message=Message(msg_type='testu', msg_payload={'a': 1}))
m = Message(msg_type='testsimple', msg_payload='ciao, simple')
l = ch.add_listener()
l_id = 'eric_queues:0b52c8e8-6556-4558-a13e-5fb7bf5251ee'
ch.get_listener(listener_id=l_id).start_sync()
#ch.broadcast(sm)
#ch.broadcast(um)
#ch.broadcast(m)

#exit(0)
while True:
    try:
        x = ch.deliver_next(l_id)
        print(x)
    except NoMessagesException:
        print('done')
        exit(0)
