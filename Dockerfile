# Use Amazon Linux as the parent image
FROM amazonlinux

# Set the working directory in the container
WORKDIR /app

# Install Python, pip, and other necessary packages
RUN yum update -y && \
    yum install -y python3 python3-pip && \
    yum clean all

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY bot.py .

# Expose port 80 (if your application has a web interface or API)
EXPOSE 80

# Run the command to start your application
CMD ["python3", "bot.py"]
