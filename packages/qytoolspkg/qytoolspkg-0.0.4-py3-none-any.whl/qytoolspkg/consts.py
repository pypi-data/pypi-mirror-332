import os
# from dotenv import load_dotenv, find_dotenv, dotenv_values

# env_file = find_dotenv(".env", 
#                         raise_error_if_not_found=True, 
#                         usecwd=True)
# print(f"find env file at {env_file}")
# load_dotenv(env_file)
# load_dotenv("~/.env")
DB_CONFIG = {
            "host": os.getenv('DB_HOST'),
            "user": os.getenv('DB_USER'),
            "password": os.getenv('DB_PASSWORD'),
            "port": os.getenv('DB_PORT')}
# DB_CONFIG = dotenv_values("~/.env")
# print(DB_CONFIG)
DB_CONFIG['auth_plugin']='caching_sha2_password'
DATE_FORMAT = "%Y%m%d"
#os.environ["R_HOME"] = r"E:\R-4.1.0" # change as needed
