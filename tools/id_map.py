#!/usr/bin/env python
# coding=utf-8
import sys
import os
import xlrd
import urllib2
book = xlrd.open_workbook('eve_db.xls', 'r')

n = book.nsheets

def get_id(item_name):
  for tab_index in range(n):
      #print('the',tab_index,' th sheet')
      sheet = book.sheet_by_index(tab_index)
      #print(u"{0} {1} {2}".format(sheet.name, sheet.nrows, sheet.ncols))
      if (sheet.name == u"物品列表"):
          item_sheet = sheet
      if (sheet.name == u"星域列表"):
          region_sheet = sheet
      if (sheet.name == u"星系列表"):
          system_sheet = sheet
      if (sheet.name == u"星座列表"):
          constellation_sheet = sheet
      if (sheet.name == u"NPC空間站"):
          station_sheet = sheet
  
  item_list = {}
  item_name_to_id = {}
  for r in range(item_sheet.nrows):
      item_name_to_id[item_sheet.cell_value(rowx=r, colx=1)] = item_sheet.cell_value(rowx=r, colx=0)
      item_list[item_sheet.cell_value(rowx=r, colx=0)] = {
              'name': item_sheet.cell_value(rowx=r, colx=1),
              'description': item_sheet.cell_value(rowx=r, colx=2),
              'market_category_1': item_sheet.cell_value(rowx=r, colx=3),
              'market_category_2': item_sheet.cell_value(rowx=r, colx=4),
              'market_category_3': item_sheet.cell_value(rowx=r, colx=5),
              'market_category_4': item_sheet.cell_value(rowx=r, colx=6),
              'market_category_5': item_sheet.cell_value(rowx=r, colx=7),
              'market_category_6': item_sheet.cell_value(rowx=r, colx=8)
              #'market_category_7': item_sheet.cell_value(rowx=r, colx=9)
              }
  #    print item_sheet.cell_value(rowx=r, colx=1)
  #    if r == 3:
  #        break
  #
  
  # verify the map between item id and item name can be matched to each other
  # so that user can use id to find name, and vice versa
  for key in item_list:
      name = item_list[key]['name']
      id = key
      if name != item_list[id]['name']:
          print name, id, 'does not match'
          break
  # verify end
  region_list = {}
  system_list = {}
  constellation_list = {}
  station_sheet = {}
  
  #print sys.argv[1]
  if type(item_name) == str:
      item_name = item_name.decode('utf-8')
  input_id = item_name_to_id[item_name]
  #input_id = item_name_to_id[item_name]
  #print input_id
  return input_id
