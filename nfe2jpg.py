import glob
import multiprocessing
import os
import time

import imageio
import rawpy


def nfeconverter(pathnef):
    # Sometimes the file ending can be .nef or .NEF, therefore I included both possibilities to save extra work.
    for path in glob.glob(pathnef):
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite("Converted//" + path.replace('.nef', '') + '.jpg', rgb)
            print('Done')


def NFEconverter(pathNEF):
    for path in glob.glob(pathNEF):
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite("Converted//" + path.replace('.NEF', '') + '.jpg', rgb)
            print('Done')


if __name__ == '__main__':
    print("Starting Now")
    start = time.time()
    print("Number of cores", multiprocessing.cpu_count())
    inputfolder = input("File Folder path...")
    pathnef = "images//*.nef"
    pathNEF = "images//*.NEF"

    p1_nfe = multiprocessing.Process(target=nfeconverter, args=(pathnef,))
    p1_nfe.start()

    p1_NFE = multiprocessing.Process(target=NFEconverter, args=(pathNEF,))
    p1_NFE.start()

    p1_nfe.join()
    p1_NFE.join()

    end = time.time()
    minutes = (end - start) / 60
    seconds = (end - start) % 60
    print("Elapsed Time:", round(minutes), "minutes and ", round(seconds), "seconds")
    convertedPath = "Converted//images"
    convertedImgs = os.listdir(convertedPath)
    for img in convertedImgs:
        print(img)
        if (".NEF" in img) or (".nef." in img):
            print("Removing file....", img)
            os.remove(convertedPath + "//" + img)
