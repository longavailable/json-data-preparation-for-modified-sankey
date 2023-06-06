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

## How to cite

If this tool is useful to your research, cite the published article as below:

>Liu, X.; Fu, D.; Zevenbergen, C.; Busker, T.; Yu, M. Assessing Sponge Cities Performance at City Scale Using Remotely Sensed LULC Changes: Case Study Nanjing. Remote Sens. 2021, 13, 580. https://doi.org/10.3390/rs13040580.

Easily, you can import it to 
<a href="https://www.mendeley.com/import/?url=https://www.mdpi.com/989436"><i class="fa fa-external-link"></i> Mendeley</a>.

<!--links-->
[Observable]: observablehq.com
