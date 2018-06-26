"""
.. module:: test/fsr_test
   : platform:
   : synopsis: test and enlists all the functions of the reride/fsr library

.. moduleauthor:: @grvashu, @anchitsh96

"""

import sys
sys.path.append("..")

from reride import fsr

# Default initialisation
f = fsr.FSR()

f.calibrate()
# Custom initialisation
#f = fsr.FSR(adc1 = [0x49,1], adc2 = [0x48,0])
while True:
    #data=f.read_fsr_sampled(sampling_duration=0.2, samples=5)
    data=f.read_fsr(read=[0,4],mapped=False)
    print(data)
s
