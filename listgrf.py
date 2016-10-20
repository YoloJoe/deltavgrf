from os import listdir
from os.path import isfile, join
from os import walk

# GraphicsIFix = "D:\DeltaV\DVData\GraphicsIFix\Pic"


def getgraphics(graphics_path, out_file="graphicsList.txt", out_path=""):
    """
    DOCSTRING: Generates an output file with the filenames in the specified directory.

    :param graphics_path: str - Fully qualified path of search space
    :param out_file: str - output file name
    :param out_path: str - Fully qualified path of destination file.  If blank, output file is created in local path
    :return:
    """
    # grf_list syntax attributed to user pycruft -
    # http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
    grf_list = [f for f in listdir(graphics_path) if isfile(join(graphics_path, f))]
    outfile = open(out_path + out_file, 'w')
    for line in grf_list:
        outfile.write(line + "\n")

    outfile.close()


def getgrfs(grf_path, out_file="grfList.txt", out_path=""):
    """
    DOCSTRING: Generates an output file with the grf filenames in the specified directory.

    :param graphics_path: str - Fully qualified path of search space
    :param out_file: str - output file name
    :param out_path: str - Fully qualified path of destination file.  If blank, output file is created in local path
    :return:
    """
    grf_list = [f for f in listdir(grf_path) if isfile(join(grf_path, f))]
    outfile = open(out_path + out_file, 'w')
    for line in grf_list:
        if 'grf' in line:
            outfile.write(line + "\n")

    outfile.close()

# getgraphics("Z:\DeltaV\SI Group\Graphics-iFix\Pic")
getgrfs("Z:\DeltaV\SI Group\Graphics-iFix\Pic")