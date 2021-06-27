# DeepSpeech files

Those are some files useful to run the model

The italian_alphabet.txt file is a file mandatory to run deepspeech

The client.py file allows you to try the model
To use it just run :

```bash
py client.py --model="output_graph.pbmm" --audio="demo.wav" --json >> results.json
```

The output_graph.pbmm and output_graph.scorer are the output of the training.

The extracted.zip are the files produce by the python script

The dld_test.csv, dld_train.csv and dld_val.csv are the dataset files.
