# PYoutube
Downloading YouTube videos mp3/mp4
## Requirements
* requests
* argparse
* tqdm
* beautifulsoup4

### pip install -r requirements.txt

## Usage:
usage: PYoutube.py [-h] -u URL [-p PLAYLIST] [-l LIST] -f FORMAT [-t TITLE] [-s START] [-e END] [-o OUTPUT]

Downloading YouTube videos: By Willian Lopes

optional arguments:

  -h, --help            show this help message and exit
  
  -u URL, --url URL     Specify url
  
  -pl PLAYLIST, --playlist PLAYLIST
                        Specify a playlist URL EX: 'http://www.youtube.com/playlist?list=PLC800B9699743BD19'

  -l LIST, --list LIST  Specify a list of URLs 'video.txt'"
  
  -f FORMAT, --format FORMAT
                        Specify format mp3 or mp4
                        
  -t TITLE, --title TITLE
                        Specify title
                        
  -s START, --start START
                        Specify start time 00:00:00
                        
  -e END, --end END     Specify end time 00:00:00
  
  -o OUTPUT, --output OUTPUT  Specify a folder to save the files
