#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys, json
import mido

# 打开文件
path = "../data"
dirs = os.listdir( path )
all_file={}
list=[0] * 28 
index=0
# 输出所有文件和文件夹
for subpath in dirs:
    subdirs = os.listdir( path+"/"+subpath )
    all_file["author"]=subpath
    all_file["children"]=[]
    for file in subdirs:
        all_file["children"].append({"name":file})
    list[index]=all_file
    all_file={}

    index+=1
# mid = mido.MidiFile('../data/Mozart/K299 Flute Harp Concerto 1mov.mid')
print(list[1])
# print(sorted(all_file),cmp=lambda x,y:cmp(x[1],y[1]))
    
with open("all_data.json","w") as file:
    file.write(json.dumps({"name":"all data","children":list}))

