import logging
import requests
import datetime
import json
import pprint
import time
import pymysql 


DB_HOST = 'localhost'
DB_USER = 'homestead'
DB_PASS = 'secret'
DB_NAME = 'crypto'
CONFIG_FILENAME = ''
CYCLE_DELAY = 60  # delay in seconds between cycles
LOG_FILENAME = 'output.log'
BASE_API_URL = 'https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10'
ALLOWED_CURRENCIES = ['EUR', 'CAD', 'USD']

# logger setup
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("app")


def main():
    while True:
        results = api_request()
        if results is not None:
            insert_data(results)
        else:
            info_msg = 'No results from api request'
            print(info_msg)
            logger.info(info_msg)
        time.sleep(CYCLE_DELAY)


def insert_data(results):
    # sql = ("INSERT INTO employees "
    #                 "(first_name, last_name, hire_date, gender, birth_date) "
    #                 "VALUES (%s, %s, %s, %s, %s)")
    #
    # timestamp = datetime.datetime.now()
    #
    # db = pymysql.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    #
    # cursor = db.cursor()
    #
    # try:
    #   cursor.execute(sql)
    #   db.commit()
    # except Exception as e:
    #   db.rollback()
    #   error_msg = 'DB insert error: {}'.format(e)
    #   logger.error(error_msg)
    #   print(error_msg)
    #
    #
    #
    # db.close()
    pprint.pprint(results)


def api_request():
    info_msg = 'Retrieve list from CoinMarketCap'
    print(info_msg)
    logger.info(info_msg)
    try:
        return requests.get(build_api_url('CAD', 100)).json()
    except Exception as e:
        error_msg = 'Error retrieving list from CoinMarketCap: {}'.format(e)
        print(error_msg)
        logger.error(error_msg)
        return None


def build_api_url(currency, limit=100):
    return '{}/convert={}&limit={}'.format(BASE_API_URL, currency, limit)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error('Exception: {}'.format(e))
        raise
