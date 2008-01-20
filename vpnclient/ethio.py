# -*- coding: UTF-8 -*-
# File: ethio.py
# Date: 2008-01-21
# Author: vpnhacker

"""
以太网抓包和发包接口
"""

import threading

import pcap
import sendpkt

import settings

class CAPThread(threading.Thread):
    """抓包线程"""

    def __init__(self,pktqueue):
        threading.Thread.__init__(self)
        self.pktqueue=pktqueue
        self.looping=True
        self.pc=pcap.pcap(settings.ETHIF)
        self.pc.setnonblock(True)
        self.pc.setfilter(settings.PCAP_FILTER)
        selt.setDaemon(True)
        return

    def run(self):
        while self.looping:
            pkt=self.pc.next()
            print pkt
            pkt=str(pkt)
            if self.filterpacket(pkt):
                self.pktqueue.add(pkt)
        return

    def filterpacket(self,pkt):
        return True

    def stop(self):
        self.looping=False
        return

###############################################################################
import unittest

class TestCapThread(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return
