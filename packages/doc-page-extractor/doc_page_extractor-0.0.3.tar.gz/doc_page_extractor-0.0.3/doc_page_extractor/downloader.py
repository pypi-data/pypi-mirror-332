import os
import requests
from pathlib import Path


def download(url: str, file_path: Path):
  response = requests.get(url, stream=True, timeout=60)
  try:
    with open(file_path, "wb") as file:
      file.write(response.content)
  except Exception as e:
    os.remove(file_path)
    raise e
