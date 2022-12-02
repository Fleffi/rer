def strip_punctuation_ru(s):
    punctuations = '"! () - = + ;: /<>,.'
    new_var = ""
    for char in s:
        if char in punctuations:
            new_var += ''
        else:
            new_var += char
    new_var = new_var.replace("_", " ")
    return " ".join(new_var.split())

print(strip_punctuation_ru(input()))
