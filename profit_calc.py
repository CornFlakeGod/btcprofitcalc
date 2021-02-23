#!/usr/bin/env python
# This is my btc.py script.
import requests

btcresponse = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#ethresponse = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')

btcdata = btcresponse.json()

btcrate = (btcdata["bpi"]["EUR"]["rate_float"])

print("1 BTC = %s €" % (btcrate))

defaulttax = 1.49

buyinvest = float(input("How much money (€) did you invest?\n"))

buyprice = float(input("How much (€) was 1 BTC worth when you purchased?\n"))

buytax = input("How much (%%) was the tax when you purchased? (Default = %s %%)\n" % (defaulttax))
if buytax=='':
	buytax=defaulttax

btcamount =  (buyinvest * (1 - (buytax / 100))) / buyprice

sellamount = input("How many bitcoins did you sell? (Default = all / %s btc)\n" % (btcamount))
if sellamount=='':
	sellamount=float(btcamount)

sellprice = input("How much (€) was 1 BTC worth when you sold? (Default = 1 btc = %s €)\n" % (btcrate))
if sellprice=='':
	sellprice=btcrate

selltax = input("How much (%%) was the tax when you purchased? (Default = %s %%)\n" % (defaulttax))
if selltax=='':
	selltax=defaulttax

sellaftertax = (float(sellamount) * float(sellprice)) * (1 - (float(selltax) / 100))
profit=sellaftertax-buyinvest
print("You sold %s btc for %s €,\nafter a %s € investment,\nresulting in a profit of %s €." % (sellamount,sellaftertax,buyinvest,profit))
