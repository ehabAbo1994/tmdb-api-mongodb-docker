# Step 1 select default OS image
FROM python:3.8-alpine

# Step 2 Setting up environment
RUN apk update
RUN apk add --no-cache python3-dev && apk add py3-pip
RUN pip3 install --upgrade pip


# Step 3 Configure a software
WORKDIR /app

# Installing dependencies.
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Copying project files.
COPY . /app



RUN mkdir -p /app/templates
RUN mkdir -p /app/temp_content
COPY ./templates/*  /app/templates

EXPOSE 5001
# Step 4 set default commands
ENTRYPOINT [ "python3" ]

# These commands will be replaced if user provides any command by himself
CMD [ "app.py" ]