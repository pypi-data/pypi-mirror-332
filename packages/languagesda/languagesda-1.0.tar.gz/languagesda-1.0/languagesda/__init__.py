__author__ = 'development'
__version__ = '1.0'
__email__ = 'agcs-development@rambler.ru'
def русский_синтаксис (cod=[]):
    cod_2=[]
    if cod == []:
        while True:
            a = input()
            if a == '':
                break
            else:
                cod += [a] 
    #'Наш аналог в коде':'Функция обозначающая из пайтон'
    library = {
    "напиши":"print",
    "раздели_по":"split",
    "повраряй_пака":"while"
    }
    for i_1 in cod:
        i_1 = i_1.split(' ')
        b = ''
        for i_2 in i_1:
            if i_2 in library:
                b += str(library[i_2])
            else:
                b += str(i_2)
        cod_2 += [b]
    for n in cod_2:
        exec(n)