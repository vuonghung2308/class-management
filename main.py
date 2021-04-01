from accesstoken.token import *
from entity.Account import *

token = get_token(Account("Vuong Manh Hung", "abc"))
print(token)
print(decode_token(token))