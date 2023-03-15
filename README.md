# วิธีการใช้งาน (Run ตามลำดับ)
## 1. create_data_from_spotify 
##### ทำการดึง data จาก spotify โดยแนวเพลงดึงจาก genres.json ซึ้งทำการเก็บไฟล์ทั้งในรูปของ csv และ .wav
  - ไฟล์เพลง (.wav) อยู่ในโฟลเดอร์ music_data โดยมีโฟลเดอร์ย่อยเป็นแนวเพลงแต่ละแนว
  - ไฟล์ csv อยู่ในโฟลเดอร์ csv-file โดยแยกแต่ละไฟล์ด้วยแนวเพลงและมี all_genre รวมข้อมูลทุกแนวเพลงเข้าด้วยกัน
## 2. preprocessing_data 
##### ทำการแปลง .wav ให้อยู่ในรูปแบบที่ต้องการโดยมี 2 แบบ คือ mfcc และ chroma_stft โดยทำการเก็บไว้ในรูป .npy โดยมีการจัดแนวเพลงหลักและย่อยไว้ใน group-genre_2.txt หลังจาก run จะได้ไฟล์ 4 ไฟล์ โดยเก็บอยู่ในโฟลเดอร์ data_preprocess
  - balanced_data.csv เป็นข้อมูลเพลงที่ทำการ balance แล้ว
  - y.npy ของ balanced_data ในรูปแบบ numpy array
  - chroma.npy เก็บช้อมูลของเสียงที่ผ่านการแปลงโดย chroma feature ในรูปแบบ numpy array
  - mfccs.npy เก็บช้อมูลของเสียงที่ผ่านการแปลงโดย mfcc ในรูปแบบ numpy array
