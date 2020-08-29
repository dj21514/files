from src.account import Account

dummyUser = {
  'name' : 'dummy',
  'email': 'dummy@example.com',
  'user_pin': 1234,
  'password': 'password12345'
}

user1 = Account(
  name = dummyUser['name'],
  email= dummyUser['email'],
  user_pin= dummyUser['user_pin'],
  password=dummyUser['password']
)

user1.save()