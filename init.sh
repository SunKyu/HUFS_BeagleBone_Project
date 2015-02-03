sudo apt-get update
sudo apt-get install -y vim
sudo apt-get install -y git
sudo apt-get install -y python-dev
sudo pip install Adafruit_BBIO

cd /opt
sudo git clone https://github.com/SunKyu/Vim_vimrc.git
sudo git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cd cd Vim_vimrc
cat vimrcfile > ~/.vimrc  
