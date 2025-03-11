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
from browserstack_sdk.bstack11lllll11_opy_ import bstack1l11l1lll1_opy_
from browserstack_sdk.bstack11l111llll_opy_ import RobotHandler
def bstack1ll1lll11l_opy_(framework):
    if framework.lower() == bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᢊ"):
        return bstack1l11l1lll1_opy_.version()
    elif framework.lower() == bstack11ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪᢋ"):
        return RobotHandler.version()
    elif framework.lower() == bstack11ll1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬᢌ"):
        import behave
        return behave.__version__
    else:
        return bstack11ll1l_opy_ (u"࠭ࡵ࡯࡭ࡱࡳࡼࡴࠧᢍ")
def bstack1l11ll11l_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11ll1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩᢎ"))
        framework_version.append(importlib.metadata.version(bstack11ll1l_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥᢏ")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᢐ"))
        framework_version.append(importlib.metadata.version(bstack11ll1l_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᢑ")))
    except:
        pass
    return {
        bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᢒ"): bstack11ll1l_opy_ (u"ࠬࡥࠧᢓ").join(framework_name),
        bstack11ll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᢔ"): bstack11ll1l_opy_ (u"ࠧࡠࠩᢕ").join(framework_version)
    }