FROM python

# cài đặt các dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        freetds-bin \
        freetds-dev \
        libkrb5-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        libpq-dev \
        default-libmysqlclient-dev \
        && \
    rm -rf /var/lib/apt/lists/*

# tạo một thư mục app trong container để lưu trữ code
RUN mkdir /airflow

# set working directory cho container
WORKDIR /airflow

# cài đặt các packages cần thiết cho Python và Airflow
COPY requirements.txt /airflow
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install apache-airflow

# copy code vào container
COPY . /airflow

# set biến môi trường cho Airflow
ENV AIRFLOW_HOME=/airflow

# Khởi tạo Airflow database
# RUN airflow db init

# Khai báo port sử dụng
EXPOSE 8080

# khởi chạy Airflow webserver
# CMD ["airflow", "webserver"]
