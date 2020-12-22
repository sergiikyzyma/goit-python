import os
'''import sys

path = sys.argv[1]
print(path)'''

files = os.listdir("/media/teosoph/Data/Квартира")
#print(files)

cortFolder = ("folder")
cortImage = ("jpeg", "png", "jpg", "")
cortVideo = ("avi", "mp4", "mov", "")
cortText = ("doc", "dcox", "txt", "odt")
cortMusic = ("mp3", "ogg", "wav", "amr")
cortVarious = ("max", "vsd", "", "")

dictFiles = {cortFolder: "", cortImage: "", cortVideo: "", cortText: "", cortMusic: "", cortVarious: ""}

for elem in files:
    if "." in elem:
        j = 0
        while not (elem.endswith(cortImage[j]) or elem.endswith(cortVideo[j]) or elem.endswith(cortText[j]) or elem.endswith(cortMusic[j]) or elem.endswith(cortVarious[j])):
            j += 1
        else:
            if elem.endswith(cortImage[j]):
                dictFiles[cortImage] = elem
            elif elem.endswith(cortVideo[j]):
                dictFiles[cortVideo] = elem
            elif elem.endswith(cortText[j]):
                dictFiles[cortText] = elem
            elif elem.endswith(cortMusic[j]):
                dictFiles[cortMusic] = elem
            elif elem.endswith(cortVarious[j]):
                dictFiles[cortVarious] = elem
    else:
        dictFiles[cortFolder] = elem

    for key, value in dictFiles.items():
        print(f"Keys = {key} Values = {value}")