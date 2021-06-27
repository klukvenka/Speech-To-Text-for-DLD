# to convert into mp3
from pydub import AudioSegment
import os


CSV_PATH_NEW = 'dld_dataset_wav.csv'
# csv for dld
CSV_PATH = 'dld_dataset.csv'



def convert_to_wav(path):
    dirs = os.listdir(path)
    for dir in dirs:
        dirpath = path+"/"+dir
        if os.path.isdir(dirpath):
            convert_to_wav(dirpath)
        elif ".mp3" in dirpath:
            sound = AudioSegment.from_mp3(dirpath)
            sound = sound.set_channels(1)
            sound = sound.set_frame_rate(16000)            
            sound.export(dirpath[:-4]+".wav", format="wav")
            update_csv(dirpath[:-4]+".wav")
            os.remove(dirpath)

def update_csv(audio_path):
    csv = []
    real = -1
    oldline = ""
    f = open(CSV_PATH, "r")

    # Read all data from the csv file.
    for line in f.readlines():
        split = line.split(',')
        if split[0][:-4] == audio_path[:-4]:
            print("path updated {}".format(audio_path))
            csv.append("{0}, {1}, {2}".format(audio_path, os.path.getsize(audio_path),split[2]))
    f = open(CSV_PATH_NEW, "a")
    f.writelines(csv)
    f.close()          

# folder of the mp3 files
convert_to_wav("extracted")