
import logging
from .Generator import gen

logging.basicConfig(level=logging.INFO)

print("Attempting to update generated class for active chromium.")
gen.update_generated_class(force=True, output_diff=True)
