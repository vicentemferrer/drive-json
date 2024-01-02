# This file use client_secrets.json and settings.yaml to generate credentials_module.json.
#
# client_secrets.json is a generated file from Google Cloud console which contains the settings
# for OAuth client (client_secrets is a default name that PyDrive use, so you must rename once
# you got it)
#
# settings.yaml contains the settings you need to obtain credentials_module.json for catch
# props needed to use credentials refresh.

from pydrive2.auth import GoogleAuth

gauth = GoogleAuth()

gauth.LocalWebserverAuth()