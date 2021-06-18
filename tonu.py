import sys
import os
from data import featurelen
from UFormer import UFormer

if __name__ == '__main__':
    model = UFormer(featurelen)
    
    if len(sys.argv)<2:
        print("Using \n\tpython tonu.py audiofile | audiolist.txt | folder")
    else:
        device = 'cpu' # or 'cuda'
        model.to(device)
        audiofile = sys.argv[1]
        print(f"\n======================\nRecognizing file {audiofile}")
        txt = model.predict(audiofile,device)
        print("%s -> %s" %(os.path.basename(audiofile),txt))
