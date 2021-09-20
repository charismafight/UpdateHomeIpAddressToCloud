import requests as requests
from loguru import logger

logger.add('UpdateHomeIpAddressToCloud.log')
ip = '221.232.174.157'

if __name__ == '__main__':
    logger.debug('UpdateHomeIpAddressToCloud started')
    while True:
        result = requests.get('http://myip.ipip.net/s')
        if result.status_code == 200 and result.text != ip:
            logger.info('ip changed to ' + result.text)
            ip = result.text
            # 调用腾讯api更新地址
        else:
            print('fuck')
