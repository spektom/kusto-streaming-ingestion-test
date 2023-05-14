kusto-streaming-ingestion-test
===============================

Example of streaming data into Kusto cluster in Python.

## Pre-requisites

1. Create a [Kusto cluster](https://kusto.io), a database and a table to stream the data into. Don't forget to enable [streaming ingestion](https://learn.microsoft.com/en-us/azure/data-explorer/ingest-data-streaming) for your cluster.

2. Register an [Azure app](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app). Just give it a name with no additional details like redirect URI, etc.

3. Allow your App to write to Kusto.

First, find 'Application (client) ID' and 'Directory (tenant) ID' GUIDs under 'Overview' page of your registered application in Azure.

Then, run the following command in your Kusto cluster:

```
.add table <YourTable> ingestors (@'aadapp=<Application (client) ID>;Directory (tenant) ID>') '<Your application name>'
```

## Running the data streaming app

### Configuration

1. Setup Python virtual environment

```
python3 -mvenv venv
pip install -r requirements.txt
```

2. Copy `config.ini.template` to `config.ini` and fill-in all the details about your Kusto cluster, database, table and the app.

### Running

```
./send_empty_record.py
```
