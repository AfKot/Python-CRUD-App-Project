#Use Python 3.6 as a base image
FROM python:3.6
# DONT NEED BUT COULD USE: RUN apt-get update && apt-get install -y python3-pip

# Copy contents into image
COPY . .

# install pip dependencies from requirements file
RUN pip3 install -r requirements.txt

# Expose correct port
EXPOSE 5000

# Create an entrypoint
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]