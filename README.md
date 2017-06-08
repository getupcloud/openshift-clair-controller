Openshift Clair Controller
==========================

> This is an experimental project. Expect bugs...

Scans [Openshift ImageStream](https://github.com/openshift/origin/) tags for known vulnerabilities using [CoreOS/Clair](https://github.com/coreos/clair).

Clair Controller listens for specific ImageStream objects updates and runs a vulnerability scan using internal Clair server. When something is found, a new
`ClairReport` object is created for that single ImageStream.


Installing
----------

Create a new project `clair-controller`:

```
$ oc new-project clair-controller
$ oc project clair-controller
```

Give permission for `clair` service account to interact with Openshift API:

```
$ oc create serviceaccount clair
$ oadm policy add-cluster-role-to-user cluster-admin system:serviceaccount:clair-controller:clair
```

Find out what's the name for docker secret of clair serviceaccount:

```
$ oc describe sa/clair
Name:       clair
Namespace:  clair-controller
Labels:     <none>

Image pull secrets: clair-dockercfg-sj8ul

Mountable secrets:  clair-token-lilv8
                    clair-dockercfg-sj8ul        <---- copy this name

Tokens:             clair-token-lilv8
                    clair-token-ozut5

```

Deploy the components:

```
$ oc process \
    -e CLAIR_DOCKERCFG_SECRET_NAME=clair-dockercfg-XXXXX \
    -f https://raw.githubusercontent.com/getupcloud/openshift-clair-controller/master/contrib/clair-controller.yaml \
  | oc create -f -
```


Scanning ImageStreams
---------------------

ClairController listens for changes in ImageStreams tagged with `vulnerability.getup.io/clairreport: active`.
Enable scanning on a given ImageStream running:

```
$ oc labels imagestream/myapp vulnerability.getup.io/clairreport=active
```

After build completes, a new `ClairReport` object is created/updated inside the ImageStream's namespace.
Each ImageStream tag will create a corresponding item in `tags[]`

```
$ oc get clairreports
NAME      KIND
myapp     ClairReport.v1.vulnerability.getup.io

$ oc get clairreports/myapp -o yaml
apiVersion: vulnerability.getup.io/v1
imageRepository: 172.30.34.145:5000/mateus/myapp
kind: ClairReport
metadata:
  creationTimestamp: 2017-07-04T21:43:41Z
  name: myapp
  namespace: mateus
  resourceVersion: "168653528"
  selfLink: /apis/vulnerability.getup.io/v1/namespaces/mateus/clairreports/myapp
  uid: d862b964-6101-11e7-9e40-000d3ac02da0
ownerReferences:
- apiVersion: v1
  controller: false
  kind: ImageStream
  name: myapp
  uid: 9559d677-4265-11e7-9e31-000d3ac02da0
status: Done
tags:
- creationTimestamp: 2017-07-04T21:43:40.636093
  latestImage: sha256:715cdec3c82bc03301e23f484e2dcbedd3594ba9fac7c5f21e4e50918f8918d4
  layerCount: 27
  tag: latest
  vulnerabilities:
  - description: 'Fontconfig is designed to locate fonts within the system and select
      them according to requirements specified by applications. Security Fix(es):
      * It was found that cache files were insufficiently validated in fontconfig.
      A local attacker could create a specially crafted cache file to trigger arbitrary
      free() calls, which in turn could lead to arbitrary code execution. (CVE-2016-5384)
      Red Hat would like to thank Tobias Stoeckmann for reporting this issue. Additional
      Changes: For detailed information on changes in this release, see the Red Hat
      Enterprise Linux 7.3 Release Notes linked from the References section.'
    fixedBy: 0:2.10.95-10.el7
    link: https://rhn.redhat.com/errata/RHSA-2016-2601.html
    name: RHSA-2016:2601
    namespaceName: centos:7
    severity: Medium
  - description: 'Network Security Services (NSS) is a set of libraries designed to
      support the cross-platform development of security-enabled client and server
      applications. The nss-util packages provide utilities for use with the Network
      Security Services (NSS) libraries. The following packages have been upgraded
      to a newer upstream version: nss (3.28.4), nss-util (3.28.4). Security Fix(es):
      * An out-of-bounds write flaw was found in the way NSS performed certain Base64-decoding
      operations. An attacker could use this flaw to create a specially crafted certificate
      which, when parsed by NSS, could cause it to crash or execute arbitrary code,
      using the permissions of the user running an application compiled against the
      NSS library. (CVE-2017-5461) Red Hat would like to thank the Mozilla project
      for reporting this issue. Upstream acknowledges Ronald Crane as the original
      reporter.'
    fixedBy: 0:3.28.4-1.0.el7_3
    link: https://access.redhat.com/errata/RHSA-2017:1100
    name: RHSA-2017:1100
    namespaceName: centos:7
    severity: Critical
  - description: 'Network Security Services (NSS) is a set of libraries designed to
      support the cross-platform development of security-enabled client and server
      applications. The nss-util packages provide utilities for use with the Network
      Security Services (NSS) libraries. The following packages have been upgraded
      to a newer upstream version: nss (3.21.3), nss-util (3.21.3). Security Fix(es):
      * Multiple buffer handling flaws were found in the way NSS handled cryptographic
      data from the network. A remote attacker could use these flaws to crash an application
      using NSS or, possibly, execute arbitrary code with the permission of the user
      running the application. (CVE-2016-2834) * A NULL pointer dereference flaw was
      found in the way NSS handled invalid Diffie-Hellman keys. A remote client could
      use this flaw to crash a TLS/SSL server using NSS. (CVE-2016-5285) * It was
      found that Diffie Hellman Client key exchange handling in NSS was vulnerable
      to small subgroup confinement attack. An attacker could use this flaw to recover
      private keys by confining the client DH key to small subgroup of the desired
      group. (CVE-2016-8635) Red Hat would like to thank the Mozilla project for reporting
      CVE-2016-2834. The CVE-2016-8635 issue was discovered by Hubert Kario (Red Hat).
      Upstream acknowledges Tyson Smith and Jed Davis as the original reporter of
      CVE-2016-2834.'
    fixedBy: 0:3.21.3-1.1.el7_3
    link: https://rhn.redhat.com/errata/RHSA-2016-2779.html
    name: RHSA-2016:2779
    namespaceName: centos:7
    severity: Medium
```

Developing
----------

There are two important scripts in this repository:

### scripts/build-and-release.sh

Creates a new pypi-suitable python package and uploads it. Before building, make sure to update `PACKAGE_VERSION` from `scripts/constants.py`.

> You must be logged in [pypi](pypi.python.org) in order for upload to succeed.

### scripts/build-image.sh

Creates a new local docker image using the newest pypi claircontroller package.

