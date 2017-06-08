import os
import json
import kubernetes
from kontroller import log
from . import controller, version, client

TPR_NAME = 'clair-report.vulnerability.getup.io'

import urllib3
urllib3.disable_warnings()

import inspect
for _name in dir(client.models):
    _attr = getattr(client.models, _name)
    if inspect.isclass(_attr) and not hasattr(kubernetes.client.models, _name):
        setattr(kubernetes.client.models, _name, _attr)


def create_third_party_resource():
    ext_v1beta1 = kubernetes.client.ExtensionsV1beta1Api()
    tpr = kubernetes.client.V1beta1ThirdPartyResource(
            description='Kubernetes Clair Vulnerability Report',
            metadata=kubernetes.client.V1ObjectMeta(
                name=TPR_NAME),
                versions=[kubernetes.client.V1beta1APIVersion(name='v1')])
    try:
        res = ext_v1beta1.create_third_party_resource(tpr)
        log('Created ThirdPartyResource %s' % TPR_NAME)
    except kubernetes.client.rest.ApiException as ex:
        if ex.status != 409 and ex.reason.lower() != 'conflict':
            raise
        log('ThirdPartyResource %s already exists' % TPR_NAME)


def main():
    log('Started Openshift Clair Controller {}'.format(version.CLAIR_CONTROLLER_VERSION))

    if 'SERVICE_TOKEN_FILENAME' in os.environ:
        kubernetes.config.incluster_config.InClusterConfigLoader(
                token_filename=os.environ.get('SERVICE_TOKEN_FILENAME'),
                cert_filename=os.environ.get('SERVICE_CERT_FILENAME')).load_and_set()
    else:
        kubernetes.config.load_incluster_config()

    kubernetes.client.configuration.verify_ssl = False

    create_third_party_resource()

    dockercfg_path = os.environ.get('DOCKERCFG_PATH', '/.docker/.dockercfg')
    with open(dockercfg_path, 'r') as df:
        dockercfg = json.load(df)

    kk = controller.ClairController(kubernetes.client, kubernetes.watch, dockercfg=dockercfg)
    kk.start()


if __name__ == '__main__':
    main()
