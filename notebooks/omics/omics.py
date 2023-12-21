from bioservices import KEGG
import re
import pandas as pd
import pandas as pd
import requests
import io
import os
import Bio
from Bio.KEGG.REST import *
from Bio.KEGG.KGML import KGML_parser
from Bio.Graphics.KGML_vis import KGMLCanvas
from Bio.Graphics.ColorSpiral import ColorSpiral
from IPython.display import Image, HTML


def map_from_compound(cp_number):
    s = KEGG()
    data = s.get(cp_number)
    dict_data = s.parse(data)
    return dict_data["PATHWAY"]
    
def ko_from_map(map_number):
    s = KEGG()
    data = s.get(map_number)
    dict_data = s.parse(data)
    return dict_data["KO_PATHWAY"]

def enzymes_from_pathway(pathway, color):
    s = KEGG()
    data = s.get(pathway)
    dict_data = s.parse(data)
    ko = []
    ECS = []
    pattern = r'\[EC:\s*([^]]*)\]'
    for k,v in dict_data["ORTHOLOGY"].items():
        ec_numbers = re.search(pattern, v)
        if ec_numbers: 
            ko.append(k)
            ECS.append(ec_numbers.group(1).split(" "))
    KEGG_return = pd.DataFrame({"KEGG_NODE_LABEL":ko,"EC_number":ECS})
    KEGG_return = KEGG_return.explode("EC_number")
    KEGG_return["KEGG_NODE_FILL_COLOR"] = [color for i in range(len(KEGG_return))]
    return KEGG_return

def draw_pathway(path_ko, outdir, ko_list, cp_list):
    pathway = KGML_parser.read(kegg_get(path_ko, "kgml"))
    for element in pathway.compounds:
        for graphic in element.graphics:
            if graphic.name in cp_list:
                graphic.bgcolor = '#ff0000'
    for element in pathway.orthologs:
        for graphic in element.graphics:
            if graphic.name in ko_list:
                graphic.bgcolor = '#65e8b4'
            else:
                graphic.bgcolor = "#FFFFFF"

    canvas = KGMLCanvas(pathway)
    canvas.import_imagemap = True
    canvas.label_compounds = False
    canvas.draw(os.path.join(outdir, f"{path_ko}.pdf"))

