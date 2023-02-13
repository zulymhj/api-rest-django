#######################################
# PRODUCTION ecommerce-API DOCKERFILE. #
########################################

########## BUILDING STAGE. ###########

# PULL OFFICIAL PYTHON 3.10 BASE IMAGE.
FROM python:3.10.6 as builder

# SET WORK DIRECTORY.
WORKDIR /zhj/ecommerce/ecommerce-api

# SET ENVIRONMENT VARIABLES.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# INSTALL UPGRADES & DEPENDENCIES.
RUN apt-get update && apt-get upgrade -y
RUN apt-get install gcc -y
RUN apt-get install python3 -y

# LINT
RUN pip install --upgrade pip
COPY . .

######### STYLE Q.A. #########
# RUN flake8 --ignore=E501,F401 .

# COPY BASE & PRODUCTION REQUIREMENTS.
COPY requirements/base.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements/base.txt

##################################
########## FINAL STAGE. ##########

# PULL OFFICIAL PYTHON 3.10 BASE IMAGE. #
FROM python:3.10.6

# create directory for the zhj user.
RUN mkdir -p /home/zhj && \
    mkdir -p /home/zhj/ecommerce && \
    mkdir /home/zhj/ecommerce/ecommerce-api

# CREATE THE "zhj" USER.
RUN addgroup -system zhj && adduser --system --group zhj

# CREATE THE APPROPRIATE DIRECTORIES.
ENV APP_HOME=/home/zhj/ecommerce/ecommerce-api
RUN mkdir $APP_HOME/static && mkdir $APP_HOME/media
WORKDIR $APP_HOME

# INSTALL DEPENDENCIES.
RUN apt-get update && apt-get upgrade -y

COPY --from=builder zhj/ecommerce/ecommerce-api/wheels /wheels
COPY --from=builder zhj/ecommerce/ecommerce-api/requirements/base.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.api.sh
COPY /entrypoint.api.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.api.sh
RUN chmod +x ./entrypoint.api.sh

# COPY PROJECT.
COPY . $APP_HOME

# CHANGE THE OWNER OF ALL THE FILES TO THE APP USER.
RUN chown -R zhj:zhj $APP_HOME


# CHANGE TO THE zhj USER.
USER zhj

# RUN entrypoint.sh
#ENTRYPOINT ["/home/zhj/ecommerce/ecommerce-api/entrypoint.api.sh"]


