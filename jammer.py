#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov  3 21:13:22 2015
##################################################
if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from grc_gnuradio import blks2 as grc_blks2
from gnuradio import digital
import osmosdr
import sys
import time


class transmitter(gr.top_block):
	def __init__(self):

      		gr.top_block.__init__(self, "Top Block")	
		self.vector = blocks.vector_source_f((5, 6, 7), True, 1, [])
		self.packet = grc_blks2.packet_mod_f(grc_blks2.packet_encoder(
			samples_per_symbol=2, 
			bits_per_symbol=1, 
			preamble="", 
			access_code="", 
			pad_for_usrp=True), 
			payload_length=256)
		self.mod = digital.gmsk_mod(
			samples_per_symbol=2, 
			bt=0.35, 
			verbose=False, 
			log=False)
		self.sender = osmosdr.sink(args="numchan" + str(1)+ "" + "")
		
		self.sender.set_sample_rate(1e6)
		self.sender.set_center_freq(100e6)
		self.sender.set_freq_corr(0, 0)
		self.sender.set_gain_mode(False, 0)
		self.sender.set_gain(20, 0)
		self.sender.set_if_gain(30, 0)
		self.sender.set_bb_gain(30, 0)
		self.sender.set_antenna("", 0)
		self.sender.set_bandwidth(0, 0)

	#connection

		self.connect((self.vector,0), (self.packet,0))
		self.connect((self.packet,0), (self.mod,0))
		self.connect((self.mod,0), (self.sender,0))

class receiver(gr.top_block):
	def __init__(self):
		
        	gr.top_block.__init__(self, "Top Block")
		self.receive = osmosdr.source(args="numchan" + str(1)+ "" + "")
		
		self.receive.set_sample_rate(1e6)
		self.receive.set_center_freq(90e6)
		self.receive.set_freq_corr(0, 0)
		self.receive.set_gain_mode(False, 0)
		self.receive.set_gain(10, 0)
		self.receive.set_if_gain(20, 0)
		self.receive.set_bb_gain(20, 0)
		self.receive.set_antenna("", 0)
		self.receive.set_bandwidth(0, 0)
	

		self.detect = analog.simple_squelch_cc(-24.5, 100e-6)
		self.comptomag=blocks.complex_to_mag(1)

		self.probe = blocks.probe_signal_f()
			

	#connection
		self.connect((self.receive,0), (self.detect,0))
		self.connect((self.detect,0), (self.comptomag,0))
		self.connect((self.comptomag,0), (self.probe,0))
		   	 
    
def main():
    
    rx=receiver()   
    rx.start()

    while(rx.probe.level()==0):
		time.sleep(1)
		print(rx.probe.level())
       
    rx.stop()	
    time.sleep(3)
  	
if __name__ == '__main__':
	main()
        tx=transmitter()
	tx.start()
        time.sleep(8)
        tx.stop()
    
