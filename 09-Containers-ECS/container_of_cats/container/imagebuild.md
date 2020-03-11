# Container of cats docker image

Ideally run this on an EC2 instance within AWS (running amazon linux)
Needs internet access for image upload to dockerhub
You will need a dockerhub account
To test the container ... tcp/80 will need to be open on the instance security group

## Download, Install and Configure docker and tools

sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user

## Use Git to get the lesson files

sudo yum install git
git clone https://github.com/acantril/aws-sa-associate-saac02.git

## Build the docker image

cd aws-sa-associate-saac02/containers/container_of_cats
docker build -t containerofcats .
docker images --filter reference=containerofcats

## Test the image by running a container
docker run -t -i -p 80:80 containerofcats

## Upload image to docker hub

docker login --username YOUR_USER
docker images
docker tag IMAGEID YOUR_USER/containerofcats
docker push YOUR_USER/containerofcats
