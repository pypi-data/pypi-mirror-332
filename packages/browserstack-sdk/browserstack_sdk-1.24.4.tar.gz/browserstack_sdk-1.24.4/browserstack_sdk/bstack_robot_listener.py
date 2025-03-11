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
import os
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11l111llll_opy_ import RobotHandler
from bstack_utils.capture import bstack11l11llll1_opy_
from bstack_utils.bstack11l11l1ll1_opy_ import bstack111llll1ll_opy_, bstack11l1l11l11_opy_, bstack11l11l1l1l_opy_
from bstack_utils.bstack11l1l1111l_opy_ import bstack111111ll_opy_
from bstack_utils.bstack11l1l11lll_opy_ import bstack1ll11l1l11_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack11l1ll1l_opy_, bstack1l1ll1111l_opy_, Result, \
    bstack111ll1l1ll_opy_, bstack11l111ll1l_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack11ll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ໘"): [],
        bstack11ll1l_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭໙"): [],
        bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬ໚"): []
    }
    bstack111ll1ll11_opy_ = []
    bstack11l111l111_opy_ = []
    @staticmethod
    def bstack11l11l1lll_opy_(log):
        if not ((isinstance(log[bstack11ll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ໛")], list) or (isinstance(log[bstack11ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫໜ")], dict)) and len(log[bstack11ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬໝ")])>0) or (isinstance(log[bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ໞ")], str) and log[bstack11ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧໟ")].strip())):
            return
        active = bstack111111ll_opy_.bstack11l1l1l111_opy_()
        log = {
            bstack11ll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭໠"): log[bstack11ll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ໡")],
            bstack11ll1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ໢"): bstack11l111ll1l_opy_().isoformat() + bstack11ll1l_opy_ (u"ࠪ࡞ࠬ໣"),
            bstack11ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ໤"): log[bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭໥")],
        }
        if active:
            if active[bstack11ll1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ໦")] == bstack11ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ໧"):
                log[bstack11ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ໨")] = active[bstack11ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ໩")]
            elif active[bstack11ll1l_opy_ (u"ࠪࡸࡾࡶࡥࠨ໪")] == bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࠩ໫"):
                log[bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ໬")] = active[bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭໭")]
        bstack1ll11l1l11_opy_.bstack1l1lllll_opy_([log])
    def __init__(self):
        self.messages = bstack11l1111l11_opy_()
        self._111llll11l_opy_ = None
        self._11l11111ll_opy_ = None
        self._111llllll1_opy_ = OrderedDict()
        self.bstack11l1l111l1_opy_ = bstack11l11llll1_opy_(self.bstack11l11l1lll_opy_)
    @bstack111ll1l1ll_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack111ll1l111_opy_()
        if not self._111llllll1_opy_.get(attrs.get(bstack11ll1l_opy_ (u"ࠧࡪࡦࠪ໮")), None):
            self._111llllll1_opy_[attrs.get(bstack11ll1l_opy_ (u"ࠨ࡫ࡧࠫ໯"))] = {}
        bstack111ll1l1l1_opy_ = bstack11l11l1l1l_opy_(
                bstack111ll11lll_opy_=attrs.get(bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬ໰")),
                name=name,
                started_at=bstack1l1ll1111l_opy_(),
                file_path=os.path.relpath(attrs[bstack11ll1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ໱")], start=os.getcwd()) if attrs.get(bstack11ll1l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ໲")) != bstack11ll1l_opy_ (u"ࠬ࠭໳") else bstack11ll1l_opy_ (u"࠭ࠧ໴"),
                framework=bstack11ll1l_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭໵")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack11ll1l_opy_ (u"ࠨ࡫ࡧࠫ໶"), None)
        self._111llllll1_opy_[attrs.get(bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬ໷"))][bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭໸")] = bstack111ll1l1l1_opy_
    @bstack111ll1l1ll_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack11l111ll11_opy_()
        self._111ll11ll1_opy_(messages)
        for bstack111ll1l11l_opy_ in self.bstack111ll1ll11_opy_:
            bstack111ll1l11l_opy_[bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭໹")][bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ໺")].extend(self.store[bstack11ll1l_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬ໻")])
            bstack1ll11l1l11_opy_.bstack1l11lll11_opy_(bstack111ll1l11l_opy_)
        self.bstack111ll1ll11_opy_ = []
        self.store[bstack11ll1l_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭໼")] = []
    @bstack111ll1l1ll_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11l1l111l1_opy_.start()
        if not self._111llllll1_opy_.get(attrs.get(bstack11ll1l_opy_ (u"ࠨ࡫ࡧࠫ໽")), None):
            self._111llllll1_opy_[attrs.get(bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬ໾"))] = {}
        driver = bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ໿"), None)
        bstack11l11l1ll1_opy_ = bstack11l11l1l1l_opy_(
            bstack111ll11lll_opy_=attrs.get(bstack11ll1l_opy_ (u"ࠫ࡮ࡪࠧༀ")),
            name=name,
            started_at=bstack1l1ll1111l_opy_(),
            file_path=os.path.relpath(attrs[bstack11ll1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ༁")], start=os.getcwd()),
            scope=RobotHandler.bstack111ll1111l_opy_(attrs.get(bstack11ll1l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭༂"), None)),
            framework=bstack11ll1l_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭༃"),
            tags=attrs[bstack11ll1l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭༄")],
            hooks=self.store[bstack11ll1l_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡡ࡫ࡳࡴࡱࡳࠨ༅")],
            bstack11l11l11l1_opy_=bstack1ll11l1l11_opy_.bstack11l11ll111_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack11ll1l_opy_ (u"ࠥࡿࢂࠦ࡜࡯ࠢࡾࢁࠧ༆").format(bstack11ll1l_opy_ (u"ࠦࠥࠨ༇").join(attrs[bstack11ll1l_opy_ (u"ࠬࡺࡡࡨࡵࠪ༈")]), name) if attrs[bstack11ll1l_opy_ (u"࠭ࡴࡢࡩࡶࠫ༉")] else name
        )
        self._111llllll1_opy_[attrs.get(bstack11ll1l_opy_ (u"ࠧࡪࡦࠪ༊"))][bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ་")] = bstack11l11l1ll1_opy_
        threading.current_thread().current_test_uuid = bstack11l11l1ll1_opy_.bstack111ll1llll_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬ༌"), None)
        self.bstack11l11ll1l1_opy_(bstack11ll1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ།"), bstack11l11l1ll1_opy_)
    @bstack111ll1l1ll_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11l1l111l1_opy_.reset()
        bstack11l111l1l1_opy_ = bstack111llll1l1_opy_.get(attrs.get(bstack11ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ༎")), bstack11ll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭༏"))
        self._111llllll1_opy_[attrs.get(bstack11ll1l_opy_ (u"࠭ࡩࡥࠩ༐"))][bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ༑")].stop(time=bstack1l1ll1111l_opy_(), duration=int(attrs.get(bstack11ll1l_opy_ (u"ࠨࡧ࡯ࡥࡵࡹࡥࡥࡶ࡬ࡱࡪ࠭༒"), bstack11ll1l_opy_ (u"ࠩ࠳ࠫ༓"))), result=Result(result=bstack11l111l1l1_opy_, exception=attrs.get(bstack11ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ༔")), bstack11l1l1l11l_opy_=[attrs.get(bstack11ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ༕"))]))
        self.bstack11l11ll1l1_opy_(bstack11ll1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ༖"), self._111llllll1_opy_[attrs.get(bstack11ll1l_opy_ (u"࠭ࡩࡥࠩ༗"))][bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣ༘ࠪ")], True)
        self.store[bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷ༙ࠬ")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack111ll1l1ll_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack111ll1l111_opy_()
        current_test_id = bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡧࠫ༚"), None)
        bstack11l111l1ll_opy_ = current_test_id if bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡨࠬ༛"), None) else bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡹࡵࡪࡶࡨࡣ࡮ࡪࠧ༜"), None)
        if attrs.get(bstack11ll1l_opy_ (u"ࠬࡺࡹࡱࡧࠪ༝"), bstack11ll1l_opy_ (u"࠭ࠧ༞")).lower() in [bstack11ll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭༟"), bstack11ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪ༠")]:
            hook_type = bstack111ll1ll1l_opy_(attrs.get(bstack11ll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ༡")), bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ༢"), None))
            hook_name = bstack11ll1l_opy_ (u"ࠫࢀࢃࠧ༣").format(attrs.get(bstack11ll1l_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬ༤"), bstack11ll1l_opy_ (u"࠭ࠧ༥")))
            if hook_type in [bstack11ll1l_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫ༦"), bstack11ll1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫ༧")]:
                hook_name = bstack11ll1l_opy_ (u"ࠩ࡞ࡿࢂࡣࠠࡼࡿࠪ༨").format(bstack111ll1lll1_opy_.get(hook_type), attrs.get(bstack11ll1l_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪ༩"), bstack11ll1l_opy_ (u"ࠫࠬ༪")))
            bstack11l1111l1l_opy_ = bstack11l1l11l11_opy_(
                bstack111ll11lll_opy_=bstack11l111l1ll_opy_ + bstack11ll1l_opy_ (u"ࠬ࠳ࠧ༫") + attrs.get(bstack11ll1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ༬"), bstack11ll1l_opy_ (u"ࠧࠨ༭")).lower(),
                name=hook_name,
                started_at=bstack1l1ll1111l_opy_(),
                file_path=os.path.relpath(attrs.get(bstack11ll1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ༮")), start=os.getcwd()),
                framework=bstack11ll1l_opy_ (u"ࠩࡕࡳࡧࡵࡴࠨ༯"),
                tags=attrs[bstack11ll1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ༰")],
                scope=RobotHandler.bstack111ll1111l_opy_(attrs.get(bstack11ll1l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ༱"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack11l1111l1l_opy_.bstack111ll1llll_opy_()
            threading.current_thread().current_hook_id = bstack11l111l1ll_opy_ + bstack11ll1l_opy_ (u"ࠬ࠳ࠧ༲") + attrs.get(bstack11ll1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ༳"), bstack11ll1l_opy_ (u"ࠧࠨ༴")).lower()
            self.store[bstack11ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨ༵ࠬ")] = [bstack11l1111l1l_opy_.bstack111ll1llll_opy_()]
            if bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭༶"), None):
                self.store[bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ༷ࠧ")].append(bstack11l1111l1l_opy_.bstack111ll1llll_opy_())
            else:
                self.store[bstack11ll1l_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪ༸")].append(bstack11l1111l1l_opy_.bstack111ll1llll_opy_())
            if bstack11l111l1ll_opy_:
                self._111llllll1_opy_[bstack11l111l1ll_opy_ + bstack11ll1l_opy_ (u"ࠬ࠳༹ࠧ") + attrs.get(bstack11ll1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ༺"), bstack11ll1l_opy_ (u"ࠧࠨ༻")).lower()] = { bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ༼"): bstack11l1111l1l_opy_ }
            bstack1ll11l1l11_opy_.bstack11l11ll1l1_opy_(bstack11ll1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ༽"), bstack11l1111l1l_opy_)
        else:
            bstack11l11ll1ll_opy_ = {
                bstack11ll1l_opy_ (u"ࠪ࡭ࡩ࠭༾"): uuid4().__str__(),
                bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡸࡵࠩ༿"): bstack11ll1l_opy_ (u"ࠬࢁࡽࠡࡽࢀࠫཀ").format(attrs.get(bstack11ll1l_opy_ (u"࠭࡫ࡸࡰࡤࡱࡪ࠭ཁ")), attrs.get(bstack11ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬག"), bstack11ll1l_opy_ (u"ࠨࠩགྷ"))) if attrs.get(bstack11ll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧང"), []) else attrs.get(bstack11ll1l_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪཅ")),
                bstack11ll1l_opy_ (u"ࠫࡸࡺࡥࡱࡡࡤࡶ࡬ࡻ࡭ࡦࡰࡷࠫཆ"): attrs.get(bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪཇ"), []),
                bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ཈"): bstack1l1ll1111l_opy_(),
                bstack11ll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧཉ"): bstack11ll1l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩཊ"),
                bstack11ll1l_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧཋ"): attrs.get(bstack11ll1l_opy_ (u"ࠪࡨࡴࡩࠧཌ"), bstack11ll1l_opy_ (u"ࠫࠬཌྷ"))
            }
            if attrs.get(bstack11ll1l_opy_ (u"ࠬࡲࡩࡣࡰࡤࡱࡪ࠭ཎ"), bstack11ll1l_opy_ (u"࠭ࠧཏ")) != bstack11ll1l_opy_ (u"ࠧࠨཐ"):
                bstack11l11ll1ll_opy_[bstack11ll1l_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩད")] = attrs.get(bstack11ll1l_opy_ (u"ࠩ࡯࡭ࡧࡴࡡ࡮ࡧࠪདྷ"))
            if not self.bstack11l111l111_opy_:
                self._111llllll1_opy_[self._11l1111111_opy_()][bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ན")].add_step(bstack11l11ll1ll_opy_)
                threading.current_thread().current_step_uuid = bstack11l11ll1ll_opy_[bstack11ll1l_opy_ (u"ࠫ࡮ࡪࠧཔ")]
            self.bstack11l111l111_opy_.append(bstack11l11ll1ll_opy_)
    @bstack111ll1l1ll_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack11l111ll11_opy_()
        self._111ll11ll1_opy_(messages)
        current_test_id = bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡪࠧཕ"), None)
        bstack11l111l1ll_opy_ = current_test_id if current_test_id else bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡷ࡬ࡸࡪࡥࡩࡥࠩབ"), None)
        bstack111ll11l1l_opy_ = bstack111llll1l1_opy_.get(attrs.get(bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧབྷ")), bstack11ll1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩམ"))
        bstack111lll1lll_opy_ = attrs.get(bstack11ll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪཙ"))
        if bstack111ll11l1l_opy_ != bstack11ll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫཚ") and not attrs.get(bstack11ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬཛ")) and self._111llll11l_opy_:
            bstack111lll1lll_opy_ = self._111llll11l_opy_
        bstack11l11l111l_opy_ = Result(result=bstack111ll11l1l_opy_, exception=bstack111lll1lll_opy_, bstack11l1l1l11l_opy_=[bstack111lll1lll_opy_])
        if attrs.get(bstack11ll1l_opy_ (u"ࠬࡺࡹࡱࡧࠪཛྷ"), bstack11ll1l_opy_ (u"࠭ࠧཝ")).lower() in [bstack11ll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ཞ"), bstack11ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪཟ")]:
            bstack11l111l1ll_opy_ = current_test_id if current_test_id else bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡺ࡯ࡴࡦࡡ࡬ࡨࠬའ"), None)
            if bstack11l111l1ll_opy_:
                bstack11l11l11ll_opy_ = bstack11l111l1ll_opy_ + bstack11ll1l_opy_ (u"ࠥ࠱ࠧཡ") + attrs.get(bstack11ll1l_opy_ (u"ࠫࡹࡿࡰࡦࠩར"), bstack11ll1l_opy_ (u"ࠬ࠭ལ")).lower()
                self._111llllll1_opy_[bstack11l11l11ll_opy_][bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩཤ")].stop(time=bstack1l1ll1111l_opy_(), duration=int(attrs.get(bstack11ll1l_opy_ (u"ࠧࡦ࡮ࡤࡴࡸ࡫ࡤࡵ࡫ࡰࡩࠬཥ"), bstack11ll1l_opy_ (u"ࠨ࠲ࠪས"))), result=bstack11l11l111l_opy_)
                bstack1ll11l1l11_opy_.bstack11l11ll1l1_opy_(bstack11ll1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫཧ"), self._111llllll1_opy_[bstack11l11l11ll_opy_][bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ཨ")])
        else:
            bstack11l111l1ll_opy_ = current_test_id if current_test_id else bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢ࡭ࡩ࠭ཀྵ"), None)
            if bstack11l111l1ll_opy_ and len(self.bstack11l111l111_opy_) == 1:
                current_step_uuid = bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡳࡵࡧࡳࡣࡺࡻࡩࡥࠩཪ"), None)
                self._111llllll1_opy_[bstack11l111l1ll_opy_][bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩཫ")].bstack11l11lllll_opy_(current_step_uuid, duration=int(attrs.get(bstack11ll1l_opy_ (u"ࠧࡦ࡮ࡤࡴࡸ࡫ࡤࡵ࡫ࡰࡩࠬཬ"), bstack11ll1l_opy_ (u"ࠨ࠲ࠪ཭"))), result=bstack11l11l111l_opy_)
            else:
                self.bstack111lll1111_opy_(attrs)
            self.bstack11l111l111_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack11ll1l_opy_ (u"ࠩ࡫ࡸࡲࡲࠧ཮"), bstack11ll1l_opy_ (u"ࠪࡲࡴ࠭཯")) == bstack11ll1l_opy_ (u"ࠫࡾ࡫ࡳࠨ཰"):
                return
            self.messages.push(message)
            logs = []
            if bstack111111ll_opy_.bstack11l1l1l111_opy_():
                logs.append({
                    bstack11ll1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨཱ"): bstack1l1ll1111l_opy_(),
                    bstack11ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ིࠧ"): message.get(bstack11ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨཱི")),
                    bstack11ll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲུࠧ"): message.get(bstack11ll1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨཱུ")),
                    **bstack111111ll_opy_.bstack11l1l1l111_opy_()
                })
                if len(logs) > 0:
                    bstack1ll11l1l11_opy_.bstack1l1lllll_opy_(logs)
        except Exception as err:
            pass
    def close(self):
        bstack1ll11l1l11_opy_.bstack111lllllll_opy_()
    def bstack111lll1111_opy_(self, bstack111lll111l_opy_):
        if not bstack111111ll_opy_.bstack11l1l1l111_opy_():
            return
        kwname = bstack11ll1l_opy_ (u"ࠪࡿࢂࠦࡻࡾࠩྲྀ").format(bstack111lll111l_opy_.get(bstack11ll1l_opy_ (u"ࠫࡰࡽ࡮ࡢ࡯ࡨࠫཷ")), bstack111lll111l_opy_.get(bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪླྀ"), bstack11ll1l_opy_ (u"࠭ࠧཹ"))) if bstack111lll111l_opy_.get(bstack11ll1l_opy_ (u"ࠧࡢࡴࡪࡷེࠬ"), []) else bstack111lll111l_opy_.get(bstack11ll1l_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨཻ"))
        error_message = bstack11ll1l_opy_ (u"ࠤ࡮ࡻࡳࡧ࡭ࡦ࠼ࠣࡠࠧࢁ࠰ࡾ࡞ࠥࠤࢁࠦࡳࡵࡣࡷࡹࡸࡀࠠ࡝ࠤࡾ࠵ࢂࡢࠢࠡࡾࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠ࡝ࠤࡾ࠶ࢂࡢོࠢࠣ").format(kwname, bstack111lll111l_opy_.get(bstack11ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵཽࠪ")), str(bstack111lll111l_opy_.get(bstack11ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬཾ"))))
        bstack11l11l1111_opy_ = bstack11ll1l_opy_ (u"ࠧࡱࡷ࡯ࡣࡰࡩ࠿ࠦ࡜ࠣࡽ࠳ࢁࡡࠨࠠࡽࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡠࠧࢁ࠱ࡾ࡞ࠥࠦཿ").format(kwname, bstack111lll111l_opy_.get(bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸྀ࠭")))
        bstack111lll11l1_opy_ = error_message if bstack111lll111l_opy_.get(bstack11ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨཱྀ")) else bstack11l11l1111_opy_
        bstack111lll1l1l_opy_ = {
            bstack11ll1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫྂ"): self.bstack11l111l111_opy_[-1].get(bstack11ll1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ྃ"), bstack1l1ll1111l_opy_()),
            bstack11ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨ྄ࠫ"): bstack111lll11l1_opy_,
            bstack11ll1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ྅"): bstack11ll1l_opy_ (u"ࠬࡋࡒࡓࡑࡕࠫ྆") if bstack111lll111l_opy_.get(bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭྇")) == bstack11ll1l_opy_ (u"ࠧࡇࡃࡌࡐࠬྈ") else bstack11ll1l_opy_ (u"ࠨࡋࡑࡊࡔ࠭ྉ"),
            **bstack111111ll_opy_.bstack11l1l1l111_opy_()
        }
        bstack1ll11l1l11_opy_.bstack1l1lllll_opy_([bstack111lll1l1l_opy_])
    def _11l1111111_opy_(self):
        for bstack111ll11lll_opy_ in reversed(self._111llllll1_opy_):
            bstack111lllll1l_opy_ = bstack111ll11lll_opy_
            data = self._111llllll1_opy_[bstack111ll11lll_opy_][bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬྊ")]
            if isinstance(data, bstack11l1l11l11_opy_):
                if not bstack11ll1l_opy_ (u"ࠪࡉࡆࡉࡈࠨྋ") in data.bstack111lllll11_opy_():
                    return bstack111lllll1l_opy_
            else:
                return bstack111lllll1l_opy_
    def _111ll11ll1_opy_(self, messages):
        try:
            bstack111lll1ll1_opy_ = BuiltIn().get_variable_value(bstack11ll1l_opy_ (u"ࠦࠩࢁࡌࡐࡉࠣࡐࡊ࡜ࡅࡍࡿࠥྌ")) in (bstack111ll11l11_opy_.DEBUG, bstack111ll11l11_opy_.TRACE)
            for message, bstack11l11111l1_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ྍ"))
                level = message.get(bstack11ll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬྎ"))
                if level == bstack111ll11l11_opy_.FAIL:
                    self._111llll11l_opy_ = name or self._111llll11l_opy_
                    self._11l11111ll_opy_ = bstack11l11111l1_opy_.get(bstack11ll1l_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣྏ")) if bstack111lll1ll1_opy_ and bstack11l11111l1_opy_ else self._11l11111ll_opy_
        except:
            pass
    @classmethod
    def bstack11l11ll1l1_opy_(self, event: str, bstack11l111111l_opy_: bstack111llll1ll_opy_, bstack111llll111_opy_=False):
        if event == bstack11ll1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪྐ"):
            bstack11l111111l_opy_.set(hooks=self.store[bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭ྑ")])
        if event == bstack11ll1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫྒ"):
            event = bstack11ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ྒྷ")
        if bstack111llll111_opy_:
            bstack11l111lll1_opy_ = {
                bstack11ll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩྔ"): event,
                bstack11l111111l_opy_.bstack111ll111ll_opy_(): bstack11l111111l_opy_.bstack11l111l11l_opy_(event)
            }
            self.bstack111ll1ll11_opy_.append(bstack11l111lll1_opy_)
        else:
            bstack1ll11l1l11_opy_.bstack11l11ll1l1_opy_(event, bstack11l111111l_opy_)
class bstack11l1111l11_opy_:
    def __init__(self):
        self._11l1111lll_opy_ = []
    def bstack111ll1l111_opy_(self):
        self._11l1111lll_opy_.append([])
    def bstack11l111ll11_opy_(self):
        return self._11l1111lll_opy_.pop() if self._11l1111lll_opy_ else list()
    def push(self, message):
        self._11l1111lll_opy_[-1].append(message) if self._11l1111lll_opy_ else self._11l1111lll_opy_.append([message])
class bstack111ll11l11_opy_:
    FAIL = bstack11ll1l_opy_ (u"࠭ࡆࡂࡋࡏࠫྕ")
    ERROR = bstack11ll1l_opy_ (u"ࠧࡆࡔࡕࡓࡗ࠭ྖ")
    WARNING = bstack11ll1l_opy_ (u"ࠨ࡙ࡄࡖࡓ࠭ྗ")
    bstack11l1111ll1_opy_ = bstack11ll1l_opy_ (u"ࠩࡌࡒࡋࡕࠧ྘")
    DEBUG = bstack11ll1l_opy_ (u"ࠪࡈࡊࡈࡕࡈࠩྙ")
    TRACE = bstack11ll1l_opy_ (u"࡙ࠫࡘࡁࡄࡇࠪྚ")
    bstack111ll111l1_opy_ = [FAIL, ERROR]
def bstack111lll11ll_opy_(bstack111lll1l11_opy_):
    if not bstack111lll1l11_opy_:
        return None
    if bstack111lll1l11_opy_.get(bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨྛ"), None):
        return getattr(bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩྜ")], bstack11ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬྜྷ"), None)
    return bstack111lll1l11_opy_.get(bstack11ll1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ྞ"), None)
def bstack111ll1ll1l_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack11ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨྟ"), bstack11ll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬྠ")]:
        return
    if hook_type.lower() == bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪྡ"):
        if current_test_uuid is None:
            return bstack11ll1l_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩྡྷ")
        else:
            return bstack11ll1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫྣ")
    elif hook_type.lower() == bstack11ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩྤ"):
        if current_test_uuid is None:
            return bstack11ll1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫྥ")
        else:
            return bstack11ll1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ྦ")