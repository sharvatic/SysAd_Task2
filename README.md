Go to the root user of your system using 
```
sudo -i
```
Run the following commands to get the necessary scripts 
```
cd /
mkdir server1
cd server1 
git clone https://github.com/sharvatic/Sysad_task1.git
cd ..
git clone https://github.com/sharvatic/SysAd_Task2.git
```
Run the hosts.sh script

Build the docker file given within the same directory using
```
docker build -t ubuntu:1.0 .
```

Run the docker container using
```
docker run -itd -p 8080:80 --name gamma ubuntu:1.0
```
Run the docker-compose.yml file using
```
docker compose up
```

Download the python extension in VScode.
Install MySQL and install the mysql connector using
```
pip install mysql-connector-python
```
Run the Database.py file first and then the Mysql.py
