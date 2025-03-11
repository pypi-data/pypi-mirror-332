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
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack11111l1l1l_opy_ import bstack1111ll11l1_opy_, bstack11111l11ll_opy_
import os
import threading
class bstack1111ll111l_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11lll_opy_ (u"ࠤࡋࡳࡴࡱࡓࡵࡣࡷࡩ࠳ࢁࡽࠣ࿐").format(self.name)
class bstack1111l1l111_opy_(Enum):
    NONE = 0
    bstack1111l11111_opy_ = 1
    bstack1111l1l1l1_opy_ = 3
    bstack1111ll1111_opy_ = 4
    bstack11111ll1l1_opy_ = 5
    QUIT = 6
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack11lll_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥ࿑").format(self.name)
class bstack1111l1llll_opy_(bstack1111ll11l1_opy_):
    framework_name: str
    framework_version: str
    state: bstack1111l1l111_opy_
    previous_state: bstack1111l1l111_opy_
    bstack111l111111_opy_: datetime
    bstack1111llll1l_opy_: datetime
    def __init__(
        self,
        context: bstack11111l11ll_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1111l1l111_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1111l1l111_opy_.NONE
        self.bstack111l111111_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1111llll1l_opy_ = datetime.now(tz=timezone.utc)
    def bstack1111ll11ll_opy_(self, bstack11111ll1ll_opy_: bstack1111l1l111_opy_):
        bstack11111ll111_opy_ = bstack1111l1l111_opy_(bstack11111ll1ll_opy_).name
        if not bstack11111ll111_opy_:
            return False
        if bstack11111ll1ll_opy_ == self.state:
            return False
        if self.state == bstack1111l1l111_opy_.bstack1111l1l1l1_opy_: # bstack1111l1111l_opy_ bstack1111lll111_opy_ for bstack1111l11l11_opy_ in bstack11111llll1_opy_, it bstack1111ll1lll_opy_ bstack1111lll1l1_opy_ bstack1111l1l1ll_opy_ times bstack1111l11ll1_opy_ a new state
            return True
        if (
            bstack11111ll1ll_opy_ == bstack1111l1l111_opy_.NONE
            or (self.state != bstack1111l1l111_opy_.NONE and bstack11111ll1ll_opy_ == bstack1111l1l111_opy_.bstack1111l11111_opy_)
            or (self.state < bstack1111l1l111_opy_.bstack1111l11111_opy_ and bstack11111ll1ll_opy_ == bstack1111l1l111_opy_.bstack1111ll1111_opy_)
            or (self.state < bstack1111l1l111_opy_.bstack1111l11111_opy_ and bstack11111ll1ll_opy_ == bstack1111l1l111_opy_.QUIT)
        ):
            raise ValueError(bstack11lll_opy_ (u"ࠦ࡮ࡴࡶࡢ࡮࡬ࡨࠥࡹࡴࡢࡶࡨࠤࡹࡸࡡ࡯ࡵ࡬ࡸ࡮ࡵ࡮࠻ࠢࠥ࿒") + str(self.state) + bstack11lll_opy_ (u"ࠧࠦ࠽࠿ࠢࠥ࿓") + str(bstack11111ll1ll_opy_))
        self.previous_state = self.state
        self.state = bstack11111ll1ll_opy_
        self.bstack1111llll1l_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack11111lll11_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1111l11lll_opy_: Dict[str, bstack1111l1llll_opy_] = dict()
    framework_name: str
    framework_version: str
    classes: List[Type]
    def __init__(
        self,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
    ):
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.classes = classes
    @abc.abstractmethod
    def bstack1111l1lll1_opy_(self, instance: bstack1111l1llll_opy_, method_name: str, bstack1111l11l1l_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack11111ll11l_opy_(
        self, method_name, previous_state: bstack1111l1l111_opy_, *args, **kwargs
    ) -> bstack1111l1l111_opy_:
        return
    @abc.abstractmethod
    def bstack1111ll1ll1_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1111llllll_opy_(self, bstack1111lll1ll_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack1111lll1ll_opy_:
                bstack1111l111l1_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1111l111l1_opy_):
                    self.logger.warning(bstack11lll_opy_ (u"ࠨࡵ࡯ࡲࡤࡸࡨ࡮ࡥࡥࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࠦ࿔") + str(method_name) + bstack11lll_opy_ (u"ࠢࠣ࿕"))
                    continue
                bstack1111l1ll1l_opy_ = self.bstack11111ll11l_opy_(
                    method_name, previous_state=bstack1111l1l111_opy_.NONE
                )
                bstack1111l111ll_opy_ = self.bstack1111lllll1_opy_(
                    method_name,
                    (bstack1111l1ll1l_opy_ if bstack1111l1ll1l_opy_ else bstack1111l1l111_opy_.NONE),
                    bstack1111l111l1_opy_,
                )
                if not callable(bstack1111l111ll_opy_):
                    self.logger.warning(bstack11lll_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࠡࡰࡲࡸࠥࡶࡡࡵࡥ࡫ࡩࡩࡀࠠࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࠩࡽࡶࡩࡱ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾ࠼ࠣࠦ࿖") + str(self.framework_version) + bstack11lll_opy_ (u"ࠤࠬࠦ࿗"))
                    continue
                setattr(clazz, method_name, bstack1111l111ll_opy_)
    def bstack1111lllll1_opy_(
        self,
        method_name: str,
        bstack1111l1ll1l_opy_: bstack1111l1l111_opy_,
        bstack1111l111l1_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack11lll1l11l_opy_ = datetime.now()
            (bstack1111l1ll1l_opy_,) = wrapped.__vars__
            bstack1111l1ll1l_opy_ = (
                bstack1111l1ll1l_opy_
                if bstack1111l1ll1l_opy_ and bstack1111l1ll1l_opy_ != bstack1111l1l111_opy_.NONE
                else self.bstack11111ll11l_opy_(method_name, previous_state=bstack1111l1ll1l_opy_, *args, **kwargs)
            )
            if bstack1111l1ll1l_opy_ == bstack1111l1l111_opy_.bstack1111l11111_opy_:
                ctx = bstack1111ll11l1_opy_.create_context(self.bstack11111l1ll1_opy_(target))
                if not self.bstack11111l1l11_opy_() or ctx.id not in bstack11111lll11_opy_.bstack1111l11lll_opy_:
                    bstack11111lll11_opy_.bstack1111l11lll_opy_[ctx.id] = bstack1111l1llll_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1111l1ll1l_opy_
                    )
                self.logger.debug(bstack11lll_opy_ (u"ࠥࡻࡷࡧࡰࡱࡧࡧࠤࡲ࡫ࡴࡩࡱࡧࠤࡨࡸࡥࡢࡶࡨࡨ࠿ࠦࡻࡵࡣࡵ࡫ࡪࡺ࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡥࡷࡼࡂࢁࡣࡵࡺ࠱࡭ࡩࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦ࿘") + str(bstack11111lll11_opy_.bstack1111l11lll_opy_.keys()) + bstack11lll_opy_ (u"ࠦࠧ࿙"))
            else:
                self.logger.debug(bstack11lll_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡩ࡯ࡸࡲ࡯ࡪࡪ࠺ࠡࡽࡷࡥࡷ࡭ࡥࡵ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡸࡃࠢ࿚") + str(bstack11111lll11_opy_.bstack1111l11lll_opy_.keys()) + bstack11lll_opy_ (u"ࠨࠢ࿛"))
            instance = bstack11111lll11_opy_.bstack11111lllll_opy_(self.bstack11111l1ll1_opy_(target))
            if bstack1111l1ll1l_opy_ == bstack1111l1l111_opy_.NONE or not instance:
                ctx = bstack1111ll11l1_opy_.create_context(self.bstack11111l1ll1_opy_(target))
                self.logger.warning(bstack11lll_opy_ (u"ࠢࡸࡴࡤࡴࡵ࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤࠡࡷࡱࡸࡷࡧࡣ࡬ࡧࡧ࠾ࠥࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡨࡺࡸ࠾ࡽࡦࡸࡽࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦ࿜") + str(bstack11111lll11_opy_.bstack1111l11lll_opy_.keys()) + bstack11lll_opy_ (u"ࠣࠤ࿝"))
                return bstack1111l111l1_opy_(target, *args, **kwargs)
            bstack1111l1l11l_opy_ = self.bstack1111ll1ll1_opy_(
                target,
                (instance, method_name),
                (bstack1111l1ll1l_opy_, bstack1111ll111l_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1111ll11ll_opy_(bstack1111l1ll1l_opy_):
                self.logger.debug(bstack11lll_opy_ (u"ࠤࡤࡴࡵࡲࡩࡦࡦࠣࡷࡹࡧࡴࡦ࠯ࡷࡶࡦࡴࡳࡪࡶ࡬ࡳࡳࡀࠠࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡴࡷ࡫ࡶࡪࡱࡸࡷࡤࡹࡴࡢࡶࡨࢁࠥࡃ࠾ࠡࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡸࡺࡡࡵࡧࢀࠤ࠭ࢁࡴࡺࡲࡨࠬࡹࡧࡲࡨࡧࡷ࠭ࢂ࠴ࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡻࡢࡴࡪࡷࢂ࠯ࠠ࡜ࠤ࿞") + str(instance.ref()) + bstack11lll_opy_ (u"ࠥࡡࠧ࿟"))
            result = (
                bstack1111l1l11l_opy_(target, bstack1111l111l1_opy_, *args, **kwargs)
                if callable(bstack1111l1l11l_opy_)
                else bstack1111l111l1_opy_(target, *args, **kwargs)
            )
            bstack11111lll1l_opy_ = self.bstack1111ll1ll1_opy_(
                target,
                (instance, method_name),
                (bstack1111l1ll1l_opy_, bstack1111ll111l_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1111l1lll1_opy_(instance, method_name, datetime.now() - bstack11lll1l11l_opy_, *args, **kwargs)
            return bstack11111lll1l_opy_ if bstack11111lll1l_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1111l1ll1l_opy_,)
        return wrapped
    @staticmethod
    def bstack11111lllll_opy_(target: object, strict=True):
        ctx = bstack1111ll11l1_opy_.create_context(target)
        instance = bstack11111lll11_opy_.bstack1111l11lll_opy_.get(ctx.id, None)
        if instance and instance.bstack1111l1ll11_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1111ll1l1l_opy_(
        ctx: bstack11111l11ll_opy_, state: bstack1111l1l111_opy_, reverse=True
    ) -> List[bstack1111l1llll_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack11111lll11_opy_.bstack1111l11lll_opy_.values(),
            ),
            key=lambda t: t.bstack111l111111_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1111ll1l11_opy_(instance: bstack1111l1llll_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack11111l11l1_opy_(instance: bstack1111l1llll_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1111ll11ll_opy_(instance: bstack1111l1llll_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack11111lll11_opy_.logger.debug(bstack11lll_opy_ (u"ࠦࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦ࡫ࡦࡻࡀࡿࡰ࡫ࡹࡾࠢࡹࡥࡱࡻࡥ࠾ࠤ࿠") + str(value) + bstack11lll_opy_ (u"ࠧࠨ࿡"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack11111lll11_opy_.bstack11111lllll_opy_(target, strict)
        return bstack11111lll11_opy_.bstack11111l11l1_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack11111lll11_opy_.bstack11111lllll_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack11111l1l11_opy_(self):
        return self.framework_name == bstack11lll_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪ࿢")
    def bstack11111l1ll1_opy_(self, target):
        return target if not self.bstack11111l1l11_opy_() else self.bstack1111lll11l_opy_()
    @staticmethod
    def bstack1111lll11l_opy_():
        return str(os.getpid()) + str(threading.get_ident())