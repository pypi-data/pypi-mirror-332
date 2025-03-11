#!/usr/bin/env python
from __future__ import print_function
from chiplotle3.tools.plottertools import instantiate_plotters
import sys
import time

def plot_hpgl_file(file):
   '''Send an HPGL file to the plotter found connected to the computer.'''
   plotter = instantiate_plotters( )[0]

   plotter.set_origin_bottom_left()

   plotter.write_file(file)
   ## call flush( ) to wait till all data is written before exiting...
   plotter._serial_port.flush( )


def main():
   if len(sys.argv) < 2:
      print('Must give HPGL file to plot.\nExample: $ plot_hpgl_file.py myfile.hpgl')
      sys.exit(2)
   file = sys.argv[1]

   plot_hpgl_file(file) 

   
if __name__ == '__main__':
   main()