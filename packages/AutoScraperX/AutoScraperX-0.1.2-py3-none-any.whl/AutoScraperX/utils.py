# -*- encoding: utf-8 -*-
'''
file       :utils.py
Description:
Date       :2025/03/07 18:24:40
Author     :czy
version    :v0.01
email      :1060324818@qq.com
'''

import random
import uuid

def rm_space(text: str) -> str:
    return text.replace(" ", "").replace("\n", "").replace("\t", "")

def random_id(self):
        return ''.join(random.choices(uuid.uuid1().hex, k=6))