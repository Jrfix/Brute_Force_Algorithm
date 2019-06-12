#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from os import system
from time import sleep
import time

chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","q","z"]
password = raw_input("password: ")
choice = ""

seconds = 50


start = time.time()


def main():
	for progress in range(0,seconds+1):
	    percent = (progress * 100) // seconds
	    print("\n")
	    print("Loading...")
	    print("<" + ("=" * progress) + (" " * (seconds-progress)) + "> " + str(percent) + "%")
	    print("\n")
	    sleep(0.04)
	    system('clear') 
	print("1) a-z")
	print("2) A-Z")
	print("3) 0-9")
	print("4) a-z , A-Z")
	print("5) a-z , 0-9")
	print("5) a-z , 0-9 , A-Z")
	print("6) !-?")
	print("7) a-z , !-?")
	print("8) 0-9 , !-?")
	print("9) A-Z , !-?")
	print("10) a-z , 0-9 , !-?")
	print("11) A-Z , 0-9 , !-?")
	print("12) a-z , A-Z , 0-9 , !-?")
	print("")
	print("")
	choice = raw_input("Select: ")
	sleep(1)
	system('clear')
	hane1()
	






def hane1():
	
	l_e = chars[-1] #son elemanı alır
	g_e = l_e
	for oku in chars:
		harf1=oku
		toplam=harf1
		print("\033[91m"+toplam)
		if password == toplam:
			print("\033[92m"+"[+] Password founded "+toplam)
			end = time.time()
			print("The time has been spent on this process is " + str(end - start) +" sec")
			exit()
		elif(password != toplam and g_e == toplam):
			print("\033[93m"+"[-]Not founded")
			hane2()

def hane2():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2	
			toplam=harf1+harf2
			print("\033[91m"+toplam)
			if password == toplam:
				print("\033[92m"+"[+] Password founded "+toplam)
				end = time.time()
				print("The time has been spent on this process is " + str(end - start) +" sec")
				exit()
			elif(password != toplam and g_e == toplam):
				print("\033[93m"+"[-]Not founded")
				hane3()

def hane3():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3	
				toplam=harf1+harf2+harf3
				print("\033[91m"+toplam)
				if password == toplam:
					print("\033[92m"+"[+] Password founded "+toplam)
					end = time.time()
					print("The time has been spent on this process is " + str(end - start) +" sec")
					exit()
				elif(password != toplam and g_e == toplam):
					print("\033[93m"+"[-]Not founded")
					hane4()

def hane4():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4	
					toplam=harf1+harf2+harf3+harf4
					print("\033[91m"+toplam)
					if password == toplam:
						print("\033[92m"+"[+] Password founded "+toplam)
						end = time.time()
						print("The time has been spent on this process is " + str(end - start)+" sec" )
						exit()
					elif(password != toplam and g_e == toplam):
						print("\033[93m"+"[-]Not founded")
						hane5()

def hane5():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5	
						toplam=harf1+harf2+harf3+harf4+harf5
						print("\033[91m"+toplam)
						if password == toplam:
							print("\033[92m"+"[+] Password founded "+toplam)
							end = time.time()
							print("The time has been spent on this process is " + str(end - start) +" sec")
							exit()
						elif(password != toplam and g_e == toplam):
							print("\033[93m"+"[-]Not founded")
							hane6()
def hane6():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6	
							toplam=harf1+harf2+harf3+harf4+harf5+harf6
							print("\033[91m"+toplam)
							if password == toplam:
								print("\033[92m"+"[+] Password founded "+toplam)
								end = time.time()
								print("The time has been spent on this process is " + str(end - start) +" sec")
								exit()
							elif(password != toplam and g_e == toplam):
								print("\033[93m"+"[-]Not founded")
								hane7()

def hane7():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7
								print("\033[91m"+toplam)
								if password == toplam:
									print("\033[92m"+"[+] Password founded "+toplam)
									end = time.time()
									print("The time has been spent on this process is " + str(end - start) +" sec")
									exit()
								elif(password != toplam and g_e == toplam):
									print("\033[93m"+"[-]Not founded")
									hane8()
def hane8():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								for oku8 in chars:
									harf8=oku8	
									toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7+harf8
									print("\033[91m"+toplam)
									if password == toplam:
										print("\033[92m"+"[+] Password founded "+toplam)
										end = time.time()
										print("The time has been spent on this process is " + str(end - start)+" sec" )
										exit()
									elif(password != toplam and g_e == toplam):
										print("\033[93m"+"[-]Not founded")
										hane9()
def hane9():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								for oku8 in chars:
									harf8=oku8	
									for oku9 in chars:
										harf9=oku9	
										toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7+harf8+harf9
										print("\033[91m"+toplam)
										if password == toplam:
											print("\033[92m"+"[+] Password founded "+toplam)
											end = time.time()
											print("The time has been spent on this process is " + str(end - start)+" sec" )
											exit()
										elif(password != toplam and g_e == toplam):
											print("\033[93m"+"[-]Not founded")
											hane10()
def hane10():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								for oku8 in chars:
									harf8=oku8	
									for oku9 in chars:
										harf9=oku9
										for oku10 in chars:
											harf10=oku10	
											toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7+harf8+harf9+harf10
											print("\033[91m"+toplam)
											if password == toplam:
												print("\033[92m"+"[+] Password founded "+toplam)
												end = time.time()
												print("The time has been spent on this process is " + str(end - start) +" sec")
												exit()
											elif(password != toplam and g_e == toplam):
												print("\033[93m"+"[-]Not founded")
												hane11()
def hane11():
	l_e = chars[-1] #son elemanı alır
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								for oku8 in chars:
									harf8=oku8	
									for oku9 in chars:
										harf9=oku9
										for oku10 in chars:
											harf10=oku10
											for oku11 in chars:
												harf11=oku11	
												toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7+harf8+harf9+harf10+harf11
												print("\033[91m"+toplam)
												if password == toplam:
													print("\033[92m"+"[+] Password founded "+toplam)
													end = time.time()
													print("The time has been spent on this process is " + str(end - start)+" sec" )
													exit()
												elif(password != toplam and g_e == toplam):
													print("\033[93m"+"[-]Not founded")
													hane12()








main()
