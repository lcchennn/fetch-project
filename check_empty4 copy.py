#fh = open('textfile.txt', 'a+')
#fh.write('*a+ added line*')

#fh = open('textfile.txt', 'r+')
#fh.write('*r+ added line*')

#fh = open('textfile.txt', 'w+')
#fh.write('*w+ added line*')

#fh = open('textfile.txt', 'w')
#fh.write('*w added line*')

#fh = open('textfile.txt', 'a')
#fh.write('*a added line*')

# fh = open('textfile.txt', 'a+')
# # fh.write('**a+ added line**')
# #
# # fh.close()

# fh = open(input('Please enter file name: '), 'r')
# try:
#     f = fh.readlines()
#     if f == []:
#         raise Exception
# except Exception:
#     print('fileisempty')


with open('empty.csv') as empty:
    first = empty.readlines()
    print('thisis',first)
    if first == []:
        print('friendsfile is empty')
