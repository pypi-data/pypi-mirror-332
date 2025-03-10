import requests
from typing import Literal, Optional

# Định nghĩa các function có trong file tc1.txt
TC1_STATE = [
        "main", "main_mes", "virtualinputs", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "previz", "strip1", "strip2", "strip3", "strip4", 
        "main_background", "virtualinputs_background", "v1_background", "v2_background", "v3_background", "v4_background", "v5_background", "v6_background", "v7_background", "v8_background", "previz_background", 
        "main_dsk1", "main_mes_dsk1", "virtualinputs_dsk1", "v1_dsk1", "v2_dsk1", "v3_dsk1", "v4_dsk1", "v5_dsk1", "v6_dsk1", "v7_dsk1", "v8_dsk1", "previz_dsk1", 
        "main_dsk2", "main_mes_dsk2", "virtualinputs_dsk2", "v1_dsk2", "v2_dsk2", "v3_dsk2", "v4_dsk2", "v5_dsk2", "v6_dsk2", "v7_dsk2", "v8_dsk2", "previz_dsk2", 
        "main_dsk3", "main_mes_dsk3", "virtualinputs_dsk3", "v1_dsk3", "v2_dsk3", "v3_dsk3", "v4_dsk3", "v5_dsk3", "v6_dsk3", "v7_dsk3", "v8_dsk3", "previz_dsk3", 
        "main_dsk4", "main_mes_dsk4", "virtualinputs_dsk4", "v1_dsk4", "v2_dsk4", "v3_dsk4", "v4_dsk4", "v5_dsk4", "v6_dsk4", "v7_dsk4", "v8_dsk4", "previz_dsk4", 
        "main_ftb", "main_mes_ftb", "virtualinputs_ftb", "v1_ftb", "v2_ftb", "v3_ftb", "v4_ftb", "v5_ftb", "v6_ftb", "v7_ftb", "v8_ftb", "previz_ftb", "main_fx", "main_output2"
    ]

def tc1_control(
    ip: str,
    state: Literal[
        "main", "main_mes", "virtualinputs", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "previz", "strip1", "strip2", "strip3", "strip4", 
        "main_background", "virtualinputs_background", "v1_background", "v2_background", "v3_background", "v4_background", "v5_background", "v6_background", "v7_background", "v8_background", "previz_background", 
        "main_dsk1", "main_mes_dsk1", "virtualinputs_dsk1", "v1_dsk1", "v2_dsk1", "v3_dsk1", "v4_dsk1", "v5_dsk1", "v6_dsk1", "v7_dsk1", "v8_dsk1", "previz_dsk1", 
        "main_dsk2", "main_mes_dsk2", "virtualinputs_dsk2", "v1_dsk2", "v2_dsk2", "v3_dsk2", "v4_dsk2", "v5_dsk2", "v6_dsk2", "v7_dsk2", "v8_dsk2", "previz_dsk2", 
        "main_dsk3", "main_mes_dsk3", "virtualinputs_dsk3", "v1_dsk3", "v2_dsk3", "v3_dsk3", "v4_dsk3", "v5_dsk3", "v6_dsk3", "v7_dsk3", "v8_dsk3", "previz_dsk3", 
        "main_dsk4", "main_mes_dsk4", "virtualinputs_dsk4", "v1_dsk4", "v2_dsk4", "v3_dsk4", "v4_dsk4", "v5_dsk4", "v6_dsk4", "v7_dsk4", "v8_dsk4", "previz_dsk4", 
        "main_ftb", "main_mes_ftb", "virtualinputs_ftb", "v1_ftb", "v2_ftb", "v3_ftb", "v4_ftb", "v5_ftb", "v6_ftb", "v7_ftb", "v8_ftb", "previz_ftb", "main_fx", "main_output2"
    ],
    function: Literal["auto", "auto_directional", "reversed_auto", "take", "take_directional", "up", "down", "up_fast", "down_fast", "goto_halfway", "goto_top", "goto_bottom", "tbar_speed", "value", "toggle_reverse", "toggle_autoreverse", "select_index", "select_next", "select_prev", "select_fade"]
):
    """
    Gửi HTTP request đến TriCaster TC1.
    
    :param ip: Địa chỉ IP của TriCaster TC1.
    :param state: Trạng thái của hệ thống.
    :param function: Hàm điều khiển được hỗ trợ.
    :param value: Giá trị cho function nếu có.
    """
    if state not in TC1_STATE:
        return {"status": "error", "message": f"Hàm '{state}' không được hỗ trợ."}
    
    # Xây dựng URL
    url = f'http://{ip}/v1/shortcut?name={state}_{function}'
    
    
    try:
        # Gửi yêu cầu HTTP
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return {"status": "success", "message": "Lệnh đã được gửi thành công."}
        else:
            return {"status": "error", "message": f"Lỗi HTTP {response.status_code}."}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

def tc1_macro(ip: str, macro_name: str):
    """
    Gửi HTTP request để chạy macro trên TriCaster TC1.
    
    :param ip: Địa chỉ IP của TriCaster TC1.
    :param macro_name: Tên macro cần chạy.
    """
    url = f'http://{ip}/v1/trigger?name={macro_name}'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return {"status": "success", "message": "Macro đã được chạy thành công."}
        else:
            return {"status": "error", "message": f"Lỗi HTTP {response.status_code}."}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}
