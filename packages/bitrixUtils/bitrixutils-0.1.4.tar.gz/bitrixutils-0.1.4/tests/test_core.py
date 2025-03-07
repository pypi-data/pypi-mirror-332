import sys
import os
from collections import defaultdict
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bitrixUtils')))
import core

# URL do webhook do Bitrix24
BITRIX_WEBHOOK_URL = "https://setup.bitrix24.com.br/rest/629/c0q6gqm7og1bs91k/"

campos = ["EMAIL", "PHONE"]
data = [
    [{"VALUE": "novo@email.com", "VALUE_TYPE": "WORK"}],
    [{"VALUE": "11999999999", "VALUE_TYPE": "WORK"}]
]
result = core.updateContactFields(BITRIX_WEBHOOK_URL, 3649, campos, data, LOG=True)
