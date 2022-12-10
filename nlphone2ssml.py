#!/usr/bin/python3
# -*- coding: utf-8 -*-

#all three-digit area codes in NL
short_areacodes = ['010','013','014','015','020','023','024','026','030','033','035','036','038','040','043','044','045','046',
                   '050','053','055','058','070','071','072','073','074','075','076','077','078','079']

#all four-digit area codes in NL
long_areacodes = ['0111', '0113', '0114', '0115', '0117', '0118', '0161', '0162', '0164', '0165', '0166', '0167', 
                  '0168', '0172', '0174', '0180', '0181', '0182', '0183', '0184', '0186', '0187', '0222', '0223',
                  '0224', '0226', '0227', '0228', '0229', '0251', '0252', '0255', '0294', '0297', '0299', '0313', 
                  '0314', '0315', '0316', '0317', '0318', '0320', '0321', '0341', '0342', '0343', '0344', '0345', 
                  '0346', '0347', '0348', '0411', '0412', '0413', '0416', '0418', '0475', '0478', '0481', '0485', 
                  '0486', '0487', '0488', '0492', '0493', '0495', '0497', '0499', '0511', '0512', '0513', '0514', 
                  '0515', '0516', '0517', '0518', '0519', '0521', '0522', '0523', '0524', '0525', '0527', '0528', 
                  '0529', '0541', '0543', '0544', '0545', '0546', '0547', '0548', '0561', '0562', '0566', '0570', 
                  '0571', '0572', '0573', '0575', '0577', '0578', '0591', '0592', '0593', '0594', '0595', '0596', 
                  '0597', '0598', '0599']

#if include_speak is True, the SSML will be inclosed with <speak></speak> tags
def nlphone2ssml(phonenumber, include_speak=False):
  phonenumber = phonenumber.replace(' ', '')
  phonenumber = phonenumber.replace('-', '')
  breaktime='200ms'
  if phonenumber.startswith('0800'):
    phonenumber = '0<say-as interpret-as=\"cardinal\">800</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[4:]+'</say-as>'
  elif phonenumber.startswith('0900'):
    phonenumber = '0<say-as interpret-as=\"cardinal\">900</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[4:]+'</say-as>'
  elif phonenumber.startswith('0906'):
    phonenumber = '<say-as interpret-as=\"characters\">0906</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[4:]+'</say-as>'
  elif phonenumber.startswith('0909'):
    phonenumber = '<say-as interpret-as=\"characters\">0909</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[4:]+'</say-as>'
  elif phonenumber.startswith('085'):
    phonenumber = '0<say-as interpret-as=\"cardinal\">85</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[3:7]+'</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[7:]+'</say-as>'
  elif phonenumber.startswith('088'):
    phonenumber = '0<say-as interpret-as=\"cardinal\">88</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[3:7]+'</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[7:]+'</say-as>'
  elif phonenumber.startswith('06'):
    phonenumber = '06<break time="'+breaktime+'"/><say-as interpret-as=\"cardinal\">'+phonenumber[2:4]+'</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[4:7]+'</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[7:]+'</say-as>'
  elif phonenumber[0:3] in short_areacodes:
    phonenumber = '0<say-as interpret-as=\"cardinal\">'+phonenumber[1:3]+'</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[3:7]+'</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[7:]+'</say-as>'
  elif phonenumber[0:4] in long_areacodes:
    phonenumber = '<say-as interpret-as=\"characters\">'+phonenumber[0:4]+'</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[4:7]+'</say-as><break time="'+breaktime+'"/><say-as interpret-as=\"characters\">'+phonenumber[7:]+'</say-as>'

  if include_speak:
    return '<speak>'+phonenumber+'</speak>'
  else:
    return phonenumber

#this only runs as a test, but not if imported
if __name__ == "__main__":
  phonenumbers = ['09001234', '0475461234', '0101234567', '0857654321']
  for phonenumber in phonenumbers:
    print(nlphone2ssml(phonenumber))

