FROM gitpod/workspace-full

USER gitpod

RUN source bin/activate

RUN pip3 install -r requirements.txt

RUN npm install -g --classic heroku

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN sudo apt-get -q update && \
#     sudo apt-get install -yq bastet && \
#     sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
