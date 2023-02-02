FROM python:3 as build

WORKDIR /opt/app

RUN pip install pdm

COPY pdm.lock .
COPY pyproject.toml .

RUN mkdir __pypackages__ &&\
    pdm install --prod --no-editable --no-lock

# ---

FROM python:3

WORKDIR /opt/app

ENV PYTHONPATH /opt/app/pkgs
ENV PYTHONDONTWRITEBYTECODE=1

COPY --from=build /opt/app/__pypackages__/3.11/lib /opt/app/pkgs
COPY ./script.py .

CMD [ "python3", "./script.py" ]
