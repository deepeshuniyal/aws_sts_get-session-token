# aws_sts_get-session-token
This process access aws cli with mfa enable accounts.
Below are steps.
1. configure aws using command **aws configure**. (Ignore this if you allready done).
2. add the below line in **~/.bashrc** at the end.
    > **. ~/.aws/.aws_access_data**
3. change **mfa_device_arn=** parameter inside **aws_cli_sts_access.py**.
4. run the python job.
    > **python aws_cli_sts_access.py** <br />
    it will ask you the MFA code.


