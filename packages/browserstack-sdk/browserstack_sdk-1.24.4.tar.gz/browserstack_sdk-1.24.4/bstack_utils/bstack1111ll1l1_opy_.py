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
import json
class bstack1l111ll1l1l_opy_(object):
  bstack1l1llll1ll_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠩࢁࠫᔺ")), bstack11ll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᔻ"))
  bstack1l111ll1l11_opy_ = os.path.join(bstack1l1llll1ll_opy_, bstack11ll1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠴ࡪࡴࡱࡱࠫᔼ"))
  commands_to_wrap = None
  perform_scan = None
  bstack111l1111_opy_ = None
  bstack1llll1l11_opy_ = None
  bstack1l11l111l11_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11ll1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠧᔽ")):
      cls.instance = super(bstack1l111ll1l1l_opy_, cls).__new__(cls)
      cls.instance.bstack1l111ll11l1_opy_()
    return cls.instance
  def bstack1l111ll11l1_opy_(self):
    try:
      with open(self.bstack1l111ll1l11_opy_, bstack11ll1l_opy_ (u"࠭ࡲࠨᔾ")) as bstack1ll111l11_opy_:
        bstack1l111ll11ll_opy_ = bstack1ll111l11_opy_.read()
        data = json.loads(bstack1l111ll11ll_opy_)
        if bstack11ll1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩᔿ") in data:
          self.bstack1l111llll11_opy_(data[bstack11ll1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪᕀ")])
        if bstack11ll1l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪᕁ") in data:
          self.bstack1l11l1l1111_opy_(data[bstack11ll1l_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫᕂ")])
    except:
      pass
  def bstack1l11l1l1111_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack11ll1l_opy_ (u"ࠫࡸࡩࡡ࡯ࠩᕃ")]
      self.bstack111l1111_opy_ = scripts[bstack11ll1l_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩᕄ")]
      self.bstack1llll1l11_opy_ = scripts[bstack11ll1l_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪᕅ")]
      self.bstack1l11l111l11_opy_ = scripts[bstack11ll1l_opy_ (u"ࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬᕆ")]
  def bstack1l111llll11_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1l111ll1l11_opy_, bstack11ll1l_opy_ (u"ࠨࡹࠪᕇ")) as file:
        json.dump({
          bstack11ll1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࠦᕈ"): self.commands_to_wrap,
          bstack11ll1l_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࡶࠦᕉ"): {
            bstack11ll1l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤᕊ"): self.perform_scan,
            bstack11ll1l_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠤᕋ"): self.bstack111l1111_opy_,
            bstack11ll1l_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠥᕌ"): self.bstack1llll1l11_opy_,
            bstack11ll1l_opy_ (u"ࠢࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠧᕍ"): self.bstack1l11l111l11_opy_
          }
        }, file)
    except:
      pass
  def bstack1ll1ll11l1_opy_(self, bstack1ll1ll1l1ll_opy_):
    try:
      return any(command.get(bstack11ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᕎ")) == bstack1ll1ll1l1ll_opy_ for command in self.commands_to_wrap)
    except:
      return False
bstack1111ll1l1_opy_ = bstack1l111ll1l1l_opy_()