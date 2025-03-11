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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11llll1l1l1_opy_
from browserstack_sdk.bstack1l1111l1l_opy_ import bstack11l111ll_opy_
def _11ll111l1ll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11ll111l111_opy_:
    def __init__(self, handler):
        self._11ll1111l1l_opy_ = {}
        self._11ll11l1111_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack11l111ll_opy_.version()
        if bstack11llll1l1l1_opy_(pytest_version, bstack11lll_opy_ (u"ࠧ࠾࠮࠲࠰࠴ࠦ᫘")) >= 0:
            self._11ll1111l1l_opy_[bstack11lll_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᫙")] = Module._register_setup_function_fixture
            self._11ll1111l1l_opy_[bstack11lll_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᫚")] = Module._register_setup_module_fixture
            self._11ll1111l1l_opy_[bstack11lll_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᫛")] = Class._register_setup_class_fixture
            self._11ll1111l1l_opy_[bstack11lll_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᫜")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11ll111ll1l_opy_(bstack11lll_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᫝"))
            Module._register_setup_module_fixture = self.bstack11ll111ll1l_opy_(bstack11lll_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᫞"))
            Class._register_setup_class_fixture = self.bstack11ll111ll1l_opy_(bstack11lll_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᫟"))
            Class._register_setup_method_fixture = self.bstack11ll111ll1l_opy_(bstack11lll_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᫠"))
        else:
            self._11ll1111l1l_opy_[bstack11lll_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᫡")] = Module._inject_setup_function_fixture
            self._11ll1111l1l_opy_[bstack11lll_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᫢")] = Module._inject_setup_module_fixture
            self._11ll1111l1l_opy_[bstack11lll_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᫣")] = Class._inject_setup_class_fixture
            self._11ll1111l1l_opy_[bstack11lll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᫤")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11ll111ll1l_opy_(bstack11lll_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᫥"))
            Module._inject_setup_module_fixture = self.bstack11ll111ll1l_opy_(bstack11lll_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᫦"))
            Class._inject_setup_class_fixture = self.bstack11ll111ll1l_opy_(bstack11lll_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᫧"))
            Class._inject_setup_method_fixture = self.bstack11ll111ll1l_opy_(bstack11lll_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᫨"))
    def bstack11ll111ll11_opy_(self, bstack11ll111l11l_opy_, hook_type):
        bstack11ll1111lll_opy_ = id(bstack11ll111l11l_opy_.__class__)
        if (bstack11ll1111lll_opy_, hook_type) in self._11ll11l1111_opy_:
            return
        meth = getattr(bstack11ll111l11l_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11ll11l1111_opy_[(bstack11ll1111lll_opy_, hook_type)] = meth
            setattr(bstack11ll111l11l_opy_, hook_type, self.bstack11ll111111l_opy_(hook_type, bstack11ll1111lll_opy_))
    def bstack11ll111llll_opy_(self, instance, bstack11ll111lll1_opy_):
        if bstack11ll111lll1_opy_ == bstack11lll_opy_ (u"ࠣࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠦ᫩"):
            self.bstack11ll111ll11_opy_(instance.obj, bstack11lll_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥ᫪"))
            self.bstack11ll111ll11_opy_(instance.obj, bstack11lll_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢ᫫"))
        if bstack11ll111lll1_opy_ == bstack11lll_opy_ (u"ࠦࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠧ᫬"):
            self.bstack11ll111ll11_opy_(instance.obj, bstack11lll_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠦ᫭"))
            self.bstack11ll111ll11_opy_(instance.obj, bstack11lll_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠣ᫮"))
        if bstack11ll111lll1_opy_ == bstack11lll_opy_ (u"ࠢࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠢ᫯"):
            self.bstack11ll111ll11_opy_(instance.obj, bstack11lll_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸࠨ᫰"))
            self.bstack11ll111ll11_opy_(instance.obj, bstack11lll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠥ᫱"))
        if bstack11ll111lll1_opy_ == bstack11lll_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠦ᫲"):
            self.bstack11ll111ll11_opy_(instance.obj, bstack11lll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠥ᫳"))
            self.bstack11ll111ll11_opy_(instance.obj, bstack11lll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠢ᫴"))
    @staticmethod
    def bstack11ll11111l1_opy_(hook_type, func, args):
        if hook_type in [bstack11lll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬ᫵"), bstack11lll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩ᫶")]:
            _11ll111l1ll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11ll111111l_opy_(self, hook_type, bstack11ll1111lll_opy_):
        def bstack11ll11111ll_opy_(arg=None):
            self.handler(hook_type, bstack11lll_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ᫷"))
            result = None
            try:
                bstack1111l111l1_opy_ = self._11ll11l1111_opy_[(bstack11ll1111lll_opy_, hook_type)]
                self.bstack11ll11111l1_opy_(hook_type, bstack1111l111l1_opy_, (arg,))
                result = Result(result=bstack11lll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᫸"))
            except Exception as e:
                result = Result(result=bstack11lll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᫹"), exception=e)
                self.handler(hook_type, bstack11lll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪ᫺"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11lll_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫ᫻"), result)
        def bstack11ll111l1l1_opy_(this, arg=None):
            self.handler(hook_type, bstack11lll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭᫼"))
            result = None
            exception = None
            try:
                self.bstack11ll11111l1_opy_(hook_type, self._11ll11l1111_opy_[hook_type], (this, arg))
                result = Result(result=bstack11lll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ᫽"))
            except Exception as e:
                result = Result(result=bstack11lll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᫾"), exception=e)
                self.handler(hook_type, bstack11lll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨ᫿"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11lll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩᬀ"), result)
        if hook_type in [bstack11lll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪᬁ"), bstack11lll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧᬂ")]:
            return bstack11ll111l1l1_opy_
        return bstack11ll11111ll_opy_
    def bstack11ll111ll1l_opy_(self, bstack11ll111lll1_opy_):
        def bstack11ll1111l11_opy_(this, *args, **kwargs):
            self.bstack11ll111llll_opy_(this, bstack11ll111lll1_opy_)
            self._11ll1111l1l_opy_[bstack11ll111lll1_opy_](this, *args, **kwargs)
        return bstack11ll1111l11_opy_