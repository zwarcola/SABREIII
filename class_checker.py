from lib import getPage, login

baseURL = "https://paws.tcnj.edu/psp/paws/?cmd=login"

cookies = login(baseURL, "warcolz1", "Sugaree1!")

print(cookies)
