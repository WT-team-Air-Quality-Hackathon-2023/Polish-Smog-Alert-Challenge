FROM python:3.9

ARG API_TOKEN

RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs

WORKDIR /src

COPY ./backend/requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./backend /src
COPY ./frontend /src

RUN rm package-lock.json
RUN rm -rf .parcel-cache

RUN npm install
RUN npm install @parcel/watcher
RUN npm install lmdb
RUN npm install lightningcss
RUN npm run build

ENV INDEX_PATH=/src/dist/index.html
ENV ASSETS_PATH=/src/dist
ENV API_TOKEN=${API_TOKEN}
CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:80"]
