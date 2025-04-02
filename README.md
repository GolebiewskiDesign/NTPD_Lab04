# NTPD_Lab04
Aplikacja udostępnia interfejs API dla modelu uczenia maszynowego, umożliwiający wykonywanie predykcji na przesłanych danych. Może służyć jako backend dla aplikacji webowych. 

# Uruchamianie aplikacji ( 3 możliwości ) :

# A. Lokalnie (bez Dockera)

 1. Sklonuj repozytorium
git clone https://github.com/GolebiewskiDesign/NTPD_Lab04.git

cd nazwa-repozytorium

 3. Stwórz i aktywuj środowisko wirtualne (opcjonalne)
python -m venv venv

source venv/bin/activate  # Linux/macOS

venv\Scripts\activate     # Windows

 5. Zainstaluj zależności

pip install -r requirements.txt

 7. Uruchom aplikację
    
uvicorn app:app --host 0.0.0.0 --port 5000

# B. Za pomocą Dockera

 1. Zbuduj obraz
docker build -t ml-app .

 2. Uruchom kontener
    
docker run -p 5000:5000 --env-file .env ml-app

# C. Za pomocą Docker Compose

 1. Uruchom usługi (aplikacja + baza danych)
docker-compose up -d --build

 2. Sprawdź działanie
curl http://localhost:5000



