import codecs
o = 'abcdefghijklmnopqrstuvwxyz123456789'
with codecs.open("PythonTest.txt", "r", "utf-8") as file1:
    lines = file1.readlines()
    lines_2 = (line for line in lines if not line.isspace() and line[0] != '#')
    with codecs.open("PythonTestNew.txt", 'w', "utf-8") as file2:
        file2.writelines(lines_2)
    file2.close()
file1.close()
with codecs.open("PythonTestNEW.txt", "r", "utf-8") as file3:
    while True:
        line_1 = file3.readline()

        if not line_1:
            break

        c = ' ; '.join(line_1.split('\t')).replace('\r\n', '').replace('\n', '').split(' ; ')
        d = []
        f = []
        for i in c:
            if i[0].lower() in o:
                d.append(i)
            else:
                f.append(i)

        with codecs.open("English.txt", "a", "utf-8") as t:
            for word in d:
                t.write((word + '\n') * len(f))
        t.close

        with codecs.open("Russian.txt", "a", "utf-8") as p:
            for s in range(len(d)):
                for wor in f:
                    p.write(wor + '\n')
        p.close

file3.close
