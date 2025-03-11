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
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1ll1l1l_opy_, bstack1lll11ll11_opy_, bstack1l11lllll_opy_, bstack1l111l1l11_opy_, \
    bstack11ll1llll1l_opy_
from bstack_utils.measure import measure
def bstack1l1ll1111_opy_(bstack11l111111l1_opy_):
    for driver in bstack11l111111l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1lll1ll1_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
def bstack111111ll1_opy_(driver, status, reason=bstack11lll_opy_ (u"ࠫࠬ᱊")):
    bstack11lll111l1_opy_ = Config.bstack1ll1ll1l1l_opy_()
    if bstack11lll111l1_opy_.bstack111l1l111l_opy_():
        return
    bstack1lll1lll11_opy_ = bstack1l1111ll11_opy_(bstack11lll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ᱋"), bstack11lll_opy_ (u"࠭ࠧ᱌"), status, reason, bstack11lll_opy_ (u"ࠧࠨᱍ"), bstack11lll_opy_ (u"ࠨࠩᱎ"))
    driver.execute_script(bstack1lll1lll11_opy_)
@measure(event_name=EVENTS.bstack1lll1ll1_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
def bstack1lll1lllll_opy_(page, status, reason=bstack11lll_opy_ (u"ࠩࠪᱏ")):
    try:
        if page is None:
            return
        bstack11lll111l1_opy_ = Config.bstack1ll1ll1l1l_opy_()
        if bstack11lll111l1_opy_.bstack111l1l111l_opy_():
            return
        bstack1lll1lll11_opy_ = bstack1l1111ll11_opy_(bstack11lll_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭᱐"), bstack11lll_opy_ (u"ࠫࠬ᱑"), status, reason, bstack11lll_opy_ (u"ࠬ࠭᱒"), bstack11lll_opy_ (u"࠭ࠧ᱓"))
        page.evaluate(bstack11lll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ᱔"), bstack1lll1lll11_opy_)
    except Exception as e:
        print(bstack11lll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨ᱕"), e)
def bstack1l1111ll11_opy_(type, name, status, reason, bstack1l111l1ll1_opy_, bstack1l1ll11l11_opy_):
    bstack1l111lllll_opy_ = {
        bstack11lll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ᱖"): type,
        bstack11lll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭᱗"): {}
    }
    if type == bstack11lll_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭᱘"):
        bstack1l111lllll_opy_[bstack11lll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ᱙")][bstack11lll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᱚ")] = bstack1l111l1ll1_opy_
        bstack1l111lllll_opy_[bstack11lll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᱛ")][bstack11lll_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᱜ")] = json.dumps(str(bstack1l1ll11l11_opy_))
    if type == bstack11lll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᱝ"):
        bstack1l111lllll_opy_[bstack11lll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᱞ")][bstack11lll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᱟ")] = name
    if type == bstack11lll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᱠ"):
        bstack1l111lllll_opy_[bstack11lll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᱡ")][bstack11lll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᱢ")] = status
        if status == bstack11lll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᱣ") and str(reason) != bstack11lll_opy_ (u"ࠤࠥᱤ"):
            bstack1l111lllll_opy_[bstack11lll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᱥ")][bstack11lll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᱦ")] = json.dumps(str(reason))
    bstack1l111lll11_opy_ = bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᱧ").format(json.dumps(bstack1l111lllll_opy_))
    return bstack1l111lll11_opy_
def bstack1l11111ll_opy_(url, config, logger, bstack11ll11ll1l_opy_=False):
    hostname = bstack1lll11ll11_opy_(url)
    is_private = bstack1l111l1l11_opy_(hostname)
    try:
        if is_private or bstack11ll11ll1l_opy_:
            file_path = bstack11ll1ll1l1l_opy_(bstack11lll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᱨ"), bstack11lll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᱩ"), logger)
            if os.environ.get(bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᱪ")) and eval(
                    os.environ.get(bstack11lll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᱫ"))):
                return
            if (bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᱬ") in config and not config[bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᱭ")]):
                os.environ[bstack11lll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᱮ")] = str(True)
                bstack11l11111111_opy_ = {bstack11lll_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨᱯ"): hostname}
                bstack11ll1llll1l_opy_(bstack11lll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᱰ"), bstack11lll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ᱱ"), bstack11l11111111_opy_, logger)
    except Exception as e:
        pass
def bstack1ll1l111ll_opy_(caps, bstack11l1111111l_opy_):
    if bstack11lll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᱲ") in caps:
        caps[bstack11lll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᱳ")][bstack11lll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪᱴ")] = True
        if bstack11l1111111l_opy_:
            caps[bstack11lll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᱵ")][bstack11lll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᱶ")] = bstack11l1111111l_opy_
    else:
        caps[bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᱷ")] = True
        if bstack11l1111111l_opy_:
            caps[bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᱸ")] = bstack11l1111111l_opy_
def bstack1l11l111l11_opy_(bstack111lll111l_opy_):
    bstack111llllllll_opy_ = bstack1l11lllll_opy_(threading.current_thread(), bstack11lll_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᱹ"), bstack11lll_opy_ (u"ࠪࠫᱺ"))
    if bstack111llllllll_opy_ == bstack11lll_opy_ (u"ࠫࠬᱻ") or bstack111llllllll_opy_ == bstack11lll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᱼ"):
        threading.current_thread().testStatus = bstack111lll111l_opy_
    else:
        if bstack111lll111l_opy_ == bstack11lll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᱽ"):
            threading.current_thread().testStatus = bstack111lll111l_opy_