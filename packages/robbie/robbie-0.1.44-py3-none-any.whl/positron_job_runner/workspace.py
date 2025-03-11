import zipfile
import os
import shutil
import re
from dataclasses import dataclass
from typing import List
from common.constants import FILE_SIZE_THRESHOLD
from positron_job_runner.runner_env import runner_env
from positron_job_runner.cloud_storage import cloud_storage
from positron_job_runner.cloud_logger import logger


EXCLUDED_DIRECTORIES = ['venv', '.venv', '.git', '__pycache__', 'job-execution', '.robbie', '.ipynb_checkpoints', 'persistent-disk']
S3_BASE_PATH = f"{runner_env.JOB_OWNER_EMAIL}/{runner_env.JOB_ID}"
S3_RESULT_PATH = f"{S3_BASE_PATH}/result"

def download_workspace_from_s3():
    """Download the workspace from S3"""
    s3_key = f"{S3_BASE_PATH}/workspace.zip"
    local_zip_path = os.path.join(runner_env.RUNNER_CWD, 'workspace.zip')
    cloud_storage.download_file(s3_key, local_zip_path)
    # the file may or may not exist

def copy_workspace_to_job_execution():
    """Copies the workspace from job-controller to job-execution"""
    local_zip_path = os.path.join(runner_env.RUNNER_CWD, 'workspace.zip')
    if os.path.exists(local_zip_path):
        destination_zip_path = os.path.join(runner_env.JOB_CWD, 'workspace.zip')
        print(f"Copying: {local_zip_path} to {destination_zip_path}")
        shutil.copy(local_zip_path, destination_zip_path)
        logger.debug(f"Copied workspace.zip to {destination_zip_path}")
    else:
        logger.error("Workspace zip not found")

def upload_results_to_s3():
    """Uploads the results to S3"""
    try:
        logger.info('Copying results to cloud storage...')

        results_dir = runner_env.JOB_CWD
        os.makedirs(results_dir, exist_ok=True)

        ignore_file_path = os.path.join(runner_env.JOB_CWD, ".robbieignore")
        exclude_regex = []
        try:
            with open(ignore_file_path, "r") as f:
                exclude_regex = f.read().splitlines()
        except FileNotFoundError:
            logger.debug("No .robbieignore file found")

        logger.debug(f"ignore_name_patterns: {exclude_regex}")

        result_files = get_file_paths(
            path=results_dir, 
            excluded_dirs=EXCLUDED_DIRECTORIES,
            exclude_regex=exclude_regex
        )

        # Create a zip of the result directory
        results_zip_file_name = f"{results_dir}/result.zip"
        with zipfile.ZipFile(results_zip_file_name, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in result_files:
                zipf.write(file.full_path, arcname=file.name)
                s3_key = f"{S3_RESULT_PATH}/{file.name}"
                cloud_storage.upload_file(file.full_path, s3_key)

        file_size = os.path.getsize(results_zip_file_name)
        if (file_size >= FILE_SIZE_THRESHOLD):
            size_in_mb = round(file_size / (1024 * 1024), 2)
            logger.warning(f"Results Archive Size: {size_in_mb} Mb. It might take a long time to upload it.")

        logger.debug(f"Uploading to cloud storage: {results_zip_file_name}")
        cloud_storage.upload_file(results_zip_file_name, f"{S3_RESULT_PATH}/result.zip")

        logger.info('Results uploaded to S3 successfully')

    except Exception as e:
        logger.error(f"Failed to upload results to S3: {e}")


@dataclass
class FileEntry:
    full_path: str
    name: str
    size: int

def get_file_paths(
    path: str, 
    excluded_dirs: List[str], 
    excluded_files: List[str] = [],
    exclude_regex: List[str] = []
) -> List[FileEntry]:
    """
    Get the file paths:

    path: str: The path to search
    excluded_dirs: List[str]: The directories to exclude (internal use)
    excluded_files: List[str]: The files to exclude (internal use)
    exclude_regex: List[str]: The regex to exclude that applies to files and dirs at the top level (user defined)

    """
    top_level = True
    all_files: List[FileEntry] = []
    for root, dirs, files in os.walk(path):
        # make a copy of the interable to avoid modifying it while iterating
        dirs_copy = dirs[:]
        for dir in dirs_copy:
            # exclude the directories
            if dir in excluded_dirs:
                dirs.remove(dir)   
                continue
            # if we are in the top level, check for the regex
            if top_level:
                for pattern in exclude_regex: 
                    if re.match(pattern, dir):
                        dirs.remove(dir)
                        break
        for file in files:
            ignore = False
            if file in excluded_files:
                continue
            if top_level:
                for pattern in exclude_regex:
                    if re.match(pattern, file):
                        ignore = True
            if not ignore:
                full_path = os.path.join(root, file)
                file_size = os.path.getsize(full_path)
                rel_path = os.path.relpath(full_path, path)
                all_files.append(FileEntry(name=rel_path, size=file_size, full_path=full_path))
        top_level = False
    return all_files

