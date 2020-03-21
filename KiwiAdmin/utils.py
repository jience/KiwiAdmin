import uuid
import random


class UUIDTools(object):
    """
    uuid function tools
    """

    @staticmethod
    def uuid1_hex():
        """
        return uuid1 hex string
        eg: 7e4e5ee86b2d11eab1c3f0761c156120
        :return: uuid hex
        """
        return uuid.uuid1().hex


def random_product_no():
    """
    return random 13 len number string for product number
    :return: string
    """
    return str(random.randint(1000000000000, 9999999999999))
