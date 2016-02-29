# -*- coding: utf-8 -*-
from tqdm import tqdm
import requests,argparse
from datetime import timedelta
from bs4 import BeautifulSoup
parser = argparse.ArgumentParser(description = 'Downloading YouTube videos: By Willian Lopes')
parser.add_argument("-u","--url",required=False ,help="Specify url")
parser.add_argument("-l","--list",required=False ,help="Specify a list of URLs 'video.txt'")
parser.add_argument("-f", "--format",required=True,help="Specify format mp3 or mp4")
parser.add_argument("-t","--title",required=False,help="Specify title")
parser.add_argument("-s", "--start",required=False,help="Specify start time 00:00:00",default=False)
parser.add_argument("-e", "--end",required=False,help="Specify end time 00:00:00",default=False)
args = parser.parse_args()
url= args.url
def down(url):
	args.url = url
	if args.format == "mp3" or args.format == "mp4":
		if "youtu" in args.url:
			if "https://" not in args.url:
					args.url = "http://%s" % (args.url)
			if "youtu.be" in args.url:
				mid = args.url.split("/")[3]
			else:
				mid = args.url.split("=")[1]
			if args.title:
				title = args.title
			else:
				r = requests.get(args.url)
				soup = BeautifulSoup(r.text, "html.parser")
				ti = soup.find('title').text
				title = ti[:-10]
			print "Downloading :", title
			if args.start:
				star=[]
				for i in args.start.split(":"):
					star.append(int(i))
				args.start = timedelta(hours=star[0],minutes=star[1], seconds=star[2]).total_seconds()
			if args.end:
				en=[]
				for i in args.end.split(":"):
					en.append(int(i))
				args.end = timedelta(hours=en[0],minutes=en[1], seconds=en[2]).total_seconds()
			down = requests.post("https://dvr.yout.com/"+args.format, data={'id_video': mid, 'video_id': mid,'title': title, 'format' : args.format, 'start_time': args.start,'end_time': args.end})
			if down.status_code == 200:
				filename = "%s.%s" % (title,args.format)
				with open(filename, "wb") as handle:
				    for data in tqdm(down.iter_content()):
					handle.write(data)
			else:
				print "[-] Error, try again"
		else:
			print "[-] Error, invalid URL"
			exit(0)
	else:
		print parser.usage
		exit(0)

if args.list:
	with open(args.list, "r") as listvid:
	    for url in listvid:
		url = url.strip("\n")
		down(url)
elif args.url:
	down(url)
else:
	print parser.usage
	exit(0)

