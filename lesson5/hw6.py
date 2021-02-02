import string

def normalize(my_string):

    alphabet_rus = ("а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я")
    alphabet_rus_eng = ("a","b","v","g","d","ye","yo","zh","z","i","j","k","l","m","n","o","p","r","s","t","u","f","kh","ts","ch","sh","shch","_","y","_","e","yu","ya")
    alphabet_ukr = ("а","б","в","г","ґ","д","е","є","ж","з","и","і","ї","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ь","ю","я")
    alphabet_ukr_eng = ("a", "b", "v", "h", "g", "d", "e", "ye", "zh", "z", "y", "i", "yi", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh", "shch", "_", "yu", "ya")
    
    map_trans = dict()
    for index, _ in enumerate(alphabet_rus):
        map_trans[ord(alphabet_rus[index])] = alphabet_rus_eng[index]
        map_trans[ord(alphabet_rus[index].upper())] = alphabet_rus_eng[index].capitalize()
        map_trans[ord(alphabet_ukr[index])] = alphabet_ukr_eng[index]
        map_trans[ord(alphabet_ukr[index].upper())] = alphabet_ukr_eng[index].capitalize()
    for symbol in string.punctuation:
        map_trans[ord(symbol)] = "_"
    for symbol in string.whitespace:
        map_trans[ord(symbol)] = "_"
    
    my_string = my_string.translate(map_trans)

    return my_string

result = "My name is Сергій Кизима!!?!#!?%!"
print("\t", result, "\t", normalize(result))
