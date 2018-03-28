import argparse
import os.path
import shutil


def create_colder(destination_dir):
    if not os.path.isdir(destination_dir):
        os.mkdir(destination_dir)
    else:
        # folder already exists so check if the user wants to override
        replace = input('Do you want to replace the folder you\'ve selected with a new pyLDAPI installation? (y or n) ')
        if replace == 'y':
            shutil.rmtree(destination_dir)
            os.mkdir(destination_dir)
        else:
            print('Exiting')
            exit()


def fill_folder(destination_dir):
    my_dir = os.path.dirname(os.path.realpath(__file__))
    copytree(os.path.join(my_dir, 'blank'), destination_dir)

    print('Creating a blank pyLDAPI instance in ' + destination_dir)


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.exists(d):
            try:
                shutil.rmtree(d)
            except Exception as e:
                print(e)
                os.unlink(d)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


if __name__ == '__main__':
    # set up command line arg parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'destination_dir',
        type=str,
        help='The folder in which to install the pyldapi instance'
    )

    args = parser.parse_args()

    # create or use the dir
    create_colder(args.destination_dir)

    # fill the destination folder
    fill_folder(args.destination_dir)

    print('New pyLDAPI instance scaffolding creation complete')
