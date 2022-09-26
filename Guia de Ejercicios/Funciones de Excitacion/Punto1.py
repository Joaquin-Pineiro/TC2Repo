# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:56:19 2022

@author: Joaquin
"""

import sympy as sp
import splane as tc2
from schemdraw import Drawing
from schemdraw.elements import  Resistor


s = sp.symbols('s ', complex=True)

FF = ((s**2+1)*(s**2+5)*(s**2+20))/(s*(s**2+10)*(s**2+2))



k0, koo, ki = tc2.foster(FF)

tc2.dibujar_foster_serie(k0, koo, ki, z_exc =FF)      
tc2.dibujar_foster_derivacion(k0, koo, ki, y_exc =FF)         