import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive"]


def get_drive_service(credentials_path=None):
    credentials_path = credentials_path or os.getenv("GOOGLE_DRIVE_CREDENTIALS", "credentials.json")
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=SCOPES
    )
    return build("drive", "v3", credentials=credentials)


def upload_folder(local_path, drive_folder_id, service=None):
    service = service or get_drive_service()
    uploaded_ids = {}

    for filename in os.listdir(local_path):
        file_path = os.path.join(local_path, filename)
        if not os.path.isfile(file_path):
            continue

        existing = service.files().list(
            q=f"name='{filename}' and '{drive_folder_id}' in parents and trashed=false",
            fields="files(id)",
        ).execute().get("files", [])

        media = MediaFileUpload(file_path, resumable=True)

        if existing:
            file_id = existing[0]["id"]
            service.files().update(fileId=file_id, media_body=media).execute()
        else:
            metadata = {"name": filename, "parents": [drive_folder_id]}
            created = service.files().create(body=metadata, media_body=media, fields="id").execute()
            file_id = created["id"]

        uploaded_ids[filename] = file_id

    return uploaded_ids


def download_folder(drive_folder_id, local_path, service=None):
    service = service or get_drive_service()
    os.makedirs(local_path, exist_ok=True)

    results = service.files().list(
        q=f"'{drive_folder_id}' in parents and trashed=false",
        fields="files(id, name)",
    ).execute()

    for file_info in results.get("files", []):
        request = service.files().get_media(fileId=file_info["id"])
        target_path = os.path.join(local_path, file_info["name"])

        with io.FileIO(target_path, "wb") as target_file:
            downloader = MediaIoBaseDownload(target_file, request)
            done = False
            while not done:
                _, done = downloader.next_chunk()

    return local_path
