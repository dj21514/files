import requests
from Crypto.PublicKey import ECC


def main():
  key = ECC.generate(curve='p256')
  f = open('myprivatekey.pem','wt')
  f.write(key.export_key(format='PEM'))
  f.close()

  print(key.public_key().export_key(format='PEM'))
  pass


if __name__ == '__main__':
  main()