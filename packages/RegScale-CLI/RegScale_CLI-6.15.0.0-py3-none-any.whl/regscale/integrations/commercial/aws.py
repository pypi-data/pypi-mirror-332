#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RegScale AWS Audit Manager Integration"""

import datetime
import os
from typing import Optional

import click

from regscale.core.app.logz import create_logger
from regscale.integrations.commercial.amazon.common import sync_aws_findings
from regscale.models.integration_models.flat_file_importer import FlatFileImporter

logger = create_logger()


# Create group to handle AWS integration
@click.group()
def aws():
    """AWS Integrations"""


@aws.group(help="Sync AWS Inspector Scans to RegScale.")
def inspector():
    """Sync AWS Inspector scans."""


@aws.command(name="sync_findings")
@click.option(
    "--regscale_ssp_id",
    type=click.INT,
    required=True,
    prompt="Enter RegScale System Security Plan ID",
    help="The ID number from RegScale of the System Security Plan",
)
@click.option(
    "--create_issue",
    type=click.BOOL,
    required=False,
    help="Create Issue in RegScale from vulnerabilities in AWS Security Hub.",
    default=False,
)
@click.option(
    "--aws_access_key_id",
    "--key_id",
    type=click.STRING,
    required=False,
    help="AWS Access Key ID",
    default=os.environ.get("AWS_ACCESS_KEY_ID"),
)
@click.option(
    "--aws_secret_access_key",
    "--key",
    type=click.STRING,
    required=False,
    help="AWS Secret Access Key",
    default=os.environ.get("AWS_SECRET_ACCESS_KEY"),
)
# noqa: E402
def sync_findings(
    regscale_ssp_id: int,
    create_issue: bool = False,
    aws_access_key_id: str = os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key: str = os.environ.get("AWS_SECRET_ACCESS_KEY"),
) -> None:
    """Sync AWS Security Hub Findings."""
    sync_aws_findings(regscale_ssp_id, create_issue, aws_access_key_id, aws_secret_access_key)


FlatFileImporter.show_mapping(
    group=inspector,  # type: ignore
    import_name="aws_inspector",
)


@inspector.command(name="import_scans")
@FlatFileImporter.common_scanner_options(
    message="File path to the folder containing AWS Inspector files to process to RegScale.",
    prompt="File path for AWS Inspector files (CSV or JSON)",
    import_name="aws_inspector",
)
def import_scans(
    folder_path: os.PathLike[str],
    regscale_ssp_id: int,
    scan_date: datetime,
    mappings_path: click.Path,
    disable_mapping: bool,
    s3_bucket: str,
    s3_prefix: str,
    aws_profile: str,
    upload_file: Optional[bool] = True,
) -> None:
    """
    Import AWS Inspector scans to a System Security Plan in RegScale as assets and vulnerabilities.
    """
    import_aws_scans(
        folder_path=folder_path,
        regscale_ssp_id=regscale_ssp_id,
        scan_date=scan_date,
        mappings_path=mappings_path,
        disable_mapping=disable_mapping,
        s3_bucket=s3_bucket,
        s3_prefix=s3_prefix,
        aws_profile=aws_profile,
        upload_file=upload_file,
    )


def import_aws_scans(
    folder_path: os.PathLike[str],
    regscale_ssp_id: int,
    mappings_path: click.Path,
    scan_date: datetime,
    s3_bucket: str,
    s3_prefix: str,
    aws_profile: str,
    disable_mapping: Optional[bool] = False,
    upload_file: Optional[bool] = True,
) -> None:
    """
    Function to import AWS Inspector scans to RegScale as assets and vulnerabilities

    :param os.PathLike[str] folder_path: Path to the folder containing AWS Inspector files
    :param int regscale_ssp_id: RegScale System Security Plan ID
    :param datetime.date scan_date: Date of the scan
    :param click.Path mappings_path: Path to the header mapping file
    :param str s3_bucket: The S3 bucket to download the files from
    :param str s3_prefix: The S3 prefix to download the files from
    :param str aws_profile: The AWS profile to use for S3 access
    :param bool disable_mapping: Disable header mapping
    :param bool upload_file: Upload the file to RegScale after processing, defaults to True
    :rtype: None
    """
    from regscale.models.integration_models.amazon_models.inspector_scan import InspectorScan

    FlatFileImporter.import_files(
        import_type=InspectorScan,
        import_name="AWS Inspector",
        file_types=[".csv", ".json"],
        folder_path=folder_path,
        regscale_ssp_id=regscale_ssp_id,
        scan_date=scan_date,
        mappings_path=mappings_path,
        disable_mapping=disable_mapping,
        s3_bucket=s3_bucket,
        s3_prefix=s3_prefix,
        aws_profile=aws_profile,
        upload_file=upload_file,
    )
