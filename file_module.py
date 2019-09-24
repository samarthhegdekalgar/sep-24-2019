import os


def get_file_content(file_path):
    '''This function does get the file content'''
    if os.path.exists(f'{file_path}'):
        with open(f'{file_path}', 'r') as file_obj:
            print(file_obj.read())
    else:
        print('No such file exist!!')


def write_into(file_path, content=None):
    with open(f'{file_path}', 'a') as file_obj:
        file_obj.write(content)


def delete_content(file_path):
    if os.path.exists(f'{file_path}'):
        os.remove(f'{file_path}')

    else:
        print('No such file exist!!')


if __name__ == '__main__':
    write_into('example.txt', 'Its just a example.')
    get_file_content('example.txt')
    delete_content('example.txt')