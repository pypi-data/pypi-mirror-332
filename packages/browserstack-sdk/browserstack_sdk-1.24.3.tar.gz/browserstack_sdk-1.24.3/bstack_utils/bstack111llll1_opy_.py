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
from collections import deque
from bstack_utils.constants import *
class bstack1l1l11ll1_opy_:
    def __init__(self):
        self._11l11l1l11l_opy_ = deque()
        self._11l11l11l1l_opy_ = {}
        self._11l11l1ll1l_opy_ = False
    def bstack11l11l1llll_opy_(self, test_name, bstack11l11l1ll11_opy_):
        bstack11l11l11lll_opy_ = self._11l11l11l1l_opy_.get(test_name, {})
        return bstack11l11l11lll_opy_.get(bstack11l11l1ll11_opy_, 0)
    def bstack11l11l11l11_opy_(self, test_name, bstack11l11l1ll11_opy_):
        bstack11l11l1l1l1_opy_ = self.bstack11l11l1llll_opy_(test_name, bstack11l11l1ll11_opy_)
        self.bstack11l11l111ll_opy_(test_name, bstack11l11l1ll11_opy_)
        return bstack11l11l1l1l1_opy_
    def bstack11l11l111ll_opy_(self, test_name, bstack11l11l1ll11_opy_):
        if test_name not in self._11l11l11l1l_opy_:
            self._11l11l11l1l_opy_[test_name] = {}
        bstack11l11l11lll_opy_ = self._11l11l11l1l_opy_[test_name]
        bstack11l11l1l1l1_opy_ = bstack11l11l11lll_opy_.get(bstack11l11l1ll11_opy_, 0)
        bstack11l11l11lll_opy_[bstack11l11l1ll11_opy_] = bstack11l11l1l1l1_opy_ + 1
    def bstack1l1l11ll1l_opy_(self, bstack11l11l1l111_opy_, bstack11l11l1l1ll_opy_):
        bstack11l11l1lll1_opy_ = self.bstack11l11l11l11_opy_(bstack11l11l1l111_opy_, bstack11l11l1l1ll_opy_)
        event_name = bstack1l11111ll1l_opy_[bstack11l11l1l1ll_opy_]
        bstack1ll11111111_opy_ = bstack11lll_opy_ (u"ࠥࡿࢂ࠳ࡻࡾ࠯ࡾࢁࠧᰃ").format(bstack11l11l1l111_opy_, event_name, bstack11l11l1lll1_opy_)
        self._11l11l1l11l_opy_.append(bstack1ll11111111_opy_)
    def bstack11ll1l1l_opy_(self):
        return len(self._11l11l1l11l_opy_) == 0
    def bstack1lllll1l11_opy_(self):
        bstack11l11l11ll1_opy_ = self._11l11l1l11l_opy_.popleft()
        return bstack11l11l11ll1_opy_
    def capturing(self):
        return self._11l11l1ll1l_opy_
    def bstack1111l1ll1_opy_(self):
        self._11l11l1ll1l_opy_ = True
    def bstack1l1l1l11_opy_(self):
        self._11l11l1ll1l_opy_ = False