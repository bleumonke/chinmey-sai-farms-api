aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 078548485543.dkr.ecr.us-east-1.amazonaws.com
docker build -t chinmey-sai-farms-apis:1.0.0 .
docker tag chinmey-sai-farms-apis:1.0.0 078548485543.dkr.ecr.us-east-1.amazonaws.com/chinmey-sai-farms-apis:1.0.0
docker push 078548485543.dkr.ecr.us-east-1.amazonaws.com/chinmey-sai-farms-apis:1.0.0