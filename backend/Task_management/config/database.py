import os 
DATABASES={
    'default': {
        'ENGINE': os.environ["DB_ENGINE"],
        'NAME': os.environ["DB_NAME"],
        'HOST' : os.environ["DB_HOST"],
        "PORT" :"",
        "OPTIONS":{
            "driver": os.environ["DB_DRIVER"],
            "trusted_connection": os.environ["DB_TRUSTED_CONNECTION"],
            "extra_params": os.environ["DB_EXTRA_PARAMS"],
        },
    }
}