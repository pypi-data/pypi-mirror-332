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
from browserstack_sdk.bstack1l1111l1l_opy_ import bstack11l111ll_opy_
from browserstack_sdk.bstack11l111l1l1_opy_ import RobotHandler
def bstack1ll1l1l11l_opy_(framework):
    if framework.lower() == bstack11lll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᢽ"):
        return bstack11l111ll_opy_.version()
    elif framework.lower() == bstack11lll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬᢾ"):
        return RobotHandler.version()
    elif framework.lower() == bstack11lll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧᢿ"):
        import behave
        return behave.__version__
    else:
        return bstack11lll_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩᣀ")
def bstack1l1lll1lll_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11lll_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫᣁ"))
        framework_version.append(importlib.metadata.version(bstack11lll_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧᣂ")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11lll_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᣃ"))
        framework_version.append(importlib.metadata.version(bstack11lll_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤᣄ")))
    except:
        pass
    return {
        bstack11lll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᣅ"): bstack11lll_opy_ (u"ࠧࡠࠩᣆ").join(framework_name),
        bstack11lll_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩᣇ"): bstack11lll_opy_ (u"ࠩࡢࠫᣈ").join(framework_version)
    }