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
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
import osmosdr
import sip
import sys
import time
import pdb


class receiver(gr.top_block, Qt.QWidget):
    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
	self.key=key=0
	self.iteration=iteration=0

        ##################################################
        # Blocks
        ##################################################
        self.receive = osmosdr.source(args="numchan" + str(1)+ "" + "")
		
        self.receive.set_sample_rate(1e6)
	self.receive.set_center_freq(100e6)
	self.receive.set_freq_corr(0, 0)
	self.receive.set_gain_mode(False, 0)
	self.receive.set_gain(10, 0)
	self.receive.set_if_gain(20, 0)
	self.receive.set_bb_gain(20, 0)
	self.receive.set_antenna("", 0)
	self.receive.set_bandwidth(0, 0)
	

        self.qtgui_number_sink_0 = qtgui.number_sink(
                gr.sizeof_float,
                0,
                qtgui.NUM_GRAPH_HORIZ,
        	1
        )

        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 3)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
          
       
    	self.digital_gmsk_demod_0 = digital.gmsk_demod(
			samples_per_symbol=2,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
        self.digital_gfsk_demod_0 = digital.gfsk_demod(
			samples_per_symbol=2,
		        sensitivity=1.0,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
  
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_f(grc_blks2.packet_decoder(
        		access_code="100010001000100010001111",
        		threshold=0,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
                        ),
        	
        )
       
        self.blks2_packet_decoder_1 = grc_blks2.packet_demod_f(grc_blks2.packet_decoder(
        		access_code="100010001000100010001000",
        		threshold=0,
        		callback=lambda ok, payload: self.blks2_packet_decoder_1.recv_pkt(ok, payload),
                        ),
        	
        )
 	self.blks2_packet_decoder_2 = grc_blks2.packet_demod_f(grc_blks2.packet_decoder(
        		access_code="100010001000100010101010",
        		threshold=0,
        		callback=lambda ok, payload: self.blks2_packet_decoder_2.recv_pkt(ok, payload),
                        ),
        	
        )


        self.file_sink_0 = blocks.file_sink(gr.sizeof_float*1, "/home/firas/Desktop/final/firas-data", False)
        self.file_sink_0.set_unbuffered(False)
	self.file_sink_1 = blocks.file_sink(gr.sizeof_float*1, "/home/firas/Desktop/final/firas-data_1", False)
        self.file_sink_1.set_unbuffered(False) 
        self.probe_sig_0 = blocks.probe_signal_f()  
        self.low_pass_filter = filter.fir_filter_ccf(1, firdes.low_pass(1, 1e6, 250000, 20000, firdes.WIN_HAMMING, 6.76))
	self.throt=blocks.throttle(gr.sizeof_gr_complex*1, 32000,True)

	self.file_sink=blocks.file_sink(gr.sizeof_float*1, "/home/firas/Desktop/paper-test.pdf", True)
	self.file_sink.set_unbuffered(False)
        ##################################################
        # Connections
        ##################################################
          
          
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))    
        self.connect((self.blks2_packet_decoder_0, 0), (self.file_sink_0, 0))
        self.connect((self.receive, 0), (self.digital_gmsk_demod_0, 0))
        self.connect((self.blks2_packet_decoder_0, 0), (self.probe_sig_0, 0))   
   

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
	
    def demodulation(self, config):

		if 0<=config<10:
			print("Mod: GMSK")
			return self.digital_gmsk_demod_0
		if 10<=config<20:
			print("Mod: GFSK")
			return self.digital_gfsk_demod_0
		if 20<=config:
			print("Mod: GMSK")
			return self.digital_gmsk_demod_0
	
    def frequency(self, config):

		if 0<=config<10:
			print("Frequency: 90MHZ")
			self.receive.set_center_freq(90e6, 0)
		if 10<=config<20:
			print("Frequency: 130MHZ")
			self.receive.set_center_freq(130e6, 0)
		if 20<=config:
			print("Frequency: 180MHZ")
			self.receive.set_center_freq(180e6, 0)

    def length(self, config):

		if 0<=config<10:
			print("Packet Length: 1024")
			return self.blks2_packet_decoder_0
		if 10<=config<20:
			print("Packet Length: 512")
			return self.blks2_packet_decoder_1
		if 20<=config:
			print("Packet Length: 256")
			return self.blks2_packet_decoder_2
    def sleep(self):
	t_end=time.time()+4
    	while time.time()<t_end:
			pass

class transmitter(gr.top_block):
	def __init__(self):
		
                if choice==1:
                	 self.num=0
               		 self.g=3
               		 self.p=5
               		 self.x=4
		if choice==2:
                	 self.num=0
               		 self.g=5
               		 self.p=7
               		 self.x=5
		num=pow(self.g,self.x)%self.p
                print("g^x mod p=%d")%num
      		gr.top_block.__init__(self, "Top Block")	
		self.vector = blocks.vector_source_f((num, num, num), True, 1, [])
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

#def main():
    


if __name__ == '__main__':
    ts=0
    choice=0
    print("Enter which key you want")
    choice=input("number")
    #main()
    
    tx=transmitter()  
    tx.start()
    print("Start Transmitting")
    time.sleep(3)   
    tx.stop()	
    time.sleep(1)
    x1=tx.x
    p1=tx.p
    tx=None
    key=0
    distin=[0.0] * 10
    dist=0.0
   
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = receiver()
    tb.start()
    tb.show()
    print("start Receiving")
    t_end=0.0
    for r in range (0,5):
		t_end=time.time()+1
    		while time.time()<t_end:
			dist = tb.probe_sig_0.level()
			if dist>0:
    				distin[r] = dist
				print(dist)
    
    
    dist1=max(distin)
    print(dist1)
    #tx=transmitter()

    key=pow(dist1,x1)%p1
 			
    print("key=%d") %key          		
    
    tb.lock()
    tb.disconnect((tb.digital_gmsk_demod_0, 0), (tb.blks2_packet_decoder_0, 0))
    tb.disconnect((tb.blks2_packet_decoder_0, 0), (tb.file_sink_0, 0))
    tb.disconnect((tb.receive, 0), (tb.digital_gmsk_demod_0, 0)) 
    tb.disconnect((tb.blks2_packet_decoder_0, 0), (tb.probe_sig_0, 0))
    tb.unlock()
    time.sleep(1) 
    ts=key+1
    i=0
    #pdb.set_trace()
    for j in range (0,9):
  
        config=0
        config=key*i	
	print("Iteration: %d")%i	
    	tb.lock()  
    	tb.connect((tb.receive, 0), (tb.low_pass_filter, 0))
	tb.connect((tb.low_pass_filter, 0),(tb.demodulation(config), 0))
   	tb.connect((tb.demodulation(config), 0), (tb.length(config), 0))
    	tb.connect((tb.length(config), 0), (tb.file_sink, 0))
    	tb.frequency(config)
    	tb.unlock()
	time.sleep(ts+i)
	tb.lock()
	tb.disconnect((tb.demodulation(config), 0), (tb.length(config), 0))
    	tb.disconnect((tb.length(config), 0), (tb.file_sink, 0))
	tb.disconnect((tb.receive, 0), (tb.low_pass_filter, 0))
	tb.disconnect((tb.low_pass_filter, 0), (tb.demodulation(config), 0))
	tb.unlock()
    	i=i+1
	time.sleep(1)
    print("Good Bye!")
    tb.stop()
    tb.wait()
    tb = None 
