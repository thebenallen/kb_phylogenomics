import os
import sys

# JUST CAN'T GET THIS WORKING.  Use subprocess instead
#
#os.environ['PATH'] = '/kb/module/anaconda_ete/bin:'+os.environ['PATH']
#sys.path.append ('/kb/module/anaconda_ete/bin')
from anaconda_ete.ete3 import Tree

class PhyloPlotUtil:

    def __init__(self, config):
        pprint(config)
        self.scratch = config['scratch']
        self.callbackURL = config['SDK_CALLBACK_URL']


    def write_species_tree_img(self, newick_str, output_path, width=150, format='png'):
        #t = Tree("(A:1,(B:1,(E:1,D:1):0.5):0.5);" )
        #t.render("test_tree.png", w=width, units="mm")

        newick_str = re.sub(" \t\n\r", '', newick_str)
        if not newick_str.endswith(';'):
            newick_str += ';'
        


        if not output_file.endswith('.'+format):
            raise ValueError ("format does not match filename extension")

        t = Tree(newick_str)
        t.render(output_path, w=width, units="mm")




