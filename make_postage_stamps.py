'''
Copyright 2023 Astrobiology Center (Madrid)

This file software allows to create postage stamps of jwst images.

@Author: Luca Costantin (lcostantin@cab.inta-csic.es)

:SPDX-License-Identifier: GPL-3.0+

:History:
18 Feb 23:  version 1.0
'''

import os
import argparse
import numpy as np

from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import Cutout2D
from astropy.coordinates import SkyCoord

__version__ = "1.0"
__author__  = "Luca Costantin, Astrobiology Center (Madrid)"

def postage_stamp(ra, dec, idx=None):
	'''Create postage stamps with a fixed size.
	'''	
	position = SkyCoord(ra, dec, frame='fk5', unit='deg')

	with fits.open(args.infile) as hdu:
		header0    = hdu[0].header
		header_SCI = hdu[1].header
		frame_SCI  = hdu[1].data

		if (args.addframe == True):
			header_ERR = hdu[2].data
			frame_ERR  = hdu[2].data
			header_WHT = hdu[2].data
			frame_WHT  = hdu[4].data

		wcs = WCS(header_SCI)

	try:
		SCI_cutout = Cutout2D(frame_SCI, position, args.xycut, 
								mode='strict', wcs=wcs)

		hdu[1].header.update(SCI_cutout.wcs.to_header())

		if args.coordfile is None:
			outname = 'image_cutout'
			if args.id is not None:
				outname = f'{args.id}_cutout'
		else:
			outname = f'{idx}_cutout'

		file_cutout = f'{os.path.abspath(os.getcwd())}/{outname}.fits'

		hdu_header = fits.PrimaryHDU(header=header0)
		hdu_SCI    = fits.ImageHDU(SCI_cutout.data, header=header_SCI)
		hdu_cutout = fits.HDUList([hdu_header, hdu_SCI])

		if (args.addframe is True):

			ERR_cutout = Cutout2D(frame_ERR, position, args.xycut, 
								  mode='strict', wcs=wcs)

			WHT_cutout = Cutout2D(frame_WHT, position, args.xycut, 
								  mode='strict', wcs=wcs)

			hdu_ERR = fits.ImageHDU(ERR_cutout.data, name='ERR')
			hdu_WHT = fits.ImageHDU(WHT_cutout.data, name='WHT')

			hdu_cutout.append(hdu_ERR)
			hdu_cutout.append(hdu_WHT)

			print(hdu_cutout)

		if (os.path.isfile(file_cutout) is False or args.overwrite is True):

			hdu_cutout.writeto(file_cutout, overwrite=True)

	except:
		pass
	

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Create postage stamps for jwst imaging data.')
	parser.add_argument("--infile", help='"Name of input image file (default=None)"', nargs='?', type=str, default=None)
	parser.add_argument("--id", help='"ID of the target (default: None)"', nargs='?', type=int, const=None, default=None)
	parser.add_argument("--ra", help='"RA of the target in degree - fk5 (default: None)"', nargs='?', type=float, const=None, default=None)
	parser.add_argument("--dec", help='"DEC of the target in degree - fk5 (default: None)"', nargs='?', type=float, const=None, default=None)
	parser.add_argument("--coordfile", help='"File with ID, RA, DEC in degree - fk5 (default: None)"', nargs='?', type=str, default=None)
	parser.add_argument("--xycut", help='"Size of the cutout in px (default: 200)"', nargs='?', type=int, const=200, default=200)
	parser.add_argument("--addframe", help='"Create ERR and WHT frames additional (default: False)"', nargs='?', type=bool, choices=(True, False), const=False, default=False)
	parser.add_argument("--overwrite", help='"Overwrite previous results (default: False)"', nargs='?', type=bool, choices=(True, False), const=False, default=False)
	args = parser.parse_args()

	if (args.coordfile is not None):

		idx = np.loadtxt(args.coordfile, usecols=0, dtype=int)
		ra  = np.loadtxt(args.coordfile, usecols=1, dtype=float)
		dec = np.loadtxt(args.coordfile, usecols=2, dtype=float)

		for i in range(idx.size):

			if (idx.size == 1):
				postage_stamp(ra, dec, idx)

			else:
				postage_stamp(ra[i], dec[i], idx[i])

	else:
		
		ra = args.ra 
		dec = args.dec

		postage_stamp(ra, dec)

