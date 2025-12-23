import os
from flask import Flask

app = Flask(__name__)

# Verinin saklanacağı klasör ve dosya
DATA_DIR = "/data"
DATA_FILE = os.path.join(DATA_DIR, "sayac.txt")

# Klasör yoksa oluştur (Hata almamak için)
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.route('/')
def hello():
    count = 0
    # 1. Dosyadan eski sayıyı oku
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                count = int(f.read())
            except:
                count = 0
    
    # 2. Sayıyı arttır
    count += 1
    
    # 3. Yeni sayıyı dosyaya yaz (Kalıcılık denemesi)
    with open(DATA_FILE, 'w') as f:
        f.write(str(count))
        
    return f"""
    <div style="text-align:center; margin-top:50px;">
        <h1>Docker & State</h1>
        <p>Bu veri diskten okunuyor.</p>
        <h1>Sayaç: {count}</h1>
    </div>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
