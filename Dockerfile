FROM betalabs/usd

RUN apt install -y python-pip && rm -rf /var/cache/apt

RUN mkdir /app
WORKDIR /app

COPY . /app/gltf2usd

RUN cd /app/gltf2usd && python setup.py sdist bdist_wheel