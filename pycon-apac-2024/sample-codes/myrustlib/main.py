from myrustlib import hello_world, User

hello_world()
# => Hello from Rust!

user = User(name="skokado", age=34)
user.greet()
# => Hi I'm skokado!

print(user.get_age())
# => 34

user.raise_angry()
# Traceback (most recent call last):
# ...
# myrustlib.UserGotAngryException: User skokado got angry🙄
