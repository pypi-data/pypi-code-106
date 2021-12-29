import os

def raspberrypiLinkGen(urlTup):
    def conTup_1(tup):
        com_1 = ''
        for item in tup:
            com_1 = com_1 + item
        return com_1
    com_1_tup = 'sudo youtube-dl -g -f 22 "', urlTup, '"'
    com_1 = conTup_1(com_1_tup)
    return(os.system(com_1))

