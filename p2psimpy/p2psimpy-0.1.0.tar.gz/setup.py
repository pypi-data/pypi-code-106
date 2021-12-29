# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['p2psimpy', 'p2psimpy.services']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'networkx>=2.6.3,<3.0.0',
 'scipy>=1.7.3,<2.0.0',
 'simpy>=4.0.1,<5.0.0']

setup_kwargs = {
    'name': 'p2psimpy',
    'version': '0.1.0',
    'description': 'Event simulator for peer-to-peer experiments',
    'long_description': "# p2psimpy\n\n[![Tests](https://github.com/grimadas/p2psimpy/workflows/Tests/badge.svg)](https://github.com/grimadas/p2psimpy/actions?workflow=Tests)\n  \n\nA simple simulator for peer-to-peer protocols based on [SimPy](https://simpy.readthedocs.io/en/latest/).\n\n  \nThe library provides means to simulate distributed or decentralized system run over a network.\nThe simulation runs as a multi-agent system each running  services and exchanging messages. \n\n## Installation \nIf you have pip installed, just type: \n```bash\n$ pip install p2psimpy \n```\n\n## Simulation example\n\nFor each simulation you should specify what each agent should run, the latency for the messages and the physical attributes on an agent.\n\nHere is an example in which peers are connected in a random network, and each peer runs a connection manager. The connection manager periodically pings the connected peers and disconnects them if they are unresponsive.  \n The simulation looks like this: \n\n```python\nimport networkx as nx\n\nfrom p2psimpy.config import Config, Dist, PeerType\nfrom p2psimpy.consts import MBit\nfrom p2psimpy.simulation import Simulation\nfrom p2psimpy.services.connection_manager import BaseConnectionManager\n\n# Locations and latency matrix between the locations \nclass Locations(Config):\n\tlocations = ['LocA', 'LocB']\n\tlatencies = {\n\t\t\t\t 'LocB': {'LocB': Dist('gamma', (1, 1, 1))},\n\t\t\t\t 'LocA': {'LocB': Dist('norm', (12, 2)), \n\t\t\t\t\t\t  'LocA': Dist('norm', (2, 0.5))},\n\t\t\t\t}\n\nN = 10\n# Generate network topology\nG = nx.erdos_renyi_graph(N, 0.5)\nnx.set_node_attributes(G, {k: 'basic' for k in G.nodes()}, 'type')\t\n\n# Physical properties of a peer. Peer will randomly get an attribute from a given distribution.\nclass PeerConfig(Config):\n\tlocation = Dist('sample', Locations.locations)\n\tbandwidth_ul = Dist( 'norm', (50*MBit, 10*MBit))\n\tbandwidth_dl = Dist( 'norm', (50*MBit, 10*MBit))\n\n# Each basic peer runs a ConnectionManager: that will periodically ping neighbours and check if they are online\nservices = (BaseConnectionManager,)\npeer_types = {'basic': PeerType(PeerConfig, services)}\n\nsim = Simulation(Locations, G, peer_types)\n# run the simulation for 1_000 milliseconds \nsim.run(1_000)\n```\n",
    'author': 'grimadas',
    'author_email': 'bulat.nasrulin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/grimadas/p2psimpy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
