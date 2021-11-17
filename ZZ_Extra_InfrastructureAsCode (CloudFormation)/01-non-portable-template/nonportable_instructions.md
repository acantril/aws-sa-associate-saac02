# Non Portable Template Demo

In this demo, you will be implementing a non-portable template.
In order to understand what benefits a portable template provides, you need to understand the limitations a non-portable template has.

## Create or verify you have an A4L SSH Key created in EC2

Move to the EC2 Console https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Home:  
Move to `Network and Security` then `KeyPairs`  
Click `Create Key pair`  
Choose `pem` (for macOS or Linux or windows 10), choose `ppk` for earlier versions of windows, or if you prefer `putty`  
Enter `A4L` in the `Name` box  
Click `Create Key Pair`  

## Move to the CloudFormation Console  
## If you're watching the videos we will write a template together and upload it.
Open https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/ in a new tab.  
Click `Create Stack`  
Select `Upload a template file` and then click `Choose File`  
Choose `nonportable.yaml` (or JSON)  
Click to upload  
Click `Next`  
For `Stack Name` enter `nonportable1`  
Click `Next`  
Scroll down, click `Next`  
Scroll down, click `Create Stack`  

## Review what's created

Wait for stack to move to finish creating.
Does it work?
It might, it probably won't
Why..?
The Bucket Name is hard coded in the template. If any other student is using this template right now, because they use the bucket name, it will fail.

Update the Bucket Name in the template and save it
Delete the failed Stack
Create a stack in the same way as above....
Now it should work...

Select the `nonportable1` stack, and delete it
This will free up the S3 bucket name you have uniquely picked
## Move to a different region and apply the template again

Click the region dropdown .. and pick another region (anything but `us-east-1`) 
Move to the CloudFormation console
Click `Create Stack`  
Select `Upload a template file` and then click `Choose File`  
Choose `nonportable.yaml` (or JSON)  
Click to upload  
Click `Next`  
For `Stack Name` enter `nonportable1`  
Click `Next`  
Scroll down, click `Next`  
Scroll down, click `Create Stack`  
Wait for the stack to finish

## Review Stack
it will fail.
Why?
Review event history
find first red item
AMI ID isn't valid ... the EC2 AMI ID is hard coded, and these are region specific .. which means this template will only work in one AWS region....

## Review




