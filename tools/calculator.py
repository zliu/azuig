#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import ceve_market
import id_map
class ExamplePanel(wx.Panel):
    buy_or_sell = 0
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.logger = wx.TextCtrl(self, pos=(40,40), size=(400,250), style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.price_label = wx.TextCtrl(self, pos=(500,180), size=(120,-1), style=wx.TE_READONLY)
        self.button = wx.Button(self, label="paste", pos=(520,125))
        self.Bind(wx.EVT_BUTTON, self.OnPaste, self.button)

        ref_price_choice_list = [u'买一', u'卖一']
        ref_price_choice = wx.RadioBox(self, label=u'价格标准', pos=(520,30),choices=ref_price_choice_list, majorDimension=3,style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, ref_price_choice)

        self.lbname = wx.StaticText(self, label=u'清单', pos=(20,20))

    def EvtRadioBox(self, event):
        #self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
        self.buy_or_sell = event.GetInt()
    def OnPaste(self, event):
        #self.logger.AppendText('click on button with id %d\n' % event.GetId())
        if wx.TheClipboard.Open():
            data = wx.TextDataObject()
            wx.TheClipboard.GetData(data)
            self.logger.SetValue(data.GetText())
            wx.TheClipboard.Close()
            total = get_total_price(data.GetText().split('\r'), self.buy_or_sell)
            self.price_label.SetValue(str(total))
        else:
            print "open clipboard failed"
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())


    def EvtChar(self, event):
        print ("char event captured")
        self.logger.AppendText('evtchar: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event):
        self.logger.AppendText('evtCheckBo: %d\n' % event.Checked())


def get_total_price(item_list, buy_or_sell):
    total = 0
    delta = 0
    policy = {0:'buy', 1:'sell'}
    for item in item_list:
        cols = item.split('\t')
        item_name = cols[0]
        item_amount = int(cols[1].replace(',',''))
        item_group = cols[2]
        item_category = cols[3]
        item_id = id_map.get_id(item_name)
        price = ceve_market.get_price(item_id, policy[buy_or_sell]) / 1
        price2 = ceve_market.get_price(item_id, 'sell')
        print item_name, item_amount, price, item_amount*price
        total = total + item_amount * price
        delta = delta + item_amount * (price2  - price)
    print 'Total:', total
    print 'Delta with sell-1:', delta
    return total

app = wx.App(False)
frame = wx.Frame(None, size=(800, 600))
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
