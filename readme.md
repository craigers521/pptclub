## PPT Club

#### Setup

`pip install -r reqs.txt`

#### Usage

usage: python pptclub.py [-h] [-o presenters] [-q qrcode] [-s score] [-p powerpoint]

options:
  -h, --help            show this help message and exit
  -o ORDER [ORDER ...], --order ORDER [ORDER ...]
                        specify space seperated list of presenters
  -q QR, --qr QR        specify URL for QR code generation
  -s [SCORE], --score [SCORE]
                        specify CSV file for scoring, otherwise will look for export.csv
  -p [POWERPOINT], --powerpoint [POWERPOINT]
                        specify filename for ppt, default will be results.pptx
