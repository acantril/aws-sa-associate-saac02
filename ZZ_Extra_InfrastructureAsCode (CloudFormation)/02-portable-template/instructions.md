# PREP

Make sure you have an A4L Key pair in us-east-1

# STEP 1 - Allowing Multiple Stacks

First we remove the Bucket Name
This allows CFN to auto name the physical resource - which allows for multiple applications in the same account in the same region.

But we can't apply in another region... why ?

- The template references a Key Pair, these are regional.
- The template references an AMI ID, these are regional.

# STEP 2 - Ask for an AMI and Ask for a Key Pair

In this version of the template, we add parameters for the AMIID to use and the Key Pair to use. This allows the template to be applied in any region as long as a valid AMIID and Key Pair is provided for that region.

Is this template portable? .. Kind Of.
It still requires some input based on the region (Valid AMIID and KeyPair)

# STEP 3 - Change the AMIID to SSM (Dynamic) and remove Key Pair

In this version of the template we remove the Key Pair Parameter and Property on the EC2 Instance Logical resource.
if we have other methods of connection such as EC2 Instance Connect, or SSM Session manager (if we configured it). The Key Pair isn't required.

We also remove the manual Parameter for AMIID and reference an SSM parameter which AWS provide, which always references the latest Amazon Linux 2 AMI in that region.




