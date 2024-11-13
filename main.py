import os
from fastapi import FastAPI, Response, UploadFile, File
from io import BytesIO
from zipfile import ZipFile

app = FastAPI()


@app.get("/download/{folder}")
async def download_directory(folder: str):
    """
    Endpoint to allow clients to download an entire directory as a ZIP file.

    Parameters:
    folder (str): The name of the folder to be downloaded.

    Returns:
    The directory contents as a ZIP file.
    """
    # Specify the base directory where the folders are stored
    base_dir = "/path/"
    #get current base directory
    base_dir = os.getcwd()
    print(base_dir)
    # Construct the full directory path
    dir_path = os.path.join(base_dir, folder)

    # Check if the directory exists
    if not os.path.isdir(dir_path):
        return {"error": "Directory not found"}, 404

    # Create a ZIP file in-memory
    zip_buffer = BytesIO()
    with ZipFile(zip_buffer, "w") as zip_file:
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, dir_path))

    # Set the ZIP file as the response content
    zip_buffer.seek(0)
    return Response(
        content=zip_buffer.read(),
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename={folder}.zip"},
    )

@app.get("/download/{folder}/{file}")
async def download_file(folder: str, file: str):

    base_dir=os.getcwd()
    file_path = os.path.join(base_dir, folder, file)

    # Check if the file exists
    if not os.path.isfile(file_path):
        return {"error": "File not found"}, 404

    return Response(
        content=open(file_path, "rb").read(),
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={file}"},
    )

# @app.post("/upload/{folder}/{file}")
# async def upload_file(folder: str, file: UploadFile = File(...)):
#     base_dir = "/path/"
#     file_path = os.path.join(base_dir, folder, file.filename)

#     with open(file_path, "wb") as f:
#         f.write(file.file.read())

#     return {"message": "File uploaded successfully"}

# @app.get("/allfiles")
# async def get_all_files():
#     base_dir = "/path/"
#     files = []
#     for root, _, filenames in os.walk(base_dir):
#         for filename in filenames:
#             files.append(os.path.relpath(os.path.join(root, filename), base_dir))
#     return {"files": files}


@app.get('/files/{folder}')
async def get_files(folder: str):
    base_dir = "/path/"
    base_dir = os.getcwd()
    dir_path = os.path.join(base_dir, folder)
    print(base_dir)
    files = []
    dir_path = os.path.join(base_dir, folder)

    # Check if the directory exists
    if not os.path.isdir(dir_path):
        return {"error": "Directory not found"}, 404
    for root, _, filenames in os.walk(dir_path):
        for filename in filenames:
            files.append(os.path.relpath(os.path.join(root, filename), dir_path))
    return { "\n".join(files)}
