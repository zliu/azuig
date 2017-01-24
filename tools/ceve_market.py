#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json

# http://www.ceve-market.org/api/market/region/{星域ID}/system/{星系ID}/type/{物品ID}.{格式}
marketurl = 'http://www.ceve-market.org/api/market'
def get_price(item_id = 34, sell_or_buy = 'buy'):
  if not item_id:
    return 0
  item='/type/' + str(item_id)
  region_id='10000002'
  region='/region/' + region_id
  jita='30000142'
  system_id=jita
  system='/system/' + system_id
  response_format='json'
  url = marketurl + region + system + item + '.' + response_format
  price = json.loads(urllib2.urlopen(url, timeout = 5).read())
  #print 'sell - min', price['sell']['min']
  #print 'buy - max', price['buy']['max']
  if sell_or_buy == 'buy':
      return price['buy']['max']
  elif sell_or_buy == 'sell':
      return price['sell']['min']

#get_price()
