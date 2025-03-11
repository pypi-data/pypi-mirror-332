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
import builtins
import logging
class bstack11l11l1lll_opy_:
    def __init__(self, handler):
        self._1l1111llll1_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._1l1111lll1l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11lll_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᖋ"), bstack11lll_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ᖌ"), bstack11lll_opy_ (u"ࠨࡹࡤࡶࡳ࡯࡮ࡨࠩᖍ"), bstack11lll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᖎ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._1l1111lll11_opy_
        self._1l111l11111_opy_()
    def _1l1111lll11_opy_(self, *args, **kwargs):
        self._1l1111llll1_opy_(*args, **kwargs)
        message = bstack11lll_opy_ (u"ࠪࠤࠬᖏ").join(map(str, args)) + bstack11lll_opy_ (u"ࠫࡡࡴࠧᖐ")
        self._log_message(bstack11lll_opy_ (u"ࠬࡏࡎࡇࡑࠪᖑ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11lll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᖒ"): level, bstack11lll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᖓ"): msg})
    def _1l111l11111_opy_(self):
        for level, bstack1l1111lllll_opy_ in self._1l1111lll1l_opy_.items():
            setattr(logging, level, self._1l111l1111l_opy_(level, bstack1l1111lllll_opy_))
    def _1l111l1111l_opy_(self, level, bstack1l1111lllll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack1l1111lllll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._1l1111llll1_opy_
        for level, bstack1l1111lllll_opy_ in self._1l1111lll1l_opy_.items():
            setattr(logging, level, bstack1l1111lllll_opy_)