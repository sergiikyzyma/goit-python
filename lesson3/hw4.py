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
cortVarious = ("max", "vsd", "blend", "")

dictFiles = {cortFolder: [], cortImage: [], cortVideo: [], cortText: [], cortMusic: [], cortVarious: []}

for elem in files:
    if "." in elem:
        j = 0
        while not (elem.endswith(cortImage[j]) or elem.endswith(cortVideo[j]) or elem.endswith(cortText[j]) or elem.endswith(cortMusic[j]) or elem.endswith(cortVarious[j])):
            j += 1
        else:
            if elem.endswith(cortImage[j]):
                dictFiles[cortImage].append(elem)
            elif elem.endswith(cortVideo[j]):
                dictFiles[cortVideo].append(elem)
            elif elem.endswith(cortText[j]):
                dictFiles[cortText].append(elem)
            elif elem.endswith(cortMusic[j]):
                dictFiles[cortMusic].append(elem)
            elif elem.endswith(cortVarious[j]):
                dictFiles[cortVarious].append(elem)
    else:
        dictFiles[cortFolder].append(elem)

while True:
    os.system("clear")
    find = input("Enter that you wanna find (folder, image, video, text, various or all) or exit\t")
    if find == "folder":
        key = cortFolder
    elif find == "image":
        key = cortImage
    elif find == "video":
        key = cortVideo
    elif find == "text":
        key = cortText
    elif find == "various":
        key = cortVarious
    elif find == "all":
        for key, value in dictFiles.items():
            if key == cortFolder:
                print(f"\nList of folders ({key}) : {value}")
            elif key == cortImage:
                print(f"\nList of images ({key}) : {value}")
            elif key == cortVideo:
                print(f"\nList of video ({key}) : {value}")
            elif key == cortText:
                print(f"\nList of documents ({key}) : {value}")
            elif key == cortMusic:
                print(f"\nList of musics ({key}) : {value}")
            elif key == cortVarious:
                print(f"\nList of various files ({key}) : {value}")
        input("\nPress any key to continue")
        break
    elif find == "exit":
        input("\nPress any key to continue")
        break
    for value in dictFiles.get(key):
        print(value)
    input("\nPress any key to continue")