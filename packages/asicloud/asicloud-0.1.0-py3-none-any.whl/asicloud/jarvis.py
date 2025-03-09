import requests

class Jarvis:
    def __init__(self, model, key):
        self.model_name = model  # Foydalanuvchi "jarvis-1-beta" kiritadi
        self.user_key = key      # Foydalanuvchi qisqa key kiritadi (masalan, "sjJiw342vqs")
        self.base_url = "https://asicloud.uz/asicloudapirequests/jarvis.php"  # Yangi URL

        # Key majburiy
        if not self.user_key:
            raise ValueError("Key kiritilmadi. Iltimos, to‘g‘ri key kiriting.")

    def generate_text(self, prompt):
        # URL parametrlarini tayyorlash
        params = {
            "key": self.user_key,
            "prompt": prompt
        }

        # API so‘rovini yuborish (GET metodi)
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            # Javobni olish
            response_text = response.text  # jarvis.php dan kelgan to‘g‘ridan-to‘g‘ri matn
            return response_text
        except requests.exceptions.RequestException as e:
            return f"Xatolik yuz berdi: {str(e)}"