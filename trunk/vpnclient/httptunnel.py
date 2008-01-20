# -*- coding: UTF-8 -*-
# File: httptunnel.py
# Date: 2008-01-21
# Author: vpnhacker

"""
HTTP通道，提供上传以太网包和获取以太网包的功能
"""

import urllib
import urllib2
import httplib

uploadpacket=lambda pkt:urllib2.urlopen(settings.VPN_SERVER_URL_UPLOAD,pkt)

def downloadpackets():
    """下载回来一批另外一端上传的包"""
    return
