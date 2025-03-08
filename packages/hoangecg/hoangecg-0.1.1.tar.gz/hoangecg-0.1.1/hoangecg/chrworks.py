import requests
import json
from typing import Literal, Optional, List

# Định nghĩa các hàm CHRWorks và tham số yêu cầu
CHRWORKS_ACTION = {
    "list_motions": [],
    "list_motions_with_ids": [],
    "list_layers": ["parent", "parent_id", "channel"],
    "play_motions": ["motions", "channel"],
    "stop_motions": ["motions", "channel"],
    "finish_motions": ["motions", "channel"],
    "pause_motions": ["motions", "channel"],
    "resume_motions": ["motions", "channel"],
    "restart_motions": ["motions", "channel"],
    "finish_and_restart_motions": ["motions", "channel"],
    "set_text": ["layer", "layer_id", "value", "channel"],
    "list_grid_names": [],
    "list_grid_cells": ["grid"],
    "activate_grid_cell": ["grid", "cell", "channel"],
    "run_data_source_query": ["data_source"],
    "set_data_source_query_parameter": ["data_source", "parameter", "value"],
    "select_data_source_rows": ["data_source", "index_list", "field", "value"]
}

headers = {'Content-type': 'application/json'}

def chrworks_control(
    ip: str, 
    action: Literal[
        "list_motions", "list_motions_with_ids", "list_layers", "play_motions", "stop_motions", "finish_motions",
        "pause_motions", "resume_motions", "restart_motions", "finish_and_restart_motions", "set_text", "list_grid_names",
        "list_grid_cells", "activate_grid_cell", "run_data_source_query", "set_data_source_query_parameter", "select_data_source_rows"
    ], 
    port: int = 5201,
    motions: Optional[List[str]] = None,
    channel: Optional[str] = None,
    **kwargs
):
    if action not in CHRWORKS_ACTION:
        return {"status": "error", "message": f"Hàm '{action}' không được hỗ trợ."}

    # Kiểm tra các tham số bắt buộc
    required_params = CHRWORKS_ACTION[action]
    data_cw = {"action": action}
    
    for param in required_params:
        if param in kwargs:
            data_cw[param] = kwargs[param]
    
    # Thêm motions nếu có
    if motions:
        data_cw["motions"] = motions
    
    # Thêm channel nếu có
    if channel:
        data_cw["channel"] = channel
    
    url = f'http://{ip}:{port}/'
    try:
        # Gửi yêu cầu HTTP POST đến CHRWorks
        response = requests.post(url, data=json.dumps(data_cw), headers=headers, timeout=5)
        
        if response.status_code == 200:
            return {"status": "success", "message": "Lệnh đã được gửi thành công.", "response": response.json()}
        else:
            return {"status": "error", "message": f"Lỗi HTTP {response.status_code}.", "response": response.text}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}
