#!/usr/bin/env python3

import configparser
import pathlib

from io import StringIO

from azure.kusto.data import (
    KustoConnectionStringBuilder,
    DataFormat,
)

from azure.kusto.ingest import (
    IngestionProperties,
    KustoStreamingIngestClient,
)

_conf = None

def read_conf():
    global _conf
    if _conf is None:
        _conf = configparser.ConfigParser()
        _conf.read(pathlib.Path(__file__).resolve().parent / "config.ini")
    return _conf

def get_conf(name):
    return read_conf()["DEFAULT"][name]


csb = KustoConnectionStringBuilder.with_aad_application_key_authentication(
    get_conf("KUSTO_CLUSTER_URL"), get_conf("APP_CLIENT_ID"), get_conf("APP_SECRET_KEY"), get_conf("APP_TENANT_ID")
)
client = KustoStreamingIngestClient(csb)

ingestionProperties = IngestionProperties(
    database=get_conf("KUSTO_DATABASE_NAME"), table=get_conf("KUSTO_TABLE_NAME"), data_format=DataFormat.CSV
)

csv_record = "foo,bar"
client.ingest_from_stream(StringIO(csv_record), ingestion_properties=ingestionProperties)
