from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import urllib
import base64

session = boto3.Session()
CREDENTIALS = session.get_credentials()
creds = CREDENTIALS.get_frozen_credentials()

def signed_request(request):
    '''Sign AWS API request headers'''
    headers = request['headers']
    url = f"https://{headers['host'][0]['value']}{request['uri']}"
    method = request['method']
    # We need to sign the body too
    data = base64.b64decode(request['body']['data'])
    # Next line flattens the AWS headers format to python 'requests' one
    headers = {v[0]['key']:v[0]['value'] for k,v in headers.items()}
    # This header should not be signed as it changes hop to hop
    headers.pop('X-Forwarded-For')
    # Grab the region from the lambda function URL, ex: kjh123kjhbrkj.lambda-url.eu-west-2.on.aws
    url_segments = urllib.parse.urlparse(url).netloc.split('.')
    region = url_segments[2]
    req = AWSRequest(method=method, url=url, params=None, headers=headers, data=data)
    SigV4Auth(creds, 'lambda', region).add_auth(req)
    signed_headers=dict(req.headers.items())
    # format the headers for Cloudfront, ex:
    # "headers": {
    #   "user-agent": [
    #     {
    #       "key": "User-Agent",
    #       "value": "Amazon CloudFront"
    #     }
    #   ]
    # }
    request['headers'] = { k.lower():[{'key':k,'value':v}] for k,v in signed_headers.items() }
    
    return request

def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']
    return signed_request(request)