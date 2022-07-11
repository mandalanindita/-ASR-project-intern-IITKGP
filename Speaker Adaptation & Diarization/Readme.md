# Speaker Adaptation & Diarization

## Speaker Adaptation:
Speaker adaptation refers to the technology whereby a speech recognition system is adapted to the acoustic features of a specific user using an extremely small sample of utterances when the system is operated.


## Speaker Diariztion:
Speaker diarization is the process of partitioning an audio stream with multiple people into homogeneous segments associated with each individual. It is an important part of speech recognition systems and a well-known open problem.

### Steps for speaker diarization:
- Speech detection
- Speech Segmentation
- Embedding Extraction
- Clustering

### Technologies used:
1. Resemblyzer: It is an open-source repository which performs the 1st 3 tasks of speaker diarization.


2. spectralclusterer: open-source implementation of Spectral Clustering by Quan Wang, one of the original authors of the paper we are implementing, who has been generous enough to provide us with the code.



### Milestones:
1. I explored various state-of-the-art techniques used for speaker adaptive speech recognition and diarization.


2. I implemented a Speaker Diarization Model using Spectral Clustering which could partition an audio stream with multiple people into homogeneous segments associated with each individual in both Hindi and English.
