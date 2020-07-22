# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import isodate

import googleapiclient.discovery

def util( videoID ):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAeL-Mh9eEnSqN5jguktWJzWd5p2QxmR2s"  #Replace your API Key here instead of this one.


    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.videos().list(
        part="contentDetails",
        id = videoID
    )
    response = request.execute()
    # print(response)
    # print(response['items'][0]['contentDetails']['duration'])
    if response['items']:
        return isodate.parse_duration(response['items'][0]['contentDetails']['duration']).seconds

    else:
        return 0
    # dur = isodate.parse_duration(response['items'][0]['contentDetails']['duration'])


    # print(type(dur.seconds))

    # return isodate.parse_duration(response['items'][0]['contentDetails']['duration']).seconds
    

