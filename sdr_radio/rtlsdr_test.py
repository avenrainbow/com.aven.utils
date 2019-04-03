#coding:utf-8

import warnings
warnings.filterwarnings("ignore")   # 屏蔽告警

from scipy import signal
from pylab import *
from rtlsdr import *

serial_numbers = RtlSdr.get_device_index_by_serial('00000001')
print serial_numbers

sdr = RtlSdr(1)
# configure device
sdr.sample_rate = 2.048e6  # Hz 采样频率
sdr.center_freq = 89.3e6    # Hz 中心频率
sdr.freq_correction = 60  # PPM 频率校正
sdr.gain = 'auto'

samples = sdr.read_samples(512)
print(samples)

delta = samples[0:-1] * samples[1:].conj()  # 求差

angs = np.angle(delta)    # 求取幅角

nd = signal.decimate(angs, 21, ftype="fir")  # 下采样，fir滤波器

nd *= 10000  # 转换值域

snd_samp = nd.astype(np.dtype('<i2')).tostring()




