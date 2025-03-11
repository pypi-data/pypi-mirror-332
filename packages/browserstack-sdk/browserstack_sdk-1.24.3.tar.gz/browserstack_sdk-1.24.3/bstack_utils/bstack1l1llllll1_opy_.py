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
class bstack1111l111_opy_:
    def __init__(self, handler):
        self._11l11111l1l_opy_ = None
        self.handler = handler
        self._11l11111l11_opy_ = self.bstack11l11111ll1_opy_()
        self.patch()
    def patch(self):
        self._11l11111l1l_opy_ = self._11l11111l11_opy_.execute
        self._11l11111l11_opy_.execute = self.bstack11l111111ll_opy_()
    def bstack11l111111ll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11lll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤ᱈"), driver_command, None, this, args)
            response = self._11l11111l1l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11lll_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤ᱉"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11111l11_opy_.execute = self._11l11111l1l_opy_
    @staticmethod
    def bstack11l11111ll1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver