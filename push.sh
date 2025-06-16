aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 078548485543.dkr.ecr.us-east-1.amazonaws.com
docker build -t chinmey-sai-farms-apis:1.0.4 .
docker tag chinmey-sai-farms-apis:1.0.4 078548485543.dkr.ecr.us-east-1.amazonaws.com/chinmey-sai-farms-apis:1.0.4
docker push 078548485543.dkr.ecr.us-east-1.amazonaws.com/chinmey-sai-farms-apis:1.0.4