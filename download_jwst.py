'''
Copyright 2023 Astrobiology Center (Madrid)

This file software allows to download jwst imaging data

@Author: Luca Costantin (lcostantin@cab.inta-csic.es)

:SPDX-License-Identifier: GPL-3.0+
:License-Filename: LICENSE.txt

:History:
20 Feb 22:  version 1.0
'''

import argparse
from astroquery.mast import Observations

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Download jwst raw data.')
    parser.add_argument("--ID", help='"Proposal ID (default=0)"', 
                                nargs='?', 
                                type=int, 
                                const='0', 
                                default='0')
    parser.add_argument("--instrument", help='"Instrument (default=NIRCam)"', 
                                        nargs='?', 
                                        choices=('NIRCam', 'MIRI'), 
                                        type=str, 
                                        const='NIRCam', 
                                        default='NIRCam')
    parser.add_argument("--filter", help='"Filter (default=None)"', 
                                    nargs='?', 
                                    type=str, 
                                    const=None, 
                                    default=None)
    parser.add_argument("--detector", help='"Detector - NIRCam (default=all)"', 
                                      nargs='?', 
                                      choices=('NRCA1','NRCA2','NRCA3','NRCA4',\
                                      'NRCALONG','NRCB1','NRCB2','NRCB3',\
                                      'NRCB4','NRCBLONG','all'), 
                                      type=str, 
                                      const='all', 
                                      default='all')
    args = parser.parse_args()

# GET YOUR OWN TOKEN HERE: https://auth.mast.stsci.edu/token'
    token = 'add your own token here'          
    Observations.login(token=token)

    if (args.filter == 'all'):
        jwst_filter = '*'
    else:
        jwst_filter = args.filter

    obs_table = Observations.query_criteria(obs_collection='JWST', 
                                            proposal_id=[args.ID], 
                                            instrument_name=args.instrument, 
                                            filters=jwst_filter,
                                            dataproduct_type='image')

    products = Observations.get_product_list(obs_table)

    which = [i for i, p in enumerate(products) if 
            (p["productSubGroupDescription"] in ["UNCAL"])]
    products_uncal = products[which]

    if (args.detector == 'all'):
        Observations.download_products(products_uncal)

    else:
        for _, file_det in enumerate(products_uncal):

            if (args.detector == 'NRCALONG' or args.detector == 'NRCBLONG'):

                check_detector = file_det["productFilename"][-19:-11]

            else:

                check_detector = file_det["productFilename"][-16:-11]

            if (check_detector == args.detector.lower()):

                Observations.download_products(file_det)
