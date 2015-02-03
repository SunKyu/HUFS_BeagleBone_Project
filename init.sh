sudo apt-get update
sudo apt-get install -y vim
sudo apt-get install -y git
sudo apt-get install -y python-dev
sudo apt-get install -y python-pip
sudo apt-get install -y python-smbus
sudo pip install Adafruit_BBIO


cd /opt
git clone https://github.com/SunKyu/Vim_vimrc.git
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cd Vim_vimrc
cat vimrcfile > ~/.vimrc 


