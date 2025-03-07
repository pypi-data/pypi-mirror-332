import os
import json
import requests

BASE_URL: str = "https://poweroperator.com"


def upload_mark_with_file(
    user,
    item,
    file_path,
    hostname,
    argv,
    environ,
    cwd,
):
    """Upload benchmark data to /api/mark endpoint"""
    endpoint = f"{BASE_URL}/api/mark"
    form_data = {
        "user": user,
        "item": item,
        "hostname": hostname,
        "cwd": cwd,
    }

    if isinstance(argv, list):
        form_data["argv"] = " ".join(str(arg) for arg in argv)
    else:
        form_data["argv"] = str(argv)

    if isinstance(environ, dict):
        form_data["environ"] = " ".join(f"{key}={value}" for key, value in environ)
    else:
        form_data["environ"] = str(environ)

    # print(f"[poweroperator] Sending POST request to {endpoint} with form data and file")
    # print(f"[poweroperator] Form data: {json.dumps(form_data, indent=2)}")

    files = {}
    if file_path and os.path.exists(file_path):
        files = {"file": open(file_path, "rb")}
    else:
        raise ValueError(f"No file provided or file not found: {file_path}")

    try:
        response = requests.post(endpoint, data=form_data, files=files)
        if response.status_code != 200:
            print(f"[poweroperator] Status Code: {response.status_code}")
            print(f"[poweroperator] Response: {response.text}")
            try:
                response_json = response.json()
                print(
                    f"[poweroperator] Response: {response.status_code} {json.dumps(response_json, indent=2)}"
                )
            except json.JSONDecodeError:
                raise Exception(
                    f"Response was not valid JSON: {response.status_code} {response}"
                )
        # Close file if opened
        if "file" in files and files["file"]:
            files["file"].close()
    except requests.exceptions.RequestException as e:
        if "file" in files and files["file"]:
            files["file"].close()
        raise e
