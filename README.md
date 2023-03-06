# Tools for dealing with JWST data

## Algorithms

* **download_jwst.py**: Download jwst imaging raw data (_uncal).

```console
lcostant:~/MEGARA/N/ $  python 1_simulations_reduction.py -h                       
usage: download_jwst.py [-h] [--ID [ID]]
                        [--instrument [{NIRCam,MIRI}]]
                        [--filter [FILTER]]
                        [--detector [{NRCA1,NRCA2,NRCA3,NRCA4,NRCALONG,NRCB1,NRCB2,NRCB3,NRCB4,NRCBLONG,all}]]

Download jwst raw data

options:
  -h, --help            show this help message and
                        exit
  --ID [ID]             "Proposal ID (default=0)"
  --instrument [{NIRCam,MIRI}]
                        "JWST instrument (default=NIRCam)"
  --filter [FILTER]     "Filter (default=None)"
  --detector [{NRCA1,NRCA2,NRCA3,NRCA4,NRCALONG,NRCB1,NRCB2,NRCB3,NRCB4,NRCBLONG,all}]
                        "Detector - NIRCam (default=all)"
  ```

- - - - - - - - - - - - -

* **make_postage_stamps.py**: Create cutouts from calibrated jwst images.

## Author

**Luca Costantin** (Centro de Astrobiología CSIC-INTA, Madrid, Spain)

## Contact

Luca Costantin: lcostantin@cab.inta-csic.es

## Licensing

JWSTools scripts are distributed under GNU GPLv3.

