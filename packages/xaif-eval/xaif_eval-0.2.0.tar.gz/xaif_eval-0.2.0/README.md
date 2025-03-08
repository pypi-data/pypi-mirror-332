# xaif_eval

[![PyPI version](https://badge.fury.io/py/xaif_eval.svg)](https://badge.fury.io/py/xaif_eval)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python version](https://img.shields.io/badge/python-%3E=3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

## Overview

`xaif` is a Python library for working with Argument Interchange Format (AIF), primarily designed to facilitate the development, manipulation, and evaluation of argumentat structures. This package provides essential utilities to validate, traverse, and manipulate AIF-compliant JSON structures, enabling users to effectively work with complex argumentation data.

## xAIF Format
 {
	"AIF": {
		"nodes": [],
		"edges": [],
		"schemefulfillments": [],
		"descriptorfulfillments": [],
		"participants": [],
		"locutions": []
	},
	"text": "",
  	"dialog": true,
	"OVA": {
		"firstname": "",
		"surname": "",
		"url": "",
		"nodes": [],
		"edges": []
	}
}

## Features

- Validate AIF JSON structures: Ensure the validity and integrity of your AIF data.
- Manage argument components: Add and manipulate various components of an argumentation framework, including relations, nodes, and edges.
- Export data in CSV format: Generate tabular representations of argument components with their respective relation types.


## Installation

You can install the `xaif_eval` package via pip:

```sh
pip install xaif_eval
```

## Usage

### Importing the Library

```python
from xaif_eval import AIF
```

### Example

```python
from xaif_eval import AIF

# Sample xAIF JSON 
aif= {
  "AIF": {
    "descriptorfulfillments": null,
    "edges": [
      {
        "edgeID": 0,
        "fromID": 0,
        "toID": 4
      },
      {
        "edgeID": 1,
        "fromID": 4,
        "toID": 3
      },
      {
        "edgeID": 2,
        "fromID": 1,
        "toID": 6
      },
      {
        "edgeID": 3,
        "fromID": 6,
        "toID": 5
      },
      {
        "edgeID": 4,
        "fromID": 2,
        "toID": 8
      },
      {
        "edgeID": 5,
        "fromID": 8,
        "toID": 7
      },
      {
        "edgeID": 6,
        "fromID": 3,
        "toID": 9
      },
      {
        "edgeID": 7,
        "fromID": 9,
        "toID": 7
      }
    ],
    "locutions": [
      {
        "nodeID": 0,
        "personID": 0
      },
      {
        "nodeID": 1,
        "personID": 1
      },
      {
        "nodeID": 2,
        "personID": 2
      }
    ],
    "nodes": [
      {
        "nodeID": 0,
        "text": "disagreements between party members are entirely to be expected.",
        "type": "L"
      },
      {
        "nodeID": 1,
        "text": "the SNP has disagreements.",
        "type": "L"
      },
      {
        "nodeID": 2,
        "text": "it's not uncommon for there to be disagreements between party members.",
        "type": "L"
      },
      {
        "nodeID": 3,
        "text": "disagreements between party members are entirely to be expected.",
        "type": "I"
      },
      {
        "nodeID": 4,
        "text": "Default Illocuting",
        "type": "YA"
      },
      {
        "nodeID": 5,
        "text": "the SNP has disagreements.",
        "type": "I"
      },
      {
        "nodeID": 6,
        "text": "Default Illocuting",
        "type": "YA"
      },
      {
        "nodeID": 7,
        "text": "it's not uncommon for there to be disagreements between party members.",
        "type": "I"
      },
      {
        "nodeID": 8,
        "text": "Default Illocuting",
        "type": "YA"
      },
      {
        "nodeID": 9,
        "text": "Default Inference",
        "type": "RA"
      }
    ],
    "participants": [
      {
        "firstname": "Speaker",
        "participantID": 0,
        "surname": "1"
      },
      {
        "firstname": "Speaker",
        "participantID": 1,
        "surname": "2"
      }
    ],
    "schemefulfillments": null
  },
  "dialog": true,
  "ova": [],
  "text": {
    "txt": " Speaker 1 <span class=\"highlighted\" id=\"0\">disagreements between party members are entirely to be expected.</span>.<br><br> Speaker 2 <span class=\"highlighted\" id=\"1\">the SNP has disagreements.</span>.<br><br> Speaker 1 <span class=\"highlighted\" id=\"2\">it's not uncommon for there to be disagreements between party members. </span>.<br><br>"
  }
}

# Initialize the AIF object with xAIF data
aif = AIF(xaif)

# Initialize the AIF object with text 
aif = AIF("here is the text.")

speaker = "First Speaker"
text = "another text"
aif.add_component("locution", text, speaker)
aif.add_component("locution", "the third text. fourth text", "Second Speaker")
aif.add_component("segment", 2, ["the third text.", "fourth text"])
aif.add_component("proposition", 3, "the third text.")
aif.add_component("proposition", 4, "fourth text.")
aif.add_component("argument_relation", "RA", 5,7)

print(aif.xaif)

print(aif.get_csv("argument-relation"))
```

## Documentation

The full documentation is available at [xaif_eval Documentation](https://github.com/debelatesfaye/xaif).

## Contributing

Contributions are welcome! Please visit the [Contributing Guidelines](https://github.com/debelatesfaye/xaif/blob/main/CONTRIBUTING.md) for more information.

## Issues

If you encounter any problems, please file an issue at the [Issue Tracker](https://github.com/debelatesfaye/xaif/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/debelatesfaye/xaif/blob/main/LICENSE) file for details.

## Authors

- DEBELA - [d.t.z.gemechu@dundee.ac.uk](mailto:d.t.z.gemechu@dundee.ac.uk)

## Acknowledgments

- Thanks to all contributors and users for their feedback and support.
```

