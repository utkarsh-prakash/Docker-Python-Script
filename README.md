<center><h1>Data processing using python scripts deployed on Docker Container</h1></center>
This repository is a very basic version of data processing python containers. For a start lets look at our folder structure.

```
ROOT
├── PythonScript
│   ├── Dockerfile
│   ├── requirements.txt
│   └── script.py
└── PythonScriptData
    ├── data.xlsx
    └── output.xlsx
```

<h2> PythonScript </h2>
<h3>requirements.txt</h3>
This file includes all the python packages that we need to install while creating the docker image.
<br><br>
<h3>script.py</h3>
It is a normal python script which reads an input, processes it and writes an output.<br>
But how do we read or write an input data? We will discuss it in a bit.
<br><br>
<h3>Dockerfile</h3>
Dockerfile is a list of steps docker has to execute while creating an image. Lets go by each and every step.<br>
Define a python base image.

```
FROM python:3.8-slim-buster
```

Copy the files in your present directory (PythonScript) to your main directory of Docker image.

```
COPY . /usr/src/myapp
```

Set your working directory and define a directory for input/output data that we talked about.

```
WORKDIR /usr/src/myapp
RUN mkdir -p /usr/src/myapp/data
```

Install the packages present in the requirements.txt file.

```
RUN pip3 install -r requirements.txt
```

Run the script as you would on command prompt.

```
CMD [ "python", "script.py"]
```
We are set with all the codefiles we need to create a docker image.
<br><br>
<h2>PythonScriptData</h2>
This will be our folder where we will keep our input data. The docker container will process that data and store the output in same folder. Lets see how.
<br><br>
<h2>Docker Commands</h2>
Command for building a docker image.

```
docker build --tag python-docker:v1.0.0 .
```
--tag - tells docker that we will provide optional tag for our image<br>
python-docker - image<br>
v1.0.0 - tag<br><br>
Command for listing images.

```
docker images
```
Command for running the docker container.

```
docker run -it --rm -v D:\Educational\Docker\PythonScriptData:/usr/src/myapp/data -w /usr/src/myapp python-docker:v1.0.0
```
-it - Interactive Terminal, supports user input<br>
--rm - Clear out docker residuals<br>
-v - volume to use<br>
Now after the -v tag we are specifying localPath:DockerImagePath , i.e. my local folder will be dynamically mapped to the docker image folder which we earlier created for input/output.<br>
-w - redefine the working directory<br>
At last specify the imageName:Tag<br><br>
Command for checking the run history.

```
docker ps -a
```
Command for checking logs of a run.

```
docker logs -f --until=2s containerRun_name (we can get this from last command)
```
Command for deleting a docker image.

```
docker rmi -f python-docker:v2.0.0
```