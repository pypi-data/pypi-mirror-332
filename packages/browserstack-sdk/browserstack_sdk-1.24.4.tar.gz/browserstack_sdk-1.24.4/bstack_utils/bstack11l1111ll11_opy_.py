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
import threading
import logging
logger = logging.getLogger(__name__)
bstack11l111l11l1_opy_ = 1000
bstack11l1111llll_opy_ = 2
class bstack11l1111l11l_opy_:
    def __init__(self, handler, bstack11l111l11ll_opy_=bstack11l111l11l1_opy_, bstack11l1111l1l1_opy_=bstack11l1111llll_opy_):
        self.queue = []
        self.handler = handler
        self.bstack11l111l11ll_opy_ = bstack11l111l11ll_opy_
        self.bstack11l1111l1l1_opy_ = bstack11l1111l1l1_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack111l11l111_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack11l1111lll1_opy_()
    def bstack11l1111lll1_opy_(self):
        self.bstack111l11l111_opy_ = threading.Event()
        def bstack11l1111l1ll_opy_():
            self.bstack111l11l111_opy_.wait(self.bstack11l1111l1l1_opy_)
            if not self.bstack111l11l111_opy_.is_set():
                self.bstack11l111l111l_opy_()
        self.timer = threading.Thread(target=bstack11l1111l1ll_opy_, daemon=True)
        self.timer.start()
    def bstack11l111l1111_opy_(self):
        try:
            if self.bstack111l11l111_opy_ and not self.bstack111l11l111_opy_.is_set():
                self.bstack111l11l111_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack11ll1l_opy_ (u"ࠫࡠࡹࡴࡰࡲࡢࡸ࡮ࡳࡥࡳ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࠨ᱃") + (str(e) or bstack11ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡤࡱࡱࡺࡪࡸࡴࡦࡦࠣࡸࡴࠦࡳࡵࡴ࡬ࡲ࡬ࠨ᱄")))
        finally:
            self.timer = None
    def bstack11l1111ll1l_opy_(self):
        if self.timer:
            self.bstack11l111l1111_opy_()
        self.bstack11l1111lll1_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack11l111l11ll_opy_:
                threading.Thread(target=self.bstack11l111l111l_opy_).start()
    def bstack11l111l111l_opy_(self, source = bstack11ll1l_opy_ (u"࠭ࠧ᱅")):
        with self.lock:
            if not self.queue:
                self.bstack11l1111ll1l_opy_()
                return
            data = self.queue[:self.bstack11l111l11ll_opy_]
            del self.queue[:self.bstack11l111l11ll_opy_]
        self.handler(data)
        if source != bstack11ll1l_opy_ (u"ࠧࡴࡪࡸࡸࡩࡵࡷ࡯ࠩ᱆"):
            self.bstack11l1111ll1l_opy_()
    def shutdown(self):
        self.bstack11l111l1111_opy_()
        while self.queue:
            self.bstack11l111l111l_opy_(source=bstack11ll1l_opy_ (u"ࠨࡵ࡫ࡹࡹࡪ࡯ࡸࡰࠪ᱇"))