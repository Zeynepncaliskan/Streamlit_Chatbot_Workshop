import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env dosyasını yükler
#load_dotenv()

# .env dosyasının içerisindeki GOOGLE_API_KEY değişkeninin değerini alır
#GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # .env dosyasından API KEY'i okuyoruz

# API Key ile Google’ın Generative AI servislerine bağlanıyoruz
genai.configure(api_key="AIzaSyBWLBZRsEIfUF-28ARa8u7Q5y-6LqxlWN8")

# Google Gemini-Pro AI modelini kuruyoruz
model = genai.GenerativeModel('gemini-1.5-flash')

def give_response(chat_history, soru, system_prompt):
    # Sistem promptunu ekliyoruz
    full_prompt = f"{system_prompt}\n\n{chat_history}\nuser: {soru}\nassistant:"

    # Hazırlanan prompt'u modele gönderir ve modelin oluşturduğu içeriği döndürür
    response = model.generate_content(full_prompt)


    return response.text