#! /usr/bin/env python
# -*- coding: utf-8 -*-

#
#dictionary.py                   
# by billy basdras
#
# this is a small script to practice english           # Use
#
# I didn't include many assertions and checks          # Not much checking
#  so it can be useful in other languages
#
#it loads file and creates dictionary and then it       # Basic Functionality
# generates a temporary dictionary with a character
# you choose to play 
#
#
# based on an upper bound it calculates exhaustively the number of rows
#   must be a more appropriate way..
#
# adds the ones that you fail to find in a new dictionary for revision !
#

import subprocess
import time

ESTIMATED_UPPER_BOUND=22000  #of input file

file_name=raw_input("filename : ")
f=open(file_name,"r")

dictionary={}
read=''




guess=0



#  ~ tilde is only because it is the delimiter I use I don't use raw_input for that
# because I think it would be boring to answer the same questions

def dictMaker(fileProcess,lineSize):
    dictionary={}
    delimiter=0
    string=[]
    firstHalf=''
    secondHalf=''
    for i in range(lineSize-1,-1,-1):
        string=fileProcess.readline()
        delimiter=string.index('~')
        firstHalf=string[:delimiter]
        delimiter=string.index('~')+1
        secondHalf=string[delimiter:]
        dictionary[firstHalf]=secondHalf
    return dictionary



for i in range(0,ESTIMATED_UPPER_BOUND):
    read=f.readline(i)
    if '\n' in str(read):
       guess+=1
    else:
        continue


f.close


# guess equals number of lines now


f2=open(file_name,'r')


dictionary=dictMaker(f2,guess)

f2.close


tempDictionary={}
length=0
score=0
times=0


failDict={}


while True:
    userIn=raw_input("Press a letter of the alphaBet you want to practice with :")
    length=int(raw_input("and for how many words ? (expect number):"))
    print userIn
    for word in dictionary.keys():
        char=word[:1]
        if char==userIn:
            tempDictionary[word]=dictionary.get(word,0)
    try:
        while length>0:
            randomizer=random.choice(tempDictionary.keys())
            print '                       '+str(randomizer)
            userIn=raw_input("say the answer outloud ")
            print str(tempDictionary[randomizer])
            userIn=raw_input("if you got it press C for correctness otherwise anything else")
            if userIn=='c' or userIn=='C':
                score+=1
            else:
                failDict[key]=tempDictionary.get(key,0)
            times+=1
            length-=1
            if length==0:
                break
        if len(failDict)>=1:
            print 'you scored : %d out of %d '%(score,times)
            score=0
            time.sleep(1)
            print 'so revision it is then...'
            for oops in failDict.keys():
                print '                       '+str(oops)
                userIn=raw_input("say the answer outloud ")
                print str(failDict.get(oops,0))
                userIn=raw_input("if you got it press C for correctness otherwise anything else")
                if userIn=='c' or userIn=='C':
                    score+=1

            
        failDict={}
    except KeyboardInterrupt, e:
        break
    tempDictionary={}
    print 'you scored : %d out of %d '%(score,times)
    score=0
    times=0




#end of file .. for now
