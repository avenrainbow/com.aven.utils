"""
BPC Timing
"""
import pyaudio
import struct
import datetime
import math

def dropandfill(l,s):return '0'*(l - len(s[2:])) + s[2:]
def time2code(date_time, dt = datetime.timedelta(0)):

    # Convert time to BPC encoding.
    date_time -= dt
    date = [date_time.day, date_time.month, date_time.year]
    timet = [date_time.hour,date_time.minute,date_time.weekday()+1]
    date[2] = date[2]%100#year
    timet[0] = timet[0]%12#am.pm
    p1 = dropandfill(2,bin(date_time.second/20))#seconds
    p2 = '00'#reserved
    sec1 = (p1+p2)+''.join(map(dropandfill,[4,6,4],map(bin,timet)))
    p31 = str(int(date_time.hour>=12))
    p32 = str((sec1.count('1'))%2)
    p3 = p31 + p32
    sec2 = ''.join(map(dropandfill,[6,4,6],map(bin,date)))
    p41 = str(int(date_time.year%1000>100))
    p42 = str(((sec2.count('1'))%2))
    p4 = p41 + p42
    code2 = sec1 + p3 +sec2 + p4
    bin2four = {'00':'1','01':'2','10':'3','11':'4'}#to base4
    return '0'+''.join([bin2four[code2[2*i:2*i+2]] for i in range(len(code2)/2)])

dt = datetime.timedelta(hours = 1)#fake time shift
samp_rate = 68500
freq = 6850 * 2 #in Hertz
ttime =20 #in Sec
SAMPLE_LEN = samp_rate * ttime # 20 seconds of cosine
value = ampl = 32725
div = samp_rate/freq/2
data = 32725
# set audio outputstream
p = pyaudio.PyAudio()
stream = p.open(format = 8,
                channels = 1,
                rate = samp_rate,
                output = True)

while True:
    date_time = datetime.datetime.now()+dt
    print date_time
    sec = (date_time.second+1)%20
    code_str = time2code(date_time)
    start = sec * samp_rate
    for i in xrange((start), SAMPLE_LEN):
        #if i % div == 0:value = -value#carrier generate
        value = ampl * int(math.cos(math.pi / float(div) * float(i)))
        pulse = (i - sec * samp_rate)/(samp_rate / 10)
        packed_value = struct.pack('h', int(pulse >= int(code_str[sec]))*value)
        stream.write(packed_value)
        if i % samp_rate == 0 and i != start:
            sec = sec + 1