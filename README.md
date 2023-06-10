Go to the root user of your system using 
```
sudo -i
```
Run the following commands to get the necessary scripts 
```
cd /
git clone https://github.com/sharvatic/Sysad_task1.git
git clone https://github.com/sharvatic/SysAd_task2.git
```
Build the docker file given with in the same directory
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
