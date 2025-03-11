# coding: UTF-8
import sys
bstack1111l1l_opy_ = sys.version_info [0] == 2
bstack1llll1l_opy_ = 2048
bstack1ll1111_opy_ = 7
def bstack11lll_opy_ (bstack11lll1_opy_):
    global bstack1lll1l_opy_
    bstack1l1l11l_opy_ = ord (bstack11lll1_opy_ [-1])
    bstack11lllll_opy_ = bstack11lll1_opy_ [:-1]
    bstack1ll1lll_opy_ = bstack1l1l11l_opy_ % len (bstack11lllll_opy_)
    bstack11l1_opy_ = bstack11lllll_opy_ [:bstack1ll1lll_opy_] + bstack11lllll_opy_ [bstack1ll1lll_opy_:]
    if bstack1111l1l_opy_:
        bstack11llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack1llll1l_opy_ - (bstack111l1l1_opy_ + bstack1l1l11l_opy_) % bstack1ll1111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack11l1_opy_)])
    else:
        bstack11llll1_opy_ = str () .join ([chr (ord (char) - bstack1llll1l_opy_ - (bstack111l1l1_opy_ + bstack1l1l11l_opy_) % bstack1ll1111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack11l1_opy_)])
    return eval (bstack11llll1_opy_)
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack11111l11ll_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1111ll11l1_opy_:
    bstack1l11l11llll_opy_ = bstack11lll_opy_ (u"ࠢࡣࡧࡱࡧ࡭ࡳࡡࡳ࡭ࠥᒂ")
    context: bstack11111l11ll_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack11111l11ll_opy_):
        self.context = context
        self.data = dict({bstack1111ll11l1_opy_.bstack1l11l11llll_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᒃ"), bstack11lll_opy_ (u"ࠩ࠳ࠫᒄ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1111l1ll11_opy_(self, target: object):
        return bstack1111ll11l1_opy_.create_context(target) == self.context
    def bstack1ll1l11l1ll_opy_(self, context: bstack11111l11ll_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack1llllllll1_opy_(self, key: str, value: timedelta):
        self.data[bstack1111ll11l1_opy_.bstack1l11l11llll_opy_][key] += value
    def bstack1lllll11ll1_opy_(self) -> dict:
        return self.data[bstack1111ll11l1_opy_.bstack1l11l11llll_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack11111l11ll_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )