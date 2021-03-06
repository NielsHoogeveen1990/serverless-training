# Welcome!
 
In order to make this API work and deploy it, one needs to take the following steps:
- Install the Python requirements plugin for Serverless
```
$ sls plugin install -n serverless-python-requirements
```
- Install dependencies
```
$ pip install -r requirements.txt
```
- Configure the config.ini file with your own S3 bucket name and key for the saved ML model
- Adjust the serverless.yml file if needed
- Test the API locally 
```
$ sls invoke local --function predict-disease --path event.json
```
- Deploy the API as an AWS Lambda function with the following bash commands
```
$ python download_model.py && sls deploy && python delete_model.py   
```
This combined bash command will first download the ML model locally,
then it will load the model in the handler.py file, and finally it will delete it locally.

## Need help with debugging?
Serverless gives little feedback at first sight.
In order to debug a failed deployment, set SLS_DEBUG to True
```
$ export SLS_DEBUG=true
```
However, when you get a 502 for example when testing the API, you can also ask
Serverless for the logs with the following bash command (after testing):
```
$ serverless logs -f [yourfunction] -s dev
```
