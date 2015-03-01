sudo apt-get update
sudo apt-get install -y vim
sudo apt-get install -y python-dev
sudo apt-get install -y python-pip
sudo apt-get install -y python-smbus
sudo apt-get install -y bluez
sudo apt-get install -y libbluetooth-dev
sudo apt-get install -y unzip
sudo pip install Adafruit_BBIO
sudo pip install pybluez
sudo cd /opt
sudo wget --no-check-certificate https://pybluez.googlecode.com/files/PyBluez-0.20.zip
sudo unzip PyBluez-0.20.zip
sudo cd PyBluez-0.20
sudo python setup.py install


#cd /opt
#git clone https://github.com/SunKyu/Vim_vimrc.git
#git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
#cd Vim_vimrc
#cat vimrcfile > ~/.vimrc 


