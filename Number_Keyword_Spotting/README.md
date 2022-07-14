# Hitachi-ASR

## Contributors
- Aniket Kumar
- Agnibha Sinha

## About
The goals of the this Project are as follows:
- "Identify numeric keywords in continuous speech"
- "Locate keywords in timeframes or in post-processed transcripts"

## Methods

### Pre-Processing using Speech Yolo

**Data:**
- The data needed to train in the model is a labelled 1 sec audio clip of a keyword.
- Each Keyword Directory has multiple .wav and .wrd files representing audio clips and
a text file with [start end keyword] tuple as in the files.

**Feature Extraction:**
- Extract preliminary features using Soundfile, a two-dimensional (frames x channels)
NumPy array is returned.
- Take Short Term Fourier Transform of the audio with windo-size=0.02, window-
stride=0.01.
- We convert the output matrix into magnitude and phase using magphase function
of librosa library.
- We take log of 1 + the output matrix to avoid errors popping in for features values
which are almost equal to 1 using numpy library of python.
- Conversion into a standard 160x100 NumPy array takes place which is used as data for our 
model after normalization.

**Model:**
- The CNN multi-layer model has 16 Convoluted Layers with 2 Fully Connected layers with 5 Pooling layers, 
each Convoluted Layer Normalises and applies ReLU before going to the next layer.
- The model is based on dividing the last connected into 3 parts c, b, k which represent container, box, 
and keyword and can be set as per the users after which a probability of keyword existing in each box is 
calculated using the loss function and greatest probability above a threshold is returned.

**Instructions:**
- Download the model from the [link](https://drive.google.com/file/d/1mkOn61zMzHi9S4XNhfDxnNSuV57OnoyN/view) and run<br /><br />
```
python test_yolo.py    --test_data [path_to_test_data]
                       --model [path_to_speechyolo_model] 
```

### Post-Processing using Soundex

**Data**<br />
- The data required for this algorithm is in form of text transcripts. We have tried out our algorithm 
in 4 languages: English, Hindi, Bengali and Tamil
- A few examples can be found in the data folder of the fuzzy matching algorithm. The data can be varied by
changing the first column of the excel files and run the run.py file
- We combine the bounding boxes if the keywords(numbers in our case) are consecutive to enable the detection of
continuous number sequences

**Algorithm**<br />
- The algorithm is based on 2 parameters, the bigram match and the soundex score.
Soundex is a phonetic matching alogrithm which matches similar sounding words
- Using soundex also enables us to match words across languages. Combining the 2 parameters we can find an approximate match for keywords

## References
- [Basics of ASR](http://www.cs.columbia.edu/~julia/courses/CS6998-2019/%5B09%5D%20Automatic%20Speech%20Recognition.pdf)

- [Aradilla, Guillermo and Ajmera, Jitendra. (2007). Detection and
Recognition of Number Sequences in Spoken Utterances.](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.367.7514&rep=rep1&type=pdf)

- [Speech YOLO paper](https://arxiv.org/pdf/1904.07704.pdf)




