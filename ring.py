# -*- coding: UTF-8 -*-
import pygame
import time
import requests
import json
import sys

url = "http://data.voiceofhand.com/app/iqueue"
header =  {'Connection': 'close',}

def main():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load("sound.wav")

	while True:
		try:
			r = requests.get(url,headers=header)
		except requests.exceptions.ConnectionError:
			print("Connection Error")
		except requests.exceptions.ConnectTimeout:
			print("Connect Time Out")
		except requests.exceptions.ReadTimeout:
			print("Read Time Out")
		else:
			json_r = r.json()
			whole =json_r['whole']
			normal = json_r['normal']
			vip = json_r['vip']
			if whole == 0:
				pygame.mixer.music.stop()
			else:
				time_now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				if vip != 0:
					print(u'有VIP在队列中' + time_now)
					pygame.mixer.music.play()
				else:
					print(u'有人在队列中' + time_now)
					pygame.mixer.music.play()
		time.sleep(1)

if __name__ == '__main__':
	main()