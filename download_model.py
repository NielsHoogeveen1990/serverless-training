import boto3
import botocore
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def download_s3_model():
    """
    Downloads a pickled model from S3.
    :return: unpickled model
    """
    # Make s3 connection
    s3 = boto3.client('s3')

    try:
        s3.download_file(config['S3']['bucket_name'], config['S3']['key'], config['S3']['key'])
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise


if __name__ == "__main__":
    download_s3_model()
    print(f'Downloaded the model {config["S3"]["key"]} successfully.')