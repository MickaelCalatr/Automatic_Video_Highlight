from time import gmtime, strftime

def debug_log(line):
    file = open("log","w")
    file.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
    for i in line:
        file.write(i + '\n')
    file.write("\n")
    file.close()
