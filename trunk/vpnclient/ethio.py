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
        self.setDaemon(True)
        return

    def run(self):
        while self.looping:
            tm,pkt=self.pc.next()
            pkt=str(pkt)
            if self.filterpacket(pkt):
                self.pktqueue.put(pkt)
        return

    def filterpacket(self,pkt):
        return True

    def stop(self):
        self.looping=False
        return

sendpacket=lambda pkt:sendpkt.sendpacket(pkt,settings.ETHIF)

###############################################################################
import unittest
import Queue
import time

class TestCapThread(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def testall_1(self):
        q=Queue.Queue()
        thrd=CAPThread(q)
        thrd.start()
        time.sleep(5)
        thrd.stop()
        for i in range(0,min(q.qsize(),10)):
            print repr(q.get())
        return

if __name__=='__main__':
    unittest.main()
