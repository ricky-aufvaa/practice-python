import pandas as pd
from torch.utils.data import Dataset
import os 
from transformers import AutoTokenizer
import cv2
import numpy as np
import torch
import subprocess
import torchaudio


class MELDDataset(Dataset):
    #I want to return the tokenised utterance,utterance id and dialogue id
    # in tensor format, audio, frames. 
    def __init__(self,csv_path,video_dir):
        self.data = pd.read_csv(csv_path) 
        self.video_dir= video_dir
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        self.emotion_map = {
            'anger': 0,
            'disgust': 1,
            'fear': 2,
            'joy': 3,
            'neutral': 4,
            'sadness': 5,
            'surprise': 6
        }
        self.sentiment_map = {
            'negative': 0,
            'neutral': 1,  # neutral sentiment is not included as it's not provided in the dataset
            'positive': 2
        }
        
        
    #overriding len()
    def __len__(self):
        return len(self.data)
    

    #overriding __getitem__()
    def __getitem__(self,idx):
        if isinstance(idx, torch.Tensor):
            idx = idx.items()
            row = self.data.iloc[idx]
        #extractinng video path, it uses sentiment and emotion
        row = self.data.iloc[idx] #extracted the row
        #tokenise the utterance
        text_inputs = self.tokenizer(row['Utterance'],
        truncation=True,
        padding='max_length',
        max_length=128,
        return_tensors='pt')
            
        print(text_inputs)
        video_filename = f"dia{row['Dialogue_ID']}_utt{row['Utterance_ID']}.mp4"        
        #video path = video dir + video_filename
        video_path = os.path.join(self.video_dir, video_filename)
    
    #confirming if the path exists
        path_exists = os.path.exists(video_path)
        if path_exists == False:
            print(f"Path not found for {video_path}")
        print(f"path found for {video_path}")
       #return video_frame
        video_frame = self._load_video_frames(video_path) 
        audio_frame = self._extract_audio_features(video_path)
        print(audio_frame)
        #map sentiment and emotion lables
        emotion_label = self.emotion_map[row['Emotion'].lower()]
        sentiment_label= self.emotion_map[row['Sentiment'].lower()]
        return {
            'text_inputs': {
                'input_ids' : text_inputs['input_ids'].squeeze(),
                'attention_mask' : text_inputs['attention_mask'].squeeze()
                },
            'video_frames': video_frame,
            'audio_frames': audio_frame,
            'emotion_label': torch.tensor(emotion_label),
          'sentiment_label': torch.tensor(sentiment_label)
        }
        
        #extract frame
    def _load_video_frames(self, video_path):
        # video_path = self.video_path
        frames = []
        cap = cv2.VideoCapture(video_path)
        try:
            if not cap.isOpened():
                raise ValueError(f"can't open{video_path}")
            ret, frame = cap.read()
            if not ret or frame is None:
                raise ValueError("Could not read the video frame")
               #bring the index back to the beginning
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            while len(frames) < 30 and cap.isOpened():
                ret, frame = cap.read()
                print(ret,frame)
                if not ret:
                    break
                # print(ret,frame)
                    #resize the frames to 244
                frame = cv2.resize(frame, (224, 224))
                frame = frame/255 # to normalise the values
                frames.append(frame)
        #         print("dfjasdkfjdskfjdks")
                
        except Exception as e:
            raise ValueError(f"Could not open the video file {str(e)}")
        finally:
            cap.release()

        if len(frame) == 0:
            raise ValueError("No frames were extracted from the video")
                
            #if I have less than 30 frames, then I will pad the remaining frames  with zeroes
        # if len(frames)<30:
        #     frames += (np.zeros_like(frames[0]) * (30- len(frames)))
            #if more than 30 then we will take only the efirst thirty frames
        else:
            frames = frames[:30]
        print(f"here are the frames {frames}")
        return torch.FloatTensor(np.array(frames)).permute(0,3,1,2)
            

        #process audio
    def _extract_audio_features(self, video_path):
        audio_path = video_path.replace(".mp4",".wav")
        # audio processing here using ffmpeg
        try:
            subprocess.run(["ffmpeg",
                "-i", video_path,
                "-acodec", "pcm_s16le",
                "-ac", "1",
                "-ar", "16000",
                "-vn", audio_path
            ],      check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        #audio processing using torchaudio
            waveform, sample_rate = torchaudio.load(audio_path) #loading the audio into the memory
            if sample_rate !=16000: #this is a typical value of sample rate in ML processing
                #resample it to 16000
                resampler = torchaudio.transforms.Resample(sample_rate,16000)
                waveform = resampler(waveform)
            mel_spectrogram = torchaudio.transforms.MelSpectrogram(
                sample_rate=16000,
                n_mels=64,
                n_fft = 1024,
                hop_length = 512
            )
            mel_spec = mel_spectrogram(waveform)
            #normalise the value 
            mel_spec = (mel_spec - mel_spec.mean())/mel_spec.std()

            #truncate the size if it exceeds
            if mel_spec.size(2) < 300:
                padding = 300 - mel_spec.size(2)
                mel_spec = torch.nn.functional.pad(mel_spec, (0, padding))
            else:
                mel_spect = mel_spec[:,:,:300]
            return mel_spec
        


        except subprocess.CalledProcessError as e:
            raise ValueError(f"audio extraction erro{str(e)}")
        except Exception as e:
            raise ValueError(f"audio error{str(e)}")
        finally:
            if os.path.exists(audio_path):
                os.remove(audio_path)


        
                                                    
        #tensorise sentiment and emotion
    
        # reutrn a dictionary with the required information
        

