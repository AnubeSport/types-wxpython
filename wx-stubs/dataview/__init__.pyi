# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

from .. import (Control, NotifyEvent, Object, RefCounter, SettableHeaderColumn,
                Window)

class DataViewCtrl(Control):
    """ DataViewCtrl is a control to display data either in a tree like
fashion or in a tabular form or both.

        Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AllowMultiColumnSort(self, allow) -> None:
        """ Call to allow using multiple columns for sorting.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendBitmapColumn(self, *args, **kw) -> None:
        """ Appends a column for rendering a bitmap.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendColumn(self, col) -> None:
        """ Appends a   wx.dataview.DataViewColumn  to the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendDateColumn(self, *args, **kw) -> None:
        """ Appends a column for rendering a date.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendIconTextColumn(self, *args, **kw) -> None:
        """ Appends a column for rendering text with an icon.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendProgressColumn(self, *args, **kw) -> None:
        """ Appends a column for rendering a progress indicator.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendTextColumn(self, *args, **kw) -> None:
        """ Appends a column for rendering text.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendToggleColumn(self, *args, **kw) -> None:
        """ Appends a column for rendering a toggle.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def _AssociateModel(self, model) -> None:
        """ Associates a   wx.dataview.DataViewModel  with the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AssociateModel(self, model) -> None:
        """ Associates a DataViewModel with the control.
Ownership of the model object is passed to C++, however it
is reference counted so it can be shared with other views.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def ClearColumns(self) -> None:
        """ Removes all columns.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Collapse(self, item) -> None:
        """ Collapses the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=DataViewCtrlNameStr) -> None:
        """ Create the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def DeleteColumn(self, column) -> None:
        """ Deletes given column.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EditItem(self, item, column) -> None:
        """ Programmatically starts editing given cell of item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnableDragSource(self, format) -> None:
        """ Enable drag operations using the given format.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnableDropTarget(self, format) -> None:
        """ Enable drop operations using the given format.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnableDropTargets(self, formats) -> None:
        """ Enable drop operations using any of the specified formats.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnableSystemTheme(self, enable=True) -> None:
        """ Can be used to disable the system theme of controls using it by default.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnsureVisible(self, item, column=None) -> None:
        """ Call this to ensure that the given item is visible.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Expand(self, item) -> None:
        """ Expands the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def ExpandAncestors(self, item) -> None:
        """ Expands all ancestors of the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def ExpandChildren(self, item) -> None:
        """ Expand all children of the given item recursively.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetColumn(self, pos) -> None:
        """ Returns pointer to the column.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetColumnCount(self) -> None:
        """ Returns the number of columns.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetColumnPosition(self, column) -> None:
        """ Returns the position of the column or -1 if not found in the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetColumns(self) -> None:
        """ Returns a list of column objects.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetCountPerPage(self) -> None:
        """ Return the number of items that can fit vertically in the visible area of the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetCurrentColumn(self) -> None:
        """ Returns the column that currently has focus.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetCurrentItem(self) -> None:
        """ Returns the currently focused item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetExpanderColumn(self) -> None:
        """ Returns column containing the expanders.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetIndent(self) -> None:
        """ Returns indentation.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetItemRect(self, item, col=None) -> None:
        """ Returns item rectangle.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetMainWindow(self) -> None:
        """ Returns the window corresponding to the main area of the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetModel(self) -> None:
        """ Returns pointer to the data model associated with the control (if any).

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetSelectedItemsCount(self) -> None:
        """ Returns the number of currently selected items.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetSelection(self) -> None:
        """ Returns first selected item or an invalid item if none is selected.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetSelections(self) -> None:
        """ Returns a list of the currently selected items.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetSortingColumn(self) -> None:
        """ Returns the   wx.dataview.DataViewColumn  currently responsible for sorting or None if none has been selected.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetTopItem(self) -> None:
        """ Return the topmost visible item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def HasSelection(self) -> None:
        """ Returns True if any items are currently selected.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def HitTest(self, point) -> None:
        """ HitTest(point) . (item, col)

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def InsertColumn(self, pos, col) -> None:
        """ Inserts a   wx.dataview.DataViewColumn  to the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def IsExpanded(self, item) -> None:
        """ Return True if the item is expanded.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def IsMultiColumnSortAllowed(self) -> None:
        """ Return True if using more than one column for sorting is allowed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def IsSelected(self, item) -> None:
        """ Return True if the item is selected.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependBitmapColumn(self, *args, **kw) -> None:
        """ Prepends a column for rendering a bitmap.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependColumn(self, col) -> None:
        """ Prepends a   wx.dataview.DataViewColumn  to the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependDateColumn(self, *args, **kw) -> None:
        """ Prepends a column for rendering a date.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependIconTextColumn(self, *args, **kw) -> None:
        """ Prepends a column for rendering text with an icon.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependProgressColumn(self, *args, **kw) -> None:
        """ Prepends a column for rendering a progress indicator.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependTextColumn(self, *args, **kw) -> None:
        """ Prepends a column for rendering text.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependToggleColumn(self, *args, **kw) -> None:
        """ Prepends a column for rendering a toggle.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Select(self, item) -> None:
        """ Select the given item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SelectAll(self) -> None:
        """ Select all items.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetAlternateRowColour(self, colour) -> None:
        """ Set custom colour for the alternate rows used with wx.dataview.DV_ROW_LINES style.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetCurrentItem(self, item) -> None:
        """ Changes the currently focused item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetExpanderColumn(self, col) -> None:
        """ Set which column shall contain the tree-like expanders.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetHeaderAttr(self, attr) -> None:
        """ Set custom colours and/or font to use for the header.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetIndent(self, indent) -> None:
        """ Sets the indentation.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetRowHeight(self, rowHeight) -> None:
        """ Sets the row height.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetSelections(self, sel) -> None:
        """ Sets the selection to the array of DataViewItems.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def ToggleSortByColumn(self, column) -> None:
        """ Toggle sorting by the given column.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Unselect(self, item) -> None:
        """ Unselect the given item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def UnselectAll(self) -> None:
        """ Unselect all item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    ColumnCount: None  # See GetColumnCount
    Columns: None  # See GetColumns
    CountPerPage: None  # See GetCountPerPage
    CurrentColumn: None  # See GetCurrentColumn
    CurrentItem: None  # See GetCurrentItem and SetCurrentItem
    ExpanderColumn: None  # See GetExpanderColumn and SetExpanderColumn
    Indent: None  # See GetIndent and SetIndent
    MainWindow: None  # See GetMainWindow
    Model: None  # See GetModel
    SelectedItemsCount: None  # See GetSelectedItemsCount
    Selection: None  # See GetSelection
    Selections: None  # See GetSelections and SetSelections
    SortingColumn: None  # See GetSortingColumn
    TopItem: None  # See GetTopItem



DV_SINGLE: int  # Single selection mode. This is the default.

DV_MULTIPLE: int  # Multiple selection mode.

DV_ROW_LINES: int  # Use alternating colours for odd and even rows.

DV_HORIZ_RULES: int  # Display the separator lines between rows.

DV_VERT_RULES: int  # Display the separator lines between columns.

DV_VARIABLE_LINE_HEIGHT: int  # Allow variable line heights. This can be inefficient when displaying large number of items.

DV_NO_HEADER: int  # Do not show column headers (which are shown by default).

EVT_DATAVIEW_SELECTION_CHANGED: int  # Process a  wxEVT_DATAVIEW_SELECTION_CHANGED   event.

EVT_DATAVIEW_ITEM_ACTIVATED: int  # Process a  wxEVT_DATAVIEW_ITEM_ACTIVATED   event. This event is triggered by double clicking an item or pressing some special key (usually âEnterâ) when it is focused.

EVT_DATAVIEW_ITEM_START_EDITING: int  # Process a  wxEVT_DATAVIEW_ITEM_START_EDITING   event. This event can be vetoed in order to prevent editing on an item by item basis.

EVT_DATAVIEW_ITEM_EDITING_STARTED: int  # Process a  wxEVT_DATAVIEW_ITEM_EDITING_STARTED   event.

EVT_DATAVIEW_ITEM_EDITING_DONE: int  # Process a  wxEVT_DATAVIEW_ITEM_EDITING_DONE   event.

EVT_DATAVIEW_ITEM_COLLAPSING: int  # Process a  wxEVT_DATAVIEW_ITEM_COLLAPSING   event.

EVT_DATAVIEW_ITEM_COLLAPSED: int  # Process a  wxEVT_DATAVIEW_ITEM_COLLAPSED   event.

EVT_DATAVIEW_ITEM_EXPANDING: int  # Process a  wxEVT_DATAVIEW_ITEM_EXPANDING   event.

EVT_DATAVIEW_ITEM_EXPANDED: int  # Process a  wxEVT_DATAVIEW_ITEM_EXPANDED   event.

EVT_DATAVIEW_ITEM_VALUE_CHANGED: int  # Process a  wxEVT_DATAVIEW_ITEM_VALUE_CHANGED   event.

EVT_DATAVIEW_ITEM_CONTEXT_MENU: int  # Process a  wxEVT_DATAVIEW_ITEM_CONTEXT_MENU   event generated when the user right clicks inside the control. Notice that this menu is generated even if the click didnât occur on any valid item, in this case  wx.dataview.DataViewEvent.GetItem   simply returns an invalid item.

EVT_DATAVIEW_COLUMN_HEADER_CLICK: int  # Process a  wxEVT_DATAVIEW_COLUMN_HEADER_CLICK   event.

EVT_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK: int  # Process a  wxEVT_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK   event.

EVT_DATAVIEW_COLUMN_SORTED: int  # Process a  wxEVT_DATAVIEW_COLUMN_SORTED   event.

EVT_DATAVIEW_COLUMN_REORDERED: int  # Process a  wxEVT_DATAVIEW_COLUMN_REORDERED   event.

EVT_DATAVIEW_ITEM_BEGIN_DRAG: int  # Process a  wxEVT_DATAVIEW_ITEM_BEGIN_DRAG   event which is generated when the user starts dragging a valid item. This event must be processed and  wx.dataview.DataViewEvent.SetDataObject   must be called to actually start dragging the item.

EVT_DATAVIEW_ITEM_DROP_POSSIBLE: int  # Process a  wxEVT_DATAVIEW_ITEM_DROP_POSSIBLE   event.

EVT_DATAVIEW_ITEM_DROP: int  # Process a  wxEVT_DATAVIEW_ITEM_DROP   event.

DF_INVALID: int

class TreeListCtrl(Window):
    """ A control combining TreeCtrl and ListCtrl features.

        Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def AppendColumn(self, title, width=COL_WIDTH_AUTOSIZE, align=ALIGN_LEFT, flags=COL_RESIZABLE) -> None:
        """ Add a column with the given title and attributes.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def AppendItem(self, parent, text, imageClosed=-1, imageOpened=-1, data=None) -> None:
        """ Same as InsertItem   with wx.dataview.TLI_LAST.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def AreAllChildrenInState(self, item, state) -> None:
        """ Return True if all children of the given item are in the specified state.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def AssignImageList(self, imageList) -> None:
        """ Sets the image list and gives its ownership to the control.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def CheckItem(self, item, state=CHK_CHECKED) -> None:
        """ Change the item checked state.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def CheckItemRecursively(self, item, state=CHK_CHECKED) -> None:
        """ Change the checked state of the given item and all its children.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def ClearColumns(self) -> None:
        """ Delete all columns.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Collapse(self, item) -> None:
        """ Collapse the given tree branch.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=TL_DEFAULT_STYLE, name=TreeListCtrlNameStr) -> None:
        """ Create the control window.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ Delete all tree items.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def DeleteColumn(self, col: int) -> bool:
        """ Delete the column with the given index.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def DeleteItem(self, item) -> None:
        """ Delete the specified item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def EnsureVisible(self, item) -> None:
        """ Call this to ensure that the given item is visible.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Expand(self, item) -> None:
        """ Expand the given tree branch.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetCheckedState(self, item) -> None:
        """ Return the checked state of the item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetColumnCount(self) -> None:
        """ Return the total number of columns.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetColumnWidth(self, col) -> None:
        """ Get the current width of the given column in pixels.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetDataView(self) -> None:
        """ Return the view part of this control as   wx.dataview.DataViewCtrl.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetFirstChild(self, item) -> None:
        """ Return the first child of the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetFirstItem(self) -> None:
        """ Return the first item in the tree.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetItemData(self, item) -> None:
        """ Get the data associated with the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetItemParent(self, item) -> None:
        """ Return the parent of the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetItemText(self, item, col=0) -> None:
        """ Return the text of the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetNextItem(self, item) -> None:
        """ Get item after the given one in the depth-first tree-traversal order.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetNextSibling(self, item) -> None:
        """ Return the next sibling of the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetRootItem(self) -> None:
        """ Return the (never shown) root item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetSelection(self) -> None:
        """ Return the currently selected item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetSelections(self) -> None:
        """ Returns a list of all selected items. This method can be used in
both single and multi-selection case.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetSortColumn(self) -> None:
        """ Return the column currently used for sorting, if any.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetView(self) -> None:
        """ Return the view part of this control as a   wx.Window.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def InsertItem(self, parent, previous, text, imageClosed=-1, imageOpened=-1, data=None) -> None:
        """ Insert a new item into the tree.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def IsExpanded(self, item) -> None:
        """ Return whether the given item is expanded.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def IsSelected(self, item) -> None:
        """ Return True if the item is selected.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def PrependItem(self, parent, text, imageClosed=-1, imageOpened=-1, data=None) -> None:
        """ Same as InsertItem   with wx.dataview.TLI_FIRST.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Select(self, item) -> None:
        """ Select the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SelectAll(self) -> None:
        """ Select all the control items.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetColumnWidth(self, col, width) -> None:
        """ Change the width of the given column.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetImageList(self, imageList) -> None:
        """ Sets the image list.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetItemComparator(self, comparator) -> None:
        """ Set the object to use for comparing the items.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetItemData(self, item, data) -> None:
        """ Set the data associated with the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetItemImage(self, item, closed, opened=-1) -> None:
        """ Set the images for the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetItemText(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetSortColumn(self, col, ascendingOrder=True) -> None:
        """ Set the column to use for sorting and the order in which to sort.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def UncheckItem(self, item) -> None:
        """ Uncheck the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Unselect(self, item) -> None:
        """ Deselect the given item.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def UnselectAll(self) -> None:
        """ Deselect all the control items.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def UpdateItemParentStateRecursively(self, item) -> None:
        """ Update the state of the parent item to reflect the checked state of its children.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def WidthFor(self, text) -> None:
        """ Get the width appropriate for showing the given text.

            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    ColumnCount: None  # See GetColumnCount
    DataView: None  # See GetDataView
    FirstItem: None  # See GetFirstItem
    NO_IMAGE: Any  # A public C++ attribute of type int. A constant indicating that no image should be used for an item.
    RootItem: None  # See GetRootItem
    Selection: None  # See GetSelection
    Selections: None  # See GetSelections
    SortColumn: None  # See GetSortColumn and SetSortColumn
    View: None  # See GetView



TL_SINGLE: int  # Single selection, this is the default.

TL_MULTIPLE: int  # Allow multiple selection, see GetSelections.

TL_CHECKBOX: int  # Show the usual, 2 state, checkboxes for the items in the first column.

TL_3STATE: int  # Show the checkboxes that can possibly be set by the program, but not the user, to a third, undetermined, state, for the items in the first column. Implies wx.dataview.TL_CHECKBOX.

TL_USER_3STATE: int  # Same as wx.dataview.TL_3STATE but the user can also set the checkboxes to the undetermined state. Implies wx.dataview.TL_3STATE.

TL_NO_HEADER: int  # Donât show the column headers, that are shown by default. Notice that this style is only available since wxWidgets 2.9.5.

TL_DEFAULT_STYLE: int  # Style used by the control by default, just wx.dataview.TL_SINGLE currently.

EVT_TREELIST_SELECTION_CHANGED: int  # Process  wxEVT_TREELIST_SELECTION_CHANGED   event and notifies about the selection change in the control. In the single selection case the item indicated by the event has been selected and previously selected item, if any, was deselected. In multiple selection case, the selection of this item has just changed (it may have been either selected or deselected) but notice that the selection of other items could have changed as well, use  wx.dataview.TreeListCtrl.GetSelections   to retrieve the new selection if necessary.

EVT_TREELIST_ITEM_EXPANDING: int  # Process  wxEVT_TREELIST_ITEM_EXPANDING   event notifying about the given branch being expanded. This event is sent before the expansion occurs and can be vetoed to prevent it from happening.

EVT_TREELIST_ITEM_EXPANDED: int  # Process  wxEVT_TREELIST_ITEM_EXPANDED   event notifying about the expansion of the given branch. This event is sent after the expansion occurs and canât be vetoed.

EVT_TREELIST_ITEM_CHECKED: int  # Process  wxEVT_TREELIST_ITEM_CHECKED   event notifying about the user checking or unchecking the item. You can use  wx.dataview.TreeListCtrl.GetCheckedState   to retrieve the new item state and wx.dataview.TreeListEvent.GetOldCheckedState   to get the previous one.

EVT_TREELIST_ITEM_ACTIVATED: int  # Process  wxEVT_TREELIST_ITEM_ACTIVATED   event notifying about the user double clicking the item or activating it from keyboard.

EVT_TREELIST_ITEM_CONTEXT_MENU: int  # Process  wxEVT_TREELIST_ITEM_CONTEXT_MENU   event indicating that the popup menu for the given item should be displayed.

EVT_TREELIST_COLUMN_SORTED: int  # Process  wxEVT_TREELIST_COLUMN_SORTED   event indicating that the control contents has just been resorted using the specified column. The event doesnât carry the sort direction, use  GetSortColumn  method if you need to know it.

COL_SORTABLE: int

TLI_LAST: int

TLI_FIRST: int

COL_WIDTH_AUTOSIZE: int

COL_RESIZABLE: int

CHK_CHECKED: int

CHK_UNCHECKED: int

CHK_UNDETERMINED: int

NO_IMAGE: int

class DataViewTreeCtrl(DataViewCtrl):
    """ This class is a DataViewCtrl which internally uses a
DataViewTreeStore and forwards most of its API to that class.

        Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def AppendContainer(self, parent, text, icon=-1, expanded=-1, data=None) -> None:
        """ Appends a container to the given parent.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def AppendItem(self, parent, text, icon=-1, data=None) -> None:
        """ Appends an item to the given parent.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=DV_NO_HEADER | DV_ROW_LINES, validator=DefaultValidator) -> None:
        """ Creates the control and a   wx.dataview.DataViewTreeStore  as its internal model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def DeleteChildren(self, item) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def DeleteItem(self, item) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetChildCount(self, parent) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetImageList(self) -> None:
        """ Returns the image list.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemData(self, item) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemExpandedIcon(self, item) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemIcon(self, item) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemParent(self, item) -> None:
        """ Returns the itemâs parent.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemText(self, item) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetNthChild(self, parent, pos) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetStore(self) -> None:
        """ Returns the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def InsertContainer(self, parent, previous, text, icon=-1, expanded=-1, data=None) -> None:
        """ Calls the same method from   wx.dataview.DataViewTreeStore  but uses an index position in the image list instead of a   wx.Icon.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def InsertItem(self, parent, previous, text, icon=-1, data=None) -> None:
        """ Calls the same method from   wx.dataview.DataViewTreeStore  but uses an index position in the image list instead of a   wx.Icon.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def IsContainer(self, item) -> None:
        """ Returns True if item is a container.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def PrependContainer(self, parent, text, icon=-1, expanded=-1, data=None) -> None:
        """ Calls the same method from   wx.dataview.DataViewTreeStore  but uses an index position in the image list instead of a   wx.Icon.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def PrependItem(self, parent, text, icon=-1, data=None) -> None:
        """ Calls the same method from   wx.dataview.DataViewTreeStore  but uses an index position in the image list instead of a   wx.Icon.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetImageList(self, imagelist) -> None:
        """ Sets the image list.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetItemData(self, item, data) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetItemExpandedIcon(self, item, icon) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetItemIcon(self, item, icon) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetItemText(self, item, text) -> None:
        """ Calls the identical method from   wx.dataview.DataViewTreeStore.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    ImageList: None  # See GetImageList and SetImageList
    Store: None  # See GetStore



class DataViewListCtrl(DataViewCtrl):
    """ This class is a DataViewCtrl which internally uses a
DataViewListStore and forwards most of its API to that class.

        Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendColumn(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendIconTextColumn(self, label, mode=DATAVIEW_CELL_INERT, width=COL_WIDTH_DEFAULT, align=ALIGN_LEFT, flags=DATAVIEW_COL_RESIZABLE) -> None:
        """ Appends an icon-and-text column to the control and the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendItem(self, values, data=None) -> None:
        """ Appends an item (i.e. a row) to the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendProgressColumn(self, label, mode=DATAVIEW_CELL_INERT, width=COL_WIDTH_DEFAULT, align=ALIGN_LEFT, flags=DATAVIEW_COL_RESIZABLE) -> None:
        """ Appends a progress column to the control and the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendTextColumn(self, label, mode=DATAVIEW_CELL_INERT, width=COL_WIDTH_DEFAULT, align=ALIGN_LEFT, flags=DATAVIEW_COL_RESIZABLE) -> None:
        """ Appends a text column to the control and the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendToggleColumn(self, label, mode=DATAVIEW_CELL_ACTIVATABLE, width=COL_WIDTH_DEFAULT, align=ALIGN_LEFT, flags=DATAVIEW_COL_RESIZABLE) -> None:
        """ Appends a toggle column to the control and the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=DV_ROW_LINES, validator=DefaultValidator) -> None:
        """ Creates the control and a   wx.dataview.DataViewListStore  as its internal model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ Delete all items (= all rows).

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def DeleteItem(self, row) -> None:
        """ Delete the row at position row.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetItemCount(self) -> None:
        """ Returns the number of items (=rows) in the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetItemData(self, item) -> int:
        """ Returns the client data associated with the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetSelectedRow(self) -> None:
        """ Returns index of the selected row or wx.NOT_FOUND.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetStore(self) -> None:
        """ Returns the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetTextValue(self, row, col) -> None:
        """ Returns the value from the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetToggleValue(self, row, col) -> None:
        """ Returns the value from the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetValue(self, row, col) -> Any:
        """ Returns the value from the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def InsertColumn(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def InsertItem(self, row, values, data=None) -> None:
        """ Inserts an item (i.e. a row) to the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def IsRowSelected(self, row) -> None:
        """ Returns True if row  is selected.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def ItemToRow(self, item) -> None:
        """ Returns the position of given item  or wx.NOT_FOUND if itâs not a valid item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def PrependColumn(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def PrependItem(self, values, data=None) -> None:
        """ Prepends an item (i.e. a row) to the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def RowToItem(self, row) -> None:
        """ Returns the   wx.dataview.DataViewItem  at the given row.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SelectRow(self, row) -> None:
        """ Selects given row.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SetItemData(self, item, data) -> None:
        """ Associates a client data pointer with the given item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SetTextValue(self, value, row, col) -> None:
        """ Sets the value in the store and update the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SetToggleValue(self, value, row, col) -> None:
        """ Sets the value in the store and update the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SetValue(self, value, row, col) -> None:
        """ Sets the value in the store and update the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def UnselectRow(self, row) -> None:
        """ Unselects given row.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    ItemCount: None  # See GetItemCount
    SelectedRow: None  # See GetSelectedRow
    Store: None  # See GetStore



NOT_FOUND: int

class DataViewModel(RefCounter):
    """ DataViewModel is the base class for all data model to be displayed
by a DataViewCtrl.

        Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def AddNotifier(self, notifier) -> None:
        """ Adds a   wx.dataview.DataViewModelNotifier  to the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ChangeValue(self, variant, item, col) -> None:
        """ Change the value of the given item and update the control to reflect it.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def Cleared(self) -> None:
        """ Called to inform the model that all of its data has been changed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def Compare(self, item1, item2, column, ascending) -> None:
        """ The compare function to be used by the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def GetAttr(self, item, col, attr) -> None:
        """ Override this to indicate that the item has special font attributes.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def GetChildren(self, item, children) -> None:
        """ Override this so the control can query the child items of an item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def GetParent(self, item) -> None:
        """ Override this to indicate which   wx.dataview.DataViewItem  representing the parent of item  or an invalid   wx.dataview.DataViewItem  if the root item is the parent item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def GetValue(self, item, col) -> Any:
        """ Override this to indicate the value of item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def HasContainerColumns(self, item) -> None:
        """ Override this method to indicate if a container item merely acts as a headline (or for categorisation) or if it also acts a normal item with entries for further columns.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def HasDefaultCompare(self) -> None:
        """ Override this to indicate that the model provides a default compare function that the control should use if no   wx.dataview.DataViewColumn  has been chosen for sorting.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def HasValue(self, item, col) -> None:
        """ Return True if there is a value in the given column of this item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def IsContainer(self, item) -> None:
        """ Override this to indicate if item  is a container, i.e. if it can have child items.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def IsEnabled(self, item, col) -> None:
        """ Override this to indicate that the item should be disabled.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def IsListModel(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def IsVirtualListModel(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemAdded(self, parent, item) -> None:
        """ Call this to inform the model that an item has been added to the data.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemChanged(self, item) -> None:
        """ Call this to inform the model that an item has changed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemDeleted(self, parent, item) -> None:
        """ Call this to inform the model that an item has been deleted from the data.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemsAdded(self, parent, items) -> None:
        """ Call this to inform the model that several items have been added to the data.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemsChanged(self, items) -> None:
        """ Call this to inform the model that several items have changed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemsDeleted(self, parent, items) -> None:
        """ Call this to inform the model that several items have been deleted.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def RemoveNotifier(self, notifier) -> None:
        """ Remove the notifier  from the list of notifiers.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def Resort(self) -> None:
        """ Call this to initiate a resort after the sort function has been changed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def SetValue(self, variant, item, col) -> None:
        """ This gets called in order to set a value in the data model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ValueChanged(self, item, col) -> None:
        """ Call this to inform this model that a value in the model has been changed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """



class DataViewItem:
    """ DataViewItem is a small opaque class that represents an item in a
DataViewCtrl in a persistent way, i.e.

        Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def GetID(self) -> None:
        """ Returns the ID.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def IsOk(self) -> None:
        """ Returns True if the ID is not None.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __bool__(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __eq__(self, item: Any) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __hash__(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __ne__(self, item: Any) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __nonzero__(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    ID: None  # See GetID



class DataViewColumn(SettableHeaderColumn):
    """ This class represents a column in a DataViewCtrl.

        Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
        """

    def GetModelColumn(self) -> None:
        """ Returns the index of the column of the model, which this   wx.dataview.DataViewColumn  is displaying.

            Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
        """

    def GetOwner(self) -> None:
        """ Returns the owning   wx.dataview.DataViewCtrl.

            Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
        """

    def GetRenderer(self) -> None:
        """ Returns the renderer of this   wx.dataview.DataViewColumn.

            Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
        """

    Alignment: Any  # See GetAlignment and SetAlignment
    Bitmap: Any  # See GetBitmap and SetBitmap
    Flags: Any  # See GetFlags and SetFlags
    MinWidth: Any  # See GetMinWidth and SetMinWidth
    ModelColumn: None  # See GetModelColumn
    Owner: None  # See GetOwner
    Renderer: None  # See GetRenderer
    SortOrder: Any  # See IsSortOrderAscending and SetSortOrder
    Title: Any  # See GetTitle and SetTitle
    Width: Any  # See GetWidth and SetWidth



class DataViewRenderer(Object):
    """ This class is used by DataViewCtrl to render the individual cells.

        Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
    """
    def __init__(self, varianttype, mode=DATAVIEW_CELL_INERT, align=DVR_DEFAULT_ALIGNMENT) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def CancelEditing(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def CreateEditorCtrl(self, parent, labelRect, value) -> None:
        """ parent (wx.Window)

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def DisableEllipsize(self) -> None:
        """ Disable replacing parts of the item text with ellipsis.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def EnableEllipsize(self, mode=ELLIPSIZE_MIDDLE) -> None:
        """ Enable or disable replacing parts of the item text with ellipsis to make it fit the column width.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def FinishEditing(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetAlignment(self) -> None:
        """ Returns the alignment.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetEditorCtrl(self) -> None:
        """ Window

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetEllipsizeMode(self) -> None:
        """ Returns the ellipsize mode used by the renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetMode(self) -> None:
        """ Returns the cell mode.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetOwner(self) -> None:
        """ Returns pointer to the owning   wx.dataview.DataViewColumn.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetValue(self) -> Any:
        """ This methods retrieves the value from the renderer in order to transfer the value back to the data model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetValueFromEditorCtrl(self, editor) -> Any:
        """ editor (wx.Window)

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetVariantType(self) -> None:
        """ Returns a string with the type of the Variant       supported by this renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetView(self) -> None:
        """ wx.dataview.DataViewCtrl

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def HasEditorCtrl(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def IsCompatibleVariantType(self, variantType) -> None:
        """ Check if the given variant type is compatible with the type expected by this renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def SetAlignment(self, align) -> None:
        """ Sets the alignment of the rendererâs content.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def SetOwner(self, owner) -> None:
        """ Sets the owning   wx.dataview.DataViewColumn.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def SetValue(self, value) -> None:
        """ Set the value of the renderer (and thus its cell) to value.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def SetValueAdjuster(self, transformer) -> None:
        """ Set the transformer object to be used to customize values before they are rendered.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def StartEditing(self, item, labelRect) -> None:
        """ item (wx.dataview.DataViewItem)

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def Validate(self, value) -> None:
        """ Before data is committed to the data model, it is passed to this method where it can be checked for validity.

            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    Alignment: None  # See GetAlignment and SetAlignment
    EditorCtrl: None  # See GetEditorCtrl
    EllipsizeMode: None  # See GetEllipsizeMode
    Mode: None  # See GetMode
    Owner: None  # See GetOwner and SetOwner
    VariantType: None  # See GetVariantType
    View: None  # See GetView



ELLIPSIZE_MIDDLE: int

ELLIPSIZE_NONE: int

class DataViewCustomRenderer(DataViewRenderer):
    """ You need to derive a new class from DataViewCustomRenderer in order
to write a new renderer.

        Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def Activate(self, cell, model, item, col) -> None:
        """ Override this to react to the activation of a cell.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def ActivateCell(self, cell, model, item, col, mouseEvent) -> None:
        """ Override this to react to cell activation.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def CreateEditorCtrl(self, parent, labelRect, value) -> None:
        """ Override this to create the actual editor control once editing is about to start.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def GetAttr(self) -> None:
        """ Return the attribute to be used for rendering.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> None:
        """ Returns the Variant       type used with this renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def GetSize(self) -> None:
        """ Return size required to show content.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def GetTextExtent(self, str) -> None:
        """ Helper for GetSize   implementations, respects attributes.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def GetValueFromEditorCtrl(self, editor) -> Any:
        """ Override this so that the renderer can get the value from the editor control (pointed to by editor):

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def HasEditorCtrl(self) -> None:
        """ Override this and make it return True in order to indicate that this renderer supports in-place editing.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def LeftClick(self, cursor, cell, model, item, col) -> None:
        """ Override this to react to a left click.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def Render(self, cell, dc, state) -> None:
        """ Override this to render the cell.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def RenderText(self, text, xoffset, cell, dc, state) -> None:
        """ This method should be called from within Render   whenever you need to render simple text.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def StartDrag(self, cursor, cell, model, item, col) -> None:
        """ Override this to start a drag operation.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    Attr: None  # See GetAttr
    Size: None  # See GetSize



DATAVIEW_CELL_ACTIVATABLE: int

DATAVIEW_CELL_EDITABLE: int

class DataViewEvent(NotifyEvent):
    """ This is the event class for the DataViewCtrl notifications.

        Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetCacheFrom(self) -> None:
        """ Return the first row that will be displayed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetCacheTo(self) -> None:
        """ Return the last row that will be displayed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetColumn(self) -> None:
        """ Returns the position of the column in the control or -1 if column field is unavailable for this event.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataBuffer(self) -> None:
        """ Gets the data buffer for a drop data transfer

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataFormat(self) -> None:
        """ Gets the   wx.DataFormat  during a drop operation.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataObject(self) -> None:
        """ DataObject

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataSize(self) -> None:
        """ Gets the data size for a drop data transfer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataViewColumn(self) -> None:
        """ Returns a pointer to the   wx.dataview.DataViewColumn  from which the event was emitted or None.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDragFlags(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDropEffect(self) -> None:
        """ Returns the effect the user requested to happen to the dropped data.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetItem(self) -> None:
        """ Returns the item affected by the event.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetModel(self) -> None:
        """ Returns the   wx.dataview.DataViewModel  associated with the event.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetPosition(self) -> None:
        """ Returns the position of a context menu event in client coordinates.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetProposedDropIndex(self) -> None:
        """ Returns the index of the child item at which an item currently being dragged would be dropped.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetValue(self) -> None:
        """ Returns a reference to a value.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def IsEditCancelled(self) -> None:
        """ Can be used to determine whether the new value is going to be accepted in wxEVT_DATAVIEW_ITEM_EDITING_DONE handler.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetCache(self, from_, to_) -> None:
        """ from_ (int)

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetColumn(self, col) -> None:
        """ Sets the column index associated with this event.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataBuffer(self, buf) -> None:
        """ buf

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataFormat(self, format) -> None:
        """ format (wx.DataFormat)

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataObject(self, obj) -> None:
        """ Set   wx.DataObject  for data transfer within a drag operation.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataSize(self, size) -> None:
        """ size (int)

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataViewColumn(self, col) -> None:
        """ For  wxEVT_DATAVIEW_COLUMN_HEADER_CLICK   only.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDragFlags(self, flags) -> None:
        """ Specify the kind of the drag operation to perform.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDropEffect(self, effect) -> None:
        """ effect (DragResult)

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetItem(self, item) -> None:
        """ item (wx.dataview.DataViewItem)

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetModel(self, model) -> None:
        """ Sets the dataview model associated with this event.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetPosition(self, x, y) -> None:
        """ x (int)

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetValue(self, value) -> None:
        """ Sets the value associated with this event.

            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    CacheFrom: None  # See GetCacheFrom
    CacheTo: None  # See GetCacheTo
    Column: None  # See GetColumn and SetColumn
    DataBuffer: None  # See GetDataBuffer and SetDataBuffer
    DataFormat: None  # See GetDataFormat and SetDataFormat
    DataObject: None  # See GetDataObject and SetDataObject
    DataSize: None  # See GetDataSize and SetDataSize
    DataViewColumn: None  # See GetDataViewColumn and SetDataViewColumn
    DragFlags: None  # See GetDragFlags and SetDragFlags
    DropEffect: None  # See GetDropEffect and SetDropEffect
    Item: None  # See GetItem and SetItem
    Model: None  # See GetModel and SetModel
    Position: None  # See GetPosition and SetPosition
    ProposedDropIndex: None  # See GetProposedDropIndex
    Value: None  # See GetValue and SetValue



EVT_DATAVIEW_CACHE_HINT: int  # Process a  wxEVT_DATAVIEW_CACHE_HINT   event.

DataViewCellMode: TypeAlias = int  # Enumeration

DATAVIEW_CELL_INERT: int

class DataViewIconTextRenderer(DataViewRenderer):
    """ The DataViewIconTextRenderer class is used to display text with a
small icon next to it as it is typically done in a file manager.

        Source: https://docs.wxpython.org/wx.dataview.DataViewIconTextRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ The constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIconTextRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> None:
        """ Returns the Variant       type used with this renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIconTextRenderer.html
        """



class TreeListEvent(NotifyEvent):
    """ Event generated by TreeListCtrl.

        Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
    """
    def __init__(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
        """

    def GetColumn(self) -> None:
        """ Return the column affected by the event.

            Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
        """

    def GetItem(self) -> None:
        """ Return the item affected by the event.

            Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
        """

    def GetOldCheckedState(self) -> None:
        """ Return the previous state of the item checkbox.

            Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
        """

    Column: None  # See GetColumn
    Item: None  # See GetItem
    OldCheckedState: None  # See GetOldCheckedState



class DataViewIconText(Object):
    """ DataViewIconText is used by DataViewIconTextRenderer for data
transfer.

        Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def GetBitmapBundle(self) -> None:
        """ Gets the associated image.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def GetIcon(self) -> None:
        """ Gets the icon.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def GetText(self) -> None:
        """ Gets the text.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def SetBitmapBundle(self, bitmap) -> None:
        """ Sets the associated image.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def SetIcon(self, icon) -> None:
        """ Set the icon.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def SetText(self, text) -> None:
        """ Set the text.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    BitmapBundle: None  # See GetBitmapBundle and SetBitmapBundle
    Icon: None  # See GetIcon and SetIcon
    Text: None  # See GetText and SetText



class TreeListItem:
    """ Unique identifier of an item in TreeListCtrl.

        Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
    """
    def __init__(self) -> None:
        """ Only the default constructor is publicly accessible.

            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def IsOk(self) -> None:
        """ Return True if the item is valid.

            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __bool__(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __eq__(self, item: Any) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __hash__(self) -> None:
        """ int

            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __ne__(self, item: Any) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __nonzero__(self) -> None:
        """ bool

            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """



class TreeListItemComparator:
    """ Class defining sort order for the items in TreeListCtrl.

        Source: https://docs.wxpython.org/wx.dataview.TreeListItemComparator.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.dataview.TreeListItemComparator.html
        """

    def Compare(self, treelist, column, first, second) -> None:
        """ Pure virtual function which must be overridden to define sort order.

            Source: https://docs.wxpython.org/wx.dataview.TreeListItemComparator.html
        """



class DataViewTreeStore(DataViewModel):
    """ DataViewTreeStore is a specialised DataViewModel for storing
simple trees very much like TreeCtrl does and it offers a similar
API.

        Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def AppendContainer(*args, **kwargs) -> None:
        """ Append a container.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def AppendItem(*args, **kwargs) -> None:
        """ Append an item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def DeleteAllItems(self) -> None:
        """ Delete all item in the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def DeleteChildren(self, item) -> None:
        """ Delete all children of the item, but not the item itself.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def DeleteItem(self, item) -> None:
        """ Delete this item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetChildCount(self, parent) -> None:
        """ Return the number of children of item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetItemData(self, item) -> None:
        """ Returns the client data associated with the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetItemExpandedIcon(self, item) -> None:
        """ Returns the icon to display in expanded containers.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetItemIcon(self, item) -> None:
        """ Returns the icon of the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetItemText(self, item) -> None:
        """ Returns the text of the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetNthChild(self, parent, pos) -> None:
        """ Returns the nth child item of item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def InsertContainer(*args, **kwargs) -> None:
        """ Inserts a container after previous.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def InsertItem(*args, **kwargs) -> None:
        """ Inserts an item after previous.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def PrependContainer(*args, **kwargs) -> None:
        """ Inserts a container before the first child item or parent.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def PrependItem(*args, **kwargs) -> None:
        """ Inserts an item before the first child item or parent.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def SetItemData(self, item, data) -> None:
        """ Sets the client data associated with the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def SetItemExpandedIcon(self, item, icon) -> None:
        """ Sets the expanded icon for the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def SetItemIcon(self, item, icon) -> None:
        """ Sets the icon for the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """



class DataViewListStore(DataViewIndexListModel):
    """ DataViewListStore is a specialised DataViewModel for storing a
simple table of data.

        Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def AppendColumn(self, varianttype) -> None:
        """ Appends a data column.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def AppendItem(self, values, data=None) -> None:
        """ Appends an item (=row) and fills it with values.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def DeleteAllItems(self) -> None:
        """ Delete all item (=all rows) in the store.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def DeleteItem(self, pos) -> None:
        """ Delete the item (=row) at position pos.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def GetItemCount(self) -> None:
        """ Returns the number of items (=rows) in the control.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def GetItemData(self, item) -> int:
        """ Returns the client data associated with the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def GetValueByRow(self, row, col) -> Any:
        """ Overridden from   wx.dataview.DataViewIndexListModel.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def InsertColumn(self, pos, varianttype) -> None:
        """ Inserts a data column before pos.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def InsertItem(self, row, values, data=None) -> None:
        """ Inserts an item (=row) and fills it with values.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def PrependColumn(self, varianttype) -> None:
        """ Prepends a data column.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def PrependItem(self, values, data=None) -> None:
        """ Prepends an item (=row) and fills it with values.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def SetItemData(self, item, data) -> None:
        """ Sets the client data associated with the item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def SetValueByRow(self, value, row, col) -> None:
        """ Overridden from   wx.dataview.DataViewIndexListModel.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    ItemCount: None  # See GetItemCount



class DataViewModelNotifier:
    """ A DataViewModelNotifier instance is owned by a DataViewModel and
mirrors its notification interface.

        Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def Cleared(self) -> None:
        """ Called by owning model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def GetOwner(self) -> None:
        """ Get owning   wx.dataview.DataViewModel.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemAdded(self, parent, item) -> None:
        """ Called by owning model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemChanged(self, item) -> None:
        """ Called by owning model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemDeleted(self, parent, item) -> None:
        """ Called by owning model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemsAdded(self, parent, items) -> None:
        """ Called by owning model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemsChanged(self, items) -> None:
        """ Called by owning model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemsDeleted(self, parent, items) -> None:
        """ Called by owning model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def Resort(self) -> None:
        """ Called by owning model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def SetOwner(self, owner) -> None:
        """ Set owner of this notifier.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ValueChanged(self, item, col) -> None:
        """ Called by owning model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    Owner: None  # See GetOwner and SetOwner



class DataViewIndexListModel(DataViewListModel):
    """ DataViewIndexListModel is a specialized data model which lets you
address an item by its position (row) rather than its DataViewItem
(which you can obtain from this class).

        Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
    """
    def __init__(self, initial_size=0) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def GetItem(self, row) -> None:
        """ Returns the   wx.dataview.DataViewItem  at the given row.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def Reset(self, new_size) -> None:
        """ Call this after if the data has to be read again from the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowAppended(self) -> None:
        """ Call this after a row has been appended to the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowChanged(self, row) -> None:
        """ Call this after a row has been changed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowDeleted(self, row) -> None:
        """ Call this after a row has been deleted.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowInserted(self, before) -> None:
        """ Call this after a row has been inserted at the given position.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowPrepended(self) -> None:
        """ Call this after a row has been prepended to the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowValueChanged(self, row, col) -> None:
        """ Call this after a value has been changed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowsDeleted(self, rows) -> None:
        """ Call this after rows have been deleted.

            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """



class DataViewVirtualListModel(DataViewListModel):
    """ DataViewVirtualListModel is a specialized data model which lets you
address an item by its position (row) rather than its DataViewItem
and as such offers the exact same interface as
DataViewIndexListModel.

        Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
    """
    def __init__(self, initial_size=0) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def GetItem(self, row) -> None:
        """ Returns the   wx.dataview.DataViewItem  at the given row.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def Reset(self, new_size) -> None:
        """ Call this after if the data has to be read again from the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowAppended(self) -> None:
        """ Call this after a row has been appended to the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowChanged(self, row) -> None:
        """ Call this after a row has been changed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowDeleted(self, row) -> None:
        """ Call this after a row has been deleted.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowInserted(self, before) -> None:
        """ Call this after a row has been inserted at the given position.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowPrepended(self) -> None:
        """ Call this after a row has been prepended to the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowValueChanged(self, row, col) -> None:
        """ Call this after a value has been changed.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowsDeleted(self, rows) -> None:
        """ Call this after rows have been deleted.

            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """



class DataViewListModel(DataViewModel):
    """ Base class with abstract API for DataViewIndexListModel and
DataViewVirtualListModel.

        Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
    """
    def Compare(self, item1, item2, column, ascending) -> None:
        """ Compare method that sorts the items by their index.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def GetAttrByRow(self, row, col, attr) -> None:
        """ Override this to indicate that the row has special font attributes.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def GetCount(self) -> None:
        """ Returns the number of items (or rows) in the list.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def GetRow(self, item) -> None:
        """ Returns the position of given item.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def GetValueByRow(self, row, col) -> Any:
        """ Override this to allow getting values from the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def IsEnabledByRow(self, row, col) -> None:
        """ Override this if you want to disable specific items.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def SetValueByRow(self, variant, row, col) -> None:
        """ Called in order to set a value in the model.

            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    Count: None  # See GetCount



class DataViewItemAttr:
    """ This class is used to indicate to a DataViewCtrl that a certain item
(see DataViewItem) has extra font attributes for its renderer.

        Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetBackgroundColour(self) -> None:
        """ Returns the colour to be used for the background.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetBold(self) -> None:
        """ Returns value of the bold property.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetColour(self) -> None:
        """ Returns this attributeâs colour.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetEffectiveFont(self, font) -> None:
        """ Return the font based on the given one with this attribute applied to it.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetItalic(self) -> None:
        """ Returns value of the italics property.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def HasBackgroundColour(self) -> None:
        """ Returns True if the background colour property has been set.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def HasColour(self) -> None:
        """ Returns True if the colour property has been set.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def HasFont(self) -> None:
        """ Returns True if any property affecting the font has been set.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def IsDefault(self) -> None:
        """ Returns True if none of the properties have been set.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetBackgroundColour(self, colour) -> None:
        """ Call this to set the background colour to use.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetBold(self, set) -> None:
        """ Call this to indicate that the item shall be displayed in bold text.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetColour(self, colour) -> None:
        """ Call this to indicate that the item shall be displayed with that colour.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetItalic(self, set) -> None:
        """ Call this to indicate that the item shall be displayed in italic text.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetStrikethrough(self, set) -> None:
        """ Call this to indicate that the item shall be displayed in strikethrough text.

            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    BackgroundColour: None  # See GetBackgroundColour and SetBackgroundColour
    Bold: None  # See GetBold and SetBold
    Colour: None  # See GetColour and SetColour
    Italic: None  # See GetItalic and SetItalic



class DataViewToggleRenderer(DataViewRenderer):
    """ This class is used by DataViewCtrl to render toggle controls.

        Source: https://docs.wxpython.org/wx.dataview.DataViewToggleRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ The constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewToggleRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> None:
        """ Returns the Variant       type used with this renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewToggleRenderer.html
        """

    def ShowAsRadio(self) -> None:
        """ Switch to using radiobutton-like appearance instead of the default checkbox-like one.

            Source: https://docs.wxpython.org/wx.dataview.DataViewToggleRenderer.html
        """



DataViewColumnFlags: TypeAlias = int  # Enumeration

DATAVIEW_COL_RESIZABLE: int

DATAVIEW_COL_SORTABLE: int

DATAVIEW_COL_REORDERABLE: int

DATAVIEW_COL_HIDDEN: int

class DataViewTextRenderer(DataViewRenderer):
    """ DataViewTextRenderer is used for rendering text.

        Source: https://docs.wxpython.org/wx.dataview.DataViewTextRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ The constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTextRenderer.html
        """

    def EnableMarkup(self, enable=True) -> None:
        """ Enable interpretation of markup in the item data.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTextRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> None:
        """ Returns the Variant       type used with this renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewTextRenderer.html
        """



class DataViewCheckIconTextRenderer(DataViewRenderer):
    """ This renderer class shows a checkbox in addition to the icon and text
shown by the base class and also allows the user to toggle this
checkbox.

        Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconTextRenderer.html
    """
    def __init__(self, mode=DATAVIEW_CELL_ACTIVATABLE, align=DVR_DEFAULT_ALIGNMENT) -> None:
        """ Create a new renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconTextRenderer.html
        """

    def Allow3rdStateForUser(self, allow=True) -> None:
        """ Allow the user to interactively select the 3rd state for the items rendered by this object.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconTextRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> None:
        """ str

            Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconTextRenderer.html
        """



class DataViewProgressRenderer(DataViewRenderer):
    """ This class is used by DataViewCtrl to render progress bars.

        Source: https://docs.wxpython.org/wx.dataview.DataViewProgressRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ The constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewProgressRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> None:
        """ Returns the Variant       type used with this renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewProgressRenderer.html
        """



class DataViewBitmapRenderer(DataViewRenderer):
    """ This class is used by DataViewCtrl to render bitmaps.

        Source: https://docs.wxpython.org/wx.dataview.DataViewBitmapRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ The constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewBitmapRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> None:
        """ Returns the Variant       type used with this renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewBitmapRenderer.html
        """



class DataViewDateRenderer(DataViewRenderer):
    """ This class is used by DataViewCtrl to render calendar controls.

        Source: https://docs.wxpython.org/wx.dataview.DataViewDateRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ The constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewDateRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> None:
        """ Returns the Variant       type used with this renderer.

            Source: https://docs.wxpython.org/wx.dataview.DataViewDateRenderer.html
        """



class DataViewSpinRenderer(DataViewCustomRenderer):
    """ This is a specialized renderer for rendering integer values.

        Source: https://docs.wxpython.org/wx.dataview.DataViewSpinRenderer.html
    """
    def __init__(self, min, max, mode=DATAVIEW_CELL_EDITABLE, align=DVR_DEFAULT_ALIGNMENT) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewSpinRenderer.html
        """



class DataViewChoiceRenderer(DataViewRenderer):
    """ A DataViewCtrl renderer using Choice control and values of strings
in it.

        Source: https://docs.wxpython.org/wx.dataview.DataViewChoiceRenderer.html
    """
    def __init__(self, choices, mode=DATAVIEW_CELL_EDITABLE, alignment=DVR_DEFAULT_ALIGNMENT) -> None:
        """ The constructor.

            Source: https://docs.wxpython.org/wx.dataview.DataViewChoiceRenderer.html
        """

    def GetChoice(self, index) -> None:
        """ Returns the choice referred to by index.

            Source: https://docs.wxpython.org/wx.dataview.DataViewChoiceRenderer.html
        """

    def GetChoices(self) -> None:
        """ Returns all choices.

            Source: https://docs.wxpython.org/wx.dataview.DataViewChoiceRenderer.html
        """

    Choices: None  # See GetChoices



DataViewCellRenderState: TypeAlias = int  # Enumeration

DATAVIEW_CELL_SELECTED: int

DATAVIEW_CELL_PRELIT: int

DATAVIEW_CELL_INSENSITIVE: int

DATAVIEW_CELL_FOCUSED: int

class DataViewValueAdjuster:
    """ This class can be used with DataViewRenderer.SetValueAdjuster() to
customize rendering of model values with standard renderers.

        Source: https://docs.wxpython.org/wx.dataview.DataViewValueAdjuster.html
    """
    def MakeHighlighted(self, value) -> None:
        """ Change value for rendering when highlighted.

            Source: https://docs.wxpython.org/wx.dataview.DataViewValueAdjuster.html
        """



class DataViewCheckIconText(DataViewIconText):
    """ DataViewCheckIconText is used by DataViewCheckIconTextRenderer for
data transfer.

        Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconText.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconText.html
        """

    def GetCheckedState(self) -> None:
        """ Gets the checked state.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconText.html
        """

    def SetCheckedState(self, state) -> None:
        """ Sets the checked state.

            Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconText.html
        """

    CheckedState: None  # See GetCheckedState and SetCheckedState



DataViewItemArray: TypeAlias = list['DataViewItem']

DVCVariant: TypeAlias = Any

