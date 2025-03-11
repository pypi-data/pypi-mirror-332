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
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111l11l111_opy_ import bstack111l111l1l_opy_
from browserstack_sdk.sdk_cli.bstack111l111lll_opy_ import bstack111l11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll111l1_opy_ import bstack1llllll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1llllllll11_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1111_opy_ import bstack1lll1llllll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1llll1l_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll111lll_opy_ import bstack1lll1llll11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1lll1_opy_ import bstack1111111l11_opy_
from browserstack_sdk.sdk_cli.bstack1llll11llll_opy_ import bstack1lll1l111ll_opy_
from browserstack_sdk.sdk_cli.bstack1l11ll11_opy_ import bstack1l11ll11_opy_, bstack1ll1llll11_opy_, bstack11l1l1lll1_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1llllll1111_opy_ import bstack1111111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack111111l111_opy_
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import bstack11111lll11_opy_
from browserstack_sdk.sdk_cli.bstack1llll1111l1_opy_ import bstack1lll1l11l1l_opy_
from bstack_utils.helper import Notset, bstack1lllll1llll_opy_, get_cli_dir, bstack1llll1l1l11_opy_, bstack11l111111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from bstack_utils.helper import Notset, bstack1lllll1llll_opy_, get_cli_dir, bstack1llll1l1l11_opy_, bstack11l111111_opy_, bstack1l1l11l1l1_opy_, bstack11lll1ll1_opy_, bstack1lll1l1l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lll1ll_opy_, bstack1llll11lll1_opy_, bstack1lll1lll11l_opy_, bstack1lll11l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import bstack1111l1llll_opy_, bstack1111l1l111_opy_, bstack1111ll111l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack111l11ll_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11ll1111l1_opy_, bstack11111ll11_opy_
logger = bstack111l11ll_opy_.get_logger(__name__, bstack111l11ll_opy_.bstack111111111l_opy_())
def bstack1lll1l1111l_opy_(bs_config):
    bstack1lll11l1lll_opy_ = None
    bstack1llll1ll1l1_opy_ = None
    try:
        bstack1llll1ll1l1_opy_ = get_cli_dir()
        bstack1lll11l1lll_opy_ = bstack1llll1l1l11_opy_(bstack1llll1ll1l1_opy_)
        bstack1llll11ll11_opy_ = bstack1lllll1llll_opy_(bstack1lll11l1lll_opy_, bstack1llll1ll1l1_opy_, bs_config)
        bstack1lll11l1lll_opy_ = bstack1llll11ll11_opy_ if bstack1llll11ll11_opy_ else bstack1lll11l1lll_opy_
        if not bstack1lll11l1lll_opy_:
            raise ValueError(bstack11lll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠦ࿣"))
    except Exception as ex:
        logger.debug(bstack11lll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡹ࡮ࡥࠡ࡮ࡤࡸࡪࡹࡴࠡࡤ࡬ࡲࡦࡸࡹࠡࡽࢀࠦ࿤").format(ex))
        bstack1lll11l1lll_opy_ = os.environ.get(bstack11lll_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠧ࿥"))
        if bstack1lll11l1lll_opy_:
            logger.debug(bstack11lll_opy_ (u"ࠥࡊࡦࡲ࡬ࡪࡰࡪࠤࡧࡧࡣ࡬ࠢࡷࡳ࡙ࠥࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠡࡨࡵࡳࡲࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷ࠾ࠥࠨ࿦") + str(bstack1lll11l1lll_opy_) + bstack11lll_opy_ (u"ࠦࠧ࿧"))
        else:
            logger.debug(bstack11lll_opy_ (u"ࠧࡔ࡯ࠡࡸࡤࡰ࡮ࡪࠠࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥ࡫࡮ࡷ࡫ࡵࡳࡳࡳࡥ࡯ࡶ࠾ࠤࡸ࡫ࡴࡶࡲࠣࡱࡦࡿࠠࡣࡧࠣ࡭ࡳࡩ࡯࡮ࡲ࡯ࡩࡹ࡫࠮ࠣ࿨"))
    return bstack1lll11l1lll_opy_, bstack1llll1ll1l1_opy_
bstack1lll1l1ll11_opy_ = bstack11lll_opy_ (u"ࠨ࠹࠺࠻࠼ࠦ࿩")
bstack1lll1l1ll1l_opy_ = bstack11lll_opy_ (u"ࠢࡳࡧࡤࡨࡾࠨ࿪")
bstack1llll11111l_opy_ = bstack11lll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡕࡈࡗࡘࡏࡏࡏࡡࡌࡈࠧ࿫")
bstack1llll111l11_opy_ = bstack11lll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡏࡍࡘ࡚ࡅࡏࡡࡄࡈࡉࡘࠢ࿬")
bstack11ll1l11_opy_ = bstack11lll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓࠨ࿭")
bstack1lll11lll11_opy_ = re.compile(bstack11lll_opy_ (u"ࡶࠧ࠮࠿ࡪࠫ࠱࠮࠭ࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࢀࡇ࡙ࠩ࠯ࠬࠥ࿮"))
bstack1lll11ll111_opy_ = bstack11lll_opy_ (u"ࠧࡪࡥࡷࡧ࡯ࡳࡵࡳࡥ࡯ࡶࠥ࿯")
bstack1llll11ll1l_opy_ = [
    bstack1ll1llll11_opy_.bstack11llll11l1_opy_,
    bstack1ll1llll11_opy_.CONNECT,
    bstack1ll1llll11_opy_.bstack1ll1ll111l_opy_,
]
class SDKCLI:
    _1llll1l11l1_opy_ = None
    process: Union[None, Any]
    bstack1lllll11lll_opy_: bool
    bstack1llll1l111l_opy_: bool
    bstack1lll11l1l11_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1lll1l1l11l_opy_: Union[None, grpc.Channel]
    bstack1lll1ll11ll_opy_: str
    test_framework: TestFramework
    bstack11111l1lll_opy_: bstack11111lll11_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1lll1ll11l1_opy_: bstack1lll1l111ll_opy_
    accessibility: bstack1llllll11ll_opy_
    ai: bstack1lllllll1l1_opy_
    bstack1lllll11111_opy_: bstack1lll1llllll_opy_
    bstack1lllllll1ll_opy_: List[bstack111l11l1ll_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1llll111l1l_opy_: Any
    bstack1lll1lll1l1_opy_: Dict[str, timedelta]
    bstack1111111lll_opy_: str
    bstack111l11l111_opy_: bstack111l111l1l_opy_
    def __new__(cls):
        if not cls._1llll1l11l1_opy_:
            cls._1llll1l11l1_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1llll1l11l1_opy_
    def __init__(self):
        self.process = None
        self.bstack1lllll11lll_opy_ = False
        self.bstack1lll1l1l11l_opy_ = None
        self.bstack111l11l1l1_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1llll111l11_opy_, None)
        self.bstack1llll1ll11l_opy_ = os.environ.get(bstack1llll11111l_opy_, bstack11lll_opy_ (u"ࠨࠢ࿰")) == bstack11lll_opy_ (u"ࠢࠣ࿱")
        self.bstack1llll1l111l_opy_ = False
        self.bstack1lll11l1l11_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1llll111l1l_opy_ = None
        self.test_framework = None
        self.bstack11111l1lll_opy_ = None
        self.bstack1lll1ll11ll_opy_=bstack11lll_opy_ (u"ࠣࠤ࿲")
        self.session_framework = None
        self.logger = bstack111l11ll_opy_.get_logger(self.__class__.__name__, bstack111l11ll_opy_.bstack111111111l_opy_())
        self.bstack1lll1lll1l1_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack111l11l111_opy_ = bstack111l111l1l_opy_()
        self.bstack1lllllllll1_opy_ = None
        self.bstack1llllll1ll1_opy_ = None
        self.bstack1lll1ll11l1_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1lllllll1ll_opy_ = []
    def bstack1l1l1ll11l_opy_(self):
        return os.environ.get(bstack11ll1l11_opy_).lower().__eq__(bstack11lll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ࿳"))
    def is_enabled(self, config):
        if bstack11lll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ࿴") in config and str(config[bstack11lll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ࿵")]).lower() != bstack11lll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ࿶"):
            return False
        bstack1lll1ll111l_opy_ = [bstack11lll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨ࿷"), bstack11lll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦ࿸")]
        bstack1llll1ll111_opy_ = config.get(bstack11lll_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦ࿹")) in bstack1lll1ll111l_opy_ or os.environ.get(bstack11lll_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ࿺")) in bstack1lll1ll111l_opy_
        os.environ[bstack11lll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨ࿻")] = str(bstack1llll1ll111_opy_) # bstack1lll1l11l11_opy_ bstack1llllll11l1_opy_ VAR to bstack1lll11lll1l_opy_ is binary running
        return bstack1llll1ll111_opy_
    def bstack1l11l1ll1l_opy_(self):
        for event in bstack1llll11ll1l_opy_:
            bstack1l11ll11_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1l11ll11_opy_.logger.debug(bstack11lll_opy_ (u"ࠦࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠣࡁࡃࠦࡻࡢࡴࡪࡷࢂࠦࠢ࿼") + str(kwargs) + bstack11lll_opy_ (u"ࠧࠨ࿽"))
            )
        bstack1l11ll11_opy_.register(bstack1ll1llll11_opy_.bstack11llll11l1_opy_, self.__1111111111_opy_)
        bstack1l11ll11_opy_.register(bstack1ll1llll11_opy_.CONNECT, self.__111111l1l1_opy_)
        bstack1l11ll11_opy_.register(bstack1ll1llll11_opy_.bstack1ll1ll111l_opy_, self.__1llllll1l1l_opy_)
        bstack1l11ll11_opy_.register(bstack1ll1llll11_opy_.bstack1ll111llll_opy_, self.__1111111ll1_opy_)
    def bstack11l11111_opy_(self):
        return not self.bstack1llll1ll11l_opy_ and os.environ.get(bstack1llll11111l_opy_, bstack11lll_opy_ (u"ࠨࠢ࿾")) != bstack11lll_opy_ (u"ࠢࠣ࿿")
    def is_running(self):
        if self.bstack1llll1ll11l_opy_:
            return self.bstack1lllll11lll_opy_
        else:
            return bool(self.bstack1lll1l1l11l_opy_)
    def bstack1lll1ll1l11_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1lllllll1ll_opy_) and cli.is_running()
    def __1lllll1111l_opy_(self, bstack1lll11ll11l_opy_=10):
        if self.bstack111l11l1l1_opy_:
            return
        bstack11lll1l11l_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1llll111l11_opy_, self.cli_listen_addr)
        self.logger.debug(bstack11lll_opy_ (u"ࠣ࡝ࠥက") + str(id(self)) + bstack11lll_opy_ (u"ࠤࡠࠤࡨࡵ࡮࡯ࡧࡦࡸ࡮ࡴࡧࠣခ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack11lll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠯ࡧࡱࡥࡧࡲࡥࡠࡪࡷࡸࡵࡥࡰࡳࡱࡻࡽࠧဂ"), 0), (bstack11lll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠰ࡨࡲࡦࡨ࡬ࡦࡡ࡫ࡸࡹࡶࡳࡠࡲࡵࡳࡽࡿࠢဃ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1lll11ll11l_opy_)
        self.bstack1lll1l1l11l_opy_ = channel
        self.bstack111l11l1l1_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1lll1l1l11l_opy_)
        self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡧࡴࡴ࡮ࡦࡥࡷࠦင"), datetime.now() - bstack11lll1l11l_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1llll111l11_opy_] = self.cli_listen_addr
        self.logger.debug(bstack11lll_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤ࠻ࠢ࡬ࡷࡤࡩࡨࡪ࡮ࡧࡣࡵࡸ࡯ࡤࡧࡶࡷࡂࠨစ") + str(self.bstack11l11111_opy_()) + bstack11lll_opy_ (u"ࠢࠣဆ"))
    def __1llllll1l1l_opy_(self, event_name):
        if self.bstack11l11111_opy_():
            self.logger.debug(bstack11lll_opy_ (u"ࠣࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡶࡸࡴࡶࡰࡪࡰࡪࠤࡈࡒࡉࠣဇ"))
        self.__1llllllll1l_opy_()
    def __1111111ll1_opy_(self, event_name, bstack1llll1l1l1l_opy_ = None, bstack1l1lll1ll_opy_=1):
        if bstack1l1lll1ll_opy_ == 1:
            self.logger.error(bstack11lll_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠤဈ"))
        bstack1lll1ll1ll1_opy_ = Path(bstack1lll11lllll_opy_ (u"ࠥࡿࡸ࡫࡬ࡧ࠰ࡦࡰ࡮ࡥࡤࡪࡴࢀ࠳ࡺࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࡸ࠴ࡪࡴࡱࡱࠦဉ"))
        if self.bstack1llll1ll1l1_opy_ and bstack1lll1ll1ll1_opy_.exists():
            with open(bstack1lll1ll1ll1_opy_, bstack11lll_opy_ (u"ࠫࡷ࠭ည"), encoding=bstack11lll_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫဋ")) as fp:
                data = json.load(fp)
                try:
                    bstack1l1l11l1l1_opy_(bstack11lll_opy_ (u"࠭ࡐࡐࡕࡗࠫဌ"), bstack11lll1ll1_opy_(bstack11llll1ll1_opy_), data, {
                        bstack11lll_opy_ (u"ࠧࡢࡷࡷ࡬ࠬဍ"): (self.config[bstack11lll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪဎ")], self.config[bstack11lll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬဏ")])
                    })
                except Exception as e:
                    logger.debug(bstack11111ll11_opy_.format(str(e)))
            bstack1lll1ll1ll1_opy_.unlink()
        sys.exit(bstack1l1lll1ll_opy_)
    @measure(event_name=EVENTS.bstack1lll1ll1l1l_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def __1111111111_opy_(self, event_name: str, data):
        from bstack_utils.bstack11l1lll1_opy_ import bstack1lll1ll1lll_opy_
        self.bstack1lll1ll11ll_opy_, self.bstack1llll1ll1l1_opy_ = bstack1lll1l1111l_opy_(data.bs_config)
        os.environ[bstack11lll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡ࡚ࡖࡎ࡚ࡁࡃࡎࡈࡣࡉࡏࡒࠨတ")] = self.bstack1llll1ll1l1_opy_
        if not self.bstack1lll1ll11ll_opy_ or not self.bstack1llll1ll1l1_opy_:
            raise ValueError(bstack11lll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡺࡨࡦࠢࡖࡈࡐࠦࡃࡍࡋࠣࡦ࡮ࡴࡡࡳࡻࠥထ"))
        if self.bstack11l11111_opy_():
            self.__111111l1l1_opy_(event_name, bstack11l1l1lll1_opy_())
            return
        try:
            bstack1lll1ll1lll_opy_.end(EVENTS.bstack1l1l1lll11_opy_.value, EVENTS.bstack1l1l1lll11_opy_.value + bstack11lll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧဒ"), EVENTS.bstack1l1l1lll11_opy_.value + bstack11lll_opy_ (u"ࠨ࠺ࡦࡰࡧࠦဓ"), status=True, failure=None, test_name=None)
            logger.debug(bstack11lll_opy_ (u"ࠢࡄࡱࡰࡴࡱ࡫ࡴࡦࠢࡖࡈࡐࠦࡓࡦࡶࡸࡴ࠳ࠨန"))
        except Exception as e:
            logger.debug(bstack11lll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴࠢࡾࢁࠧပ").format(e))
        start = datetime.now()
        is_started = self.__1llll1111ll_opy_()
        self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠤࡶࡴࡦࡽ࡮ࡠࡶ࡬ࡱࡪࠨဖ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1lllll1111l_opy_()
            self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࡣࡹ࡯࡭ࡦࠤဗ"), datetime.now() - start)
            start = datetime.now()
            self.__1llll1l1lll_opy_(data)
            self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤဘ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1llll1l1111_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def __111111l1l1_opy_(self, event_name: str, data: bstack11l1l1lll1_opy_):
        if not self.bstack11l11111_opy_():
            self.logger.debug(bstack11lll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥࡲࡲࡳ࡫ࡣࡵ࠼ࠣࡲࡴࡺࠠࡢࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴࠤမ"))
            return
        bin_session_id = os.environ.get(bstack1llll11111l_opy_)
        start = datetime.now()
        self.__1lllll1111l_opy_()
        self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺ࡟ࡵ࡫ࡰࡩࠧယ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack11lll_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦࠣࡸࡴࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡࡅࡏࡍࠥࠨရ") + str(bin_session_id) + bstack11lll_opy_ (u"ࠣࠤလ"))
        start = datetime.now()
        self.__11111111ll_opy_()
        self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢဝ"), datetime.now() - start)
    def __1llll111ll1_opy_(self):
        if not self.bstack111l11l1l1_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack11lll_opy_ (u"ࠥࡧࡦࡴ࡮ࡰࡶࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࠦ࡭ࡰࡦࡸࡰࡪࡹࠢသ"))
            return
        bstack1lllllll111_opy_ = {
            bstack11lll_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣဟ"): (bstack1lll1llll11_opy_, bstack1111111l11_opy_, bstack1lll1l11l1l_opy_),
            bstack11lll_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢဠ"): (bstack1llll1llll1_opy_, bstack1lllll11l1l_opy_, bstack111111l111_opy_),
        }
        if not self.bstack1lllllllll1_opy_ and self.session_framework in bstack1lllllll111_opy_:
            bstack1lll1l11ll1_opy_, bstack1llllllllll_opy_, bstack111111llll_opy_ = bstack1lllllll111_opy_[self.session_framework]
            bstack111111ll11_opy_ = bstack1llllllllll_opy_()
            self.bstack1llllll1ll1_opy_ = bstack111111ll11_opy_
            self.bstack1lllllllll1_opy_ = bstack111111llll_opy_
            self.bstack1lllllll1ll_opy_.append(bstack111111ll11_opy_)
            self.bstack1lllllll1ll_opy_.append(bstack1lll1l11ll1_opy_(self.bstack1llllll1ll1_opy_))
        if not self.bstack1lll1ll11l1_opy_ and self.config_observability and self.config_observability.success: # bstack1llll1lllll_opy_
            self.bstack1lll1ll11l1_opy_ = bstack1lll1l111ll_opy_(self.bstack1lllllllll1_opy_, self.bstack1llllll1ll1_opy_) # bstack1lll1l1l1l1_opy_
            self.bstack1lllllll1ll_opy_.append(self.bstack1lll1ll11l1_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1llllll11ll_opy_(self.bstack1lllllllll1_opy_, self.bstack1llllll1ll1_opy_)
            self.bstack1lllllll1ll_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack11lll_opy_ (u"ࠨࡳࡦ࡮ࡩࡌࡪࡧ࡬ࠣအ"), False) == True:
            self.ai = bstack1lllllll1l1_opy_()
            self.bstack1lllllll1ll_opy_.append(self.ai)
        if not self.percy and self.bstack1llll111l1l_opy_ and self.bstack1llll111l1l_opy_.success:
            self.percy = bstack1lll1llllll_opy_(self.bstack1llll111l1l_opy_)
            self.bstack1lllllll1ll_opy_.append(self.percy)
        for mod in self.bstack1lllllll1ll_opy_:
            if not mod.bstack111l111ll1_opy_():
                mod.configure(self.bstack111l11l1l1_opy_, self.config, self.cli_bin_session_id, self.bstack111l11l111_opy_)
    def __111111l11l_opy_(self):
        for mod in self.bstack1lllllll1ll_opy_:
            if mod.bstack111l111ll1_opy_():
                mod.configure(self.bstack111l11l1l1_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1llll111111_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def __1llll1l1lll_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1llll1l111l_opy_:
            return
        self.__1lllll1ll1l_opy_(data)
        bstack11lll1l11l_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack11lll_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࠢဢ")
        req.sdk_language = bstack11lll_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣဣ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1lll11lll11_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack11lll_opy_ (u"ࠤ࡞ࠦဤ") + str(id(self)) + bstack11lll_opy_ (u"ࠥࡡࠥࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡹࡴࡢࡴࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤဥ"))
            r = self.bstack111l11l1l1_opy_.StartBinSession(req)
            self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡸࡦࡸࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨဦ"), datetime.now() - bstack11lll1l11l_opy_)
            os.environ[bstack1llll11111l_opy_] = r.bin_session_id
            self.__1lll1l1l111_opy_(r)
            self.__1llll111ll1_opy_()
            self.bstack111l11l111_opy_.start()
            self.bstack1llll1l111l_opy_ = True
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡡࠢဧ") + str(id(self)) + bstack11lll_opy_ (u"ࠨ࡝ࠡ࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠦဨ"))
        except grpc.bstack1llllll1lll_opy_ as bstack1llll1ll1ll_opy_:
            self.logger.error(bstack11lll_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡴࡪ࡯ࡨࡳࡪࡻࡴ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤဩ") + str(bstack1llll1ll1ll_opy_) + bstack11lll_opy_ (u"ࠣࠤဪ"))
            traceback.print_exc()
            raise bstack1llll1ll1ll_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨါ") + str(e) + bstack11lll_opy_ (u"ࠥࠦာ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllll111l_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def __11111111ll_opy_(self):
        if not self.bstack11l11111_opy_() or not self.cli_bin_session_id or self.bstack1lll11l1l11_opy_:
            return
        bstack11lll1l11l_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack11lll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫိ"), bstack11lll_opy_ (u"ࠬ࠶ࠧီ")))
        try:
            self.logger.debug(bstack11lll_opy_ (u"ࠨ࡛ࠣု") + str(id(self)) + bstack11lll_opy_ (u"ࠢ࡞ࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤူ"))
            r = self.bstack111l11l1l1_opy_.ConnectBinSession(req)
            self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡣࡰࡰࡱࡩࡨࡺ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧေ"), datetime.now() - bstack11lll1l11l_opy_)
            self.__1lll1l1l111_opy_(r)
            self.__1llll111ll1_opy_()
            self.bstack111l11l111_opy_.start()
            self.bstack1lll11l1l11_opy_ = True
            self.logger.debug(bstack11lll_opy_ (u"ࠤ࡞ࠦဲ") + str(id(self)) + bstack11lll_opy_ (u"ࠥࡡࠥࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥࠤဳ"))
        except grpc.bstack1llllll1lll_opy_ as bstack1llll1ll1ll_opy_:
            self.logger.error(bstack11lll_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡸ࡮ࡳࡥࡰࡧࡸࡸ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨဴ") + str(bstack1llll1ll1ll_opy_) + bstack11lll_opy_ (u"ࠧࠨဵ"))
            traceback.print_exc()
            raise bstack1llll1ll1ll_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥံ") + str(e) + bstack11lll_opy_ (u"့ࠢࠣ"))
            traceback.print_exc()
            raise e
    def __1lll1l1l111_opy_(self, r):
        self.bstack1llll11l11l_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack11lll_opy_ (u"ࠣࡷࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡹࡥࡳࡸࡨࡶࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢး") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack11lll_opy_ (u"ࠤࡨࡱࡵࡺࡹࠡࡥࡲࡲ࡫࡯ࡧࠡࡨࡲࡹࡳࡪ္ࠢ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack11lll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡧࡵࡧࡾࠦࡩࡴࠢࡶࡩࡳࡺࠠࡰࡰ࡯ࡽࠥࡧࡳࠡࡲࡤࡶࡹࠦ࡯ࡧࠢࡷ࡬ࡪࠦࠢࡄࡱࡱࡲࡪࡩࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱ࠰ࠧࠦࡡ࡯ࡦࠣࡸ࡭࡯ࡳࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣ࡭ࡸࠦࡡ࡭ࡵࡲࠤࡺࡹࡥࡥࠢࡥࡽ࡙ࠥࡴࡢࡴࡷࡆ࡮ࡴࡓࡦࡵࡶ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬ࡪࡸࡥࡧࡱࡵࡩ࠱ࠦࡎࡰࡰࡨࠤ࡭ࡧ࡮ࡥ࡮࡬ࡲ࡬ࠦࡩࡴࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡪࡪ࠮ࠋࠢࠣࠤ်ࠥࠦࠠࠡࠢࠥࠦࠧ")
        self.bstack1llll111l1l_opy_ = getattr(r, bstack11lll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪျ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack11lll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩြ")] = self.config_testhub.jwt
        os.environ[bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫွ")] = self.config_testhub.build_hashed_id
    def bstack111111lll1_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1lllll11lll_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1llll1lll1l_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1llll1lll1l_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack111111lll1_opy_(event_name=EVENTS.bstack111111ll1l_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def __1llll1111ll_opy_(self, bstack1lll11ll11l_opy_=10):
        if self.bstack1lllll11lll_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠢࡴࡶࡤࡶࡹࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡴࡸࡲࡳ࡯࡮ࡨࠤှ"))
            return True
        self.logger.debug(bstack11lll_opy_ (u"ࠣࡵࡷࡥࡷࡺࠢဿ"))
        if os.getenv(bstack11lll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡋࡎࡗࠤ၀")) == bstack1lll11ll111_opy_:
            self.cli_bin_session_id = bstack1lll11ll111_opy_
            self.cli_listen_addr = bstack11lll_opy_ (u"ࠥࡹࡳ࡯ࡸ࠻࠱ࡷࡱࡵ࠵ࡳࡥ࡭࠰ࡴࡱࡧࡴࡧࡱࡵࡱ࠲ࠫࡳ࠯ࡵࡲࡧࡰࠨ၁") % (self.cli_bin_session_id)
            self.bstack1lllll11lll_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1lll1ll11ll_opy_, bstack11lll_opy_ (u"ࠦࡸࡪ࡫ࠣ၂")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1lll1l1llll_opy_ compat for text=True in bstack11111l1111_opy_ python
            encoding=bstack11lll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦ၃"),
            bufsize=1,
            close_fds=True,
        )
        bstack1lll1lll111_opy_ = threading.Thread(target=self.__1lllllll11l_opy_, args=(bstack1lll11ll11l_opy_,))
        bstack1lll1lll111_opy_.start()
        bstack1lll1lll111_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack11lll_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡹࡰࡢࡹࡱ࠾ࠥࡸࡥࡵࡷࡵࡲࡨࡵࡤࡦ࠿ࡾࡷࡪࡲࡦ࠯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡵࡩࡹࡻࡲ࡯ࡥࡲࡨࡪࢃࠠࡰࡷࡷࡁࢀࡹࡥ࡭ࡨ࠱ࡴࡷࡵࡣࡦࡵࡶ࠲ࡸࡺࡤࡰࡷࡷ࠲ࡷ࡫ࡡࡥࠪࠬࢁࠥ࡫ࡲࡳ࠿ࠥ၄") + str(self.process.stderr.read()) + bstack11lll_opy_ (u"ࠢࠣ၅"))
        if not self.bstack1lllll11lll_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠣ࡝ࠥ၆") + str(id(self)) + bstack11lll_opy_ (u"ࠤࡠࠤࡨࡲࡥࡢࡰࡸࡴࠧ၇"))
            self.__1llllllll1l_opy_()
        self.logger.debug(bstack11lll_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡳࡶࡴࡩࡥࡴࡵࡢࡶࡪࡧࡤࡺ࠼ࠣࠦ၈") + str(self.bstack1lllll11lll_opy_) + bstack11lll_opy_ (u"ࠦࠧ၉"))
        return self.bstack1lllll11lll_opy_
    def __1lllllll11l_opy_(self, bstack1llll11l1ll_opy_=10):
        bstack1lll1lllll1_opy_ = time.time()
        while self.process and time.time() - bstack1lll1lllll1_opy_ < bstack1llll11l1ll_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack11lll_opy_ (u"ࠧ࡯ࡤ࠾ࠤ၊") in line:
                    self.cli_bin_session_id = line.split(bstack11lll_opy_ (u"ࠨࡩࡥ࠿ࠥ။"))[-1:][0].strip()
                    self.logger.debug(bstack11lll_opy_ (u"ࠢࡤ࡮࡬ࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨ࠿ࠨ၌") + str(self.cli_bin_session_id) + bstack11lll_opy_ (u"ࠣࠤ၍"))
                    continue
                if bstack11lll_opy_ (u"ࠤ࡯࡭ࡸࡺࡥ࡯࠿ࠥ၎") in line:
                    self.cli_listen_addr = line.split(bstack11lll_opy_ (u"ࠥࡰ࡮ࡹࡴࡦࡰࡀࠦ၏"))[-1:][0].strip()
                    self.logger.debug(bstack11lll_opy_ (u"ࠦࡨࡲࡩࡠ࡮࡬ࡷࡹ࡫࡮ࡠࡣࡧࡨࡷࡀࠢၐ") + str(self.cli_listen_addr) + bstack11lll_opy_ (u"ࠧࠨၑ"))
                    continue
                if bstack11lll_opy_ (u"ࠨࡰࡰࡴࡷࡁࠧၒ") in line:
                    port = line.split(bstack11lll_opy_ (u"ࠢࡱࡱࡵࡸࡂࠨၓ"))[-1:][0].strip()
                    self.logger.debug(bstack11lll_opy_ (u"ࠣࡲࡲࡶࡹࡀࠢၔ") + str(port) + bstack11lll_opy_ (u"ࠤࠥၕ"))
                    continue
                if line.strip() == bstack1lll1l1ll1l_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack11lll_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡌࡓࡤ࡙ࡔࡓࡇࡄࡑࠧၖ"), bstack11lll_opy_ (u"ࠦ࠶ࠨၗ")) == bstack11lll_opy_ (u"ࠧ࠷ࠢၘ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1lllll11lll_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack11lll_opy_ (u"ࠨࡥࡳࡴࡲࡶ࠿ࠦࠢၙ") + str(e) + bstack11lll_opy_ (u"ࠢࠣၚ"))
        return False
    @measure(event_name=EVENTS.bstack1lllll1l111_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def __1llllllll1l_opy_(self):
        if self.bstack1lll1l1l11l_opy_:
            self.bstack111l11l111_opy_.stop()
            start = datetime.now()
            if self.bstack1lll1l11lll_opy_():
                self.cli_bin_session_id = None
                if self.bstack1lll11l1l11_opy_:
                    self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠣࡵࡷࡳࡵࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧၛ"), datetime.now() - start)
                else:
                    self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠤࡶࡸࡴࡶ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨၜ"), datetime.now() - start)
            self.__111111l11l_opy_()
            start = datetime.now()
            self.bstack1lll1l1l11l_opy_.close()
            self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠥࡨ࡮ࡹࡣࡰࡰࡱࡩࡨࡺ࡟ࡵ࡫ࡰࡩࠧၝ"), datetime.now() - start)
            self.bstack1lll1l1l11l_opy_ = None
        if self.process:
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡸࡺ࡯ࡱࠤၞ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠧࡱࡩ࡭࡮ࡢࡸ࡮ࡳࡥࠣၟ"), datetime.now() - start)
            self.process = None
            if self.bstack1llll1ll11l_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1l1l1l1ll_opy_()
                self.logger.info(
                    bstack11lll_opy_ (u"ࠨࡖࡪࡵ࡬ࡸࠥ࡮ࡴࡵࡲࡶ࠾࠴࠵࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠥࡺ࡯ࠡࡸ࡬ࡩࡼࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡱࡱࡵࡸ࠱ࠦࡩ࡯ࡵ࡬࡫࡭ࡺࡳ࠭ࠢࡤࡲࡩࠦ࡭ࡢࡰࡼࠤࡲࡵࡲࡦࠢࡧࡩࡧࡻࡧࡨ࡫ࡱ࡫ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰࠣࡥࡱࡲࠠࡢࡶࠣࡳࡳ࡫ࠠࡱ࡮ࡤࡧࡪࠧ࡜࡯ࠤၠ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack11lll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ၡ")] = self.config_testhub.build_hashed_id
        self.bstack1lllll11lll_opy_ = False
    def __1lllll1ll1l_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack11lll_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥၢ")] = selenium.__version__
            data.frameworks.append(bstack11lll_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦၣ"))
        except:
            pass
        try:
            from playwright._1llll11l111_opy_ import __version__
            data.framework_versions[bstack11lll_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢၤ")] = __version__
            data.frameworks.append(bstack11lll_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣၥ"))
        except:
            pass
    def bstack1llll1l11ll_opy_(self, hub_url: str, platform_index: int, bstack1l1l1l1l1l_opy_: Any):
        if self.bstack11111l1lll_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠦࡳࡦࡶࡸࡴࠥࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡶࡩࡹࠦࡵࡱࠤၦ"))
            return
        try:
            bstack11lll1l11l_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack11lll_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣၧ")
            self.bstack11111l1lll_opy_ = bstack111111l111_opy_(
                hub_url,
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llllll1l11_opy_={bstack11lll_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࡠࡨࡵࡳࡲࡥࡣࡢࡲࡶࠦၨ"): bstack1l1l1l1l1l_opy_}
            )
            def bstack111111l1ll_opy_(self):
                return
            if self.config.get(bstack11lll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠥၩ"), True):
                Service.start = bstack111111l1ll_opy_
                Service.stop = bstack111111l1ll_opy_
            def get_accessibility_results(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results(driver, framework_name=framework)
            def get_accessibility_results_summary(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results_summary(driver, framework_name=framework)
            def perform_scan(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.perform_scan(driver, method=None, framework_name=framework)
            WebDriver.getAccessibilityResults = get_accessibility_results
            WebDriver.get_accessibility_results = get_accessibility_results
            WebDriver.getAccessibilityResultsSummary = get_accessibility_results_summary
            WebDriver.get_accessibility_results_summary = get_accessibility_results_summary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࠥၪ"), datetime.now() - bstack11lll1l11l_opy_)
        except Exception as e:
            self.logger.error(bstack11lll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠺ࠡࠤၫ") + str(e) + bstack11lll_opy_ (u"ࠦࠧၬ"))
    def bstack1lllll1l1ll_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._1lll11llll1_opy_ import Connection
            from playwright._1llll11l111_opy_ import __version__
            from bstack_utils.helper import bstack1llll11l1l_opy_
            self.bstack11111l1lll_opy_ = bstack1lll1l11l1l_opy_(
                platform_index,
                framework_name=bstack11lll_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤၭ"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack11lll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠿ࠦࠢၮ") + str(e) + bstack11lll_opy_ (u"ࠢࠣၯ"))
            pass
    def bstack11111111l1_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack11lll_opy_ (u"ࠣࡵ࡮࡭ࡵࡶࡥࡥࠢࡶࡩࡹࡻࡰࠡࡲࡼࡸࡪࡹࡴ࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡷࡪࡺࠠࡶࡲࠥၰ"))
            return
        if bstack11l111111_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack11lll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤၱ"): pytest.__version__ }, [bstack11lll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢၲ")])
            return
        try:
            import pytest
            self.test_framework = bstack1111111l1l_opy_({ bstack11lll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦၳ"): pytest.__version__ }, [bstack11lll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧၴ")])
        except Exception as e:
            self.logger.error(bstack11lll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡼࡸࡪࡹࡴ࠻ࠢࠥၵ") + str(e) + bstack11lll_opy_ (u"ࠢࠣၶ"))
        self.bstack1lllll111ll_opy_()
    def bstack1lllll111ll_opy_(self):
        if not self.bstack1l1l1ll11l_opy_():
            return
        bstack1lllllllll_opy_ = None
        def bstack1l111l11l_opy_(config, startdir):
            return bstack11lll_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨၷ").format(bstack11lll_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣၸ"))
        def bstack1l1l1l1111_opy_():
            return
        def bstack1l11ll1l11_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack11lll_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪၹ"):
                return bstack11lll_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥၺ")
            else:
                return bstack1lllllllll_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1lllllllll_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1l111l11l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1l1l1111_opy_
            Config.getoption = bstack1l11ll1l11_opy_
        except Exception as e:
            self.logger.error(bstack11lll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡸࡨ࡮ࠠࡱࡻࡷࡩࡸࡺࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡩࡳࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠿ࠦࠢၻ") + str(e) + bstack11lll_opy_ (u"ࠨࠢၼ"))
    def bstack1lll1l1lll1_opy_(self):
        bstack1lllll1l11l_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1lllll1l11l_opy_, dict):
            if cli.config_observability:
                bstack1lllll1l11l_opy_.update(
                    {bstack11lll_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢၽ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack11lll_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࡢࡸࡴࡥࡷࡳࡣࡳࠦၾ") in accessibility.get(bstack11lll_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥၿ"), {}):
                    bstack1lll11ll1ll_opy_ = accessibility.get(bstack11lll_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦႀ"))
                    bstack1lll11ll1ll_opy_.update({ bstack11lll_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸ࡚࡯ࡘࡴࡤࡴࠧႁ"): bstack1lll11ll1ll_opy_.pop(bstack11lll_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹ࡟ࡵࡱࡢࡻࡷࡧࡰࠣႂ")) })
                bstack1lllll1l11l_opy_.update({bstack11lll_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠨႃ"): accessibility })
        return bstack1lllll1l11l_opy_
    @measure(event_name=EVENTS.bstack11111l111l_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1lll1l11lll_opy_(self, bstack1lllll11l11_opy_: str = None, bstack1lllll1ll11_opy_: str = None, bstack1l1lll1ll_opy_: int = None):
        if not self.cli_bin_session_id or not self.bstack111l11l1l1_opy_:
            return
        bstack11lll1l11l_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if bstack1l1lll1ll_opy_:
            req.bstack1l1lll1ll_opy_ = bstack1l1lll1ll_opy_
        if bstack1lllll11l11_opy_:
            req.bstack1lllll11l11_opy_ = bstack1lllll11l11_opy_
        if bstack1lllll1ll11_opy_:
            req.bstack1lllll1ll11_opy_ = bstack1lllll1ll11_opy_
        try:
            r = self.bstack111l11l1l1_opy_.StopBinSession(req)
            self.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡴࡰࡲࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣႄ"), datetime.now() - bstack11lll1l11l_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1llllllll1_opy_(self, key: str, value: timedelta):
        tag = bstack11lll_opy_ (u"ࠣࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳࠣႅ") if self.bstack11l11111_opy_() else bstack11lll_opy_ (u"ࠤࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳࠣႆ")
        self.bstack1lll1lll1l1_opy_[bstack11lll_opy_ (u"ࠥ࠾ࠧႇ").join([tag + bstack11lll_opy_ (u"ࠦ࠲ࠨႈ") + str(id(self)), key])] += value
    def bstack1l1l1l1ll_opy_(self):
        if not os.getenv(bstack11lll_opy_ (u"ࠧࡊࡅࡃࡗࡊࡣࡕࡋࡒࡇࠤႉ"), bstack11lll_opy_ (u"ࠨ࠰ࠣႊ")) == bstack11lll_opy_ (u"ࠢ࠲ࠤႋ"):
            return
        bstack1llll11l1l1_opy_ = dict()
        bstack1111l11lll_opy_ = []
        if self.test_framework:
            bstack1111l11lll_opy_.extend(list(self.test_framework.bstack1111l11lll_opy_.values()))
        if self.bstack11111l1lll_opy_:
            bstack1111l11lll_opy_.extend(list(self.bstack11111l1lll_opy_.bstack1111l11lll_opy_.values()))
        for instance in bstack1111l11lll_opy_:
            if not instance.platform_index in bstack1llll11l1l1_opy_:
                bstack1llll11l1l1_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1llll11l1l1_opy_[instance.platform_index]
            for k, v in instance.bstack1lllll11ll1_opy_().items():
                report[k] += v
                report[k.split(bstack11lll_opy_ (u"ࠣ࠼ࠥႌ"))[0]] += v
        bstack1lll11l1l1l_opy_ = sorted([(k, v) for k, v in self.bstack1lll1lll1l1_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1lll1l111l1_opy_ = 0
        for r in bstack1lll11l1l1l_opy_:
            bstack1lll11ll1l1_opy_ = r[1].total_seconds()
            bstack1lll1l111l1_opy_ += bstack1lll11ll1l1_opy_
            self.logger.debug(bstack11lll_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡦࡰ࡮ࡀࡻࡳ࡝࠳ࡡࢂࡃႍࠢ") + str(bstack1lll11ll1l1_opy_) + bstack11lll_opy_ (u"ࠥࠦႎ"))
        self.logger.debug(bstack11lll_opy_ (u"ࠦ࠲࠳ࠢႏ"))
        bstack1lllll1l1l1_opy_ = []
        for platform_index, report in bstack1llll11l1l1_opy_.items():
            bstack1lllll1l1l1_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1lllll1l1l1_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll11ll1_opy_ = set()
        bstack1lll1l11111_opy_ = 0
        for r in bstack1lllll1l1l1_opy_:
            bstack1lll11ll1l1_opy_ = r[2].total_seconds()
            bstack1lll1l11111_opy_ += bstack1lll11ll1l1_opy_
            bstack1lll11ll1_opy_.add(r[0])
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡺࡥࡴࡶ࠽ࡴࡱࡧࡴࡧࡱࡵࡱ࠲ࢁࡲ࡜࠲ࡠࢁ࠿ࢁࡲ࡜࠳ࡠࢁࡂࠨ႐") + str(bstack1lll11ll1l1_opy_) + bstack11lll_opy_ (u"ࠨࠢ႑"))
        if self.bstack11l11111_opy_():
            self.logger.debug(bstack11lll_opy_ (u"ࠢ࠮࠯ࠥ႒"))
            self.logger.debug(bstack11lll_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡥ࡯࡭࠿ࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷࡂࢁࡴࡰࡶࡤࡰࡤࡩ࡬ࡪࡿࠣࡸࡪࡹࡴ࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶ࠱ࢀࡹࡴࡳࠪࡳࡰࡦࡺࡦࡰࡴࡰࡷ࠮ࢃ࠽ࠣ႓") + str(bstack1lll1l11111_opy_) + bstack11lll_opy_ (u"ࠤࠥ႔"))
        else:
            self.logger.debug(bstack11lll_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡧࡱ࡯࠺࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࡃࠢ႕") + str(bstack1lll1l111l1_opy_) + bstack11lll_opy_ (u"ࠦࠧ႖"))
        self.logger.debug(bstack11lll_opy_ (u"ࠧ࠳࠭ࠣ႗"))
    def bstack1llll11l11l_opy_(self, r):
        if r is not None and getattr(r, bstack11lll_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࠧ႘"), None) and getattr(r.testhub, bstack11lll_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧ႙"), None):
            errors = json.loads(r.testhub.errors.decode(bstack11lll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢႚ")))
            for bstack1lll1l1l1ll_opy_, err in errors.items():
                if err[bstack11lll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧႛ")] == bstack11lll_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨႜ"):
                    self.logger.info(err[bstack11lll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬႝ")])
                else:
                    self.logger.error(err[bstack11lll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭႞")])
cli = SDKCLI()