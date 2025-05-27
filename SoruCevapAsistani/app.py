from flask import Flask, request, render_template

app = Flask(__name__)

# Kural tabanlı yanıt sistemi
def generate_response(user_input):
    user_input = user_input.lower().strip()
    
    # Kural tabanı: Anahtar kelimeler ve yanıtlar
    rules = {
        "merhaba": "Merhaba! Nasılsın?",
        "selam": "Merhaba! Nasılsın?",
        "iyiyim": "Harika! Size nasıl yardımcı olabilirim?",
        "kötü": "Üzgünüm, böyle hissettiğin için. Size nasıl yardımcı olabilirim?",
        "nasılsın": "Ben bir yapay zeka modeliyim, duygularım yok ama size yardımcı olmak için buradayım!",
        "yapay zeka nedir": "Yapay zeka, makinelerin insan gibi düşünmesini sağlayan bir teknolojidir.",
        "yapay zeka hayat": "Yapay zeka, hayatımızı iş, eğitim ve sağlık gibi alanlarda dönüştürüyor.",
        "aslı": "Aslı, bu uygulamanın geliştiricisidir.",
        "erkan": "Erkan, bu uygulamanın geliştiricisidir.",
        "yapay zeka kullan": "Yapay zeka, makine öğrenimi ve derin öğrenme teknikleri ile kullanılır.",
        "yapay zeka ne demek": "Yapay zeka, makinelerin insan benzeri düşünme ve öğrenme yeteneklerine sahip olmasıdır.",
        "yapay zeka nerelerde": "Yapay zeka, sağlık, finans, otomotiv ve daha birçok alanda kullanılır.",
        "yapay zeka öğren": "Yapay zeka, verilerden öğrenerek ve deneyimlerden gelişerek çalışır.",
        "yapay zeka çalış": "Yapay zeka, verileri analiz ederek ve öğrenerek kararlar alır.",
        "yapay zeka ne işe yarar": "Yapay zeka, veri analizi, otomasyon ve tahmin gibi birçok alanda kullanılır.",
        "yapay zeka örnek": "Yapay zeka örnekleri arasında sesli asistanlar, otonom araçlar ve öneri sistemleri bulunur.",
        "nasıl çalışıyorsun": "Ben, kullanıcı girdilerine göre önceden tanımlanmış kurallara göre yanıt veriyorum.",
        "yapay zeka etik": "Yapay zeka, veri gizliliği ve önyargı gibi etik sorunlar doğurabilir.",
        "yapay zeka gelecek": "Yapay zeka, gelecekte daha da yaygınlaşacak ve hayatımızı daha da kolaylaştıracak.",
        "yapay zeka insan": "Yapay zeka, insanlarla işbirliği yaparak daha iyi sonuçlar elde edebilir."
    }
    
    # Kullanıcı girdisini kelimelere ayır
    words = user_input.split()
    
    # Her bir kural için anahtar kelimelerle eşleşme kontrolü
    for key, response in rules.items():
        key_words = key.split()
        # Eğer kullanıcı girdisindeki kelimeler, kuralın anahtar kelimelerini içeriyorsa
        if all(word in words for word in key_words):
            return response
            
    return "Üzgünüm, bu soruya yanıt veremiyorum."

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("text")
        print(f"Alınan kullanıcı girdisi: {user_input}")
        if user_input:
            response = generate_response(user_input)
            print(f"Üretilen yanıt: {response}")
    return render_template("index.html", response=response, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)