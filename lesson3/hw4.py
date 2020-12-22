import os
'''import sys

path = sys.argv[1]
print(path)'''

files = os.listdir("/media/teosoph/Data/Квартира")
#print(files)

cortEmpty = tuple("")
cortImage = tuple("jpeg" "png" "jpg")
cortVideo = tuple("avi" "mp4" "mov")
cortText = tuple("doc" "dcox" "txt" "odt")
cortMusic = tuple("mp3" "ogg" "wav" "amr")
cortVarious = tuple("max" "vsd")

dictFiles = {cortEmpty: "", cortImage: "", cortVideo: "", cortText: "", cortMusic: "", cortVarious: ""}
'''
i = 0
for ch in files[i]:
    strType = ""
    if "." in files[i]:
        if cortImage[j] in files[i]:
            strType += files[i].endswith(cortImage[j])
    else:
        pass
else:
    i += 1

print(dictFiles)'''
if "." in files[0]:
    print(files[0].endswith(cortImage[3]))
    #dictFiles[cortImage] = cortImage[3]
    #files[0].find(sub: text, end: cortImage[3])
    print(dictFiles)