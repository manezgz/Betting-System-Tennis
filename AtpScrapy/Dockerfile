

FROM centos:latest

RUN yum install -y sudo
RUN yum install -y centos-release-scl
RUN yum install -y python27
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
sudo yum install git
RUN yum install -y vim
RUN yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel
RUN yum groupinstall -y "Development tools"
RUN yum install -y python-setuptools python-setuptools-devel
RUN easy_install pip
RUN yum install -y gcc libffi-devel python-devel openssl-devel
RUN pip install scrapy
RUN pip install pandas
RUN pip install numpy


