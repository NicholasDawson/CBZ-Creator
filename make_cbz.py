from shutil import make_archive, rmtree
from os import rename


def make_cbz(directory, remove_old=True):
    make_archive(directory, 'zip', directory)
    rename(directory + '.zip', directory + '.cbz')
    print('CBZ Archive created for: ' + directory)

    if remove_old:
        rmtree(directory)
        print('Old Directory was deleted.')
