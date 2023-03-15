# วิธีการใช้งาน
1. ทำการ run create_data_from_spotify เพื่อทำการดึง data จาก spotify โดยแนวเพลงดึงจาก genres.json ซึ้งทำการเก็บไฟล์ทั้งในรูปของ csv และ .wav
1.1 โดยเพลงอยู่ในโฟลเดอร์ music_data โดยมีโฟลเดอร์ย่อยเป็นแนวเพลงแต่ละแนว
1.2 โดย csv ไฟล์อยู่ในโฟลเดอร์ csv-file โดยแยกแต่ละไฟล์ด้วยแนวเพลงและมี all_genre รวมข้อมูลทุกแนวเพลงเข้าด้วยกัน
2. ทำการ run preprocessing_data เพื่อทำการแปลง .wav ให้อยู่ในรูปแบบที่ต้องการโดยมี 2 แบบ คือ mfcc และ chroma_stft โดยทำการเก็บไว้ในรูป .npy โดยมีการจัดแนวเพลงหลักและย่อยไว้ใน group-genre_2.txt หลังจาก run จะได้ไฟล์ 4 ไฟล์ โดยเก็บอยู่ในโฟลเดอร์ data_preprocess
2.1 balanced_data.csv เป็นข้อมูลเพลงที่ทำการ balance แล้ว
2.2 y.npy ของ balanced_data ในรูปแบบ numpy array
2.3 chroma.npy เก็บช้อมูลของเสียงที่ผ่านการแปลงโดย chroma feature ในรูปแบบ numpy array
2.4 mfccs.npy เก็บช้อมูลของเสียงที่ผ่านการแปลงโดย mfcc ในรูปแบบ numpy array
