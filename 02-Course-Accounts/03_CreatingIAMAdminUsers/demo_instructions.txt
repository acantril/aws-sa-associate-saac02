# GENERAL ACCOUNT

Login to `GENERAL` AWS account using the Account Root User
Move to IAM console
Locate IAM Signin Link
Click `Customize`
Customize this alias
I use `saac02-general` you will need to pick something else
Click `Yes Create`
Note down the signin URL (mark it as for the GENERAL account) you will need this later

Click `Users`
Click `Add User`
username `iamadmin`
select `AWS Management Console Access`
Custom Password
Pick something Secure
Click `Next Permissions`
Add `Administrator Access`
Click `Next Tags`
Click `Next Review`
Click `Create User`
Click `Close`

paste in the `GENERAL ACCOUNT SIGNING URL` 
username `iamadmin`
Enter your chosen Password
Signin

Select `My Security credentials` from the Account dropdown
Click `Assign MFA Device`
Virtual MFA Device
using a MFA application (lesson links) scan the QR Code
Enter 2 generated codes
Assign the MFA
Signout of the account (account menu)
Paste in the GENERAL account signin URL again
iamadmin
chosen Password
enter MFA one time Password
Assuming that works ... the general account is setup correctly.

# PRODUCTION ACCOUNT

Login to `PRODUCTION` AWS account using the Account Root User
Move to IAM console
Locate IAM Signin Link
Click `Customize`
Customize this alias
I use `saac02-production` you will need to pick something else
Click `Yes Create`
Note down the signin URL (mark it as for the PRODUCTION account) you will need this later

Click `Users`
Click `Add User`
username `iamadmin`
select `AWS Management Console Access`
Custom Password
Pick something Secure
Click `Next Permissions`
Add `Administrator Access`
Click `Next Tags`
Click `Next Review`
Click `Create User`
Click `Close`

paste in the `PRODUCTION ACCOUNT SIGNING URL` 
username `iamadmin`
Enter your chosen Password
Signin

Select `My Security credentials` from the Account dropdown
Click `Assign MFA Device`
Virtual MFA Device
using a MFA application (lesson links) scan the QR Code
Enter 2 generated codes
Assign the MFA
Signout of the account (account menu)
Paste in the PRODUCTION account signin URL again
iamadmin
chosen Password
enter MFA one time Password
Assuming that works ... the PRODUCTION account is setup correctly.