# json-data-preparation-for-modified-sankey
Steps and explanation to prepare json data for modified Sankey chart.


## Steps to create a M-Sankey chart

1. prepare the nodes file

    - Each node for a sub-column,

    - Edit by hand

1. prepare the links file

    - Calculated by a 3rd-party

1. concatenate the links and nodes

    - [concatenate-links-nodes.py](/concatenate-links-nodes.py)

    - Output is [data-msankey.json](/data-msankey.json), which used in [Observable].

1. [Observable]

    - <https://observablehq.com/@longavailable/the-modified-sankey-diagram-for-lulc-changes>


<!--links-->
[Observable]: observablehq.com
