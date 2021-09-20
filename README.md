# hello-python

```
sudo apt update
sudo apt install build-essential libbz2-dev libdb-dev \
  libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
  libncursesw5-dev libsqlite3-dev libssl-dev \
  zlib1g-dev uuid-dev tk-dev

# v3.9.7
wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tar.xz
tar xJf Python-3.9.7.tar.xz
cd Python3.9.7
./configure
make
sudo make install

# version 確認
exec $SHELL -l
python3 --version
```