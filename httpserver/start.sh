#! /bin/sh

QSERVER_HTTP_SERVER_CONFIG=config.yml uvicorn --host 0.0.0.0 --port 60610 bluesky_httpserver.server:app

#uvicorn --port 60610 --host 0.0.0.0 bluesky_queueserver.server.server:app
