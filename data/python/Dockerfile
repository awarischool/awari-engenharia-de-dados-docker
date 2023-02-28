FROM continuumio/miniconda:latest

WORKDIR /home/awari/

COPY ./data/python/environment.yml ./
COPY ./data/python/api.py ./
COPY ./data/python/boot.sh ./

RUN ["chmod", "+x", "./boot.sh"]

RUN conda env create -f environment.yml

RUN echo "source activate awari" > ~/.bashrc
ENV PATH /opt/conda/envs/awari/bin:$PATH

RUN pip install kafka-python pandas boto3 Faker

EXPOSE 5001

#ENTRYPOINT ["./boot.sh"]