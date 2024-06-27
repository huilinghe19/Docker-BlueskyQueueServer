import socket
#from tiled.client import from_uri
from bluesky import RunEngine
from bluesky_queueserver import parameter_annotation_decorator
RE = RunEngine({})


#client = from_uri("http://bluesky-tiled:8000", api_key="secret")
#def post_document(name,doc):
#    client.post_document(name,doc)
#RE.subscribe(post_document)



# import devices and plans, add your own devices and plans here
from ophyd.sim import det1, det2, det3, det4, motor1, motor2, motor, det
from bluesky.plans import count, scan, grid_scan, fly
from ophyd import Device, EpicsMotor, EpicsSignal

@parameter_annotation_decorator({
    "parameters": {
        "detectors": {
            "annotation": "typing.List[str]",
            "convert_device_names": True,
        },
        "delay": {
            "annotation": "int",
            "default": 1,
            "min": 0,
            "max": 5,
            "step": 0.2,
        }
    }
})
def new_count(detectors, num:int, delay:int=1, *, md:dict={}):
    yield from count(detectors, num, delay, md)

