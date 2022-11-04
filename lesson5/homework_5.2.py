"""read math expresion from file, calculate and write in file"""
import os
def main(file_name: str):
    with open('temp.txt', 'w') as fw:
        with open(file_name, 'r+') as fr:
            for line in fr:
                line = line.rstrip('\n')
                try:
                    calculation_result = eval(line)
                except ZeroDivisionError:
                    new_line = line + ' = ' + 'can\'t divide by zero' + '\n'
                    fw.write(new_line)
                    continue
                new_line = line + ' = ' + str(calculation_result) + '\n'
                fw.write(new_line)
    os.remove(file_name)
    os.rename('temp.txt', file_name)


if __name__ == '__main__':
    file_name = 'file_1.txt'
    main(file_name)
