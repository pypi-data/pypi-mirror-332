from argconf import argconf_parse
from pprint import pprint

from omegaconf import OmegaConf 
# Load the configuration file
config = argconf_parse()
pprint(config.scene_filters)
