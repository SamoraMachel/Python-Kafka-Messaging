# Messaging with kafka in python
A sample project for message passing with kafka

## Requirements
In order to run this project you are required to have the following softwares installed
 - docker
 - python 3

## Project Execution 
First you'll have to start the kafka server using 
```bash
docker-compose up 
```

Once the kafka server is up the you can open 2 separate terminals. First install the necessary requirements using 
```bash
pip install -r requirements.txt
```
Afterwards in the first terminal run
```bash
python src/consumer.py
```

in the second instance of the terminal run 
```bash
python src/producer.py
```
