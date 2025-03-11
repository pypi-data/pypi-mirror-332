FROM python:3.12-slim as bkstart

WORKDIR /app

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt  .

RUN pip install -U pip setuptools uv && uv pip install -r requirements.txt --python `which python`

### BEEKEEPER START LOGIC ENDS HERE ###

############################################################################################

### YOUR DOCKERFILE STEPS BEGIN BELOW
FROM python:3.12-slim

WORKDIR /app

COPY --from=bkstart /opt/venv /opt/venv

COPY . .

ENV PATH="/opt/venv/bin:$PATH"

# Make the run.sh script executable
RUN chmod +x run.sh

# set the start command
ENTRYPOINT ["./run.sh"]