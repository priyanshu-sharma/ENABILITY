# -*- coding: utf-8 -*- 

#Take note
#Purpose:Python code to convert Hex code to Text as per Grade 1 Braille 
 
#@author Manikandan V
#@version 1.0
#@date 09/01/18

from __future__ import print_function
import os,sys
#****** Declaration of Alphebets and corresponding Hex codes *********** 

alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alp_index = ['210','230','218','21c','214','238','23c','234','228','22c','250','270','258','25c','254','278','27c','274','268','26c','252','272','22e','25a','25e','256']

#****** Declaration of Numbers and corresponding Hex codes ************

no=['1','2','3','4','5','6','7','8','9','0']
no_index = ['210','230','218','21c','214','238','23c','234','228','22c']

#****** Declaration of Special Charaters (which is used without sign) and corresponding Hex codes ***********

sp_chr1=['.',',',';',':','!','?','\'','-']
sp_chr_index1=['226','220','260','224','264','262','240','242']

#****** Declaration of Special Charaters (which is used with sign) and corresponding Hex codes **************

sp_chr2=['"','"','(',')','/','*']
sp_chr_index2=['262','246','232','24c','248','244']

cp_cnt=0 # To identify Letter Caps, Word Caps and Paragraph Caps
number=0 # To identify number or Alphebet
sign=0 # For sign procesing

#************** Open and Read text file containing Hex code ***************

file = open("NOTE1.TXT", "r") # Rename your file name
data = file.read()
file.close()

#*************** open new text file to store converted text ****************

new_file=open("NOTE_op.TXT", "w")

#******** Function to print Alphebets  (including Caps) ***************

def alp_decode(char):
	global cp_cnt
	if cp_cnt==0: # Small letters
		#print (alp[alp_index.index(char)], end='')
		new_file.write(alp[alp_index.index(char)])
	elif cp_cnt==1: # letter Caps
		#print ((alp[alp_index.index(char)]).upper(), end='')
		new_file.write((alp[alp_index.index(char)]).upper())
		cp_cnt=0
	elif cp_cnt>1: # Word caps and Paragraph Caps
		#print ((alp[alp_index.index(char)]).upper(), end='')
		new_file.write((alp[alp_index.index(char)]).upper())

#************** Function to print Numbers **************

def no_decode(char):
	print (no[no_index.index(char)], end='')
	new_file.write(no[no_index.index(char)])

#************** Function to print special character *********

def sp_chr_decode(char):
	global sign
	if sign==0: # Spececial character without sign
		#print (sp_chr1[sp_chr_index1.index(char)], end='')
		new_file.write(sp_chr1[sp_chr_index1.index(char)])
	else: # Special character with sign
		#print (sp_chr2[sp_chr_index2.index(char)], end='')
		new_file.write(sp_chr2[sp_chr_index2.index(char)])
		sign=0

#**************** Function to find the hex code is Alphebet or number or special character

def convert():
	try:
		if number==1: # Number
			no_decode(Hex)
		elif number==0: # Alphebet 
			alp_decode(Hex)
	except ValueError:
		pass
	try:
		sp_chr_decode(Hex) # Special character
	except ValueError:
		pass

#*********************** Main function starts Here ********************************

for i in range(0, len(data)-1, 3): # Split text to hexcode size of 3
	Hex = data[i:i + 3] 

#*********************** Sign Processing **********************

	if Hex=='24e': # Letter to number Sign          #done
		number=1
		continue
	elif Hex=='206': # Number to letter Sign                #done
		number=0
		continue
	elif Hex =='202': # Capital letter/word/paragraph Identification Sign           #done
		cp_cnt=cp_cnt+1
		continue
	elif Hex=='300':# Space                 #done
		#print(' ')
		new_file.write(' ')
		number=0		
		if cp_cnt==2:cp_cnt=0
		continue
	elif Hex=='280':#Enter                  #done
		#print('\n')
		new_file.write('\n')
		cp_cnt=0
		number=0
		continue
	elif Hex=='201':# Back space             #done
		#print('\b')
		#new_file.write('\b')
		new_file.seek(-1, os.SEEK_CUR)
		continue
	elif Hex=='204':#Sign To write ( ) *            #done
		sign=1
		continue
	elif Hex=='20c':#Sign To write “ ”              #done
		sign=2
		continue
	elif Hex=='20e':#Sign To write  /               #done
		sign=3
		continue
	convert()
	
new_file.close() # close the text file

new_file=open("NOTE_op.TXT", "r") # Open text file contains converted data
final_data=new_file.read() # Read file
print(final_data) #Print file data
new_file.close() # close file 


