# Tools for dealing with JWST data

## Algorithms

* **download_jwst.py**: Download jwst imaging raw data (_uncal).

* **make_postage_stamps.py**: Create cutouts from calibrated jwst images.

## How to use them

* **download_jwst.py**

```console
lcostant:~$  python download_jwst.py -h                       
usage: download_jwst.py [-h] [--ID [ID]]
                        [--instrument [{NIRCam,MIRI}]]
                        [--filter [FILTER]]
                        [--detector [{NRCA1,NRCA2,NRCA3,NRCA4,NRCALONG,NRCB1,NRCB2,NRCB3,NRCB4,NRCBLONG,all}]]

Download jwst raw data.

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

* **make_postage_stamps.py**

```console
lcostant:~$  python make_postage_stamps.py -h                       
usage: make_postage_stamps.py [-h] [--infile [INFILE]] [--id [ID]] [--ra [RA]] [--dec [DEC]]
                              [--coordfile [COORDFILE]] [--xycut [XYCUT]] [--addframe [{True,False}]]
                              [--overwrite [{True,False}]]

Create postage stamps for jwst imaging data.

optional arguments:
  -h, --help            show this help message and exit
  --infile [INFILE]     "Name of input image file (default=None)"
  --id [ID]             "ID of the target (default: None)"
  --ra [RA]             "RA of the target in degree - fk5 (default: None)"
  --dec [DEC]           "DEC of the target in degree - fk5 (default: None)"
  --coordfile [COORDFILE]
                        "File with ID, RA, DEC in degree - fk5 (default: None)"
  --xycut [XYCUT]       "Size of the cutout in arcsec (default: 10)"
  --addframe [{True,False}]
                        "Create ERR and WHT frames additional (default: False)"
  --overwrite [{True,False}]
                        "Overwrite previous results (default: False)"
```

## Author

**Luca Costantin** (Centro de Astrobiología CSIC-INTA, Madrid, Spain)

## Contact

Luca Costantin: lcostantin@cab.inta-csic.es

## Licensing

JWSTools scripts are distributed under GNU GPLv3.

