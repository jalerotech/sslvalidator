import requests
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger('Getting Egress IP')


def ret_egress_ip() -> str:
    """
    Returns the egress IP (public IP address) of my machine.
    :return:
    """
    f = requests.request('GET', 'http://myip.dnsomatic.com', verify=False)
    external_ip = f.text
    return external_ip


if __name__ == '__main__':
    ret_egress_ip()
