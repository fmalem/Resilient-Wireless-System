#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Nov  4 09:11:50 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print ("Warning: failed to XInitThreads()")
import sys
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
import osmosdr
import sip
import time
import pdb
sys.path.insert(0,'/home/firas/pybombs/src/gnuradio/grc/grc_gnuradio/blks2/packet-encoder.py')
 


class transmitter(gr.top_block, Qt.QWidget):

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
        self.samp_rate = samp_rate = 32000
	
        #self.ac1=ac1
        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(1e6)
        self.osmosdr_sink_0.set_center_freq(100e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(20, 0)
        self.osmosdr_sink_0.set_if_gain(30, 0)
        self.osmosdr_sink_0.set_bb_gain(30, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(400000, 0)
          
	self.file_source=blocks.file_source(gr.sizeof_float*1, '/home/firas/Downloads/10.1.1.623.6305.pdf', True)

        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
                bt=0.35,
                verbose=False,
                log=False,
        )
        self.digital_gfsk_mod_0 = digital.gfsk_mod(
        	samples_per_symbol=2,
                sensitivity=1.0,
                bt=0.35,
                verbose=False,
                log=False,	
	)
        if choice==1:
        	self.num=0
        	self.g=3
        	self.p=5	
        	self.y=6
	if choice==2:
        	self.num=0
        	self.g=5
        	self.p=7	
        	self.y=9
        num=pow(self.g,self.y)%self.p
	print(num)
        self.blocks_vector_source_x_0 = blocks.vector_source_f((num,num,num), True, 1, [])
        self.blocks_vector_source_x_1 = blocks.vector_source_f((1,2,3), True, 1, [])
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_f(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble="",
        		access_code="100010001000100010001111",
        		pad_for_usrp=True,
        	),
        	payload_length=1024,
         )

        self.blks2_packet_encoder_1 = grc_blks2.packet_mod_f(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble="",
        		access_code="100010001000100010001000",
        		pad_for_usrp=True,
        	),
        	payload_length=512,
         )

        self.blks2_packet_encoder_2 = grc_blks2.packet_mod_f(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble="",
        		access_code="100010001000100010101010",
        		pad_for_usrp=True,
        	),
        	payload_length=256,
         )

        self.probe_sig_0 = blocks.probe_signal_f()
	

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gmsk_mod_0 , 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blks2_packet_encoder_0, 0))    
        self.connect((self.digital_gmsk_mod_0 , 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.probe_sig_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
    
    def modulation(self, config):

                if 0<=config<10:
			print("Mod: GMSK")
                        return self.digital_gmsk_mod_0
                if 10<=config<20:
			print("Mod: GFSK")
                        return self.digital_gfsk_mod_0
                if 20<=config:
			print("Mod: GMSK")
                        return self.digital_gmsk_mod_0

    def frequency(self, config):
	
                if 0<=config<10:
			print("Frquency: 90MHz")
                        self.osmosdr_sink_0.set_center_freq(90e6, 0)
                if 10<=config<20:
			print("Frquency: 130MHz")
                        self.osmosdr_sink_0.set_center_freq(130e6, 0)
                if 20<=config:
			print("Frquency: 180MHz")
                        self.osmosdr_sink_0.set_center_freq(180e6, 0)

    def length(self, config):
	
                if 0<=config<10:
			print("Packet Length: 1024")
                        return self.blks2_packet_encoder_0
                if 10<=config<20:
			print("Packet Length: 512")
                        return self.blks2_packet_encoder_1
                if 20<=config:
			print("Packet Length: 256")
                        return self.blks2_packet_encoder_2


class receiver(gr.top_block):
	def __init__(self):
	
                gr.top_block.__init__(self, "Top Block")
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

                self.probe = blocks.probe_signal_f()
		
                self.digital_gmsk_demod_0=digital.gmsk_demod(
			samples_per_symbol=2,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
			)
			

	#connection
		


class packet(gr.top_block):
  def __init__(self):
    gr.top_block.__init__(self, "Top Block")	

    self.blks2_packet_decoder_1 = grc_blks2.packet_demod_f(grc_blks2.packet_decoder(
					access_code="",
					threshold=0,
					callback=lambda ok, payload: self.blks2_packet_decoder_1.recv_pkt(ok, payload),
				        ),  
    )
		


	  	 

if __name__ == '__main__':
    ts=0
    choice=0
    print("Enter key you want")
    choice=input("number")
    dist=0.0
    temp=0.0
    rx=receiver()
    pkt=packet()
    rx.start()
    rx.lock()
    rx.connect((rx.receive,0), (rx.digital_gmsk_demod_0,0))
    rx.connect((rx.digital_gmsk_demod_0,0), (pkt.blks2_packet_decoder_1,0))
    rx.connect((pkt.blks2_packet_decoder_1,0), (rx.probe,0))
    rx.unlock()
    print("Start Receiving")
    while(rx.probe.level()==0):
	pass

    temp=rx.probe.level()
    time.sleep(1)
    print(temp)
    dist1=temp       
    rx.stop()
    print("stop Receiving")	
    time.sleep(1)
    rx=None

    

    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = transmitter()
    tb.start()
    tb.show()
    print("Start Transmitting")

    key=pow(dist1,tb.y)%tb.p
    print("key=%d")%key
    time.sleep(5)
    tb.lock()
    tb.disconnect((tb.blks2_packet_encoder_0, 0), (tb.digital_gmsk_mod_0 , 0))    
    tb.disconnect((tb.blocks_vector_source_x_0, 0), (tb.blks2_packet_encoder_0, 0))    
    tb.disconnect((tb.digital_gmsk_mod_0 , 0), (tb.osmosdr_sink_0, 0))    
    tb.disconnect((tb.blocks_vector_source_x_0, 0), (tb.probe_sig_0, 0))
    tb.unlock()

    time.sleep(1)	
    #pdb.set_trace()
    ts=key+1
    i=0
    for j in range (0,15):
   
        config=0
        config=key*i
        print("Iteration: %d")%i
        tb.lock()
        tb.connect((tb.length(config), 0), (tb.modulation(config) , 0)) 
        tb.connect((tb.file_source, 0), (tb.length(config), 0))
        tb.connect((tb.modulation(config) , 0), (tb.osmosdr_sink_0, 0)) 
        tb.frequency(config)
        tb.unlock() 
        time.sleep(ts+i)
        tb.lock()
        tb.disconnect((tb.length(config), 0), (tb.modulation(config), 0)) 
        tb.disconnect((tb.file_source, 0), (tb.length(config), 0))
        tb.disconnect((tb.modulation(config) , 0), (tb.osmosdr_sink_0, 0))
        tb.unlock()
	i=i+1 
        time.sleep(1)
    print("Good Bye!")
    tb.stop()
    tb.wait()
