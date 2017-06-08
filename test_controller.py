#!/usr/bin/env python

import datetime
from dateutil.tz import tzutc
import json

from klair.controller import *

from kubernetes import client

class Response:
    def __init__(self, data):
        self.data = json.dumps(data)


def deserialize(data, model):
    return c.deserialize(Response(data), model)


c = client.ApiClient()

old_data = {
    "kind": "ImageStream",
    "apiVersion": "v1",
    "metadata": {
        "name": "php",
        "namespace": "mateus",
        "selfLink": "/oapi/v1/namespaces/mateus/imagestreams/php",
        "uid": "9559d677-4265-11e7-9e31-000d3ac02da0",
        "resourceVersion": "158159455",
        "generation": 1,
        "creationTimestamp": "2017-05-26T22:49:32Z",
        "labels": {
            "app": "php",
            "template": "php"
        },
        "annotations": {
            "getup.io/application-name": "php",
            "openshift.io/generated-by": "GetupCloudWebConsole"
        }
    },
    "spec": {},
    "status": {
        "dockerImageRepository": "172.30.34.145:5000/mateus/php",
        "tags": [
            {
                "tag": "latest",
                "items": [
                    {
                        "created": "2017-06-07T14:11:46Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:c899c26765a1314b1e0bae1cd2f0f3c743f0aae4dd0dbd3e1e05418b2b6539b3",
                        "image": "sha256:c899c26765a1314b1e0bae1cd2f0f3c743f0aae4dd0dbd3e1e05418b2b6539b3",
                        "generation": 1
                    },
                    {
                        "created": "2017-06-07T14:06:53Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:d965ff60b586866b8981ff0428411719fba53877689c34945f537989cabebc64",
                        "image": "sha256:d965ff60b586866b8981ff0428411719fba53877689c34945f537989cabebc64",
                        "generation": 1
                    },
                    {
                        "created": "2017-06-07T12:42:32Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:339b7afbede7c28a9003dc43be21326cb4a6906f1b853a7a47062a9c7eb69354",
                        "image": "sha256:339b7afbede7c28a9003dc43be21326cb4a6906f1b853a7a47062a9c7eb69354",
                        "generation": 1
                    },
                    {
                        "created": "2017-05-26T22:55:47Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:e4a67bf2cbc5483791120631db7eed4af10ae65467989d7f5c03b2eb8bdb56d5",
                        "image": "sha256:e4a67bf2cbc5483791120631db7eed4af10ae65467989d7f5c03b2eb8bdb56d5",
                        "generation": 1
                    }
                ]
            }
        ]
    }
}

new_data = {
    "kind": "ImageStream",
    "apiVersion": "v1",
    "metadata": {
        "name": "php",
        "namespace": "mateus",
        "selfLink": "/oapi/v1/namespaces/mateus/imagestreams/php",
        "uid": "9559d677-4265-11e7-9e31-000d3ac02da0",
        "resourceVersion": "158159455",
        "generation": 1,
        "creationTimestamp": "2017-05-26T22:49:32Z",
        "labels": {
            "app": "php",
            "template": "php"
        },
        "annotations": {
            "getup.io/application-name": "php",
            "openshift.io/generated-by": "GetupCloudWebConsole"
        }
    },
    "spec": {},
    "status": {
        "dockerImageRepository": "172.30.34.145:5000/mateus/php",
        "tags": [
            {
                "tag": "latest",
                "items": [
                    {
                        "created": "2017-06-07T14:15:58Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:f5534a0a882a7859acbae39c143af068806f33597bd1c6687b392298406aa55f",
                        "image": "sha256:f5534a0a882a7859acbae39c143af068806f33597bd1c6687b392298406aa55f",
                        "generation": 1
                    },
                    {
                        "created": "2017-06-07T14:11:46Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:c899c26765a1314b1e0bae1cd2f0f3c743f0aae4dd0dbd3e1e05418b2b6539b3",
                        "image": "sha256:c899c26765a1314b1e0bae1cd2f0f3c743f0aae4dd0dbd3e1e05418b2b6539b3",
                        "generation": 1
                    },
                    {
                        "created": "2017-06-07T14:06:53Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:d965ff60b586866b8981ff0428411719fba53877689c34945f537989cabebc64",
                        "image": "sha256:d965ff60b586866b8981ff0428411719fba53877689c34945f537989cabebc64",
                        "generation": 1
                    },
                    {
                        "created": "2017-06-07T12:42:32Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:339b7afbede7c28a9003dc43be21326cb4a6906f1b853a7a47062a9c7eb69354",
                        "image": "sha256:339b7afbede7c28a9003dc43be21326cb4a6906f1b853a7a47062a9c7eb69354",
                        "generation": 1
                    },
                    {
                        "created": "2017-05-26T22:55:47Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:e4a67bf2cbc5483791120631db7eed4af10ae65467989d7f5c03b2eb8bdb56d5",
                        "image": "sha256:e4a67bf2cbc5483791120631db7eed4af10ae65467989d7f5c03b2eb8bdb56d5",
                        "generation": 1
                    }
                ]
            },
            {
                "tag": "stable",
                "items": [
                    {
                        "created": "2017-06-07T14:06:53Z",
                        "dockerImageReference": "172.30.34.145:5000/mateus/php@sha256:d965ff60b586866b8981ff0428411719fba53877689c34945f537989cabebc64",
                        "image": "sha256:d965ff60b586866b8981ff0428411719fba53877689c34945f537989cabebc64",
                        "generation": 1
                    }
                ]
            }
        ]
    }
}

old = deserialize(old_data, client.models.V1ImageStream)
new = deserialize(new_data, client.models.V1ImageStream)


cr_data = {
    "api_version": "vulnerability.getup.io/v1",
    "kind": "ClairReport",
    "metadata": {
        "creation_timestamp": "2017-06-07T14:16:08Z",
        "uid": "6a343187-506c-11e7-b7f6-000d3ac04b9b"
    },
    "image_repository": "172.30.34.145:5000/pensatica/cdapreview",
    "image_stream_uid": "4ee012e7-bd3d-11e6-b4cc-000d3ac01d22",
    "layer_count": None,
    "notification_name": None,
    "status": None,
    "tags": [
        {
            "latest_image": "sha256:f5534a0a882a7859acbae39c143af068806f33597bd1c6687b392298406aa55f",
            "tag": "latest"
        },
        {
            "latest_image": "sha256:d965ff60b586866b8981ff0428411719fba53877689c34945f537989cabebc64",
            "tag": "stable"
        }
    ],
    "vulnerabilities": None
}

cr = deserialize(cr_data, client.models.V1ClairReport)

def test_imagestream_tags():
    global old

    tags = imagestream_tags(old)

    assert len(tags) == 1
    assert tags[0].tag == 'latest'


def test_imagestream_tag_docker_image_references():
    global old

    dirs = set((
        "172.30.34.145:5000/mateus/php@sha256:c899c26765a1314b1e0bae1cd2f0f3c743f0aae4dd0dbd3e1e05418b2b6539b3",
        "172.30.34.145:5000/mateus/php@sha256:d965ff60b586866b8981ff0428411719fba53877689c34945f537989cabebc64",
        "172.30.34.145:5000/mateus/php@sha256:339b7afbede7c28a9003dc43be21326cb4a6906f1b853a7a47062a9c7eb69354",
        "172.30.34.145:5000/mateus/php@sha256:e4a67bf2cbc5483791120631db7eed4af10ae65467989d7f5c03b2eb8bdb56d5",
    ))

    assert imagestream_tag_docker_image_references(old.status.tags[0]) == dirs


def test_imagestream_has_changed():
    global old, new

    assert imagestream_has_changed(old, old) == False
    assert imagestream_has_changed(old, new) == True


def test_imagestream_tags_by_name():
    global old, new

    assert set(imagestream_tags_by_name(old).keys()) == set(['latest',])
    assert set(imagestream_tags_by_name(new).keys()) == set(['latest', 'stable'])


def test_clairreport_tags_by_name():
    global cr

    assert set(clairreport_tags_by_name(cr)) == set(['latest', 'stable'])

print('-- Started test')
_locals = locals()
for name in filter(lambda n: callable(_locals[n]) and n.startswith('test_'), dir()):
    print('testing %s' % name)
    _locals[name]()
print('-- Finished test')
