# e-Shop
После копирования с Github в терминале нужно перейти параллельно директории shop, там выполнить следующие команды для установки вируального пространства: 

sudo apt-get install virtualenv

virtualenv venv --python=python3

. venv/bin/activate
	
После перейти в директорию shop там выполнить следующие команды:

sudo chmod +x main.sh
	
./main.sh

После запуска локального сервера запустить:

	http://127.0.0.1:8000/main/
