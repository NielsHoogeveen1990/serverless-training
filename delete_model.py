import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def delete_model():
    """
    Deleted a model with a certain file name.
    :return: Nothing
    """
    try:
        os.remove(config['S3']['key'])
    except OSError as e:
        print(f'Error: {config["S3"]["key"]}: {e.strerror}.')


if __name__=='__main__':
    delete_model()
    print(f'Deleted the model {config["S3"]["key"]} successfully.')