# coding: UTF-8
import sys
bstack1111ll1_opy_ = sys.version_info [0] == 2
bstack1ll11l_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11ll1l_opy_ (bstack111l1l1_opy_):
    global bstack1l111_opy_
    bstack1l1lll_opy_ = ord (bstack111l1l1_opy_ [-1])
    bstack1l1llll_opy_ = bstack111l1l1_opy_ [:-1]
    bstack1l11ll1_opy_ = bstack1l1lll_opy_ % len (bstack1l1llll_opy_)
    bstack1l11ll_opy_ = bstack1l1llll_opy_ [:bstack1l11ll1_opy_] + bstack1l1llll_opy_ [bstack1l11ll1_opy_:]
    if bstack1111ll1_opy_:
        bstack11l1111_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll11l_opy_ - (bstack111ll_opy_ + bstack1l1lll_opy_) % bstack11lllll_opy_) for bstack111ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack11l1111_opy_ = str () .join ([chr (ord (char) - bstack1ll11l_opy_ - (bstack111ll_opy_ + bstack1l1lll_opy_) % bstack11lllll_opy_) for bstack111ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack11l1111_opy_)
from collections import deque
from bstack_utils.constants import *
class bstack1llll111l_opy_:
    def __init__(self):
        self._11l11lllll1_opy_ = deque()
        self._11l11ll1l11_opy_ = {}
        self._11l11ll1lll_opy_ = False
    def bstack11l11ll1ll1_opy_(self, test_name, bstack11l11llllll_opy_):
        bstack11l11llll1l_opy_ = self._11l11ll1l11_opy_.get(test_name, {})
        return bstack11l11llll1l_opy_.get(bstack11l11llllll_opy_, 0)
    def bstack11l11lll1ll_opy_(self, test_name, bstack11l11llllll_opy_):
        bstack11l11llll11_opy_ = self.bstack11l11ll1ll1_opy_(test_name, bstack11l11llllll_opy_)
        self.bstack11l11lll1l1_opy_(test_name, bstack11l11llllll_opy_)
        return bstack11l11llll11_opy_
    def bstack11l11lll1l1_opy_(self, test_name, bstack11l11llllll_opy_):
        if test_name not in self._11l11ll1l11_opy_:
            self._11l11ll1l11_opy_[test_name] = {}
        bstack11l11llll1l_opy_ = self._11l11ll1l11_opy_[test_name]
        bstack11l11llll11_opy_ = bstack11l11llll1l_opy_.get(bstack11l11llllll_opy_, 0)
        bstack11l11llll1l_opy_[bstack11l11llllll_opy_] = bstack11l11llll11_opy_ + 1
    def bstack1l1l1lll1l_opy_(self, bstack11l11ll1l1l_opy_, bstack11l11lll111_opy_):
        bstack11l11ll11ll_opy_ = self.bstack11l11lll1ll_opy_(bstack11l11ll1l1l_opy_, bstack11l11lll111_opy_)
        event_name = bstack1l1111ll1l1_opy_[bstack11l11lll111_opy_]
        bstack1l1llllll11_opy_ = bstack11ll1l_opy_ (u"ࠣࡽࢀ࠱ࢀࢃ࠭ࡼࡿࠥᯐ").format(bstack11l11ll1l1l_opy_, event_name, bstack11l11ll11ll_opy_)
        self._11l11lllll1_opy_.append(bstack1l1llllll11_opy_)
    def bstack1ll1l1111_opy_(self):
        return len(self._11l11lllll1_opy_) == 0
    def bstack11l1lllll_opy_(self):
        bstack11l11lll11l_opy_ = self._11l11lllll1_opy_.popleft()
        return bstack11l11lll11l_opy_
    def capturing(self):
        return self._11l11ll1lll_opy_
    def bstack1ll1111l1_opy_(self):
        self._11l11ll1lll_opy_ = True
    def bstack1llll1llll_opy_(self):
        self._11l11ll1lll_opy_ = False