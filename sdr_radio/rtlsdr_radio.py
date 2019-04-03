#coding:utf-8

import threading
import Queue
import pyaudio
import warnings
from scipy import signal
from pylab import *
from rtlsdr import *

# 84.25华农英语考试

warnings.filterwarnings("ignore")   # 屏蔽告警


class th(threading.Thread):
    def __init__(self, func):
        super(th, self).__init__()
        self.func = func

    def run(self):
        self.func()


def cb(samples, rtlobj):
    global q
    q.put(samples)


def sound():
    global qs
    global s
    while True:
        nd = qs.get()
        s.write(nd)


def defm():
    global q
    global s
    while True:
        samples = q.get()
        delta = samples[0:-1] * samples[1:].conj()
        angs = np.angle(delta)
        nd = signal.decimate(angs, 21, ftype="fir")
        #nd = angs[0::21]
        print nd

        nd *= 10000
        ndt = nd.astype(np.dtype('<i2')).tostring()

        qs.put(ndt)

sdr = RtlSdr(1)

sdr.sample_rate = 1.024e6
sdr.center_freq = 84.25e6
sdr.gain = 'auto'

p = pyaudio.PyAudio()
s = p.open(format=p.get_format_from_width(2), channels=1, rate=48000, output=True)
q = Queue.Queue()
qs = Queue.Queue()
t1 = th(defm)
t1.start()
t = th(sound)
t.start()
sdr.read_samples_async(cb, 1024*500)
