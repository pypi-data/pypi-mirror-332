#!/usr/bin/env python3
# -*- coding: latin-1 -*-
"""Collect AWS SSO Permission Set assignment data from multiple accounts."""

from . import helper_aws_sso
from . import helper_common
from . import helper_aws_entrypoint
from .helper_parameters import *  # NOQA
from multithreader import threads


def aws_sso_get():
    """Collect AWS SSO Permission Set assignment data."""
    # Enter AWS environment.
    session = helper_aws_entrypoint.auth(
        auth_method=auth_method,
        profile_name=profile_name,
        access_key_id=access_key_id,
        secret_access_key=secret_access_key,
        sso_url=sso_url,
        sso_role_name=sso_role_name,
        sso_account_id=sso_account_id
    )
    account_ids = helper_aws_entrypoint.crawler(
        session,
        accounts_list_src,
        accounts,
        ou,
        statuses
    )
    sso_admin = session.client(
        'sso-admin',
        region_name=region
    )
    identity_store = session.client(
        'identitystore',
        region_name=region
    )

    # Execute task with multithreading.
    items = {
        'sso_admin': sso_admin,
        'identity_store': identity_store,
        'sso_instance_arn': sso_instance_arn,
        'identity_store_id': identity_store_id
    }
    results = threads(
        helper_aws_sso.get_permission_sets,
        account_ids,
        items,
        thread_num=THREAD_NUM
    )

    # Write results to file.
    helper_common.write_json_obj(
        sso_get_output_file,
        results
    )


def main():
    """Execute main function."""
    aws_sso_get()


if __name__ == '__main__':
    main()
