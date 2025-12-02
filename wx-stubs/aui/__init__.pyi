# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

from .. import (BookCtrlBase, BookCtrlEvent, Control, Event, EvtHandler, Frame,
                NotifyEvent, Panel)

class AuiNotebook(BookCtrlBase):
    """ AuiNotebook is part of the AUI class framework, which represents a
notebook control, managing multiple windows with associated tabs.

        Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def AddPage(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def AdvanceSelection(self, forward=True) -> None:
        """ Sets the selection to the next or previous page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def ChangeSelection(self, n) -> None:
        """ Changes the selection for the given page, returning the previous selection.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> None:
        """ Creates the notebook window.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def DeleteAllPages(self) -> None:
        """ Deletes all pages.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def DeletePage(self, page) -> None:
        """ Deletes a page at the given index.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def FindTab(self, page, ctrl, idx) -> None:
        """ Finds tab control associated with a given window and its tab index.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetActiveTabCtrl(self) -> None:
        """ Returns active tab control for this notebook.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetArtProvider(self) -> None:
        """ Returns the associated art provider.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetCurrentPage(self) -> None:
        """ Returns the currently selected page or None.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetHeightForPageHeight(self, pageHeight) -> None:
        """ Returns the desired height of the notebook for the given page height.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPage(self, page_idx) -> None:
        """ Returns the page specified by the given index.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageBitmap(self, page) -> None:
        """ Returns the tab bitmap for the page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageCount(self) -> None:
        """ Returns the number of pages in the notebook.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageImage(self, nPage) -> None:
        """ Returns the image index for the given page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageIndex(self, page_wnd) -> None:
        """ Returns the page index for the specified window.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageText(self, page) -> None:
        """ Returns the tab label for the page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageToolTip(self, pageIdx) -> None:
        """ Returns the tooltip for the tab label of the page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetSelection(self) -> None:
        """ Returns the currently selected page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetTabCtrlFromPoint(self, pt) -> None:
        """ Returns tab control based on point coordinates inside the tab frame.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetTabCtrlHeight(self) -> None:
        """ Returns the height of the tab control.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def InsertPage(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def RemovePage(self, page) -> None:
        """ Removes a page, without deleting the window pointer.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetArtProvider(self, art) -> None:
        """ Sets the art provider to be used by the notebook.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetFont(self, font) -> None:
        """ Sets the font for drawing the tab labels, using a bold version of the font for selected tab labels.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetMeasuringFont(self, font) -> None:
        """ Sets the font for measuring tab labels.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetNormalFont(self, font) -> None:
        """ Sets the font for drawing unselected tab labels.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetPageBitmap(self, page, bitmap) -> None:
        """ Sets the bitmap for the page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetPageImage(self, n, imageId) -> None:
        """ Sets the image index for the given page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetPageText(self, page, text) -> None:
        """ Sets the tab label for the page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetPageToolTip(self, page, text) -> None:
        """ Sets the tooltip displayed when hovering over the tab label of the page.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetSelectedFont(self, font) -> None:
        """ Sets the font for drawing selected tab labels.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetSelection(self, new_page) -> None:
        """ Sets the page selection.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetTabCtrlHeight(self, height) -> None:
        """ Sets the tab height.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetUniformBitmapSize(self, size) -> None:
        """ Ensure that all tabs have the same height, even if some of them donât have bitmaps.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def ShowWindowMenu(self) -> None:
        """ Shows the window menu for the active tab control associated with this notebook, and returns True if a selection was made.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def Split(self, page, direction) -> None:
        """ Split performs a split operation programmatically.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    ActiveTabCtrl: None  # See GetActiveTabCtrl
    ArtProvider: None  # See GetArtProvider and SetArtProvider
    CurrentPage: None  # See GetCurrentPage
    PageCount: None  # See GetPageCount
    Selection: None  # See GetSelection and SetSelection
    TabCtrlHeight: None  # See GetTabCtrlHeight and SetTabCtrlHeight



AUI_NB_DEFAULT_STYLE: int  # Defined as wx.aui.AUI_NB_TOP | wx.aui.AUI_NB_TAB_SPLIT | wx.aui.AUI_NB_TAB_MOVE | wx.aui.AUI_NB_SCROLL_BUTTONS | wx.aui.AUI_NB_CLOSE_ON_ACTIVE_TAB | wx.aui.AUI_NB_MIDDLE_CLICK_CLOSE.

AUI_NB_TAB_SPLIT: int  # Allows the tab control to be split by dragging a tab.

AUI_NB_TAB_MOVE: int  # Allows a tab to be moved horizontally by dragging.

AUI_NB_TAB_EXTERNAL_MOVE: int  # Allows a tab to be moved to another tab control.

AUI_NB_TAB_FIXED_WIDTH: int  # With this style, all tabs have the same width.

AUI_NB_SCROLL_BUTTONS: int  # With this style, left and right scroll buttons are displayed.

AUI_NB_WINDOWLIST_BUTTON: int  # With this style, a drop-down list of windows is available.

AUI_NB_CLOSE_BUTTON: int  # With this style, a close button is available on the tab bar.

AUI_NB_CLOSE_ON_ACTIVE_TAB: int  # With this style, the close button is visible on the active tab.

AUI_NB_CLOSE_ON_ALL_TABS: int  # With this style, the close button is visible on all tabs.

AUI_NB_MIDDLE_CLICK_CLOSE: int  # With this style, middle click on a tab closes the tab.

AUI_NB_TOP: int  # With this style, tabs are drawn along the top of the notebook.

AUI_NB_BOTTOM: int  # With this style, tabs are drawn along the bottom of the notebook.

EVT_AUINOTEBOOK_PAGE_CLOSE: int  # A page is about to be closed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CLOSE   event.

EVT_AUINOTEBOOK_PAGE_CLOSED: int  # A page has been closed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CLOSED   event.

EVT_AUINOTEBOOK_PAGE_CHANGED: int  # The page selection was changed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CHANGED   event.

EVT_AUINOTEBOOK_PAGE_CHANGING: int  # The page selection is about to be changed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CHANGING   event. This event can be vetoed.

EVT_AUINOTEBOOK_BUTTON: int  # The window list button has been pressed. Processes a  wxEVT_AUINOTEBOOK_BUTTON   event.

EVT_AUINOTEBOOK_BEGIN_DRAG: int  # Dragging is about to begin. Processes a  wxEVT_AUINOTEBOOK_BEGIN_DRAG   event.

EVT_AUINOTEBOOK_END_DRAG: int  # Dragging has ended. Processes a  wxEVT_AUINOTEBOOK_END_DRAG   event.

EVT_AUINOTEBOOK_DRAG_MOTION: int  # Emitted during a drag and drop operation. Processes a  wxEVT_AUINOTEBOOK_DRAG_MOTION   event.

EVT_AUINOTEBOOK_ALLOW_DND: int  # Whether to allow a tab to be dropped. Processes a  wxEVT_AUINOTEBOOK_ALLOW_DND   event. This event must be specially allowed.

EVT_AUINOTEBOOK_DRAG_DONE: int  # Notify that the tab has been dragged. Processes a  wxEVT_AUINOTEBOOK_DRAG_DONE   event.

EVT_AUINOTEBOOK_TAB_MIDDLE_DOWN: int  # The middle mouse button is pressed on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_MIDDLE_DOWN   event.

EVT_AUINOTEBOOK_TAB_MIDDLE_UP: int  # The middle mouse button is released on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_MIDDLE_UP   event.

EVT_AUINOTEBOOK_TAB_RIGHT_DOWN: int  # The right mouse button is pressed on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_RIGHT_DOWN   event.

EVT_AUINOTEBOOK_TAB_RIGHT_UP: int  # The right mouse button is released on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_RIGHT_UP   event.

EVT_AUINOTEBOOK_BG_DCLICK: int  # Double clicked on the tabs background area. Processes a  wxEVT_AUINOTEBOOK_BG_DCLICK   event.

NOT_FOUND: int

TOP: int

BOTTOM: int

LEFT: int

RIGHT: int

class AuiNotebookEvent(BookCtrlEvent):
    """ This class is used by the events generated by AuiNotebook.

        Source: https://docs.wxpython.org/wx.aui.AuiNotebookEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.aui.AuiNotebookEvent.html
        """

    def Clone(self) -> None:
        """ Event

            Source: https://docs.wxpython.org/wx.aui.AuiNotebookEvent.html
        """



class AuiDefaultTabArt(AuiTabArt):
    """ Default art provider for AuiNotebook.

        Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
    """
    def __init__(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def Clone(self) -> None:
        """ Clones the art object.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ Draws a background on the given area.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def DrawButton(self, dc, wnd, in_rect, bitmap_id, button_state, orientation, out_rect) -> None:
        """ Draws a button.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def DrawTab(self, dc, wnd, page, rect, close_button_state, out_tab_rect, out_button_rect, x_extent) -> None:
        """ Draws a tab.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def GetBestTabCtrlSize(self) -> None:
        """ Returns the tab control size.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def GetIndentSize(self) -> None:
        """ Returns the indent size.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, x_extent) -> None:
        """ Returns the tab size for the given caption, bitmap and state.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetActiveColour(self, colour) -> None:
        """ Sets the colour of the selected tab.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetColour(self, colour) -> None:
        """ Sets the colour of the inactive tabs.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetFlags(self, flags) -> None:
        """ Sets flags.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetMeasuringFont(self, font) -> None:
        """ Sets the font used for calculating measurements.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetNormalFont(self, font) -> None:
        """ Sets the normal font for drawing labels.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetSelectedFont(self, font) -> None:
        """ Sets the font for drawing text for selected UI elements.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, wnd=None) -> None:
        """ Sets sizing information.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def ShowDropDown(self, wnd, items, activeIdx) -> None:
        """ wnd (wx.Window)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    IndentSize: None  # See GetIndentSize



class AuiMDIClientWindow(AuiNotebook):
    """  Overloaded Implementations:

        Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    def CreateClient(self, parent, style=VSCROLL | HSCROLL) -> None:
        """ parent (wx.aui.AuiMDIParentFrame)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    def GetActiveChild(self) -> None:
        """ wx.aui.AuiMDIChildFrame

            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    def SetActiveChild(self, pChildFrame) -> None:
        """ pChildFrame (wx.aui.AuiMDIChildFrame)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    def SetSelection(self, new_page) -> None:
        """ Sets the page selection.

            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    ActiveChild: None  # See GetActiveChild and SetActiveChild



class AuiTabCtrl:
    """ parent (wx.Window)

        Source: https://docs.wxpython.org/wx.aui.AuiTabCtrl.html
    """
    def __init__(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> None:
        """ parent (wx.Window)

            Source: https://docs.wxpython.org/wx.aui.AuiTabCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.aui.AuiTabCtrl.html
        """

    def IsDragging(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiTabCtrl.html
        """



class AuiTabArt:
    """ Tab art provider defines all the drawing functions used by
AuiNotebook.

        Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def Clone(self) -> None:
        """ Clones the art object.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ Draws a background on the given area.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def DrawButton(self, dc, wnd, in_rect, bitmap_id, button_state, orientation, out_rect) -> None:
        """ Draws a button.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def DrawTab(self, dc, wnd, page, rect, close_button_state, out_tab_rect, out_button_rect, x_extent) -> None:
        """ Draws a tab.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def GetBestTabCtrlSize(self) -> None:
        """ Returns the tab control size.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def GetIndentSize(self) -> None:
        """ Returns the indent size.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, x_extent) -> None:
        """ Returns the tab size for the given caption, bitmap and state.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetActiveColour(self, colour) -> None:
        """ Sets the colour of the selected tab.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetColour(self, colour) -> None:
        """ Sets the colour of the inactive tabs.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetFlags(self, flags) -> None:
        """ Sets flags.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetMeasuringFont(self, font) -> None:
        """ Sets the font used for calculating measurements.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetNormalFont(self, font) -> None:
        """ Sets the normal font for drawing labels.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetSelectedFont(self, font) -> None:
        """ Sets the font for drawing text for selected UI elements.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, wnd=None) -> None:
        """ Sets sizing information.

            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    IndentSize: None  # See GetIndentSize



class AuiToolBar(Control):
    """ AuiToolBar is a dockable toolbar, part of the AUI class framework.

        Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddControl(self, control, label='') -> None:
        """ control (wx.Control)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddLabel(self, toolId, label='', width=-1) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddSeparator(self) -> None:
        """ wx.aui.AuiToolBarItem

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddSpacer(self, pixels) -> None:
        """ pixels (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddStretchSpacer(self, proportion=1) -> None:
        """ proportion (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddTool(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def Clear(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def ClearTools(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=AUI_TB_DEFAULT_STYLE) -> None:
        """ Really create   wx.aui.AuiToolBar  created using default constructor.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def DeleteByIndex(self, idx) -> None:
        """ Removes the tool at the given position from the toolbar.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def DeleteTool(self, toolId) -> None:
        """ Removes the tool with the given ID from the toolbar.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def DestroyTool(self, toolId) -> None:
        """ Destroys the tool with the given ID and its associated window, if any.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def DestroyToolByIndex(self, idx) -> None:
        """ Destroys the tool at the given position and its associated window, if any.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def EnableTool(self, toolId, state) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def FindControl(self, window_id) -> None:
        """ window_id (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def FindTool(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def FindToolByIndex(self, idx) -> None:
        """ idx (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def FindToolByPosition(self, x, y) -> None:
        """ x (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetArtProvider(self) -> None:
        """ wx.aui.AuiToolBarArt

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetGripperVisible(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetHintSize(self, dock_direction) -> None:
        """ get size of hint rectangle for a particular dock location

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetOverflowVisible(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolBarFits(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolBitmap(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolBitmapSize(self) -> None:
        """ Size

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolBorderPadding(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolCount(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolDropDown(self, toolId) -> None:
        """ Returns whether the specified toolbar item has an associated drop down button.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolEnabled(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolFits(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolFitsByIndex(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolIndex(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolLabel(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolLongHelp(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolPacking(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolPos(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolProportion(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolRect(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolSeparation(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolShortHelp(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolSticky(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolTextOrientation(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolToggled(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetWindowStyleFlag(self) -> None:
        """ Gets the window style that was passed to the constructor or Create   method.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def IsPaneValid(self, pane) -> None:
        """ pane (wx.aui.AuiPaneInfo)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def Realize(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetArtProvider(self, art) -> None:
        """ art (wx.aui.AuiToolBarArt)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetCustomOverflowItems(self, prepend, append) -> None:
        """ Add toolbar items that are always displayed in the overflow menu.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetFont(self, font) -> None:
        """ Sets the font for this window.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetGripperVisible(self, visible) -> None:
        """ visible (bool)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetMargins(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetOverflowVisible(self, visible) -> None:
        """ visible (bool)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolBitmap(self, toolId, bitmap) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolBitmapSize(self, size) -> None:
        """ size (wx.Size)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolBorderPadding(self, padding) -> None:
        """ padding (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolDropDown(self, toolId, dropdown) -> None:
        """ Set whether the specified toolbar item has a drop down button.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolLabel(self, toolId, label) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolLongHelp(self, toolId, help_string) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolPacking(self, packing) -> None:
        """ packing (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolProportion(self, toolId, proportion) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolSeparation(self, separation) -> None:
        """ separation (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolShortHelp(self, toolId, help_string) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolSticky(self, toolId, sticky) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolTextOrientation(self, orientation) -> None:
        """ orientation (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetWindowStyleFlag(self, style) -> None:
        """ Sets the style of the window.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def ToggleTool(self, toolId, state) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    ArtProvider: None  # See GetArtProvider and SetArtProvider
    GripperVisible: None  # See GetGripperVisible and SetGripperVisible
    OverflowVisible: None  # See GetOverflowVisible and SetOverflowVisible
    ToolBarFits: None  # See GetToolBarFits
    ToolBitmapSize: None  # See GetToolBitmapSize and SetToolBitmapSize
    ToolBorderPadding: None  # See GetToolBorderPadding and SetToolBorderPadding
    ToolCount: None  # See GetToolCount
    ToolPacking: None  # See GetToolPacking and SetToolPacking
    ToolSeparation: None  # See GetToolSeparation and SetToolSeparation
    ToolTextOrientation: None  # See GetToolTextOrientation and SetToolTextOrientation
    WindowStyleFlag: None  # See GetWindowStyleFlag and SetWindowStyleFlag



AUI_TB_TEXT: int  # Display the label strings on the toolbar buttons.

AUI_TB_NO_TOOLTIPS: int  # Do not show tooltips for the toolbar items.

AUI_TB_NO_AUTORESIZE: int  # Do not automatically resize the toolbar when new tools are added.

AUI_TB_GRIPPER: int  # Show the toolbarâs gripper control. If the toolbar is added to an AUI pane that contains a gripper, this style will be automatically set.

AUI_TB_OVERFLOW: int  # Show an overflow menu containing toolbar items that canât fit on the toolbar if it is too small.

AUI_TB_VERTICAL: int  # Using this style forces the toolbar to be vertical and be only dockable to the left or right sides of the window whereas by default it can be horizontal or vertical and be docked anywhere.

AUI_TB_HORZ_LAYOUT: int

AUI_TB_HORIZONTAL: int  # Analogous to wx.aui.AUI_TB_VERTICAL, but forces the toolbar to be horizontal.

AUI_TB_PLAIN_BACKGROUND: int  # Draw a plain background (based on parent) instead of the default gradient background.

AUI_TB_HORZ_TEXT: int  # Equivalent to wx.aui.AUI_TB_HORZ_LAYOUT | wx.aui.AUI_TB_TEXT

AUI_TB_DEFAULT_STYLE: int  # The default is to have no styles.

EVT_AUITOOLBAR_TOOL_DROPDOWN: int  # Process a wxEVT_AUITOOLBAR_TOOL_DROPDOWN event

EVT_AUITOOLBAR_OVERFLOW_CLICK: int  # Process a wxEVT_AUITOOLBAR_OVERFLOW_CLICK event

EVT_AUITOOLBAR_RIGHT_CLICK: int  # Process a wxEVT_AUITOOLBAR_RIGHT_CLICK event

EVT_AUITOOLBAR_MIDDLE_CLICK: int  # Process a wxEVT_AUITOOLBAR_MIDDLE_CLICK event

EVT_AUITOOLBAR_BEGIN_DRAG: int  # Process a wxEVT_AUITOOLBAR_BEGIN_DRAG event

ITEM_NORMAL: int

class AuiManagerEvent(Event):
    """ Event used to indicate various actions taken with AuiManager.

        Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
    """
    def __init__(self, type=wxEVT_NULL) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def CanVeto(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetButton(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetDC(self) -> None:
        """ DC

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetManager(self) -> None:
        """ wx.aui.AuiManager

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetPane(self) -> None:
        """ wx.aui.AuiPaneInfo

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetVeto(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetButton(self, button) -> None:
        """ Sets the ID of the button clicked that triggered this event.

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetCanVeto(self, can_veto) -> None:
        """ Sets whether or not this event can be vetoed.

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetDC(self, pdc) -> None:
        """ pdc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetManager(self, manager) -> None:
        """ Sets the   wx.aui.AuiManager  this event is associated with.

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetPane(self, pane) -> None:
        """ Sets the pane this event is associated with.

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def Veto(self, veto=True) -> None:
        """ Cancels the action indicated by this event if CanVeto   is True.

            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    Button: None  # See GetButton and SetButton
    DC: None  # See GetDC and SetDC
    Manager: None  # See GetManager and SetManager
    Pane: None  # See GetPane and SetPane



EVT_AUI_PANE_BUTTON: int  # Triggered when any button is pressed for any docked panes.

EVT_AUI_PANE_CLOSE: int  # Triggered when a docked or floating pane is closed.

EVT_AUI_PANE_MAXIMIZE: int  # Triggered when a pane is maximized.

EVT_AUI_PANE_RESTORE: int  # Triggered when a pane is restored.

EVT_AUI_PANE_ACTIVATED: int  # Triggered when a pane is made âactiveâ. This event is new since wxWidgets 2.9.4.

EVT_AUI_RENDER: int  # This event can be caught to override the default renderer in order to custom draw your   wx.aui.AuiManager  window (not recommended).

class AuiManager(EvtHandler):
    """ AuiManager is the central class of the AUI class framework.

        Source: https://docs.wxpython.org/wx.aui.AuiManager.html
    """
    def __init__(self, managed_wnd=None, flags=AUI_MGR_DEFAULT) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def AddPane(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    @staticmethod
    def AlwaysUsesLiveResize() -> None:
        """ Returns True if live resize is always used on the current platform.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def CalculateHintRect(self, paneWindow, pt, offset) -> None:
        """ This function is used by controls to calculate the drop hint rectangle.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def CanDockPanel(self, p) -> None:
        """ Check if a key modifier is pressed (actually   or ) while dragging the frame to not dock the window.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def ClosePane(self, paneInfo) -> None:
        """ Destroys or hides the given pane depending on its flags.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def CreateFloatingFrame(self, parent, p) -> None:
        """ Creates a floating frame in this   wx.aui.AuiManager  with the given parent and   wx.aui.AuiPaneInfo.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def DetachPane(self, window) -> None:
        """ Tells the   wx.aui.AuiManager  to stop managing the pane specified by window.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def DrawHintRect(self, paneWindow, pt, offset) -> None:
        """ This function is used by controls to draw the hint window.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetAllPanes(self) -> None:
        """ Returns an array of all panes managed by the frame manager.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetArtProvider(self) -> None:
        """ Returns the current art provider being used.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetDockSizeConstraint(self, widthpct, heightpct) -> None:
        """ Returns the current dock constraint values.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetFlags(self) -> None:
        """ Returns the current   wx.aui.AuiManagerOptionâs flags.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetManagedWindow(self) -> None:
        """ Returns the frame currently being managed by   wx.aui.AuiManager.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    @staticmethod
    def GetManager(window) -> None:
        """ Calling this method will return the   wx.aui.AuiManager  for a given window.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetPane(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def HasLiveResize(self) -> None:
        """ Returns True if windows are resized live.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def HideHint(self) -> None:
        """ HideHint   hides any docking hint that may be visible.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def InsertPane(self, window, insert_location, insert_level=AUI_INSERT_PANE) -> None:
        """ This method is used to insert either a previously unmanaged pane window into the frame manager, or to insert a currently managed pane somewhere else.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def LoadPaneInfo(self, pane_part, pane) -> None:
        """ LoadPaneInfo   is similar to LoadPerspective, with the exception that it only loads information about a single pane.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def LoadPerspective(self, perspective, update=True) -> None:
        """ Loads a saved perspective.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def MaximizePane(self, paneInfo) -> None:
        """ Maximize the given pane.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def ProcessDockResult(self, target, new_pos) -> None:
        """ ProcessDockResult   is a protected member of the AUI layout manager.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def RestoreMaximizedPane(self) -> None:
        """ Restore the previously maximized pane.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def RestorePane(self, paneInfo) -> None:
        """ Restore the last state of the given pane.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SavePaneInfo(self, pane) -> None:
        """ SavePaneInfo   is similar to SavePerspective, with the exception that it only saves information about a single pane.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SavePerspective(self) -> None:
        """ Saves the entire user interface layout into an encoded String     , which can then be stored by the application (probably using Config).

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SetArtProvider(self, art_provider) -> None:
        """ Instructs   wx.aui.AuiManager  to use art provider specified by parameter art_provider  for all drawing calls.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SetDockSizeConstraint(self, widthpct, heightpct) -> None:
        """ When a user creates a new dock by dragging a window into a docked position, often times the large size of the window will create a dock that is unwieldy large.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SetFlags(self, flags) -> None:
        """ This method is used to specify   wx.aui.AuiManagerOptionâs flags.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SetManagedWindow(self, managed_wnd) -> None:
        """ Called to specify the frame or window which is to be managed by   wx.aui.AuiManager.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def ShowHint(self, rect) -> None:
        """ This function is used by controls to explicitly show a hint window at the specified rectangle.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def StartPaneDrag(self, paneWindow, offset) -> None:
        """ Mostly used internally to define the drag action parameters.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def UnInit(self) -> None:
        """ Dissociate the managed window from the manager.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def Update(self) -> None:
        """ This method is called after any number of changes are made to any of the managed panes.

            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    AllPanes: None  # See GetAllPanes
    ArtProvider: None  # See GetArtProvider and SetArtProvider
    Flags: None  # See GetFlags and SetFlags
    ManagedWindow: None  # See GetManagedWindow and SetManagedWindow



AUI_MGR_ALLOW_FLOATING: int  # Allow a pane to be undocked to take the form of a   wx.MiniFrame.

AUI_MGR_ALLOW_ACTIVE_PANE: int  # Change the color of the title bar of the pane when it is activated.

AUI_MGR_TRANSPARENT_DRAG: int  # Make the pane transparent during its movement.

AUI_MGR_TRANSPARENT_HINT: int  # The possible location for docking is indicated by a translucent area.

AUI_MGR_VENETIAN_BLINDS_HINT: int  # The possible location for docking is indicated by gradually appearing partially transparent hint.

AUI_MGR_RECTANGLE_HINT: int  # The possible location for docking is indicated by a rectangular outline.

AUI_MGR_HINT_FADE: int  # The translucent area where the pane could be docked appears gradually.

AUI_MGR_NO_VENETIAN_BLINDS_FADE: int  # Used in complement of wx.aui.AUI_MGR_VENETIAN_BLINDS_HINT to show the docking hint immediately.

AUI_MGR_LIVE_RESIZE: int  # When a docked pane is resized, its content is refreshed in live (instead of moving the border alone and refreshing the content at the end).

AUI_MGR_DEFAULT: int  # Default behaviour, combines: wx.aui.AUI_MGR_ALLOW_FLOATING | wx.aui.AUI_MGR_TRANSPARENT_HINT | wx.aui.AUI_MGR_HINT_FADE | wx.aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE.

class AuiFloatingFrame(Frame):
    """ parent (wx.Window)

        Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
    """
    def __init__(self, parent, ownerMgr, pane, id=ID_ANY, style=RESIZE_BORDER | SYSTEM_MENU | CAPTION | FRAME_NO_TASKBAR | FRAME_FLOAT_ON_PARENT | CLIP_CHILDREN) -> None:
        """ parent (wx.Window)

            Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
        """

    def GetAuiManager(self) -> None:
        """ Returns the embedded   wx.aui.AuiManager  managing this floating paneâs contents.

            Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
        """

    def GetOwnerManager(self) -> None:
        """ wx.aui.AuiManager

            Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
        """

    def SetPaneWindow(self, pane) -> None:
        """ pane (wx.aui.AuiPaneInfo)

            Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
        """

    AuiManager: None  # See GetAuiManager
    OwnerManager: None  # See GetOwnerManager



class AuiMDIParentFrame(Frame):
    """  Overloaded Implementations:

        Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def ActivateNext(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def ActivatePrevious(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def ArrangeIcons(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def Cascade(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def Create(self, parent, winid=ID_ANY, title='', pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE | VSCROLL | HSCROLL, name=FrameNameStr) -> None:
        """ parent (wx.Window)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetActiveChild(self) -> None:
        """ wx.aui.AuiMDIChildFrame

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetArtProvider(self) -> None:
        """ wx.aui.AuiTabArt

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetClientWindow(self) -> None:
        """ wx.aui.AuiMDIClientWindow

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetNotebook(self) -> None:
        """ wx.aui.AuiNotebook

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetWindowMenu(self) -> None:
        """ Menu

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def OnCreateClient(self) -> None:
        """ wx.aui.AuiMDIClientWindow

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetActiveChild(self, pChildFrame) -> None:
        """ pChildFrame (wx.aui.AuiMDIChildFrame)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetArtProvider(self, provider) -> None:
        """ provider (wx.aui.AuiTabArt)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetChildMenuBar(self, pChild) -> None:
        """ pChild (wx.aui.AuiMDIChildFrame)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetMenuBar(self, menuBar) -> None:
        """ Tells the frame to show the given menu bar.

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetWindowMenu(self, pMenu) -> None:
        """ pMenu (wx.Menu)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def Tile(self, orient=HORIZONTAL) -> None:
        """ orient (Orientation)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    ActiveChild: None  # See GetActiveChild and SetActiveChild
    ArtProvider: None  # See GetArtProvider and SetArtProvider
    ClientWindow: None  # See GetClientWindow
    Notebook: None  # See GetNotebook
    WindowMenu: None  # See GetWindowMenu and SetWindowMenu



class AuiToolBarEvent(NotifyEvent):
    """ AuiToolBarEvent is used for the events generated by AuiToolBar.

        Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def GetClickPoint(self) -> None:
        """ Returns the point where the user clicked with the mouse.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def GetItemRect(self) -> None:
        """ Returns the   wx.aui.AuiToolBarItem  rectangle bounding the mouse click point.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def GetToolId(self) -> None:
        """ Returns the   wx.aui.AuiToolBarItem  identifier.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def IsDropDownClicked(self) -> None:
        """ Returns whether the drop down menu has been clicked.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def SetClickPoint(self, p) -> None:
        """ p (wx.Point)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def SetDropDownClicked(self, c) -> None:
        """ c (bool)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def SetItemRect(self, r) -> None:
        """ r (wx.Rect)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def SetToolId(self, toolId) -> None:
        """ toolId (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    ClickPoint: None  # See GetClickPoint and SetClickPoint
    ItemRect: None  # See GetItemRect and SetItemRect
    ToolId: None  # See GetToolId and SetToolId



class AuiMDIChildFrame(Panel):
    """  Overloaded Implementations:

        Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Activate(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Create(self, parent, winid=ID_ANY, title='', pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameStr) -> None:
        """ parent (wx.aui.AuiMDIParentFrame)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def CreateStatusBar(self, number=1, style=1, winid=1, name='') -> None:
        """ number (int)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def CreateToolBar(self, style, winid, name) -> None:
        """ style (long)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Destroy(self) -> None:
        """ Destroys the window safely.

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetIcon(self) -> None:
        """ Icon

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetIcons(self) -> None:
        """ IconBundle

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetMDIParentFrame(self) -> None:
        """ wx.aui.AuiMDIParentFrame

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetMenuBar(self) -> None:
        """ MenuBar

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetStatusBar(self) -> None:
        """ StatusBar

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetTitle(self) -> None:
        """ str

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetToolBar(self) -> None:
        """ ToolBar

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Iconize(self, iconize=True) -> None:
        """ iconize (bool)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def IsFullScreen(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def IsIconized(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def IsMaximized(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def IsTopLevel(self) -> None:
        """ Returns True if the given window is a top-level one.

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Maximize(self, maximize=True) -> None:
        """ maximize (bool)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Restore(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetIcon(self, icon) -> None:
        """ icon (wx.Icon)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetIcons(self, icons) -> None:
        """ icons (wx.IconBundle)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetMDIParentFrame(self, parent) -> None:
        """ parent (wx.aui.AuiMDIParentFrame)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetMenuBar(self, menuBar) -> None:
        """ menuBar (wx.MenuBar)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetStatusText(self, text, number=0) -> None:
        """ text (string)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetStatusWidths(self, widths) -> None:
        """ widths (list of integers)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetTitle(self, title) -> None:
        """ title (string)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Show(self, show=True) -> None:
        """ Shows or hides the window.

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def ShowFullScreen(self, show, style) -> None:
        """ show (bool)

            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    Icon: None  # See GetIcon and SetIcon
    Icons: None  # See GetIcons and SetIcons
    MDIParentFrame: None  # See GetMDIParentFrame and SetMDIParentFrame
    MenuBar: None  # See GetMenuBar and SetMenuBar
    StatusBar: None  # See GetStatusBar
    Title: None  # See GetTitle and SetTitle
    ToolBar: None  # See GetToolBar



class AuiNotebookPage:
    """ A simple class which holds information about the notebookâs pages and
their state.

        Source: https://docs.wxpython.org/wx.aui.AuiNotebookPage.html
    """
    active: Any  # A public C++ attribute of type bool.
    bitmap: Any  # A public C++ attribute of type BitmapBundle     .
    caption: Any  # A public C++ attribute of type string.
    rect: Any  # A public C++ attribute of type Rect     .
    tooltip: Any  # A public C++ attribute of type string.
    window: Any  # A public C++ attribute of type Window     .



class AuiSimpleTabArt(AuiTabArt):
    """ Another standard tab art provider for AuiNotebook.

        Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
    """
    def __init__(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def Clone(self) -> None:
        """ Clones the art object.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ Draws a background on the given area.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def DrawButton(self, dc, wnd, in_rect, bitmap_id, button_state, orientation, out_rect) -> None:
        """ Draws a button.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def DrawTab(self, dc, wnd, page, rect, close_button_state, out_tab_rect, out_button_rect, x_extent) -> None:
        """ Draws a tab.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def GetBestTabCtrlSize(self) -> None:
        """ Returns the tab control size.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def GetIndentSize(self) -> None:
        """ Returns the indent size.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, closeButtonState, xExtent) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetActiveColour(self, colour) -> None:
        """ Sets the colour of the selected tab.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetColour(self, colour) -> None:
        """ Sets the colour of the inactive tabs.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetFlags(self, flags) -> None:
        """ Sets flags.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetMeasuringFont(self, font) -> None:
        """ Sets the font used for calculating measurements.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetNormalFont(self, font) -> None:
        """ Sets the normal font for drawing labels.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetSelectedFont(self, font) -> None:
        """ Sets the font for drawing text for selected UI elements.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, wnd=None) -> None:
        """ Sets sizing information.

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def ShowDropDown(self, wnd, items, activeIdx) -> None:
        """ wnd (wx.Window)

            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    IndentSize: None  # See GetIndentSize



class AuiToolBarItem:
    """ AuiToolBarItem is part of the AUI class framework, representing a
toolbar element.

        Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def Assign(self, c) -> None:
        """ Assigns the properties of the   wx.aui.AuiToolBarItem  âcâ to this.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def CanBeToggled(self) -> None:
        """ Returns whether the toolbar item can be toggled.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetAlignment(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetBitmap(self) -> None:
        """ Bitmap

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetDisabledBitmap(self) -> None:
        """ Bitmap

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetHoverBitmap(self) -> None:
        """ Bitmap

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetId(self) -> None:
        """ Returns the toolbar item identifier.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetKind(self) -> None:
        """ Returns the toolbar item kind.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetLabel(self) -> None:
        """ str

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetLongHelp(self) -> None:
        """ str

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetMinSize(self) -> None:
        """ Size

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetProportion(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetShortHelp(self) -> None:
        """ str

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetSizerItem(self) -> None:
        """ SizerItem

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetSpacerPixels(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetState(self) -> None:
        """ Gets the current state of the toolbar item.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetUserData(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetWindow(self) -> None:
        """ Returns the Window associated to the toolbar item.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def HasDropDown(self) -> None:
        """ Returns whether the toolbar item has an associated drop down button.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def IsActive(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def IsSticky(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetActive(self, b) -> None:
        """ b (bool)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetAlignment(self, l) -> None:
        """ l (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetBitmap(self, bmp) -> None:
        """ bmp (wx.BitmapBundle)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetDisabledBitmap(self, bmp) -> None:
        """ bmp (wx.BitmapBundle)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetHasDropDown(self, b) -> None:
        """ Set whether this tool has a drop down button.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetHoverBitmap(self, bmp) -> None:
        """ bmp (wx.BitmapBundle)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetId(self, new_id) -> None:
        """ Sets the toolbar item identifier.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetKind(self, new_kind) -> None:
        """ Sets the   wx.aui.AuiToolBarItem  kind.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetLabel(self, s) -> None:
        """ s (string)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetLongHelp(self, s) -> None:
        """ s (string)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetMinSize(self, s) -> None:
        """ s (wx.Size)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetProportion(self, p) -> None:
        """ p (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetShortHelp(self, s) -> None:
        """ s (string)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetSizerItem(self, s) -> None:
        """ s (wx.SizerItem)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetSpacerPixels(self, s) -> None:
        """ s (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetState(self, new_state) -> None:
        """ Set the current state of the toolbar item.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetSticky(self, b) -> None:
        """ b (bool)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetUserData(self, l) -> None:
        """ l (long)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetWindow(self, w) -> None:
        """ Assigns a window to the toolbar item.

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    Alignment: None  # See GetAlignment and SetAlignment
    Bitmap: None  # See GetBitmap and SetBitmap
    DisabledBitmap: None  # See GetDisabledBitmap and SetDisabledBitmap
    HoverBitmap: None  # See GetHoverBitmap and SetHoverBitmap
    Id: None  # See GetId and SetId
    Kind: None  # See GetKind and SetKind
    Label: None  # See GetLabel and SetLabel
    LongHelp: None  # See GetLongHelp and SetLongHelp
    MinSize: None  # See GetMinSize and SetMinSize
    Proportion: None  # See GetProportion and SetProportion
    ShortHelp: None  # See GetShortHelp and SetShortHelp
    SizerItem: None  # See GetSizerItem and SetSizerItem
    SpacerPixels: None  # See GetSpacerPixels and SetSpacerPixels
    State: None  # See GetState and SetState
    UserData: None  # See GetUserData and SetUserData
    Window: None  # See GetWindow and SetWindow



class AuiToolBarArt:
    """ AuiToolBarArt is part of the AUI class framework.

        Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
    """
    def __init__(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def Clone(self) -> None:
        """ wx.aui.AuiToolBarArt

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawButton(self, dc, wnd, item, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawControlLabel(self, dc, wnd, item, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawDropDownButton(self, dc, wnd, item, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawGripper(self, dc, wnd, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawLabel(self, dc, wnd, item, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawOverflowButton(self, dc, wnd, rect, state) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawPlainBackground(self, dc, wnd, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawSeparator(self, dc, wnd, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetElementSize(self, element_id) -> None:
        """ element_id (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetFlags(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetFont(self) -> None:
        """ Font

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetLabelSize(self, dc, wnd, item) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetTextOrientation(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetToolSize(self, dc, wnd, item) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def SetElementSize(self, element_id, size) -> None:
        """ element_id (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def SetFlags(self, flags) -> None:
        """ flags (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def SetFont(self, font) -> None:
        """ font (wx.Font)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def SetTextOrientation(self, orientation) -> None:
        """ orientation (int)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def ShowDropDown(self, wnd, items) -> None:
        """ wnd (wx.Window)

            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    Flags: None  # See GetFlags and SetFlags
    Font: None  # See GetFont and SetFont
    TextOrientation: None  # See GetTextOrientation and SetTextOrientation



class AuiPaneInfo:
    """ AuiPaneInfo is part of the AUI class framework.

        Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def BestSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Bottom(self) -> None:
        """ wx.Bottom       sets the pane dock position to the bottom side of the frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def BottomDockable(self, b=True) -> None:
        """ BottomDockable   indicates whether a pane can be docked at the bottom of the frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Caption(self, c) -> None:
        """ Caption   sets the caption of the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def CaptionVisible(self, visible=True) -> None:
        """ CaptionVisible indicates that a pane caption should be visible.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Center(self) -> None:
        """ wx.aui.AuiPaneInfo

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def CenterPane(self) -> None:
        """ wx.aui.AuiPaneInfo

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Centre(self) -> None:
        """ wx.Center       sets the pane dock position to the left side of the frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def CentrePane(self) -> None:
        """ CentrePane   specifies that the pane should adopt the default center pane settings.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def CloseButton(self, visible=True) -> None:
        """ CloseButton   indicates that a close button should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def DefaultPane(self) -> None:
        """ DefaultPane   specifies that the pane should adopt the default pane settings.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def DestroyOnClose(self, b=True) -> None:
        """ DestroyOnClose   indicates whether a pane should be destroyed when it is closed.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Direction(self, direction) -> None:
        """ wx.DataObject.Direction  determines the direction of the docked pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Dock(self) -> None:
        """ Dock   indicates that a pane should be docked.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def DockFixed(self, b=True) -> None:
        """ DockFixed   causes the containing dock to have no resize sash.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Dockable(self, b=True) -> None:
        """ Dockable   specifies whether a frame can be docked or not.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Fixed(self) -> None:
        """ Fixed   forces a pane to be fixed size so that it cannot be resized.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Float(self) -> None:
        """ Float   indicates that a pane should be floated.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Floatable(self, b=True) -> None:
        """ Floatable   sets whether the user will be able to undock a pane and turn it into a floating window.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def FloatingPosition(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def FloatingSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Gripper(self, visible=True) -> None:
        """ Gripper   indicates that a gripper should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def GripperTop(self, attop=True) -> None:
        """ GripperTop   indicates that a gripper should be drawn at the top of the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasBorder(self) -> None:
        """ HasBorder   returns True if the pane displays a border.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasCaption(self) -> None:
        """ HasCaption   returns True if the pane displays a caption.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasCloseButton(self) -> None:
        """ HasCloseButton   returns True if the pane displays a button to close the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasFlag(self, flag) -> None:
        """ HasFlag   returns True if the property specified by flag is active for the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasGripper(self) -> None:
        """ HasGripper   returns True if the pane displays a gripper.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasGripperTop(self) -> None:
        """ HasGripper   returns True if the pane displays a gripper at the top.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasMaximizeButton(self) -> None:
        """ HasMaximizeButton   returns True if the pane displays a button to maximize the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasMinimizeButton(self) -> None:
        """ HasMinimizeButton   returns True if the pane displays a button to minimize the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasPinButton(self) -> None:
        """ HasPinButton   returns True if the pane displays a button to float the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Hide(self) -> None:
        """ Hide   indicates that a pane should be hidden.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Icon(self, b) -> None:
        """ wx.Icon  sets the icon of the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsBottomDockable(self) -> None:
        """ IsBottomDockable   returns True if the pane can be docked at the bottom of the managed frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsDockable(self) -> None:
        """ Returns True if the pane can be docked at any side.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsDocked(self) -> None:
        """ IsDocked   returns True if the pane is currently docked.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsFixed(self) -> None:
        """ IsFixed   returns True if the pane cannot be resized.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsFloatable(self) -> None:
        """ IsFloatable   returns True if the pane can be undocked and displayed as a floating window.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsFloating(self) -> None:
        """ IsFloating   returns True if the pane is floating.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsLeftDockable(self) -> None:
        """ IsLeftDockable   returns True if the pane can be docked on the left of the managed frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsMovable(self) -> None:
        """ IsMoveable() returns True if the docked frame can be undocked or moved to another dock position.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsOk(self) -> None:
        """ IsOk   returns True if the   wx.aui.AuiPaneInfo  structure is valid.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsResizable(self) -> None:
        """ IsResizable   returns True if the pane can be resized.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsRightDockable(self) -> None:
        """ IsRightDockable   returns True if the pane can be docked on the right of the managed frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsShown(self) -> None:
        """ IsShown   returns True if the pane is currently shown.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsToolbar(self) -> None:
        """ IsToolbar   returns True if the pane contains a toolbar.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsTopDockable(self) -> None:
        """ IsTopDockable   returns True if the pane can be docked at the top of the managed frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsValid(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Layer(self, layer) -> None:
        """ Layer   determines the layer of the docked pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Left(self) -> None:
        """ wx.Left       sets the pane dock position to the left side of the frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def LeftDockable(self, b=True) -> None:
        """ LeftDockable   indicates whether a pane can be docked on the left of the frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def MaxSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def MaximizeButton(self, visible=True) -> None:
        """ MaximizeButton   indicates that a maximize button should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def MinSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def MinimizeButton(self, visible=True) -> None:
        """ MinimizeButton   indicates that a minimize button should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Movable(self, b=True) -> None:
        """ Movable indicates whether a frame can be moved.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Name(self, n) -> None:
        """ Name   sets the name of the pane so it can be referenced in lookup functions.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def PaneBorder(self, visible=True) -> None:
        """ PaneBorder indicates that a border should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def PinButton(self, visible=True) -> None:
        """ PinButton   indicates that a pin button should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Position(self, pos) -> None:
        """ wx.Position  determines the position of the docked pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Resizable(self, resizable=True) -> None:
        """ Resizable   allows a pane to be resized if the parameter is True, and forces it to be a fixed size if the parameter is False.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Right(self) -> None:
        """ wx.Right       sets the pane dock position to the right side of the frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def RightDockable(self, b=True) -> None:
        """ RightDockable   indicates whether a pane can be docked on the right of the frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Row(self, row) -> None:
        """ Row   determines the row of the docked pane.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def SafeSet(self, source) -> None:
        """ Write the safe parts of a PaneInfo object âsourceâ into âthisâ.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def SetFlag(self, flag, option_state) -> None:
        """ SetFlag   turns the property given by flag on or off with the option_state parameter.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Show(self, show=True) -> None:
        """ Show   indicates that a pane should be shown.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def ToolbarPane(self) -> None:
        """ ToolbarPane   specifies that the pane should adopt the default toolbar pane settings.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Top(self) -> None:
        """ wx.Top       sets the pane dock position to the top of the frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def TopDockable(self, b=True) -> None:
        """ TopDockable   indicates whether a pane can be docked at the top of the frame.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Window(self, w) -> None:
        """ wx.Window  assigns the window pointer that the   wx.aui.AuiPaneInfo  should use.

            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    best_size: Any  # A public C++ attribute of type Size     . size that the layout engine will prefer
    caption: Any  # A public C++ attribute of type string. caption displayed on the window
    dock_direction: Any  # A public C++ attribute of type int. dock direction (top, bottom, left, right, center)
    dock_layer: Any  # A public C++ attribute of type int. layer number (0 = innermost layer)
    dock_pos: Any  # A public C++ attribute of type int. position inside the row (0 = first position)
    dock_proportion: Any  # A public C++ attribute of type int. proportion while docked
    dock_row: Any  # A public C++ attribute of type int. row number on the docking bar (0 = first row)
    floating_pos: Any  # A public C++ attribute of type Point     . position while floating
    floating_size: Any  # A public C++ attribute of type Size     . size while floating
    frame: Any  # A public C++ attribute of type Frame     . floating frame window that holds the pane
    icon: Any  # A public C++ attribute of type BitmapBundle     . icon of the pane, may be invalid
    max_size: Any  # A public C++ attribute of type Size     . maximum size the pane window can tolerate
    min_size: Any  # A public C++ attribute of type Size     . minimum size the pane window can tolerate
    name: Any  # A public C++ attribute of type string. name of the pane
    rect: Any  # A public C++ attribute of type Rect     . current rectangle (populated by AUI)
    state: Any  # A public C++ attribute of type int. a combination of PaneState values
    window: Any  # A public C++ attribute of type Window     . window that is in this pane



class AuiDockArt:
    """ AuiDockArt is part of the AUI class framework.

        Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def Clone(self) -> None:
        """ Create a copy of this   wx.aui.AuiDockArt  instance.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawBackground(self, dc, window, orientation, rect) -> None:
        """ Draws a background.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawBorder(self, dc, window, rect, pane) -> None:
        """ Draws a border.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawCaption(self, dc, window, text, rect, pane) -> None:
        """ Draws a caption.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawGripper(self, dc, window, rect, pane) -> None:
        """ Draws a gripper.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawPaneButton(self, dc, window, button, button_state, rect, pane) -> None:
        """ Draws a button in the paneâs title bar.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawSash(self, dc, window, orientation, rect) -> None:
        """ Draws a sash between two windows.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def GetColour(self, id) -> None:
        """ Get the colour of a certain setting.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def GetFont(self, id) -> None:
        """ Get a font setting.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def GetMetric(self, id) -> None:
        """ Get the value of a certain setting.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def SetColour(self, id, colour) -> None:
        """ Set a certain setting with the value colour.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def SetFont(self, id, font) -> None:
        """ Set a font setting.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def SetMetric(self, id, new_val) -> None:
        """ Set a certain setting with the value new_val.

            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """



AuiManagerOption: TypeAlias = int  # Enumeration

class AuiDefaultToolBarArt(AuiToolBarArt):
    """ AuiDefaultToolBarArt is part of the AUI class framework.

        Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
    """
    def __init__(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def Clone(self) -> None:
        """ wx.aui.AuiToolBarArt

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawButton(self, dc, wnd, item, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawControlLabel(self, dc, wnd, item, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawDropDownButton(self, dc, wnd, item, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawGripper(self, dc, wnd, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawLabel(self, dc, wnd, item, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawOverflowButton(self, dc, wnd, rect, state) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawPlainBackground(self, dc, wnd, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawSeparator(self, dc, wnd, rect) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetElementSize(self, element) -> None:
        """ element (int)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetFlags(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetFont(self) -> None:
        """ Font

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetLabelSize(self, dc, wnd, item) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetTextOrientation(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetToolSize(self, dc, wnd, item) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def SetElementSize(self, element_id, size) -> None:
        """ element_id (int)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def SetFlags(self, flags) -> None:
        """ flags (int)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def SetFont(self, font) -> None:
        """ font (wx.Font)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def SetTextOrientation(self, orientation) -> None:
        """ orientation (int)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def ShowDropDown(self, wnd, items) -> None:
        """ wnd (wx.Window)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    Flags: None  # See GetFlags and SetFlags
    Font: None  # See GetFont and SetFont
    TextOrientation: None  # See GetTextOrientation and SetTextOrientation



class AuiDefaultDockArt(AuiDockArt):
    """ This is the default art provider for AuiManager.

        Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
    """
    def __init__(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def Clone(self) -> None:
        """ Create a copy of this   wx.aui.AuiDockArt  instance.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawBackground(self, dc, window, orientation, rect) -> None:
        """ Draws a background.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawBorder(self, dc, window, rect, pane) -> None:
        """ Draws a border.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawCaption(self, dc, window, text, rect, pane) -> None:
        """ Draws a caption.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawGripper(self, dc, window, rect, pane) -> None:
        """ Draws a gripper.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawIcon(self, dc, rect, pane) -> None:
        """ dc (wx.DC)

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawPaneButton(self, dc, window, button, button_state, rect, pane) -> None:
        """ Draws a button in the paneâs title bar.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawSash(self, dc, window, orientation, rect) -> None:
        """ Draws a sash between two windows.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def GetColour(self, id) -> None:
        """ Get the colour of a certain setting.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def GetFont(self, id) -> None:
        """ Get a font setting.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def GetMetric(self, id) -> None:
        """ Get the value of a certain setting.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def SetColour(self, id, colour) -> None:
        """ Set a certain setting with the value colour.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def SetFont(self, id, font) -> None:
        """ Set a font setting.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def SetMetric(self, id, new_val) -> None:
        """ Set a certain setting with the value new_val.

            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """



AuiPaneInfoArray: TypeAlias = list['AuiPaneInfo']

