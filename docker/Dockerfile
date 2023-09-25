FROM bcgovimages/aries-cloudagent:py36-1.16-0_0.6.0

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# Make site packages location more accessible (for use with volumes)
RUN ln -s $(pyenv prefix)/lib/python3.6/site-packages site-packages

USER root
COPY acapy_resolver_oracle acapy-resolver-oracle/acapy_resolver_oracle
COPY README.md acapy-resolver-oracle
COPY setup.py acapy-resolver-oracle
COPY pyproject.toml acapy-resolver-oracle
COPY poetry.lock acapy-resolver-oracle
COPY docker/default.yml .
RUN chown -R indy:indy acapy-resolver-oracle
USER $user

RUN cd acapy-resolver-oracle; poetry install --no-dev
RUN pip3 install -I --no-cache git+https://github.com/hyperledger/aries-cloudagent-python.git@main

ENTRYPOINT ["/bin/bash", "-c", "aca-py \"$@\"", "--"]
CMD ["start", "--arg-file", "default.yml"]
