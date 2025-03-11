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
import builtins
import logging
class bstack11l11llll1_opy_:
    def __init__(self, handler):
        self._1l111l1ll1l_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._1l111l1llll_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11ll1l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᕘ"), bstack11ll1l_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫᕙ"), bstack11ll1l_opy_ (u"࠭ࡷࡢࡴࡱ࡭ࡳ࡭ࠧᕚ"), bstack11ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᕛ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._1l111l1ll11_opy_
        self._1l111ll111l_opy_()
    def _1l111l1ll11_opy_(self, *args, **kwargs):
        self._1l111l1ll1l_opy_(*args, **kwargs)
        message = bstack11ll1l_opy_ (u"ࠨࠢࠪᕜ").join(map(str, args)) + bstack11ll1l_opy_ (u"ࠩ࡟ࡲࠬᕝ")
        self._log_message(bstack11ll1l_opy_ (u"ࠪࡍࡓࡌࡏࠨᕞ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11ll1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᕟ"): level, bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᕠ"): msg})
    def _1l111ll111l_opy_(self):
        for level, bstack1l111ll1111_opy_ in self._1l111l1llll_opy_.items():
            setattr(logging, level, self._1l111l1lll1_opy_(level, bstack1l111ll1111_opy_))
    def _1l111l1lll1_opy_(self, level, bstack1l111ll1111_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack1l111ll1111_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._1l111l1ll1l_opy_
        for level, bstack1l111ll1111_opy_ in self._1l111l1llll_opy_.items():
            setattr(logging, level, bstack1l111ll1111_opy_)