"""Adapted from <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html>."""

from pathlib import Path

import boto3


def upload_to_s3(file_loc: Path, bucket: str) -> None:
    """Upload `file_loc` to S3 `bucket`."""
    s3 = boto3.client("s3")
    with open(file_loc, "rb") as f:
        s3.upload_fileobj(f, bucket, file_loc.name)
