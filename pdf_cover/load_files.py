 #coding=utf-8
import os
import fnmatch

files = fnmatch.filter(os.listdir('D:/BaiduNetdiskDownload/[銃夢+外傳+Last.Order][木城幸人][天下][C.C][9完+1完+15未]/第一部/[Comic][銃夢][木城ゆきと][天下][C.C]Vol_01/'), '*.png')

for img in  files:
    print img