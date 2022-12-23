import os
path = '/home/alex/Documents/pythonProject/netology/python/task3/'


def list_of_files():
    """Вернет список названий всех файлов находящихся в той же директории,
       где запускается файл."""
    files_list = os.listdir(path)
    empty_dict = {}
    for name in files_list:
        if name.rfind('.txt', -4) >= 0:
            with open(os.path.join(path, name), 'r', encoding='UTF-8') as file:
                empty_dict[name] = file.readlines()

    with open('sorted_files.txt', 'w', encoding='UTF-8') as file:
        for file_name, rows in sorted(empty_dict.items(),
                                      key=lambda x: len(x[1])):
            file.write(file_name + '\n')
            file.write(str(len(rows)) + '\n')
            if '\n' not in rows[-1]:
                rows[-1] += '\n'
            file.write(''.join(rows))


list_of_files()
