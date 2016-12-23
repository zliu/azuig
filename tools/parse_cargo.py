#!/usr/bin/env python
# coding=utf-8
import sys
from ceve_market import get_price
from id_map import get_id

file = open(sys.argv[1])
linenum = 0
total = 0
delta = 0
while True:
    line = file.readline()
    if line:
        linenum += 1
        if len(line) > 1:
            #print '(', linenum, ':', len(line), ')', '[', line, ']'
            tokens = line[:-1].split()
            #tokens = line[:-1].split("\t| |\\s+")
            if len(tokens) == 1:
                tokens = line[:-1].split(' ')
            if len(tokens) == 1:
                print "lines are not splited by space or tab"
                break
            #if len(tokens) != 2:
            #    print line
            # 货币逗号分隔计数法？
            if tokens[1] == 'I' or tokens[1] == 'II':
                item = tokens[0]+' '+tokens[1]
                count = tokens[2]
            else:
                item = tokens[0]
                count = tokens[1]
            countnumbers = count.split(',')
            if len(countnumbers) > 1:
                #print countnumbers
                tmp = ''
                for number in countnumbers:
                    tmp = tmp + number
                count = tmp

            count = int(count)
            item_id = get_id(item)
            price = get_price(item_id, 'sell') / 1
            price2 = get_price(item_id, 'sell')
            print item,'['+item_id+']', '\tx[', count, ']', price, count*price
            total = total + count * price
            delta = delta + count * (price2  - price)
    else:
        break

print "total", total
print "delta", delta
