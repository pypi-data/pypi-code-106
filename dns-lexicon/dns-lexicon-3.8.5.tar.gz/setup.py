# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lexicon', 'lexicon.providers', 'lexicon.tests', 'lexicon.tests.providers']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4',
 'cryptography>=2',
 'pyyaml>=3',
 'requests>=2',
 'tldextract>=2']

extras_require = \
{'ddns': ['dnspython>=2'],
 'full': ['boto3>=1', 'localzone>=0.9.8', 'softlayer>=5', 'zeep>=3', 'oci>=2'],
 'gransy': ['zeep>=3'],
 'localzone': ['localzone>=0.9.8'],
 'oci': ['oci>=2'],
 'route53': ['boto3>=1'],
 'softlayer': ['softlayer>=5'],
 'transip': ['transip>=2']}

entry_points = \
{'console_scripts': ['lexicon = lexicon.cli:main']}

setup_kwargs = {
    'name': 'dns-lexicon',
    'version': '3.8.5',
    'description': 'Manipulate DNS records on various DNS providers in a standardized/agnostic way',
    'long_description': '============\n|logo_named|\n============\n\nManipulate DNS records on various DNS providers in a standardized/agnostic way.\n\n|build_status| |coverage_status| |docker_pulls| |pypy_version| |pypy_python_support| |github_license|\n\n.. |logo_named| image:: https://raw.githubusercontent.com/AnalogJ/lexicon/master/docs/images/logo_named.svg\n    :alt: Lexicon\n\n.. |build_status| image:: https://dev.azure.com/AnalogJ/lexicon/_apis/build/status/AnalogJ.lexicon?branchName=master\n    :target: https://dev.azure.com/AnalogJ/lexicon/_build/latest?definitionId=1&branchName=master\n\n.. |coverage_status| image:: https://coveralls.io/repos/github/AnalogJ/lexicon/badge.svg\n    :target: https://coveralls.io/github/AnalogJ/lexicon?branch=master\n\n.. |docker_pulls| image:: https://img.shields.io/docker/pulls/analogj/lexicon.svg\n    :target: https://hub.docker.com/r/analogj/lexicon\n\n.. |pypy_version| image:: https://img.shields.io/pypi/v/dns-lexicon.svg\n    :target: https://pypi.python.org/pypi/dns-lexicon\n\n.. |pypy_python_support| image:: https://img.shields.io/pypi/pyversions/dns-lexicon.svg\n    :target: https://pypi.python.org/pypi/dns-lexicon\n\n.. |github_license| image:: https://img.shields.io/github/license/AnalogJ/lexicon.svg\n    :target: https://github.com/AnalogJ/lexicon/blob/master/LICENSE\n\n.. contents:: Table of Contents\n   :local:\n\n.. tag:intro-begin\n\nWhy using Lexicon?\n==================\n\nLexicon provides a way to manipulate DNS records on multiple DNS providers in a standardized way.\n\nLexicon can be used as:\n\n- a CLI tool:\n\n.. code-block:: bash\n\n    # Create a TXT entry in domain.net zone hosted by CloudFlare\n    lexicon cloudflare create domain.net TXT --name foo --content bar\n\n- or a Python library:\n\n.. code-block:: python\n\n    # Create a TXT entry in domain.net zone hosted by CloudFlare\n    from lexicon.client import Client\n    from lexicon.config import ConfigResolver\n\n    action = {\n        "provider_name" : "cloudflare",\n        "action": "create",\n        "domain": "domain.net",\n        "type": "TXT",\n        "name": "foo",\n        "content": "bar",\n    }\n    config = ConfigResolver().with_env().with_dict(action)\n    Client(config).execute()\n\nLexicon was designed to be used in automation, specifically letsencrypt.\n\n* `Generating Intranet & Private Network SSL Certificates using Lets Encrypt & Lexicon <http://blog.thesparktree.com/post/138999997429/generating-intranet-and-private-network-ssl>`_\n\nSupported providers\n===================\n\nOnly DNS providers who have an API can be supported by `lexicon`.\n\nThe current supported providers are:\n\n- `Aliyun.com <https://help.aliyun.com/document_detail/29739.html>`_\n- `AuroraDNS <https://www.pcextreme.com/aurora/dns>`_\n- `AWS Route53 <https://docs.aws.amazon.com/Route53/latest/APIReference/Welcome.html>`_\n- `Azure DNS <https://docs.microsoft.com/en-us/rest/api/dns/>`_\n- `Cloudflare <https://api.cloudflare.com/#endpoints>`_\n- `ClouDNS <https://www.cloudns.net/wiki/article/56/>`_\n- `CloudXNS <https://www.cloudxns.net/Support/lists/cid/17.html>`_\n- `ConoHa <https://www.conoha.jp/docs/>`_\n- `Constellix <https://api-docs.constellix.com/?version=latest>`_\n- `DigitalOcean <https://developers.digitalocean.com/documentation/v2/#create-a-new-domain>`_\n- `Dinahosting <https://en.dinahosting.com/api>`_\n- `DirectAdmin <https://www.directadmin.com/features.php?id=504>`_\n- DNSimple `v1 <https://developer.dnsimple.com/>`_, `v2 <https://developer.dnsimple.com/v2/>`_\n- `DnsMadeEasy <https://api-docs.dnsmadeeasy.com/?version=latest>`_\n- `DNSPark <https://dnspark.zendesk.com/entries/31210577-REST-API-DNS-Documentation>`_\n- `DNSPod <https://support.dnspod.cn/Support/api>`_\n- `Dreamhost <https://help.dreamhost.com/hc/en-us/articles/217560167-API_overview>`_\n- `Dynu <https://www.dynu.com/Support/API>`_\n- `EasyDNS <http://docs.sandbox.rest.easydns.net/>`_\n- `Easyname <https://www.easyname.com/en>`_\n- `EUserv <https://support.euserv.com/api-doc/>`_\n- `ExoScale <https://community.exoscale.com/documentation/dns/api/>`_\n- Gandi `RPC (old) <http://doc.rpc.gandi.net>`_ / `LiveAPI <http://doc.livedns.gandi.net/>`_\n- `Gehirn <https://support.gehirn.jp/apidocs/gis/dns/index.html>`_\n- `Glesys <https://github.com/glesys/API/wiki/>`_\n- `GoDaddy <https://developer.godaddy.com/getstarted#access>`_\n- `Google Cloud DNS <https://cloud.google.com/dns/api/v1/>`_\n- `Gransy (sites subreg.cz, regtons.com and regnames.eu) <https://subreg.cz/manual/>`_\n- `Hover <https://hoverapi.docs.apiary.io/>`_\n- `Hurricane Electric DNS <https://dns.he.net/>`_\n- `Hetzner <https://dns.hetzner.com/api-docs/>`_\n- `Infoblox <https://docs.infoblox.com/display/ILP/Infoblox+Documentation+Portal>`_\n- `Infomaniak <https://www.infomaniak.com>`_\n- `Internet.bs <https://internetbs.net/ResellerRegistrarDomainNameAPI>`_\n- `INWX <https://www.inwx.de/en/offer/api>`_\n- `Joker.com <https://joker.com/faq/index.php?action=show&cat=39>`_\n- `Linode <https://www.linode.com/api/dns>`_\n- `Linode v4 <https://developers.linode.com/api/docs/v4#tag/Domains>`_\n- `LuaDNS <http://www.luadns.com/api.html>`_\n- `Memset <https://www.memset.com/apidocs/methods_dns.html>`_\n- `Mythic Beasts (v2 API) <https://www.mythic-beasts.com/support/api/dnsv2>`_\n- `Njalla <https://njal.la/api/>`_\n- `Namecheap <https://www.namecheap.com/support/api/methods.aspx>`_\n- `Namesilo <https://www.namesilo.com/api_reference.php>`_\n- `Netcup <https://ccp.netcup.net/run/webservice/servers/endpoint.php>`_\n- NFSN (NearlyFreeSpeech)\n- `NS1 <https://ns1.com/api/>`_\n- `OnApp <https://docs.onapp.com/display/55API/OnApp+5.5+API+Guide>`_\n- Online\n- `OVH <https://api.ovh.com/>`_\n- `Plesk <https://docs.plesk.com/en-US/onyx/api-rpc/about-xml-api.28709/>`_\n- `PointHQ <https://pointhq.com/api/docs>`_\n- `PowerDNS <https://doc.powerdns.com/md/httpapi/api_spec/>`_\n- `Rackspace <https://developer.rackspace.com/docs/cloud-dns/v1/developer-guide/>`_\n- `Rage4 <https://gbshouse.uservoice.com/knowledgebase/articles/109834-rage4-dns-developers-api>`_\n- `RcodeZero <https://my.rcodezero.at/api-doc>`_\n- `RFC2136 <https://en.wikipedia.org/wiki/Dynamic_DNS>`_\n- `Sakura Cloud by SAKURA Internet Inc. <https://developer.sakura.ad.jp/cloud/api/1.1/>`_\n- `SafeDNS by UKFast <https://developers.ukfast.io/documentation/safedns>`_\n- `SoftLayer <https://sldn.softlayer.com/article/REST#HTTP_Request_Types>`_\n- `Transip <https://www.transip.nl/transip/api/>`_\n- `UltraDNS <https://ultra-portalstatic.ultradns.com/static/docs/REST-API_User_Guide.pdf>`_\n- `Value-Domain <https://www.value-domain.com/service/api/>`_\n- `Vercel <https://vercel.com/docs/api#endpoints/dns>`_\n- `Vultr <https://www.vultr.com/api/#tag/dns>`_\n- `Yandex <https://tech.yandex.com/domain/doc/reference/dns-add-docpage/>`_\n- `Zilore <https://zilore.com/en/help/api>`_\n- `Zonomi <http://zonomi.com/app/dns/dyndns.jsp>`_\n\n.. tag:intro-end\n\nDocumentation\n=============\n\nOnline documentation (user guide, configuration reference) is available in the `Lexicon documentation`_.\n\nFor a quick start, please have a look in particular at the `User guide`_.\n\n.. _Lexicon documentation: https://dns-lexicon.readthedocs.io\n.. _User guide: https://dns-lexicon.readthedocs.io/en/latest/user_guide.html\n\nContributing\n============\n\nIf you want to help in the Lexicon development, you are welcome!\n\nPlease have a look at the `Developer guide`_ page to know how to start.\n\n.. _Developer guide: https://dns-lexicon.readthedocs.io/en/latest/developer_guide.html\n\nLicensing\n=========\n\n- MIT\n- Logo_: transform by Mike Rowe from the Noun Project\n\n.. _Logo: https://thenounproject.com/term/transform/397964\n',
    'author': 'Jason Kulatunga',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AnalogJ/lexicon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
