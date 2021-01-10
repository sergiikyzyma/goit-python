import os
import sys
import pathlib

def inputing(path = sys.argv[1]):
    path = pathlib.Path(path)
    try:
        listContain = os.listdir(path.absolute())
    except NotADirectoryError:
        listContain = inputing(path = input("\nReenter your directory, please "))
    except FileNotFoundError:
        listContain = inputing(path = input("\nReenter your directory, please "))
    return listContain

def outputing(dictFiles):
    os.system("clear")
    find = input("Enter that you wanna find (folder, image, video, text, musics, various or all) or exit\t")
    key = list(dictFiles.keys())
    if find == "folder":
        i = 0
        print(f"\nList of folders ({key[i]})\n")
    elif find == "image":
        i = 1
        print(f"\nList of images ({key[i]})\n")
    elif find == "video":
        i = 2
        print(f"\nList of video files ({key[i]})\n")
    elif find == "text":
        i = 3
        print(f"\nList of documents ({key[i]})\n")
    elif find == "music":
        i = 4
        print(f"\nList of music files ({key[i]})\n")
    elif find == "various":
        i = 5
        print(f"\nList of various files ({key[i]})\n")
    elif find == "all":
        for key, value in dictFiles.items():
            print(f"\nList of contains ({key}) : {value}")
    elif find == "exit":
        input("\nPress any key to exit")
        return None
    if find != "all":
        try:
            for value in dictFiles.get(key[i]):
                print(value)
        except NameError:
            print("\nYou maked the fail by inputing the command for search")
    input("\nPress any key to continue")
    outputing(dictFiles)

def sorting(contains):
    cortFolder = ("folder")
    cortImage = ("jpeg", "png", "jpg", "svg")
    cortVideo = ("avi", "mp4", "mov", "mpg")
    cortText = ("doc", "dcox", "txt", "odt")
    cortMusic = ("mp3", "ogg", "wav", "amr")
    cortVarious = ("max", "vsd", "blend", "")

    dictFiles = {cortFolder: [], cortImage: [], cortVideo: [], cortText: [], cortMusic: [], cortVarious: []}

    for contain in contains:
        if "." in contain:
            j = 0
            while not (contain.endswith(cortImage[j]) or contain.endswith(cortVideo[j]) or contain.endswith(cortText[j]) or contain.endswith(cortMusic[j]) or contain.endswith(cortVarious[j])):
                j += 1
            else:
                if contain.endswith(cortImage[j]):
                    dictFiles[cortImage].append(contain)
                elif contain.endswith(cortVideo[j]):
                    dictFiles[cortVideo].append(contain)
                elif contain.endswith(cortText[j]):
                    dictFiles[cortText].append(contain)
                elif contain.endswith(cortMusic[j]):
                    dictFiles[cortMusic].append(contain)
                elif contain.endswith(cortVarious[j]):
                    dictFiles[cortVarious].append(contain)
        else:
            dictFiles[cortFolder].append(contain)
            sub_dir = inputing(path = contain)
            dictFiles[cortFolder].append(sorting(sub_dir))
    return dictFiles

def main():

    contains = inputing(path = "/home/teosoph/Стільниця/goit-python")
    #contains = inputing()

    dictFiles = sorting(contains)

    outputing(dictFiles)

if __name__ == "__main__":
    main()