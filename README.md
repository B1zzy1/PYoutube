# PYoutube
Downloading YouTube videos mp3/mp4
## Requirements
* requests
* tqdm
* beautifulsoup4

### pip install -r requirements.txt

## Usage:
usage: PYoutube.py [-h] -u URL -f FORMAT [-t TITLE] [-s START] [-e END]

Download YouTube Video: By Willian Lopes

optional arguments:

  -h, --help            show this help message and exit
  
  -u URL, --url URL     Specify url
  
  -f FORMAT, --format FORMAT
                        Specify format mp3 or mp4
                        
  -t TITLE, --title TITLE
                        Specify title
                        
  -s START, --start START
                        Specify start video 00:00:00
                        
  -e END, --end END     Specify end video 00:00:00
