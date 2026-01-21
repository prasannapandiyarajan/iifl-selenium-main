FROM selenium/standalone-chrome:latest

# Install Python
USER root
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /home/seluser/project

# Copy project
COPY . .

# Install Python deps
RUN pip3 install selenium pytest pytest-html beautifulsoup4 pandas pytest-asyncio

# Default command to run tests
CMD ["bash", "run_tests.sh"]


