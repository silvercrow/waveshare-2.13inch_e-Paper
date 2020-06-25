#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13_V2 Demo")
    
    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    
    # Drawing on the image
    font24 = ImageFont.truetype(os.path.join(picdir, 'Poppins-SemiBold.ttf'), 24)
    font38 = ImageFont.truetype(os.path.join(picdir, 'Poppins-SemiBold.ttf'), 38)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    
    logging.info("1.Drawing on the image...")
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    

    draw.text((10, 10), 'David Balan', font = font38, fill = 0)
    draw.text((70, 50), u'デビッド', font = font24, fill = 0)
    draw.text((10, 60), 'The quick brown fox', font = font24, fill = 0)
    epd.display(epd.getbuffer(image))
    time.sleep(2)
    
    # read bmp file 
    #logging.info("2.read bmp file...")
    #image = Image.open(os.path.join(picdir, '2in13.bmp'))
    #epd.display(epd.getbuffer(image))
   # time.sleep(2)
        
    # # partial update
    
    logging.info("Goto Sleep...")
    #epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
