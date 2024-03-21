import requests
from getServerConnection.egressIP import ret_egress_ip
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger('SSL validator')


def getConnection(domain):
    connection_data = {
        "destination": domain,
        'port_443_status':'',
        'port_80_status':'',
        'is_redirected': None,
        'redirect_port': None,
        'redirect_port_status':''
    }
    url_80 = f"http://{domain}"
    url_443 = f'https://{domain}'
    # Check TCP port 80 status
    try:
        req = requests.get(url_80, timeout=10)
        print(req.text)
        if req.status_code == 200:
            logger.info(f"Connection towards TCP port 80 successful!")
            connection_data['port_80_status'] = 'open'
        if req.status_code == 301:
            logger.info(f"Connection towards TCP port 80 successful but redirected!")
            connection_data['is_redirected'] = True
    except ConnectionError or ConnectionResetError as e:
        connection_data['port_80_status'] = 'closed'
        logger.info(f"Connection towards TCP port 80 failed with error {e.args}")
    # Check TCP port 443 status
    try:
        req = requests.get(url_443, timeout=10)
        print(req.text)
        if req.status_code == 200:
            logger.info(f"Connection towards TCP port 443 successful!")
            connection_data['port_443_status'] = 'open'
        if req.status_code == 301:
            logger.info(f"Connection towards TCP port 443 successful but redirected!")
            connection_data['is_redirected'] = True
    except ConnectionError or ConnectionResetError as e:
        connection_data['port_443_status'] = 'closed'
        logger.info(f"Connection towards TCP port 443 failed with error {e.args}")
    print(connection_data)
    return connection_data


if __name__ == '__main__':
    # dest = "sodexo4you.be"
    # # dest = 'api.monday.com'
    # getConnection(dest)
    ret_egress_ip()

