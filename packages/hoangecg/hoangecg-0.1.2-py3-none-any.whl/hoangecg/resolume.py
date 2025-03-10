import requests
from typing import Optional
import json

def resolume_check_colum(
    ip: str,
    port: int = 8080,
    colum: int = 0
):
    try:
        url = f"http://{ip}:{port}/api/v1/composition/columns/{colum}"
        # Gửi yêu cầu HTTP đến vMix
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            res = response.json()
            return res['connected']['value']
        else:
            return {"status": "error", "message": f"Lỗi HTTP {response.status_code}."}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}