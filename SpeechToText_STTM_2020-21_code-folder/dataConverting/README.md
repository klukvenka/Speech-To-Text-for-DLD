# Python Scripts to convert DLD data into Deepspeech format

## install dependencies

```bash
pip install pydub
pip install audioclipextractor
```

## change values

Before running the scripts you need to change where the initial data is

For the extractaudio.py file

Line 88

```python
process_Audio_Files("path/to/dld/data")
```

For the convertwav.py file, you need to specify where the extracted clips are located, as well as the initial csv file :

Line 43

```python
# folder of the mp3 files
convert_to_wav("extracted")
```

Line 6

```python
CSV_PATH_NEW = 'dld_dataset_wav.csv'
# csv for dld
CSV_PATH = 'dld_dataset.csv'
```
