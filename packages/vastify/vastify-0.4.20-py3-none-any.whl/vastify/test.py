from vastify.decorator import run_on_vastai
from .test_code import test_func
import logging

@run_on_vastai(
               gpu_name="Tesla T4",
               price=0.25,
               disk=100.0,
               image='pytorch/pytorch:2.1.0-cuda11.8-cudnn8-devel',
               num_gpus='1',
               regions=['North_America', 'Europe', 'World'],
               env='-p 70000:8000', 
                 include_files=[
                ],
               additional_reqs=[])
def example_function():
    return test_func()


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(name)s:%(lineno)d:%(message)s', level=logging.INFO)
    res = example_function()

    print("Result from test example function:", res)
