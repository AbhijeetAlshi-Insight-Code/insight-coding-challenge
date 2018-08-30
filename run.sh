curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
pip install pandas
pip isntall sys
python ./src/average-error.py ./input/actual.txt ./input/predicted.txt ./input/window.txt ./output/comparison.txt
