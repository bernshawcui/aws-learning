# AWS Networking Overview

- [AWS Networking Overview](#aws-networking-overview)
  - [Classless Inter-Domain Routing (CIDR)](#classless-inter-domain-routing-cidr)
    - [Overview](#overview)
    - [IPv4](#ipv4)
    - [Private vs Public IP (IPv4)](#private-vs-public-ip-ipv4)


<img src="assets/vpc-components-diagram.png" alt="VPC Components Overview" width="1500"/>


## Classless Inter-Domain Routing (CIDR)
### Overview
- CIDR is a method of  <ins>**allocating IP addresses** </ins>
- A CIDR consists of 2 components:
  - **Base IP**: e.g 192.168.0.0 (dotted-decimal notation)
  - **Subnet Mask**: defines how many <ins>**bits**</ins> can change in the IP
### IPv4
- An IP address is an idenfifier of a device on the network for communication purposes
- 8-bit number: 11000000 == 192
- Base IP consists of 4 number in 8-bit binary form (32 bit): 11000000.10101000.00000000.00000000
- Subnet mask (e.g /8) means the first 8 bits are constant, and the remaining can vary
- Each 8-bit is 1 byte, which is also an ***octet***
- <img src="assets/cidr-ipv4-octet.png" alt="CIDR Octect" width="200"/>
- |Subnet Mask|No. of Avail. IP| Avail. IP Range |
  |-|-|-|
  |192.168.0.0/32|2<sup>0</sup> = 1 |192.168.0.0|
  |192.168.0.0/31|2<sup>1</sup> = 2 |192.168.0.0 - 192.168.0.1|
  |192.168.0.0/30|2<sup>2</sup> = 4 |192.168.0.0 - 192.168.0.3|
  |192.168.0.0/24|2<sup>8</sup> = 256 |192.168.0.0 - 192.168.0.255|
  |192.168.0.0/16|2<sup>16</sup> = 65,536 |192.168.0.0 - 192.168.255.255|
  |192.168.0.0/8|2<sup>24</sup> = 	16,777,216 |192.168.0.0 - 192.255.255.255|

### Private vs Public IP (IPv4)
- The Internet Assigned Numbers Authority (IANA) sets the public & private blocks of IPv4 addresses
- Private IPs:
  - **Class A**: 10.0.0.0 to 10.255.255.255 (10.0.0.0/8, for large networks)
  - **Class B**: 172.16.0.0 to 172.31.255.255 (for medium networks, AWS default VPC is in this range)
  - **Class C**: 192.168.0.0 to 192.168.255.255 (for small networks liek home network)
- Public IPs: all remaining