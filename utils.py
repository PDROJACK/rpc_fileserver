import string
import random
import json

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def dictToJSON(data):
    k = json.dumps(data)
    return k

def JsonToDict(jsn):
    k = json.loads(jsn)
    return k


dictToJSON({ 'is':'not' })