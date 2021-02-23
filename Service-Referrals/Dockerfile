# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-buster

EXPOSE 8888

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Tells the container to run the application using production settings
ENV DJANGO_SETTINGS_MODULE ReferralService.settings.prod

# Add MySQL
RUN apt-get install -y default-libmysqlclient-dev

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder:DjangoProjectTemplate. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8888", "referrals.wsgi"]
