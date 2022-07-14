# Frame Level Language Identification in Code-Mixed Text

## Contributor - **Sridhara Manideep**

## Competitions

- [Microsoft's First Workshop on Speech Technologies for Code-switching in Multilingual Communities 2020](https://www.microsoft.com/en-us/research/event/workshop-on-speech-technologies-for-code-switching-2020/shared-task/)

- [MUCS 2021](https://navana-tech.github.io/MUCS2021/challenge_details.html)

## Papers
- [Shared Task on Code-switched Spoken Language Identification](Papers/Shared%20Task%20on%20Code-switched%20Spoken%20Language%20Identification.pdf)

- [Vocapia-LIMSI System for 2020 Shared Task on Code-switched Spoken Language Identification](Papers/Vocapia-LIMSI%20System%20for%202020%20Shared%20Task%20on%20Code-switched%20Spoken.pdf)


### References
- [A GMM-Supervector Approach to Langugage Recognition with Adaptive Relevance Factor](Papers/A%20GMM-Supervector%20Approach%20to%20Langugage%20Recognition%20with%20Adaptive%20Relevance%20Factor.pdf)

- [Joint Factor Analysis versus Eigenchannes in Speaker Recognition](Papers/Joint%20Factor%20Analysis%20versus%20Eigenchannels%20in%20Speaker%20Recognition.pdf)

- [Language Recognition in iVectors Space](Papers/Language%20Recognition%20in%20iVectors%20Space.pdf)

- [Maximum a posteriori estimation for multivariate Gaussian mixture observations of Markov chains](Papers/Maximum%20a%20posteriori%20estimation%20for%20multivariate%20Gaussian%20mixture%20observations%20of%20Markov%20chains.pdf)

- [TRAPS - CLASSIFIERS OF TEMPORAL PATTERNS](Papers/TRAPS%20-%20CLASSIFIERS%20OF%20TEMPORAL%20PATTERNS.pdf)


## Dataset

- [Microsoft Shared Task Dataset](Dataset/First%20Workshop%20on%20Speech%20Technologies%20for%20Code-switching%20in%20Multilingual%20Communities%3A%20Shared%20Task%20Description.pdf) : Not Availalble publicly

- [MUCS 2021 Code Switched Dataset](https://www.openslr.org/104/) : Hindi-English and Bengali-English Corpus Available publicly

&nbsp;

In the Microsoft dataset, 200ms frames from the audio files are classified into one of the three classes: Silence, Primary Langugae and Secondary Language according to this [official document](Dataset/First%20Workshop%20on%20Speech%20Technologies%20for%20Code-switching%20in%20Multilingual%20Communities%3A%20Shared%20Task%20Description.pdf).

Ex: `Ground Truth Language Tag Sequence:         SSTTTTTTTTTSSSSSEETTSSTTTETTTTSTTTTS`

But it is also mentioned in this [paper](Papers/Shared%20Task%20on%20Code-switched%20Spoken%20Language%20Identification.pdf) that each character in the transcript was replaced its corresponding language tag i.e., ‘T’ for Telugu or Tamil and ‘G’ for Gujarati. And for the test and blind test sets, they generated language tags for every
200 ms of the code-mixed audio.

As the required Microsoft Shared Task Code-Mixed Dataset along with frame level annotations is not available publicly, annotations are generated for the best possible extent using this [script](fllid_annotations.py) for MUCS 2021 code-mixed dataset according to the description provided in the [paper](Papers/Shared%20Task%20on%20Code-switched%20Spoken%20Language%20Identification.pdf).

## Methods

### Baseline

**Feature Extraction:**
- Take Short Term Fourier Transform of the audio with windo-size=0.02, window-
stride=0.01.
- We convert the output matrix into magnitude and phase using magphase function
of librosa library.
- We take log of 1 + the output matrix to avoid errors popping in for features values
which are almost equal to 1 using numpy library of python.

**Model**
- End-to-End multi-layer model consisting of 5 layers of LSTM, each consisting of 1024 neurons.
- The model is based on deepspeech 2 with CTC Loss function trained for 40 epochs.

### Vocapia-LIMSI Submission 
[Link to PPT](https://docs.google.com/presentation/d/1VFVWqbWu_0ymVH1qNZqIsOc-vsXWcmasn9x3XtKOzw8/edit?usp=sharing)

- Audio Segmentation and Frame extraction
- Generate 32 band Mel Spectrogram
- Estimate TRAP-DCT Features
- Pass the TRAP-DCT Features through a bottle-neck DNN
- Extract i-vector and normalize its length to unity
- Classify into one of the 3 classes using Multi class logistic regression

## Problems
 
 - There are no publications on frame level language identification in code-mixed audio except for the one submission by Vocapia-LIMSI in a competition.
 - No official public datasets are avaialable for frame level language identification in code-mixed audio.
 - For both the Baseline and the Vocapia-LIMSI submission, provided that no code-bases are availalbe at any level of the implementations and the descriptions in the papers are very vague, it was very challenging and almost found impossible implementing the models from scratch.
 
 ## Future Work
 - As there are are no prior work available on frame level language identification in code-mixed audio, and no publicly availalbe datasets, we have to start from scratch.
 - Due to the lack of proprietary dataset, we can approach this problem in a different way. Instead of frame level language identification, we can work on character level language identification using the above generated annotations like a generic ASR system but with only two characters instead of 26 characters.

**Note:** Some notes collected during this internship are available in the `\Notes` folder

