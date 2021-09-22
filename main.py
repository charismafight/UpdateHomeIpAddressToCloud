import requests as requests
from loguru import logger
import time

import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models

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


def call_txapi():
    try:
        cred = credential.Credential("AKIDrXx70cy3rPggQt50f3A0ziALFtGMBk23", "lFTQ5TbU6RWKq54lCMEqBE0XnmUv5wWo")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "dnspod.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = dnspod_client.DnspodClient(cred, "", clientProfile)

        req = models.DescribeRecordRequest()
        params = {

        }
        req.from_json_string(json.dumps(params))

        resp = client.DescribeRecord(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)