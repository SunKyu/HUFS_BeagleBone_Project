apt-get update
apt-get install -y vim
apt-get install -y git
apt-get install -y python-dev
apt-get install -y python-pip
pip install Adafruit_BBIO

cd /opt
git clone https://github.com/SunKyu/Vim_vimrc.git
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cd cd Vim_vimrc
cat vimrcfile > ~/.vimrc 

exit
