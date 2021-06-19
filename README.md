# Speech Recognition for Uyghur using Speech transformer

### Training:

this model using CTC loss and Cross Entropy loss for training.

Download [pretrained model](https://github.com/gheyret/uyghur-asr-transformer/releases/download/premodel/results.7z) and [dataset](https://github.com/gheyret/uyghur-asr-ctc/releases/download/data/thuyg20_data.7z).

unzip results.7z and thuyg20_data.7z to the same folder where python source files located. then run:
```
python train.py
```

### Recognition:

for recognition download only [pretrained model](https://github.com/gheyret/uyghur-asr-transformer/releases/download/premodel/results.7z). then run:

```
python .\tonu.py .\test6.wav
```
result will be:
```
        Model loaded: results/UFormer_last.pth
            Best CER: 4.16%
             Trained: 276 epochs
The model has 36,418,306 trainable parameters
 Feature  has 25,869,058 trainable parameters
  Encoder has 4,205,568 trainable parameters
  Decoder has 6,343,680 trainable parameters

======================
Recognizing file .\test6.wav
test6.wav -> u qizlarning resimi chiqip qalsa bilekchila sinchilap qaraytti
```

### This project using 

[**A free Uyghur speech database Released by CSLT@Tsinghua University & Xinjiang University**](http://www.openslr.org/22/)


### Reference
https://github.com/gentaiscool/end2end-asr-pytorch

