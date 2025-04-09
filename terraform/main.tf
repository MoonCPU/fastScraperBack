terraform {
   required_providers {
     aws = {
       source  = "hashicorp/aws"
       version = "5.92.0"
     }
   }

  backend "s3" {}
 }
 
 provider "aws" {
   region = "sa-east-1"
}

// 1 - setting up the VPC 

resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "sa-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main-igw"
  }
}

// route tables are usef only for outbound requests
// with a cidr block of 0.0.0.0/0,
// route tables will take any requests from resources inside the subnet and route them to the IGW
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "public-route-table"
  }
}

// attach the route table to our public subnet
resource "aws_route_table_association" "public_assoc" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_security_group" "web_sg" {
  name        = "web-sg"
  description = "Allow web and SSH traffic"
  vpc_id      = aws_vpc.main.id

  // we have to allow our security group to let in requests to the fastapi app thats running on port 8000 inside the ec2
  // the user will try to access the ec2 public ip address, but just accessing the ec2 does nothing
  // we also need to the port the fastapi app is running on, which is port 8000
  ingress {
    description = "Allow HTTP/FastAPI"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 
  }

  # inbound: allow SSH
  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # outbound: allow all
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "web-sg"
  }
}

// 2 - create ec2 instance

resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = file("${path.module}/keys/id_rsa.pub") 
}

resource "aws_instance" "app_server" {
  ami                         = "ami-0d866da98d63e2b42" 
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.public.id
  vpc_security_group_ids      = [aws_security_group.web_sg.id]
  key_name                    = aws_key_pair.deployer.key_name

  associate_public_ip_address = true

  tags = {
    Name = "fastapi-ec2"
  }

  user_data = file("${path.module}/setup.sh")
}

// 3 - set up cloudfront

resource "aws_cloudfront_distribution" "api_distribution" {

  depends_on = [aws_instance.app_server]

  origin {
    domain_name = aws_instance.app_server.public_dns 
    origin_id   = "apiEC2Origin"

    custom_origin_config {
      http_port              = 8000
      https_port             = 443
      origin_protocol_policy = "http-only"
      origin_ssl_protocols   = ["TLSv1.2"]
    }
  }

  enabled             = true
  default_root_object = ""

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "apiEC2Origin"

    viewer_protocol_policy = "redirect-to-https"
    compress               = true

    forwarded_values {
      query_string = true
      cookies {
        forward = "all"
      }
    }
  }

  price_class = "PriceClass_100"

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn      = var.acm_certificate_arn
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2021"
  }

  aliases = [
    "api.moondev-cloud.com"
  ]
}

// add record to route53 to validate ssl certificate
resource "aws_route53_record" "acm_validation_api" {
  zone_id = var.hosted_zone_id
  name    = var.route53_record_name
  type    = "CNAME"
  ttl     = 300
  records = [var.route53_record_value]
}

resource "aws_route53_record" "api_alias" {
  zone_id = var.hosted_zone_id
  name    = "api.moondev-cloud.com"
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.api_distribution.domain_name
    zone_id                = aws_cloudfront_distribution.api_distribution.hosted_zone_id
    evaluate_target_health = false
  }
}