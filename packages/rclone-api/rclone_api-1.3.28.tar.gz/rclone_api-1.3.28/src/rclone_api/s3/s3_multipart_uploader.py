import _thread
import os
import traceback
import warnings
from concurrent.futures import Future, ThreadPoolExecutor
from pathlib import Path
from queue import Queue
from threading import Event, Thread
from typing import Any, Callable

from botocore.client import BaseClient

from rclone_api.mount_read_chunker import FilePart
from rclone_api.s3.chunk_task import S3FileInfo, file_chunker
from rclone_api.s3.chunk_types import (
    FinishedPiece,
    UploadInfo,
    UploadState,
)
from rclone_api.s3.types import MultiUploadResult
from rclone_api.types import EndOfStream
from rclone_api.util import locked_print


class S3MultiPartUploader:

    def __init__(s3_client: BaseClient, bucket_name: str, object_name: str, chunk_size: int, file_size: int):
        pass