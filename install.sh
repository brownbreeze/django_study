sed -i -e '/override_install_langs/s/$/,ko_KR.utf8/g' /etc/yum.conf 
yum install -y https://repo.ius.io/ius-release-el7.rpm
yum -y update 
yum reinstall -y glibc-common 
yum install -y wget && \
yum install -y lsof vim net-tools 
yum install -y xz-devel 
yum install sqlite-devel -y
yum install -y gcc make openssl-devel bzip2-devel libffi-devel gcc-c++ automake autoconf make perl aclocal java-1.8.0-openjdk-devel rsyslog 
cd /usr/src 
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz 
tar xzf Python-3.7.5.tgz 
cd Python-3.7* 
./configure --enable-optimizations 
make altinstall 
cd /usr/src 
rm -rf Python-3.7.5.tgz 
alias python='/usr/local/bin/python3.7' 
ln -sf /usr/local/bin/pip3.7 /usr/bin/pip3 
pip3 install "django~=3.0.0"
pip3 install Django==2.1.*
django-admin --version
