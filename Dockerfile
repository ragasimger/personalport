FROM python:3.10-slim-buster


# Creating workdir and copying the config and lock files for poetry
WORKDIR /portfolio
COPY Pipfile.lock Pipfile /portfolio/

# Installing the system dependencies
RUN apt-get update && apt-get install -y git gcc\
    && pip install pipenv 



# Installing the python dependencies
RUN pipenv install --system --deploy --ignore-pipfile --dev

# Running the bot
COPY . /portfolio/
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "sh", "entrypoint.sh" ]