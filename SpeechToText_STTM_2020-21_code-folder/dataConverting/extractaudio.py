import os
from audioclipextractor import AudioClipExtractor, SpecsParser
import csv



FFMEPG_PATH = 'C:/Users/Victor/Downloads/ffmpeg-4.3.1-2020-11-19-essentials_build/bin/ffmpeg.exe'

CSV_PATH = 'dld_dataset.csv'



def interpretTranscript(path):
    if not os.path.isfile(path):
        print('File does not exist. path wanted = {}'.format(path))
        return None, None, None
    else:
        with open(path) as f:
            content = f.read().splitlines()
        # we need to get the duration
        #  extract the beginning and the end of the audio extract
        time = content[6][16:].strip()
        begin = time.split("-")[0].split(':')
        end = time.split("-")[1].split(':')
        # we now need to extract the phrases
        phrases = []
        for i in range(len(content)):
            if content[i][0] == '*':
                if content[i][-1] not in ['.','!','?']:
                   phrases.append(content[i][8:]+" "+content[i+1].lstrip())
                else:
                    phrases.append(content[i][8:])
        return begin, end, phrases

def extract_audio(audio_path, transcript_path, output_dir):    
    if not os.path.isfile(audio_path):
        print('File does not exist. path wanted = {}'.format(audio_path))
        return None
    else:
       ext = AudioClipExtractor(audio_path, FFMEPG_PATH)
       begin, end, phrases = interpretTranscript(transcript_path)
       if begin == None:
           return None
       # get the average time for each phrase, from the number of phrases and the length of the clip
       avg = ((int(end[0])-int(begin[0]))*60 + (int(end[1])-int(begin[1])))/len(phrases)
       specs =""
       previous = [int(begin[0]),int(begin[1])]
       for i in range(0,len(phrases)):
           newEndS = previous[1]+avg # +1 to account for the time between the phrases
           newEndM = previous[0]
           specs = specs + "{0}  {1} {2}\n".format(previous[0]*60+previous[1], newEndM*60+newEndS, audio_path.split("/")[-1][:-4])
           previous = [newEndM, newEndS]
       f = open("specs.txt", "x")
       f.writelines(specs)
       f.close()
       ext.extract_clips(specs_file_path_or_str="specs.txt", output_dir=output_dir, zip_output=False, text_as_title=True)
       os.remove("specs.txt")
       return phrases

def process_Audio_Files(path):
    dirs = os.listdir(path)
    for dir in dirs:
        dirpath = path+"/"+dir
        if os.path.isdir(dirpath):
            process_Audio_Files(dirpath)
        else:
            output_dir = "extracted/"+dir[:-4]
            try:
                os.mkdir(output_dir)
            except:
                pass
            phrases = extract_audio(dirpath,dirpath.replace("LD_audio_ITA", "LD ITA").replace("wav","cha").replace("3gp","cha").replace("mp4","cha").replace("mpeg","cha").replace("m4a","cha").replace("mp3","cha"), output_dir)
            if phrases != None:
                create_csv(output_dir, phrases)
            
def create_csv(path, phrases):
    dirs = os.listdir(path)
    csv = []
    for i in range(len(dirs)):
        dirpath = path+"/"+dirs[i]
        csv.append("{0}, {1}, {2}\n".format(dirpath, os.path.getsize(dirpath),phrases[i]))
    f = open(CSV_PATH, "a")
    f.writelines(csv)
    f.close()  


    
process_Audio_Files("C:/Users/Victor/Downloads/LD_audio_ITA")

