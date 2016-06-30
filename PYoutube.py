# -*- coding: utf-8 -*-
from tqdm import tqdm
import requests,argparse,os
from datetime import timedelta
from bs4 import BeautifulSoup
parser = argparse.ArgumentParser(description = 'Downloading YouTube videos: By Willian Lopes')
parser.add_argument("-u","--url",required=False ,help="Specify url")
parser.add_argument("-p","--playlist",required=False ,help="Specify a playlist URL EX: 'http://www.youtube.com/playlist?list=PLC800B9699743BD19' ")
parser.add_argument("-l","--list",required=False ,help="Specify a list of URLs EX: 'list.txt'")
parser.add_argument("-f", "--format",required=True,help="Specify format mp3 or mp4")
parser.add_argument("-t","--title",required=False,help="Specify title")
parser.add_argument("-s", "--start",required=False,help="Specify start time 00:00:00",default=False)
parser.add_argument("-e", "--end",required=False,help="Specify end time 00:00:00",default=False)
parser.add_argument("-o", "--output",required=False,help="Specify a folder to save the files")
args = parser.parse_args()
url= args.url
def down(url,titles):
	args.url = url
	if args.format == "mp3" or args.format == "mp4":
		if "youtu" in args.url and "playlist?list=" not in args.url:
			if "https://" not in args.url:
					args.url = "http://%s" % (args.url)
			if "youtu.be" in args.url:
				mid = args.url.split("/")[3]
			else:
				mid = args.url.split("=")[1]
			if titles:
				title = titles.encode('utf8')
			else:
				if args.title:
					title = args.title.encode('utf8')
				else:
					r = requests.get(args.url)
					soup = BeautifulSoup(r.text, "html.parser")
					ti = soup.find('title').text
					title = ti[:-10].encode('utf8').decode('utf-8').replace('/',"").replace("\\","").replace("|","").replace('"',"").replace("'","")
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
			try:
				down = requests.post("https://dvr.yout.com/"+args.format, data={'id_video': mid, 'video_id': mid,'title': title, 'format' : args.format, 'start_time': args.start,'end_time': args.end})
				if down.status_code == 200:
					if args.output:
						if os.path.exists(args.output):
							filename = "%s/%s.%s" % (args.output.decode('utf-8'),title,args.format)
						else:
							print "[-] The folder '%s' does not exist " % (args.output.decode('utf-8'))
							exit(0)
					else:
						filename = "%s.%s" % (title,args.format)
					with open(filename, "wb") as handle:
						for data in tqdm(down.iter_content()):
							handle.write(data)
					print "Successfully concluded"
				else:
					print "[-] Error, try again"
			except:
				print "[-] Error, Download %s" % (title)
		else:
			print "[-] Error, invalid URL"
			exit(0)
	else:
		print parser.usage
		exit(0)

try:
	if args.list:
		with open(args.list, "r") as listvid:
		    for url in listvid:
			url = url.strip("\n")
			down(url,False)
	elif args.url:
		down(url,False)

	elif args.playlist:
		if "/playlist?list=" in args.playlist:
			rec = "https://api.import.io/store/connector/f4d61ed2-3d40-4371-84cf-fb399b008c37/_query?input=webpage/url:%s&_apikey=b66cfe87eb494b759b4aa5b42ac0f4c57f5b303285e7d8670e381dbfa5a9d8c4cb84023448214d875aa268edaeef07dc6b86ba192a44be472114b2741b1606b13e122e59ff728d051fb9ebdbda59d058" %(args.playlist)
			r = requests.get(rec)
			cap = r.json()
			for i in cap['results']:
				qnt = i['videotitle_link'].split('index=')[1]
			cont = 0
			for i in cap['results']:
				titles = i['videotitle_link/_text'] 
				url = "https://www.youtube.com/watch?v=%s" % (i['videotitle_link/_source'].split("=")[1].replace("&index",""))
				cont = cont+1
				print "%s/%s"%(str(cont),str(qnt))
				down(url,titles)
		else:
			print parser.parse_args(['-p'])
			exit(0)
	else:
		print parser.usage
		exit(0)
except KeyboardInterrupt:
	print "\nExit"
	exit(0)


