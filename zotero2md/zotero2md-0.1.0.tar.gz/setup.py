# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zotero2md', 'zotero2md.test']

package_data = \
{'': ['*']}

install_requires = \
['Pyzotero>=1.4.26,<2.0.0',
 'SnakeMD>=0.9.3,<0.10.0',
 'markdownify>=0.10.1,<0.11.0']

setup_kwargs = {
    'name': 'zotero2md',
    'version': '0.1.0',
    'description': 'Export Zotero annotations and notes to Markdown files.',
    'long_description': '# Zotero to Markdown\n\nGenerate Markdown files from Zotero annotations and notes. \nWith new [Zotero PDF Reader](https://www.zotero.org/support/pdf_reader_preview), all highlights are saved in the Zotero database.\nThe highlights are NOT saved in the PDF file unless you export the highlights in order to save them.\n\nIf you annotate your files outside the new Zotero PDF reader, this library will not work with your PDF annotations as those are not retrievable from Zotero API.\nIn that case, you may want to use zotfile + mdnotes to extract the annotations and convert them into markdown files.\n\n\n**_This library is for you if you annotate (highlight + note) using the Zotero\'s PDF reader (including the beta version in iOs)_**\n\n# Installation \nYou can install the library by running \n```shell\npip install zotero2md\n```\n\nNote: If you do not have pip installed on your system, you can follow the instructions [here](https://pip.pypa.io/en/stable/installation/).\n\n# Usage\n```shell\npython zotero2md/generate.py <zotero_key> <zotero_id>\n```\n\nFor instance, assuming zotero_key=abcd and zotero_id=1234, you can simply run the following:\n```shell\npython zotero2md/generate.py abcd 1234\n```\n\n\n## Custom Output Parameters\nYou can change default parameters by passing the `--config_filepath` option with the path to a\nJSON file containing the desired configurations. For instance,\n\n```shell\npython zotero2md/generate.py <zotero_key> <zotero_id> --config_filepath ./sample_params.json\n```\n\n| Parameter                         | type            | default value |\n|-----------------------------------|-----------------|---------------|\n| `convertTagsToInternalLinks`      | bool            | true          |\n| `doNotConvertFollowingTagsToLink` | List of strings | \\[ \\]         |\n| `includeHighlightDate`            | bool            | true          |\n| `hideHighlightDateInPreview`      | bool            | true          |\n\n\nAny parameter in the JSON file will override the default setting. \nIf a parameter is not provided, then the default value will be used. \n\nFor example, if you don\'t want to show the highlight date in the output file, you can simply pass\na JSON file with the following content:\n```json\n{\n  "hideHighlightDateInPreview": false\n}\n```\n\n# Features\n- Generate MD files for all annotations and notes saved in Zotero\n- The ability to convert Zotero tags to internal links (`[[ ]]`) used in many bidirectional MD editors.\n  - You can even pass certain tags that you don\'t want to convert to internal links! (using `doNotConvertFollowingTagsToLink` parameter)\n\n## Quick note\nSince I\'m personally using Obsidian as my markdown editor, there are custom parameters to generate MD files that are consistent with Obsidian and I\'m planning to add more option there. \n\n\n# Roadmap\n- [ ] Update existing annotations and notes\n- [ ] Option to add frontmatter section (particularly useful for Obsidian)\n- [ ] More flexibility in styling the output files \n\n# Request a new feature or report a bug\nFeel free to request a new feature or report a bug in GitHub issue [here](https://github.com/e-alizadeh/Zotero2MD/issues).\n\n## 📫 How to reach me:\n<a href="https://ealizadeh.com" target="_blank"><img alt="Personal Website" src="https://img.shields.io/badge/Personal%20Website-%2312100E.svg?&style=for-the-badge&logoColor=white" /></a>\n<a href="https://www.linkedin.com/in/alizadehesmaeil/" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>\n<a href="https://medium.com/@ealizadeh" target="_blank"><img alt="Medium" src="https://img.shields.io/badge/medium-%2312100E.svg?&style=for-the-badge&logo=medium&logoColor=white" /></a>\n<a href="https://twitter.com/intent/follow?screen_name=es_alizadeh&tw_p=followbutton" target="_blank"><img alt="Twitter" src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" /></a>\n\n<a href="https://www.buymeacoffee.com/ealizadeh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>',
    'author': 'ealizadeh',
    'author_email': 'hello@ealizadeh.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/e-alizadeh/Zotero2MD',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
