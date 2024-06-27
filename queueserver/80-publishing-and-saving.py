#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bluesky.callbacks.zmq import Publisher
from bluesky import RunEngine

from databroker import Broker


RE = RunEngine()
publisher = Publisher("localhost:5577")
RE.subscribe(publisher)

db = Broker.named("test")
RE.subscribe(db.insert)

from dataclasses import dataclass
import logging
import os
from typing import Optional

from daiquiri.core.saving.base import SavingHandler

logger = logging.getLogger(__name__)


@dataclass
class ScanSaving:
    base_path: Optional[str] = None
    template: Optional[str] = None
    data_filename: Optional[str] = None

    @property
    def root_path(self):
        return os.path.join(self.base_path, self.template)

    @property
    def filename(self):
        return os.path.join(self.root_path, self.data_filename) + ".h5"


class SimpleSavingHandler(SavingHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._scan_saving = ScanSaving()

    @property
    def scan_saving(self):
        return self._scan_saving

    def _set_filename(self, base_path=None, template=None, data_filename=None):
        self.scan_saving.base_path = base_path
        self.scan_saving.template = os.path.join(template, data_filename)
        self.scan_saving.data_filename = data_filename

    @property
    def filename(self):
        return self.scan_saving.filename

    def create_root_path(self, wait_exists=False, wait_timeout=360):
        if not os.path.exists(self._scan_saving.root_path):
            os.makedirs(self._scan_saving.root_path)

    def create_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
