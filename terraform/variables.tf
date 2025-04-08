variable "acm_certificate_arn" {
  description = "The ARN of the existing ACM certificate for CloudFront"
  type        = string
}

variable "hosted_zone_id" {
  description = "The Route 53 hosted zone ID for moondev-cloud.com"
  type        = string
}

variable "route53_record_name" {
  description = "Route53 Record name"
  type        = string
}

variable "route53_record_value" {
  description = "Route53 Record value"
  type        = string
}