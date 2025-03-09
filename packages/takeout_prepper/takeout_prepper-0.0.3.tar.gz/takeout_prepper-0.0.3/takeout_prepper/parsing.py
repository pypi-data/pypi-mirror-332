from os.path import isdir

def dir_path(string):
    if isdir(string):
        return string
    else:
        raise NotADirectoryError(string)
