t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
     'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
     'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
     'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
     'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу
s = input().lower()


def decor_txt(func):
    def wraper(*args, **kwargs):

        st2 = func(*args, **kwargs).replace(' - ', '-').replace(' ', '-')
        while '--' in st2:
            st2 = st2.replace('--', '-')

        return st2
    return wraper


@decor_txt
def get_trans(txt):
    t2 = txt.maketrans(t)
    txt2 = txt.translate(t2)
    txt2 = txt2.replace(':', '-').replace('.', '-').replace(',',
                                                            '-').replace('_', '-').replace(';', '-')
    return txt2


print(get_trans(s))
