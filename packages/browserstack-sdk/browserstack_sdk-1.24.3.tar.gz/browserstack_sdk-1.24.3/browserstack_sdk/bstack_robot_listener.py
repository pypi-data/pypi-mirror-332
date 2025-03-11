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
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11l111l1l1_opy_ import RobotHandler
from bstack_utils.capture import bstack11l11l1lll_opy_
from bstack_utils.bstack11l11l1l1l_opy_ import bstack111ll1l111_opy_, bstack11l1l1l111_opy_, bstack11l1l11lll_opy_
from bstack_utils.bstack11l11l1ll1_opy_ import bstack11l1ll1l1_opy_
from bstack_utils.bstack11l1l1l1l1_opy_ import bstack1ll111ll11_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l11lllll_opy_, bstack11111lll1_opy_, Result, \
    bstack11l111llll_opy_, bstack11l111ll1l_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack11lll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ໘"): [],
        bstack11lll_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭໙"): [],
        bstack11lll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬ໚"): []
    }
    bstack111llllll1_opy_ = []
    bstack111ll1ll1l_opy_ = []
    @staticmethod
    def bstack11l11l11ll_opy_(log):
        if not ((isinstance(log[bstack11lll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ໛")], list) or (isinstance(log[bstack11lll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫໜ")], dict)) and len(log[bstack11lll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬໝ")])>0) or (isinstance(log[bstack11lll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ໞ")], str) and log[bstack11lll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧໟ")].strip())):
            return
        active = bstack11l1ll1l1_opy_.bstack11l11l1l11_opy_()
        log = {
            bstack11lll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭໠"): log[bstack11lll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ໡")],
            bstack11lll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ໢"): bstack11l111ll1l_opy_().isoformat() + bstack11lll_opy_ (u"ࠪ࡞ࠬ໣"),
            bstack11lll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ໤"): log[bstack11lll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭໥")],
        }
        if active:
            if active[bstack11lll_opy_ (u"࠭ࡴࡺࡲࡨࠫ໦")] == bstack11lll_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ໧"):
                log[bstack11lll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ໨")] = active[bstack11lll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ໩")]
            elif active[bstack11lll_opy_ (u"ࠪࡸࡾࡶࡥࠨ໪")] == bstack11lll_opy_ (u"ࠫࡹ࡫ࡳࡵࠩ໫"):
                log[bstack11lll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ໬")] = active[bstack11lll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭໭")]
        bstack1ll111ll11_opy_.bstack1ll1ll1l11_opy_([log])
    def __init__(self):
        self.messages = bstack111llll111_opy_()
        self._111ll1llll_opy_ = None
        self._11l1111l1l_opy_ = None
        self._11l111ll11_opy_ = OrderedDict()
        self.bstack11l11ll11l_opy_ = bstack11l11l1lll_opy_(self.bstack11l11l11ll_opy_)
    @bstack11l111llll_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack111ll11l1l_opy_()
        if not self._11l111ll11_opy_.get(attrs.get(bstack11lll_opy_ (u"ࠧࡪࡦࠪ໮")), None):
            self._11l111ll11_opy_[attrs.get(bstack11lll_opy_ (u"ࠨ࡫ࡧࠫ໯"))] = {}
        bstack11l111lll1_opy_ = bstack11l1l11lll_opy_(
                bstack111lll1111_opy_=attrs.get(bstack11lll_opy_ (u"ࠩ࡬ࡨࠬ໰")),
                name=name,
                started_at=bstack11111lll1_opy_(),
                file_path=os.path.relpath(attrs[bstack11lll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ໱")], start=os.getcwd()) if attrs.get(bstack11lll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ໲")) != bstack11lll_opy_ (u"ࠬ࠭໳") else bstack11lll_opy_ (u"࠭ࠧ໴"),
                framework=bstack11lll_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭໵")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack11lll_opy_ (u"ࠨ࡫ࡧࠫ໶"), None)
        self._11l111ll11_opy_[attrs.get(bstack11lll_opy_ (u"ࠩ࡬ࡨࠬ໷"))][bstack11lll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭໸")] = bstack11l111lll1_opy_
    @bstack11l111llll_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack111lll1l1l_opy_()
        self._111llll11l_opy_(messages)
        for bstack11l111l1ll_opy_ in self.bstack111llllll1_opy_:
            bstack11l111l1ll_opy_[bstack11lll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭໹")][bstack11lll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ໺")].extend(self.store[bstack11lll_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬ໻")])
            bstack1ll111ll11_opy_.bstack1l11l1l1_opy_(bstack11l111l1ll_opy_)
        self.bstack111llllll1_opy_ = []
        self.store[bstack11lll_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭໼")] = []
    @bstack11l111llll_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11l11ll11l_opy_.start()
        if not self._11l111ll11_opy_.get(attrs.get(bstack11lll_opy_ (u"ࠨ࡫ࡧࠫ໽")), None):
            self._11l111ll11_opy_[attrs.get(bstack11lll_opy_ (u"ࠩ࡬ࡨࠬ໾"))] = {}
        driver = bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ໿"), None)
        bstack11l11l1l1l_opy_ = bstack11l1l11lll_opy_(
            bstack111lll1111_opy_=attrs.get(bstack11lll_opy_ (u"ࠫ࡮ࡪࠧༀ")),
            name=name,
            started_at=bstack11111lll1_opy_(),
            file_path=os.path.relpath(attrs[bstack11lll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ༁")], start=os.getcwd()),
            scope=RobotHandler.bstack111llll1ll_opy_(attrs.get(bstack11lll_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭༂"), None)),
            framework=bstack11lll_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭༃"),
            tags=attrs[bstack11lll_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭༄")],
            hooks=self.store[bstack11lll_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡡ࡫ࡳࡴࡱࡳࠨ༅")],
            bstack11l11ll1l1_opy_=bstack1ll111ll11_opy_.bstack11l1l111ll_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack11lll_opy_ (u"ࠥࡿࢂࠦ࡜࡯ࠢࡾࢁࠧ༆").format(bstack11lll_opy_ (u"ࠦࠥࠨ༇").join(attrs[bstack11lll_opy_ (u"ࠬࡺࡡࡨࡵࠪ༈")]), name) if attrs[bstack11lll_opy_ (u"࠭ࡴࡢࡩࡶࠫ༉")] else name
        )
        self._11l111ll11_opy_[attrs.get(bstack11lll_opy_ (u"ࠧࡪࡦࠪ༊"))][bstack11lll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ་")] = bstack11l11l1l1l_opy_
        threading.current_thread().current_test_uuid = bstack11l11l1l1l_opy_.bstack111ll1l1ll_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack11lll_opy_ (u"ࠩ࡬ࡨࠬ༌"), None)
        self.bstack11l1l11111_opy_(bstack11lll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ།"), bstack11l11l1l1l_opy_)
    @bstack11l111llll_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11l11ll11l_opy_.reset()
        bstack111lll111l_opy_ = bstack11l111l111_opy_.get(attrs.get(bstack11lll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ༎")), bstack11lll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭༏"))
        self._11l111ll11_opy_[attrs.get(bstack11lll_opy_ (u"࠭ࡩࡥࠩ༐"))][bstack11lll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ༑")].stop(time=bstack11111lll1_opy_(), duration=int(attrs.get(bstack11lll_opy_ (u"ࠨࡧ࡯ࡥࡵࡹࡥࡥࡶ࡬ࡱࡪ࠭༒"), bstack11lll_opy_ (u"ࠩ࠳ࠫ༓"))), result=Result(result=bstack111lll111l_opy_, exception=attrs.get(bstack11lll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ༔")), bstack11l11ll1ll_opy_=[attrs.get(bstack11lll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ༕"))]))
        self.bstack11l1l11111_opy_(bstack11lll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ༖"), self._11l111ll11_opy_[attrs.get(bstack11lll_opy_ (u"࠭ࡩࡥࠩ༗"))][bstack11lll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣ༘ࠪ")], True)
        self.store[bstack11lll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷ༙ࠬ")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack11l111llll_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack111ll11l1l_opy_()
        current_test_id = bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡧࠫ༚"), None)
        bstack111lll1ll1_opy_ = current_test_id if bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡨࠬ༛"), None) else bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡹࡵࡪࡶࡨࡣ࡮ࡪࠧ༜"), None)
        if attrs.get(bstack11lll_opy_ (u"ࠬࡺࡹࡱࡧࠪ༝"), bstack11lll_opy_ (u"࠭ࠧ༞")).lower() in [bstack11lll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭༟"), bstack11lll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪ༠")]:
            hook_type = bstack111lllll11_opy_(attrs.get(bstack11lll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ༡")), bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ༢"), None))
            hook_name = bstack11lll_opy_ (u"ࠫࢀࢃࠧ༣").format(attrs.get(bstack11lll_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬ༤"), bstack11lll_opy_ (u"࠭ࠧ༥")))
            if hook_type in [bstack11lll_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫ༦"), bstack11lll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫ༧")]:
                hook_name = bstack11lll_opy_ (u"ࠩ࡞ࡿࢂࡣࠠࡼࡿࠪ༨").format(bstack111ll1ll11_opy_.get(hook_type), attrs.get(bstack11lll_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪ༩"), bstack11lll_opy_ (u"ࠫࠬ༪")))
            bstack11l1111ll1_opy_ = bstack11l1l1l111_opy_(
                bstack111lll1111_opy_=bstack111lll1ll1_opy_ + bstack11lll_opy_ (u"ࠬ࠳ࠧ༫") + attrs.get(bstack11lll_opy_ (u"࠭ࡴࡺࡲࡨࠫ༬"), bstack11lll_opy_ (u"ࠧࠨ༭")).lower(),
                name=hook_name,
                started_at=bstack11111lll1_opy_(),
                file_path=os.path.relpath(attrs.get(bstack11lll_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ༮")), start=os.getcwd()),
                framework=bstack11lll_opy_ (u"ࠩࡕࡳࡧࡵࡴࠨ༯"),
                tags=attrs[bstack11lll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ༰")],
                scope=RobotHandler.bstack111llll1ll_opy_(attrs.get(bstack11lll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ༱"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack11l1111ll1_opy_.bstack111ll1l1ll_opy_()
            threading.current_thread().current_hook_id = bstack111lll1ll1_opy_ + bstack11lll_opy_ (u"ࠬ࠳ࠧ༲") + attrs.get(bstack11lll_opy_ (u"࠭ࡴࡺࡲࡨࠫ༳"), bstack11lll_opy_ (u"ࠧࠨ༴")).lower()
            self.store[bstack11lll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨ༵ࠬ")] = [bstack11l1111ll1_opy_.bstack111ll1l1ll_opy_()]
            if bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭༶"), None):
                self.store[bstack11lll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ༷ࠧ")].append(bstack11l1111ll1_opy_.bstack111ll1l1ll_opy_())
            else:
                self.store[bstack11lll_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪ༸")].append(bstack11l1111ll1_opy_.bstack111ll1l1ll_opy_())
            if bstack111lll1ll1_opy_:
                self._11l111ll11_opy_[bstack111lll1ll1_opy_ + bstack11lll_opy_ (u"ࠬ࠳༹ࠧ") + attrs.get(bstack11lll_opy_ (u"࠭ࡴࡺࡲࡨࠫ༺"), bstack11lll_opy_ (u"ࠧࠨ༻")).lower()] = { bstack11lll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ༼"): bstack11l1111ll1_opy_ }
            bstack1ll111ll11_opy_.bstack11l1l11111_opy_(bstack11lll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ༽"), bstack11l1111ll1_opy_)
        else:
            bstack11l1l11l11_opy_ = {
                bstack11lll_opy_ (u"ࠪ࡭ࡩ࠭༾"): uuid4().__str__(),
                bstack11lll_opy_ (u"ࠫࡹ࡫ࡸࡵࠩ༿"): bstack11lll_opy_ (u"ࠬࢁࡽࠡࡽࢀࠫཀ").format(attrs.get(bstack11lll_opy_ (u"࠭࡫ࡸࡰࡤࡱࡪ࠭ཁ")), attrs.get(bstack11lll_opy_ (u"ࠧࡢࡴࡪࡷࠬག"), bstack11lll_opy_ (u"ࠨࠩགྷ"))) if attrs.get(bstack11lll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧང"), []) else attrs.get(bstack11lll_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪཅ")),
                bstack11lll_opy_ (u"ࠫࡸࡺࡥࡱࡡࡤࡶ࡬ࡻ࡭ࡦࡰࡷࠫཆ"): attrs.get(bstack11lll_opy_ (u"ࠬࡧࡲࡨࡵࠪཇ"), []),
                bstack11lll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ཈"): bstack11111lll1_opy_(),
                bstack11lll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧཉ"): bstack11lll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩཊ"),
                bstack11lll_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧཋ"): attrs.get(bstack11lll_opy_ (u"ࠪࡨࡴࡩࠧཌ"), bstack11lll_opy_ (u"ࠫࠬཌྷ"))
            }
            if attrs.get(bstack11lll_opy_ (u"ࠬࡲࡩࡣࡰࡤࡱࡪ࠭ཎ"), bstack11lll_opy_ (u"࠭ࠧཏ")) != bstack11lll_opy_ (u"ࠧࠨཐ"):
                bstack11l1l11l11_opy_[bstack11lll_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩད")] = attrs.get(bstack11lll_opy_ (u"ࠩ࡯࡭ࡧࡴࡡ࡮ࡧࠪདྷ"))
            if not self.bstack111ll1ll1l_opy_:
                self._11l111ll11_opy_[self._11l111111l_opy_()][bstack11lll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ན")].add_step(bstack11l1l11l11_opy_)
                threading.current_thread().current_step_uuid = bstack11l1l11l11_opy_[bstack11lll_opy_ (u"ࠫ࡮ࡪࠧཔ")]
            self.bstack111ll1ll1l_opy_.append(bstack11l1l11l11_opy_)
    @bstack11l111llll_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack111lll1l1l_opy_()
        self._111llll11l_opy_(messages)
        current_test_id = bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡪࠧཕ"), None)
        bstack111lll1ll1_opy_ = current_test_id if current_test_id else bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡷ࡬ࡸࡪࡥࡩࡥࠩབ"), None)
        bstack11l111l11l_opy_ = bstack11l111l111_opy_.get(attrs.get(bstack11lll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧབྷ")), bstack11lll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩམ"))
        bstack111ll111ll_opy_ = attrs.get(bstack11lll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪཙ"))
        if bstack11l111l11l_opy_ != bstack11lll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫཚ") and not attrs.get(bstack11lll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬཛ")) and self._111ll1llll_opy_:
            bstack111ll111ll_opy_ = self._111ll1llll_opy_
        bstack11l1l111l1_opy_ = Result(result=bstack11l111l11l_opy_, exception=bstack111ll111ll_opy_, bstack11l11ll1ll_opy_=[bstack111ll111ll_opy_])
        if attrs.get(bstack11lll_opy_ (u"ࠬࡺࡹࡱࡧࠪཛྷ"), bstack11lll_opy_ (u"࠭ࠧཝ")).lower() in [bstack11lll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ཞ"), bstack11lll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪཟ")]:
            bstack111lll1ll1_opy_ = current_test_id if current_test_id else bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡺ࡯ࡴࡦࡡ࡬ࡨࠬའ"), None)
            if bstack111lll1ll1_opy_:
                bstack11l11lll1l_opy_ = bstack111lll1ll1_opy_ + bstack11lll_opy_ (u"ࠥ࠱ࠧཡ") + attrs.get(bstack11lll_opy_ (u"ࠫࡹࡿࡰࡦࠩར"), bstack11lll_opy_ (u"ࠬ࠭ལ")).lower()
                self._11l111ll11_opy_[bstack11l11lll1l_opy_][bstack11lll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩཤ")].stop(time=bstack11111lll1_opy_(), duration=int(attrs.get(bstack11lll_opy_ (u"ࠧࡦ࡮ࡤࡴࡸ࡫ࡤࡵ࡫ࡰࡩࠬཥ"), bstack11lll_opy_ (u"ࠨ࠲ࠪས"))), result=bstack11l1l111l1_opy_)
                bstack1ll111ll11_opy_.bstack11l1l11111_opy_(bstack11lll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫཧ"), self._11l111ll11_opy_[bstack11l11lll1l_opy_][bstack11lll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ཨ")])
        else:
            bstack111lll1ll1_opy_ = current_test_id if current_test_id else bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢ࡭ࡩ࠭ཀྵ"), None)
            if bstack111lll1ll1_opy_ and len(self.bstack111ll1ll1l_opy_) == 1:
                current_step_uuid = bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡳࡵࡧࡳࡣࡺࡻࡩࡥࠩཪ"), None)
                self._11l111ll11_opy_[bstack111lll1ll1_opy_][bstack11lll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩཫ")].bstack11l11l111l_opy_(current_step_uuid, duration=int(attrs.get(bstack11lll_opy_ (u"ࠧࡦ࡮ࡤࡴࡸ࡫ࡤࡵ࡫ࡰࡩࠬཬ"), bstack11lll_opy_ (u"ࠨ࠲ࠪ཭"))), result=bstack11l1l111l1_opy_)
            else:
                self.bstack111ll1lll1_opy_(attrs)
            self.bstack111ll1ll1l_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack11lll_opy_ (u"ࠩ࡫ࡸࡲࡲࠧ཮"), bstack11lll_opy_ (u"ࠪࡲࡴ࠭཯")) == bstack11lll_opy_ (u"ࠫࡾ࡫ࡳࠨ཰"):
                return
            self.messages.push(message)
            logs = []
            if bstack11l1ll1l1_opy_.bstack11l11l1l11_opy_():
                logs.append({
                    bstack11lll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨཱ"): bstack11111lll1_opy_(),
                    bstack11lll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ིࠧ"): message.get(bstack11lll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨཱི")),
                    bstack11lll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲུࠧ"): message.get(bstack11lll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨཱུ")),
                    **bstack11l1ll1l1_opy_.bstack11l11l1l11_opy_()
                })
                if len(logs) > 0:
                    bstack1ll111ll11_opy_.bstack1ll1ll1l11_opy_(logs)
        except Exception as err:
            pass
    def close(self):
        bstack1ll111ll11_opy_.bstack111ll1l1l1_opy_()
    def bstack111ll1lll1_opy_(self, bstack11l11l1111_opy_):
        if not bstack11l1ll1l1_opy_.bstack11l11l1l11_opy_():
            return
        kwname = bstack11lll_opy_ (u"ࠪࡿࢂࠦࡻࡾࠩྲྀ").format(bstack11l11l1111_opy_.get(bstack11lll_opy_ (u"ࠫࡰࡽ࡮ࡢ࡯ࡨࠫཷ")), bstack11l11l1111_opy_.get(bstack11lll_opy_ (u"ࠬࡧࡲࡨࡵࠪླྀ"), bstack11lll_opy_ (u"࠭ࠧཹ"))) if bstack11l11l1111_opy_.get(bstack11lll_opy_ (u"ࠧࡢࡴࡪࡷེࠬ"), []) else bstack11l11l1111_opy_.get(bstack11lll_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨཻ"))
        error_message = bstack11lll_opy_ (u"ࠤ࡮ࡻࡳࡧ࡭ࡦ࠼ࠣࡠࠧࢁ࠰ࡾ࡞ࠥࠤࢁࠦࡳࡵࡣࡷࡹࡸࡀࠠ࡝ࠤࡾ࠵ࢂࡢࠢࠡࡾࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠ࡝ࠤࡾ࠶ࢂࡢོࠢࠣ").format(kwname, bstack11l11l1111_opy_.get(bstack11lll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵཽࠪ")), str(bstack11l11l1111_opy_.get(bstack11lll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬཾ"))))
        bstack111lllllll_opy_ = bstack11lll_opy_ (u"ࠧࡱࡷ࡯ࡣࡰࡩ࠿ࠦ࡜ࠣࡽ࠳ࢁࡡࠨࠠࡽࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡠࠧࢁ࠱ࡾ࡞ࠥࠦཿ").format(kwname, bstack11l11l1111_opy_.get(bstack11lll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸྀ࠭")))
        bstack111lll1l11_opy_ = error_message if bstack11l11l1111_opy_.get(bstack11lll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨཱྀ")) else bstack111lllllll_opy_
        bstack111ll111l1_opy_ = {
            bstack11lll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫྂ"): self.bstack111ll1ll1l_opy_[-1].get(bstack11lll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ྃ"), bstack11111lll1_opy_()),
            bstack11lll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨ྄ࠫ"): bstack111lll1l11_opy_,
            bstack11lll_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ྅"): bstack11lll_opy_ (u"ࠬࡋࡒࡓࡑࡕࠫ྆") if bstack11l11l1111_opy_.get(bstack11lll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭྇")) == bstack11lll_opy_ (u"ࠧࡇࡃࡌࡐࠬྈ") else bstack11lll_opy_ (u"ࠨࡋࡑࡊࡔ࠭ྉ"),
            **bstack11l1ll1l1_opy_.bstack11l11l1l11_opy_()
        }
        bstack1ll111ll11_opy_.bstack1ll1ll1l11_opy_([bstack111ll111l1_opy_])
    def _11l111111l_opy_(self):
        for bstack111lll1111_opy_ in reversed(self._11l111ll11_opy_):
            bstack11l11111l1_opy_ = bstack111lll1111_opy_
            data = self._11l111ll11_opy_[bstack111lll1111_opy_][bstack11lll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬྊ")]
            if isinstance(data, bstack11l1l1l111_opy_):
                if not bstack11lll_opy_ (u"ࠪࡉࡆࡉࡈࠨྋ") in data.bstack111ll1l11l_opy_():
                    return bstack11l11111l1_opy_
            else:
                return bstack11l11111l1_opy_
    def _111llll11l_opy_(self, messages):
        try:
            bstack111lll11ll_opy_ = BuiltIn().get_variable_value(bstack11lll_opy_ (u"ࠦࠩࢁࡌࡐࡉࠣࡐࡊ࡜ࡅࡍࡿࠥྌ")) in (bstack11l1111l11_opy_.DEBUG, bstack11l1111l11_opy_.TRACE)
            for message, bstack111lllll1l_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack11lll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ྍ"))
                level = message.get(bstack11lll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬྎ"))
                if level == bstack11l1111l11_opy_.FAIL:
                    self._111ll1llll_opy_ = name or self._111ll1llll_opy_
                    self._11l1111l1l_opy_ = bstack111lllll1l_opy_.get(bstack11lll_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣྏ")) if bstack111lll11ll_opy_ and bstack111lllll1l_opy_ else self._11l1111l1l_opy_
        except:
            pass
    @classmethod
    def bstack11l1l11111_opy_(self, event: str, bstack111ll11l11_opy_: bstack111ll1l111_opy_, bstack111lll1lll_opy_=False):
        if event == bstack11lll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪྐ"):
            bstack111ll11l11_opy_.set(hooks=self.store[bstack11lll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭ྑ")])
        if event == bstack11lll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫྒ"):
            event = bstack11lll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ྒྷ")
        if bstack111lll1lll_opy_:
            bstack111ll1111l_opy_ = {
                bstack11lll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩྔ"): event,
                bstack111ll11l11_opy_.bstack11l1111lll_opy_(): bstack111ll11l11_opy_.bstack111ll11lll_opy_(event)
            }
            self.bstack111llllll1_opy_.append(bstack111ll1111l_opy_)
        else:
            bstack1ll111ll11_opy_.bstack11l1l11111_opy_(event, bstack111ll11l11_opy_)
class bstack111llll111_opy_:
    def __init__(self):
        self._111lll11l1_opy_ = []
    def bstack111ll11l1l_opy_(self):
        self._111lll11l1_opy_.append([])
    def bstack111lll1l1l_opy_(self):
        return self._111lll11l1_opy_.pop() if self._111lll11l1_opy_ else list()
    def push(self, message):
        self._111lll11l1_opy_[-1].append(message) if self._111lll11l1_opy_ else self._111lll11l1_opy_.append([message])
class bstack11l1111l11_opy_:
    FAIL = bstack11lll_opy_ (u"࠭ࡆࡂࡋࡏࠫྕ")
    ERROR = bstack11lll_opy_ (u"ࠧࡆࡔࡕࡓࡗ࠭ྖ")
    WARNING = bstack11lll_opy_ (u"ࠨ࡙ࡄࡖࡓ࠭ྗ")
    bstack111llll1l1_opy_ = bstack11lll_opy_ (u"ࠩࡌࡒࡋࡕࠧ྘")
    DEBUG = bstack11lll_opy_ (u"ࠪࡈࡊࡈࡕࡈࠩྙ")
    TRACE = bstack11lll_opy_ (u"࡙ࠫࡘࡁࡄࡇࠪྚ")
    bstack111ll11ll1_opy_ = [FAIL, ERROR]
def bstack11l1111111_opy_(bstack11l11111ll_opy_):
    if not bstack11l11111ll_opy_:
        return None
    if bstack11l11111ll_opy_.get(bstack11lll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨྛ"), None):
        return getattr(bstack11l11111ll_opy_[bstack11lll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩྜ")], bstack11lll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬྜྷ"), None)
    return bstack11l11111ll_opy_.get(bstack11lll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ྞ"), None)
def bstack111lllll11_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack11lll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨྟ"), bstack11lll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬྠ")]:
        return
    if hook_type.lower() == bstack11lll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪྡ"):
        if current_test_uuid is None:
            return bstack11lll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩྡྷ")
        else:
            return bstack11lll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫྣ")
    elif hook_type.lower() == bstack11lll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩྤ"):
        if current_test_uuid is None:
            return bstack11lll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫྥ")
        else:
            return bstack11lll_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ྦ")