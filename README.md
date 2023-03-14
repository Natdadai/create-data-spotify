# วิธีการใช้งาน
1. ทำการ run create_data_from_spotify เพื่อทำการดึง data จาก spotify โดยหมวดหมู่จะดึงจาก genres.json ซึ้งจะทำการเก็บไฟล์ทั้งในรูปของ csv และ .wav
2. ทำการ run preprocessing_data เพื่อทำการแปลง .wav ให้อยู่ในรูปแบบที่ต้องการโดยจะมี 2 แบบ คือ mfcc และ chroma_stft โดยทำการเก็บไว้ในรูป .npy