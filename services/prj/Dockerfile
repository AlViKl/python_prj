# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10.6-slim-bullseye

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Add appuser
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser

# Upgrade pip
RUN pip install --upgrade pip

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "main.py"]