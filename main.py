import requests as requests
from loguru import logger
import time

logger.add('UpdateHomeIpAddressToCloud.log')
ip = '221.232.174.157'

if __name__ == '__main__':
    logger.debug('UpdateHomeIpAddressToCloud started')
    while True:
        result = requests.get('http://myip.ipip.net/s')
        if result.status_code == 200:
            if result.text.strip() != ip:
                logger.info('ip:' + ip)
                logger.info('result:' + result.text)
                ip = result.text
                # call txcloud api
            else:
                logger.info('ip has not changed')
        else:
            logger.info('can not visit http://myip.ipip.net/s')

        time.sleep(20)
