# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

import matplotlib as mpl
from matplotlib import pyplot as plt

from scipy import signal as sig
from splane import analyze_sys, pretty_print_bicuad_omegayq


C = 1e-6
R1=5e3
R2 = 5e3
R3 = 1e3

wc = 1/(C*R3)


num = np.array([1,wc*R2/R1])
den = np.array([1,wc])

T = sig.TransferFunction(num , den)


pretty_print_bicuad_omegayq(num,den)


analyze_sys(T,'Filtro Pasa Todo')

