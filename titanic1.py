#titanic1.py

#PYTHON CONVENTIONS:
#use underscore naming
#use capslock for constants

#import modules
#"os" module: Miscellaneous operating system interfaces
import os
import matplotlib.pyplot as plt
import urllib #urllib to download a file from web

#https://raw.githubusercontent.com/williamszk/python-hands-on/master/dataset/titanic/train.csv


PROJECT_ROOT = "."
CHAPTER_ID = "titanic"
IMAGES_PATH = os.path.join(PROJECT_ROOT, "images", CHAPTER_ID)

#os.makedirs creates a directory
os.makedirs(IMAGES_PATH, exist_ok=True)


def save_fig(fig_id="figure_name", tight_layout=True, fig_extension="jpg", resolution=300):
    path = os.path.join(images_path, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

#create directory to store dataset
DATASET = os.path.join(PROJECT_ROOT,"datasets/titanic")
os.makedirs(DATASET, exist_ok=True)

#string of root of repository
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/williamszk/python-hands-on/master/"
#simple: creates a string 'dataset/titanic' 
TITANIC = os.path.join("dataset","titanic") 
TRAIN_PATH = os.path.join(DOWNLOAD_ROOT,TITANIC)
#download files from dataset titanic
urllib.request.urlretrieve(TRAIN_PATH+"/train.csv",os.path.join(DATASET,"train.csv"))
urllib.request.urlretrieve(TRAIN_PATH+"/test.csv",os.path.join(DATASET,"test.csv"))
#if we download a file even if it exists the file is replaced
















