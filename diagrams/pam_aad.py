from diagrams import Diagram
from diagrams.aws.compute import EC2 as host
from diagrams.azure.identity import ActiveDirectory as aad
from diagrams.generic.os import Ubuntu as linux
from diagrams.programming.language import C as code

with Diagram("pam_aad", show=False):
    host("server") >> linux("ubuntu") >> code("pam_aad.c") >> aad("Azure Active Directory")

