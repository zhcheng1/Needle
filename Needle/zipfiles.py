import os
import zipfile


def zipfile_info():
    # get the file name
    get_file_name = raw_input("Enter a filename: ")

    # check if it is a zipfile
    while zipfile.is_zipfile(get_file_name) is False:
        get_file_name = raw_input("Not a valid zip file. Enter a filename: ")

    # get the file path
    get_file = os.path.abspath(get_file_name)

    # read a zip file
    with zipfile.ZipFile(get_file, 'r') as z:
        # get the info of the file which includes filename, filesize
        for i in z.infolist():
            file_name = i.filename.split("/")
            size = convert_bytes(i.file_size)
            if file_name[-1] != "":
                print file_name[-1], " ", size


def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.1f TB' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.1f GB' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.1f MB' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.1f KB' % kilobytes
    else:
        size = '%d Bytes' % bytes
    return size


if __name__ == '__main__':
    zipfile_info()

