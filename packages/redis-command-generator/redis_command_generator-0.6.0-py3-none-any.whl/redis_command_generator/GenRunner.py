import threading
import copy
import sys
from simple_parsing import parse
from dataclasses import dataclass
from redis_command_generator.AllGen import *

def create_tg(base_classes):
    return type('TypeGen', base_classes, {})

def cast_to_tg(obj_with_args, class_type):
    class_obj = copy.deepcopy(obj_with_args)
    class_obj.__class__ = class_type
    return class_obj

def strings_to_classes(classnames):
    classes = []
    for name in classnames:
        classes.append(getattr(sys.modules[__name__], name))
    
    return classes

# Append thread number to logfile name
def rename_log(logfile, thread_num):
    if logfile is None:
        return None
    
    logfile = logfile.split(".")
    return f"{logfile[0]}_t{thread_num}.{logfile[1]}"

# You may run `python -m redis_command_generator.GenRunner -h` to see all available args combined
@dataclass
class Args(AllGen):
    num_threads: int = 3
    include_gens: tuple = ("SetGen", "ZSetGen", "StringGen", "StreamGen", "ListGen", "HyperLogLogGen", "HashGen", "GeoGen", "BitmapGen")
    exclude_gens: tuple = ()

class GenRunner():
    def __init__(self):
        self.threads = []
        self.events = []
    
    def __enter__(self):
        return self
    
    def start(self, args):
        gen_names = [gen for gen in args.include_gens if gen not in args.exclude_gens]
        gen_types = strings_to_classes(gen_names)
        TypeGen = create_tg(tuple(gen_types))  # Create a new class from all the selected generators
        
        for i in range(args.num_threads):
            generator = cast_to_tg(args, TypeGen)
            generator.logfile = rename_log(args.logfile, i)
            
            self.events.append(threading.Event())
            self.threads.append(threading.Thread(target=(generator._run), args=(self.events[i],)))
            self.threads[i].start()

    def join(self):
        for t in self.threads:
            t.join()

    def __exit__(self, exc_type, exc_value, traceback):
        for e in self.events:
            e.set()
        self.join()

if __name__ == "__main__":
    args = parse(Args)
    
    gen_runner = GenRunner()
    gen_runner.start(args)
    gen_runner.join()