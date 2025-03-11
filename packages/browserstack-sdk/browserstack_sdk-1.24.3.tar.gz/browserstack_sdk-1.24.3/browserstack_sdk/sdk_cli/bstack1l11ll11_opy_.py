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
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack11111ll1_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack11l1l1lll1_opy_:
    pass
class bstack1ll1llll11_opy_:
    bstack11llll11l1_opy_ = bstack11lll_opy_ (u"ࠨࡢࡰࡱࡷࡷࡹࡸࡡࡱࠤ႟")
    CONNECT = bstack11lll_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣႠ")
    bstack1ll1ll111l_opy_ = bstack11lll_opy_ (u"ࠣࡵ࡫ࡹࡹࡪ࡯ࡸࡰࠥႡ")
    CONFIG = bstack11lll_opy_ (u"ࠤࡦࡳࡳ࡬ࡩࡨࠤႢ")
    bstack1lll11l1111_opy_ = bstack11lll_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡹࠢႣ")
    bstack1ll111llll_opy_ = bstack11lll_opy_ (u"ࠦࡪࡾࡩࡵࠤႤ")
class bstack1lll111ll11_opy_:
    bstack1lll111lll1_opy_ = bstack11lll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡸࡺࡡࡳࡶࡨࡨࠧႥ")
    FINISHED = bstack11lll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢႦ")
class bstack1lll11l11l1_opy_:
    bstack1lll111lll1_opy_ = bstack11lll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡶࡸࡦࡸࡴࡦࡦࠥႧ")
    FINISHED = bstack11lll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧႨ")
class bstack1lll111ll1l_opy_:
    bstack1lll111lll1_opy_ = bstack11lll_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡸࡺࡡࡳࡶࡨࡨࠧႩ")
    FINISHED = bstack11lll_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢႪ")
class bstack1lll111llll_opy_:
    bstack1lll11l111l_opy_ = bstack11lll_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡦࡶࡪࡧࡴࡦࡦࠥႫ")
class bstack1lll11l11ll_opy_:
    _1llll1l11l1_opy_ = None
    def __new__(cls):
        if not cls._1llll1l11l1_opy_:
            cls._1llll1l11l1_opy_ = super(bstack1lll11l11ll_opy_, cls).__new__(cls)
        return cls._1llll1l11l1_opy_
    def __init__(self):
        self._hooks = defaultdict(lambda: defaultdict(list))
        self._lock = Lock()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def clear(self):
        with self._lock:
            self._hooks = defaultdict(list)
    def register(self, event_name, callback):
        with self._lock:
            if not callable(callback):
                raise ValueError(bstack11lll_opy_ (u"ࠧࡉࡡ࡭࡮ࡥࡥࡨࡱࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡥࡤࡰࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࠣႬ") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack11lll_opy_ (u"ࠨࡒࡦࡩ࡬ࡷࡹ࡫ࡲࡪࡰࡪࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࠢࠪࡿࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࡾࠩࠣࡻ࡮ࡺࡨࠡࡲ࡬ࡨࠥࠨႭ") + str(pid) + bstack11lll_opy_ (u"ࠢࠣႮ"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack11lll_opy_ (u"ࠣࡐࡲࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡹࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࠣࠫࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠪࠤࡼ࡯ࡴࡩࠢࡳ࡭ࡩࠦࠢႯ") + str(pid) + bstack11lll_opy_ (u"ࠤࠥႰ"))
                return
            self.logger.debug(bstack11lll_opy_ (u"ࠥࡍࡳࡼ࡯࡬࡫ࡱ࡫ࠥࢁ࡬ࡦࡰࠫࡧࡦࡲ࡬ࡣࡣࡦ࡯ࡸ࠯ࡽࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࡶࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࠠࠨࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠧࠡࡹ࡬ࡸ࡭ࠦࡰࡪࡦࠣࠦႱ") + str(pid) + bstack11lll_opy_ (u"ࠦࠧႲ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack11lll_opy_ (u"ࠧࡏ࡮ࡷࡱ࡮ࡩࡩࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࠣႳ") + str(pid) + bstack11lll_opy_ (u"ࠨࠢႴ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack11lll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࠦࠧࡼࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࢂ࠭ࠠࡸ࡫ࡷ࡬ࠥࡶࡩࡥࠢࡾࡴ࡮ࡪࡽ࠻ࠢࠥႵ") + str(e) + bstack11lll_opy_ (u"ࠣࠤႶ"))
                    traceback.print_exc()
bstack1l11ll11_opy_ = bstack1lll11l11ll_opy_()