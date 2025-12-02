# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

from .. import CommandEvent, Control, TextEntry

class StyledTextEvent(CommandEvent):
    """ The type of events sent from StyledTextCtrl.

        Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetAlt(self) -> None:
        """ Returns True if the Alt key is pressed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetAnnotationsLinesAdded(self) -> None:
        """ Returns the number of lines that have been added to or removed from an annotation.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetControl(self) -> None:
        """ Returns True if the Control key is pressed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetDragFlags(self) -> None:
        """ Returns flags for the drag operation associated with this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetDragResult(self) -> None:
        """ Returns drag result for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetDragText(self) -> None:
        """ str

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetFoldLevelNow(self) -> None:
        """ Returns the current fold level for the line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetFoldLevelPrev(self) -> None:
        """ Returns previous fold level for the line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetKey(self) -> None:
        """ Returns the key code of the key that generated this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetLParam(self) -> None:
        """ Returns the value of the LParam field for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetLength(self) -> None:
        """ Returns the length (number of characters) of this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetLine(self) -> None:
        """ Returns zero-based line number for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetLinesAdded(self) -> None:
        """ Returns the number of lines added or deleted with this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetListCompletionMethod(self) -> None:
        """ Returns a value describing the action that closed the list.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetListType(self) -> None:
        """ Returns the list type for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetMargin(self) -> None:
        """ Returns the zero-based index of the margin that generated this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetMessage(self) -> None:
        """ Returns a message number while a macro is being recorded.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetModificationType(self) -> None:
        """ Returns the modification type for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetModifiers(self) -> None:
        """ Returns the modifiers of the key press or mouse click for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetPosition(self) -> None:
        """ Returns the zero-based text position associated this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetShift(self) -> None:
        """ Returns True if the Shift key is pressed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetText(self) -> None:
        """ str

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetToken(self) -> None:
        """ Returns the token value for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetUpdated(self) -> None:
        """ Returns the value of the updated field for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetWParam(self) -> None:
        """ Returns value of the WParam field for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetX(self) -> None:
        """ Returns the X coordinate of the mouse for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetY(self) -> None:
        """ Returns the Y coordinate of the mouse for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetAnnotationLinesAdded(self, val) -> None:
        """ Sets the annotation lines added value for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetDragFlags(self, flags) -> None:
        """ Sets the drag flags for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetDragResult(self, val) -> None:
        """ Sets the drag result for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetDragText(self, val) -> None:
        """ Sets the drag text for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetFoldLevelNow(self, val) -> None:
        """ Sets the current fold level for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetFoldLevelPrev(self, val) -> None:
        """ Sets the previous fold level for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetKey(self, k) -> None:
        """ Sets the key code for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetLParam(self, val) -> None:
        """ Sets value of the LParam field for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetLength(self, len) -> None:
        """ Sets the length value for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetLine(self, val) -> None:
        """ Sets line number for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetLinesAdded(self, num) -> None:
        """ Sets the number of lines added for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetListCompletionMethod(self, val) -> None:
        """ Sets the list completion method for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetListType(self, val) -> None:
        """ Sets the list type for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetMargin(self, val) -> None:
        """ Sets margin number for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetMessage(self, val) -> None:
        """ Sets message number for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetModificationType(self, t) -> None:
        """ Sets the modification type for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetModifiers(self, m) -> None:
        """ Sets the value of the modifiers field for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetPosition(self, pos) -> None:
        """ Sets file position for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetText(self, t) -> None:
        """ Sets the text for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetToken(self, val) -> None:
        """ Sets the token for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetUpdated(self, val) -> None:
        """ Sets the value of the updated field for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetWParam(self, val) -> None:
        """ Sets the value of the WParam field for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetX(self, val) -> None:
        """ Sets the X value for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetY(self, val) -> None:
        """ Sets the Y value for this event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    Alt: None  # See GetAlt
    AnnotationsLinesAdded: None  # See GetAnnotationsLinesAdded
    Control: None  # See GetControl
    DragFlags: None  # See GetDragFlags and SetDragFlags
    DragResult: None  # See GetDragResult and SetDragResult
    DragText: None  # See GetDragText and SetDragText
    FoldLevelNow: None  # See GetFoldLevelNow and SetFoldLevelNow
    FoldLevelPrev: None  # See GetFoldLevelPrev and SetFoldLevelPrev
    Key: None  # See GetKey and SetKey
    LParam: None  # See GetLParam and SetLParam
    Length: None  # See GetLength and SetLength
    Line: None  # See GetLine and SetLine
    LinesAdded: None  # See GetLinesAdded and SetLinesAdded
    ListCompletionMethod: None  # See GetListCompletionMethod and SetListCompletionMethod
    ListType: None  # See GetListType and SetListType
    Margin: None  # See GetMargin and SetMargin
    Message: None  # See GetMessage and SetMessage
    ModificationType: None  # See GetModificationType and SetModificationType
    Modifiers: None  # See GetModifiers and SetModifiers
    Position: None  # See GetPosition and SetPosition
    Shift: None  # See GetShift
    Text: None  # See GetText and SetText
    Token: None  # See GetToken and SetToken
    Updated: None  # See GetUpdated and SetUpdated
    WParam: None  # See GetWParam and SetWParam
    X: None  # See GetX and SetX
    Y: None  # See GetY and SetY



EVT_STC_AUTOCOMP_CANCELLED: int  # Process a  wxEVT_STC_AUTOCOMP_CANCELLED   event.

EVT_STC_AUTOCOMP_CHAR_DELETED: int  # Process a  wxEVT_STC_AUTOCOMP_CHAR_DELETED   event.

EVT_STC_AUTOCOMP_COMPLETED: int  # Process a  wxEVT_STC_AUTOCOMP_COMPLETED   event.

EVT_STC_AUTOCOMP_SELECTION: int  # Process a  wxEVT_STC_AUTOCOMP_SELECTION   event.

EVT_STC_AUTOCOMP_SELECTION_CHANGE: int  # Process a  wxEVT_STC_AUTOCOMP_SELECTION_CHANGE   event.

EVT_STC_CALLTIP_CLICK: int  # Process a  wxEVT_STC_CALLTIP_CLICK   event.

EVT_STC_CHANGE: int  # Process a  wxEVT_STC_CHANGE   event.

EVT_STC_CHARADDED: int  # Process a  wxEVT_STC_CHARADDED   event.

EVT_STC_CLIPBOARD_COPY: int  # Process a  wxEVT_STC_CLIPBOARD_COPY   event.

EVT_STC_CLIPBOARD_PASTE: int  # Process a  wxEVT_STC_CLIPBOARD_PASTE   event.

EVT_STC_DO_DROP: int  # Process a  wxEVT_STC_DO_DROP   event.

EVT_STC_DOUBLECLICK: int  # Process a  wxEVT_STC_DOUBLECLICK   event.

EVT_STC_DRAG_OVER: int  # Process a  wxEVT_STC_DRAG_OVER   event.

EVT_STC_DWELLEND: int  # Process a  wxEVT_STC_DWELLEND   event.

EVT_STC_DWELLSTART: int  # Process a  wxEVT_STC_DWELLSTART   event.

EVT_STC_HOTSPOT_CLICK: int  # Process a  wxEVT_STC_HOTSPOT_CLICK   event.

EVT_STC_HOTSPOT_DCLICK: int  # Process a  wxEVT_STC_HOTSPOT_DCLICK   event.

EVT_STC_HOTSPOT_RELEASE_CLICK: int  # Process a  wxEVT_STC_HOTSPOT_RELEASE_CLICK   event.

EVT_STC_INDICATOR_CLICK: int  # Process a  wxEVT_STC_INDICATOR_CLICK   event.

EVT_STC_INDICATOR_RELEASE: int  # Process a  wxEVT_STC_INDICATOR_RELEASE   event.

EVT_STC_MACRORECORD: int  # Process a  wxEVT_STC_MACRORECORD   event.

EVT_STC_MARGIN_RIGHT_CLICK: int  # Process a  wxEVT_STC_MARGIN_RIGHT_CLICK   event.

EVT_STC_MARGINCLICK: int  # Process a  wxEVT_STC_MARGINCLICK   event.

EVT_STC_MODIFIED: int  # Process a  wxEVT_STC_MODIFIED   event.

EVT_STC_NEEDSHOWN: int  # Process a  wxEVT_STC_NEEDSHOWN   event.

EVT_STC_PAINTED: int  # Process a  wxEVT_STC_PAINTED   event.

EVT_STC_ROMODIFYATTEMPT: int  # Process a  wxEVT_STC_ROMODIFYATTEMPT   event.

EVT_STC_SAVEPOINTLEFT: int  # Process a  wxEVT_STC_SAVEPOINTLEFT   event.

EVT_STC_SAVEPOINTREACHED: int  # Process a  wxEVT_STC_SAVEPOINTREACHED   event.

EVT_STC_START_DRAG: int  # Process a  wxEVT_STC_START_DRAG   event.

EVT_STC_STYLENEEDED: int  # Process a  wxEVT_STC_STYLENEEDED   event.

EVT_STC_UPDATEUI: int  # Process a  wxEVT_STC_UPDATEUI   event.

EVT_STC_USERLISTSELECTION: int  # Process a  wxEVT_STC_USERLISTSELECTION   event.

EVT_STC_ZOOM: int  # Process a  wxEVT_STC_ZOOM   event.

class StyledTextCtrl(Control,TextEntry):
    """ A wxWidgets implementation of the Scintilla source code editing
component.

        Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddRefDocument(self, docPointer) -> None:
        """ Extend life of document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddSelection(self, caret, anchor) -> None:
        """ Add a selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddStyledText(self, data) -> None:
        """ Add array of cells to document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddTabStop(self, line, x) -> None:
        """ Add an explicit tab stop for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddText(self, text) -> None:
        """ Add text to the document at current position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddTextRaw(self, text, length=-1) -> None:
        """ Add text to the document at current position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddUndoAction(self, token, flags) -> None:
        """ Add a container action to the undo stack.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Allocate(self, bytes) -> None:
        """ Enlarge the document to a particular size of text bytes.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AllocateExtendedStyles(self, numberStyles) -> None:
        """ Allocate some extended (>255) style numbers and return the start of the range.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AllocateSubStyles(self, styleBase, numberStyles) -> None:
        """ Allocate a set of sub styles for a particular base style, returning start of range.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationClearAll(self) -> None:
        """ Clear the annotations from all lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationClearLine(self, line) -> None:
        """ Clear annotations from the given line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetLines(self, line) -> None:
        """ Get the number of annotation lines for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetStyle(self, line) -> None:
        """ Get the style number for the annotations for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetStyleOffset(self) -> None:
        """ Get the start of the range of style numbers used for annotations.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetStyles(self, line) -> None:
        """ Get the annotation styles for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetText(self, line) -> None:
        """ Get the annotation text for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetVisible(self) -> None:
        """ Get the visibility for the annotations for a view.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetStyle(self, line, style) -> None:
        """ Set the style number for the annotations for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetStyleOffset(self, style) -> None:
        """ Get the start of the range of style numbers used for annotations.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetStyles(self, line, styles) -> None:
        """ Set the annotation styles for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetText(self, line, text) -> None:
        """ Set the annotation text for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetVisible(self, visible) -> None:
        """ Set the visibility for the annotations for a view.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AppendText(self, text) -> None:
        """ Append a string to the end of the document without changing the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AppendTextRaw(self, text, length=-1) -> None:
        """ Append a string to the end of the document without changing the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompActive(self) -> None:
        """ Is there an auto-completion list visible?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompCancel(self) -> None:
        """ Remove the auto-completion list from the screen.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompComplete(self) -> None:
        """ User has selected an item so remove the list and insert the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetAutoHide(self) -> None:
        """ Retrieve whether or not autocompletion is hidden automatically when nothing matches.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetCancelAtStart(self) -> None:
        """ Retrieve whether auto-completion cancelled by backspacing before start.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetCaseInsensitiveBehaviour(self) -> None:
        """ Get auto-completion case insensitive behaviour.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetChooseSingle(self) -> None:
        """ Retrieve whether a single item auto-completion list automatically choose the item.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetCurrent(self) -> None:
        """ Get currently selected item position in the auto-completion list.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetCurrentText(self) -> None:
        """ Get currently selected item text in the auto-completion list.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetDropRestOfWord(self) -> None:
        """ Retrieve whether or not autocompletion deletes any word characters after the inserted text upon completion.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetIgnoreCase(self) -> None:
        """ Retrieve state of ignore case flag.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetMaxHeight(self) -> None:
        """ Set the maximum height, in rows, of auto-completion and user lists.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetMaxWidth(self) -> None:
        """ Get the maximum width, in characters, of auto-completion and user lists.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetMulti(self) -> None:
        """ Retrieve the effect of autocompleting when there are multiple selections.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetOrder(self) -> None:
        """ Get the way autocompletion lists are ordered.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetSeparator(self) -> None:
        """ Retrieve the auto-completion list separator character.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetTypeSeparator(self) -> None:
        """ Retrieve the auto-completion list type-separator character.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompPosStart(self) -> None:
        """ Retrieve the position of the caret when the auto-completion list was displayed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSelect(self, select) -> None:
        """ Select the item in the auto-completion list that starts with a string.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetAutoHide(self, autoHide) -> None:
        """ Set whether or not autocompletion is hidden automatically when nothing matches.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetCancelAtStart(self, cancel) -> None:
        """ Should the auto-completion list be cancelled if the user backspaces to a position before where the box was created.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetCaseInsensitiveBehaviour(self, behaviour) -> None:
        """ Set auto-completion case insensitive behaviour to either prefer case-sensitive matches or have no preference.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetChooseSingle(self, chooseSingle) -> None:
        """ Should a single item auto-completion list automatically choose the item.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetDropRestOfWord(self, dropRestOfWord) -> None:
        """ Set whether or not autocompletion deletes any word characters after the inserted text upon completion.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetFillUps(self, characterSet) -> None:
        """ Define a set of characters that when typed will cause the autocompletion to choose the selected item.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetIgnoreCase(self, ignoreCase) -> None:
        """ Set whether case is significant when performing auto-completion searches.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetMaxHeight(self, rowCount) -> None:
        """ Set the maximum height, in rows, of auto-completion and user lists.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetMaxWidth(self, characterCount) -> None:
        """ Set the maximum width, in characters, of auto-completion and user lists.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetMulti(self, multi) -> None:
        """ Change the effect of autocompleting when there are multiple selections.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetOrder(self, order) -> None:
        """ Set the way autocompletion lists are ordered.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetSeparator(self, separatorCharacter) -> None:
        """ Change the separator character in the string setting up an auto-completion list.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetTypeSeparator(self, separatorCharacter) -> None:
        """ Change the type-separator character in the string setting up an auto-completion list.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompShow(self, lengthEntered, itemList) -> None:
        """ Display an auto-completion list.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompStops(self, characterSet) -> None:
        """ Define a set of character that when typed cancel the auto-completion list.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoComplete(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompleteDirectories(self) -> None:
        """ Call this function to enable auto-completion of the text using the file system directories.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompleteFileNames(self) -> None:
        """ Call this function to enable auto-completion of the text typed in a single-line text control using all valid file system paths.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BackTab(self) -> None:
        """ Dedent the selected lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BeginUndoAction(self) -> None:
        """ Start a sequence of actions that is undone and redone as a unit.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceBadLight(self, pos) -> None:
        """ Highlight the character at a position indicating there is no matching brace.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceBadLightIndicator(self, useSetting, indicator) -> None:
        """ Use specified indicator to highlight non matching brace instead of changing its style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceHighlight(self, posA, posB) -> None:
        """ Highlight the characters at two positions.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceHighlightIndicator(self, useSetting, indicator) -> None:
        """ Use specified indicator to highlight matching braces instead of changing their style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceMatch(self, pos, maxReStyle=0) -> None:
        """ Find the position of a matching brace or wx.stc.STC_INVALID_POSITION if no match.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipActive(self) -> None:
        """ Is there an active call tip?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipCancel(self) -> None:
        """ Remove the call tip from the screen.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipPosAtStart(self) -> None:
        """ Retrieve the position where the caret was before displaying the call tip.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetBackground(self, back) -> None:
        """ Set the background colour for the call tip.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetForeground(self, fore) -> None:
        """ Set the foreground colour for the call tip.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetForegroundHighlight(self, fore) -> None:
        """ Set the foreground colour for the highlighted part of the call tip.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetHighlight(self, highlightStart, highlightEnd) -> None:
        """ Highlight a segment of the definition.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetPosAtStart(self, posStart) -> None:
        """ Set the start position in order to change when backspacing removes the calltip.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetPosition(self, above) -> None:
        """ Set position of calltip, above or below text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipShow(self, pos, definition) -> None:
        """ Show a call tip containing a definition near position pos.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipUseStyle(self, tabSize) -> None:
        """ Enable use of wx.stc.STC_STYLE_CALLTIP and set call tip tab size in pixels.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanCopy(self) -> None:
        """ Returns True if the selection can be copied to the clipboard.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanCut(self) -> None:
        """ Returns True if the selection can be cut to the clipboard.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanPaste(self) -> None:
        """ Will a paste succeed?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanRedo(self) -> None:
        """ Are there any redoable actions in the undo history?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanUndo(self) -> None:
        """ Are there any undoable actions in the undo history?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Cancel(self) -> None:
        """ Cancel any modes such as call tip or auto-completion list display.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ChangeInsertion(self, length, text) -> None:
        """ Change the text that is being inserted in response to wx.stc.STC_MOD_INSERTCHECK.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ChangeLexerState(self, start, end) -> None:
        """ Indicate that the internal state of a lexer has changed over a range and therefore there may be a need to redraw.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ChangeValue(self, value) -> None:
        """ Sets the new text control value.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharLeft(self) -> None:
        """ Move caret left one character.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharLeftExtend(self) -> None:
        """ Move caret left one character extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharLeftRectExtend(self) -> None:
        """ Move caret left one character, extending rectangular selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharPositionFromPoint(self, x, y) -> None:
        """ Find the position of a character from a point within the window.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharPositionFromPointClose(self, x, y) -> None:
        """ Find the position of a character from a point within the window.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharRight(self) -> None:
        """ Move caret right one character.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharRightExtend(self) -> None:
        """ Move caret right one character extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharRightRectExtend(self) -> None:
        """ Move caret right one character, extending rectangular selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ChooseCaretX(self) -> None:
        """ Set the last x chosen value to be the caret x position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Clear(self) -> None:
        """ Clear the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearAll(self) -> None:
        """ Delete all text in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearDocumentStyle(self) -> None:
        """ Set all style bytes to 0, remove all folding information.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearRegisteredImages(self) -> None:
        """ Clear all the registered images.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearRepresentation(self, encodedCharacter) -> None:
        """ Remove a character representation.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearSelections(self) -> None:
        """ Clear selections to a single empty stream selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearTabStops(self, line) -> None:
        """ Clear explicit tabstops on a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CmdKeyAssign(self, key, modifiers, cmd) -> None:
        """ When key+modifier combination keyDefinition is pressed perform sciCommand.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CmdKeyClear(self, key, modifiers) -> None:
        """ When key+modifier combination keyDefinition is pressed do nothing.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CmdKeyClearAll(self) -> None:
        """ Drop all key mappings.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CmdKeyExecute(self, cmd) -> None:
        """ Perform one of the operations defined by the STC_CMD_ constants.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Colourise(self, start, end) -> None:
        """ Colourise a segment of the document using the current lexing language.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ContractedFoldNext(self, lineStart) -> None:
        """ Find the next line at or after lineStart that is a contracted fold header line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ConvertEOLs(self, eolMode) -> None:
        """ Convert all line endings in the document to one mode.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Copy(self) -> None:
        """ Copy the selection to the clipboard.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CopyAllowLine(self) -> None:
        """ Copy the selection, if selection empty copy the line with the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CopyRange(self, start, end) -> None:
        """ Copy a range of text to the clipboard.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CopyText(self, length, text) -> None:
        """ Copy argument text to the clipboard.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CountCharacters(self, start, end) -> None:
        """ Count characters between two positions.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=STCNameStr) -> None:
        """ Create the UI elements for a STC that was created with the default constructor.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CreateDocument(self) -> None:
        """ Create a new document object.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CreateLoader(self, bytes) -> None:
        """ Create an ILoader.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Cut(self) -> None:
        """ Cut the selection to the clipboard.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelLineLeft(self) -> None:
        """ Delete back from the current position to the start of the line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelLineRight(self) -> None:
        """ Delete forwards from the current position to the end of the line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelWordLeft(self) -> None:
        """ Delete the word to the left of the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelWordRight(self) -> None:
        """ Delete the word to the right of the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelWordRightEnd(self) -> None:
        """ Delete the word to the right of the caret, but not the trailing non-word characters.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DeleteBack(self) -> None:
        """ Delete the selection or if no selection, the character before the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DeleteBackNotLine(self) -> None:
        """ Delete the selection or if no selection, the character before the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DeleteRange(self, start, lengthDelete) -> None:
        """ Delete a range of text in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DescribeKeyWordSets(self) -> None:
        """ Retrieve a â\nâ separated list of descriptions of the keyword sets understood by the current lexer.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DescribeProperty(self, name) -> None:
        """ Describe a property.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DiscardEdits(self) -> None:
        """ Resets the internal modified flag as if the current changes had been saved.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DistanceToSecondaryStyles(self) -> None:
        """ Where styles are duplicated by a feature such as active/inactive code return the distance between the two types.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DoDragEnter(self, x, y, defaultRes) -> None:
        """ Allow for simulating a DnD DragEnter.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DoDragLeave(self) -> None:
        """ Allow for simulating a DnD DragLeave.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DoDragOver(self, x, y, defaultRes) -> None:
        """ Allow for simulating a DnD DragOver.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DoDropText(self, x, y, data) -> None:
        """ Allow for simulating a DnD DropText.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocLineFromVisible(self, displayLine) -> None:
        """ Find the document line of a display line taking hidden lines into account.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocumentEnd(self) -> None:
        """ Move caret to last position in document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocumentEndExtend(self) -> None:
        """ Move caret to last position in document extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocumentStart(self) -> None:
        """ Move caret to first position in document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocumentStartExtend(self) -> None:
        """ Move caret to first position in document extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DropSelectionN(self, selection) -> None:
        """ Drop one selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EditToggleOvertype(self) -> None:
        """ Switch from insert to overtype mode or the reverse.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EmptyUndoBuffer(self) -> None:
        """ Delete the undo history.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EndUndoAction(self) -> None:
        """ End a sequence of actions that is undone and redone as a unit.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EnsureCaretVisible(self) -> None:
        """ Ensure the caret is visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EnsureVisible(self, line) -> None:
        """ Ensure a particular line is visible by expanding any header line hiding it.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EnsureVisibleEnforcePolicy(self, line) -> None:
        """ Ensure a particular line is visible by expanding any header line hiding it.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ExpandChildren(self, line, level) -> None:
        """ Expand a fold header and all children.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FindColumn(self, line, column) -> None:
        """ Find the position of a column on a line taking into account tabs and multi-byte characters.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FindText(self, minPos, maxPos, text, flags=0) -> None:
        """ Find some text in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FoldAll(self, action) -> None:
        """ Expand or contract all fold headers.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FoldChildren(self, line, action) -> None:
        """ Expand or contract a fold header and its children.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FoldDisplayTextSetStyle(self, style) -> None:
        """ Set the style of fold display text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FoldLine(self, line, action) -> None:
        """ Expand or contract a fold header.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ForceUpper(self) -> None:
        """ Convert all text entered into the control to upper case.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FormFeed(self) -> None:
        """ Insert a Form Feed character.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FormatRange(self, doDraw, startPos, endPos, draw, target, renderRect, pageRect) -> None:
        """ On Windows, will draw the document into a display context such as a printer.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FreeSubStyles(self) -> None:
        """ Free allocated sub styles.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalCaretForeground(self) -> None:
        """ Get the foreground colour of additional carets.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalCaretsBlink(self) -> None:
        """ Whether additional carets will blink.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalCaretsVisible(self) -> None:
        """ Whether additional carets are visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalSelAlpha(self) -> None:
        """ Get the alpha of the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalSelectionTyping(self) -> None:
        """ Whether typing can be performed into multiple selections.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAllLinesVisible(self) -> None:
        """ Are all lines visible?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAnchor(self) -> None:
        """ Returns the position of the opposite end of the selection to the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAutomaticFold(self) -> None:
        """ Get automatic folding behaviours.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetBackSpaceUnIndents(self) -> None:
        """ Does a backspace pressed when caret is within indentation unindent?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetBufferedDraw(self) -> None:
        """ Is drawing done first into a buffer or direct to the screen?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretForeground(self) -> None:
        """ Get the foreground colour of the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretLineBackAlpha(self) -> None:
        """ Get the background alpha of the caret line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretLineBackground(self) -> None:
        """ Get the colour of the background of the line containing the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretLineVisible(self) -> None:
        """ Is the background of the line containing the caret in a different colour?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretLineVisibleAlways(self) -> None:
        """ Is the caret line always visible?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretPeriod(self) -> None:
        """ Get the time in milliseconds that the caret is on and off.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretSticky(self) -> None:
        """ Can the caret preferred x position only be changed by explicit movement commands?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretStyle(self) -> None:
        """ Returns the current style of the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretWidth(self) -> None:
        """ Returns the width of the insert mode caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCharAt(self, pos) -> None:
        """ Returns the character byte at the position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCharacterPointer(self) -> None:
        """ Compact the document buffer and return a read-only memoryview
object of the characters in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCodePage(self) -> None:
        """ Get the code page used to interpret the bytes of the document as characters.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetColumn(self, pos) -> None:
        """ Retrieve the column number of a position, taking tab width into account.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetControlCharSymbol(self) -> None:
        """ Get the way control characters are displayed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCurLine(self) -> None:
        """ Retrieve the text of the line containing the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCurLineRaw(self) -> None:
        """ Retrieve the text of the line containing the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCurrentLine(self) -> None:
        """ Returns the line number of the line with the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCurrentPos(self) -> None:
        """ Returns the position of the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetDefaultStyle(self) -> None:
        """ Returns the style currently used for the new text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetDirectFunction(self) -> None:
        """ Retrieve a pointer to a function that processes messages for this Scintilla.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetDirectPointer(self) -> None:
        """ Retrieve a pointer value to use as the first argument when calling the function returned by GetDirectFunction.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetDocPointer(self) -> None:
        """ Retrieve a pointer to the document object.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEOLMode(self) -> None:
        """ Retrieve the current end of line mode - one of wx.stc.STC_EOL_CRLF, wx.stc.STC_EOL_CR, or wx.stc.STC_EOL_LF.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEdgeColour(self) -> None:
        """ Retrieve the colour used in edge indication.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEdgeColumn(self) -> None:
        """ Retrieve the column number which text should be kept within.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEdgeMode(self) -> None:
        """ Retrieve the edge highlight mode.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEndAtLastLine(self) -> None:
        """ Retrieve whether the maximum scroll position has the last line at the bottom of the view.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEndStyled(self) -> None:
        """ Retrieve the position of the last correctly styled character.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetExtraAscent(self) -> None:
        """ Get extra ascent for each line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetExtraDescent(self) -> None:
        """ Get extra descent for each line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFirstVisibleLine(self) -> None:
        """ Retrieve the display line at the top of the display.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFoldExpanded(self, line) -> None:
        """ Is a header line expanded?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFoldLevel(self, line) -> None:
        """ Retrieve the fold level of a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFoldParent(self, line) -> None:
        """ Find the parent line of a child line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFontQuality(self) -> None:
        """ Retrieve the quality level for text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetGapPosition(self) -> None:
        """ Return a position which, to avoid performance costs, should not be within the range of a call to GetRangePointer.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHighlightGuide(self) -> None:
        """ Get the highlighted indentation guide column.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHint(self) -> None:
        """ Returns the current hint string.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHotspotActiveBackground(self) -> None:
        """ Get the back colour for active hotspots.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHotspotActiveForeground(self) -> None:
        """ Get the fore colour for active hotspots.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHotspotActiveUnderline(self) -> None:
        """ Get whether underlining for active hotspots.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHotspotSingleLine(self) -> None:
        """ Get the HotspotSingleLine property.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIMEInteraction(self) -> None:
        """ Is the IME displayed in a window or inline?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIdentifier(self) -> None:
        """ Get the identifier.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIdleStyling(self) -> None:
        """ Retrieve the limits to idle styling.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIndent(self) -> None:
        """ Retrieve indentation size.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIndentationGuides(self) -> None:
        """ Are the indentation guides visible?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIndicatorCurrent(self) -> None:
        """ Get the current indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIndicatorValue(self) -> None:
        """ Get the current indicator value.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetInsertionPoint(self) -> None:
        """ Returns the insertion point, or cursor, position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLastChild(self, line, level) -> None:
        """ Find the last child line of a header line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLastKeydownProcessed(self) -> None:
        """ Can be used to prevent the EVT_CHAR handler from adding the char.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLastPosition(self) -> None:
        """ Returns the zero based index of the last position in the text control, which is equal to the number of characters in the control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLayoutCache(self) -> None:
        """ Retrieve the degree of caching of layout information.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLength(self) -> None:
        """ Returns the number of bytes in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLexer(self) -> None:
        """ Retrieve the lexing language of the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLexerLanguage(self) -> None:
        """ Retrieve the lexing language of the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    @staticmethod
    def GetLibraryVersionInfo() -> None:
        """ Returns the version of the Scintilla library used by this control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLine(self, line) -> None:
        """ Retrieve the contents of a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineCount(self) -> None:
        """ Returns the number of lines in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineEndPosition(self, line) -> None:
        """ Get the position after the last visible characters on a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineEndTypesActive(self) -> None:
        """ Get the line end types currently recognised.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineEndTypesAllowed(self) -> None:
        """ Get the line end types currently allowed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineEndTypesSupported(self) -> None:
        """ Bit set of LineEndType enumertion for which line ends beyond the standard LF, CR, and CRLF are supported by the lexer.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineIndentPosition(self, line) -> None:
        """ Retrieve the position before the first non indentation character on a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineIndentation(self, line) -> None:
        """ Retrieve the number of columns that a line is indented.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineLength(self, lineNo) -> None:
        """ Gets the length of the specified line, not including any trailing newline character(s).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineRaw(self, line) -> None:
        """ Retrieve the contents of a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineSelEndPosition(self, line) -> None:
        """ Retrieve the position of the end of the selection at the given line (wx``wx.stc.STC_INVALID_POSITION`` if no selection on this line).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineSelStartPosition(self, line) -> None:
        """ Retrieve the position of the start of the selection at the given line (wx``wx.stc.STC_INVALID_POSITION`` if no selection on this line).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineState(self, line) -> None:
        """ Retrieve the extra styling information for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineText(self, lineNo) -> None:
        """ Returns the contents of a given line in the text control, not including any trailing newline character(s).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineVisible(self, line) -> None:
        """ Is a line visible?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMainSelection(self) -> None:
        """ Which selection is the main selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginBackground(self, margin) -> None:
        """ Retrieve the background colour of a margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginCount(self) -> None:
        """ How many margins are there?.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginCursor(self, margin) -> None:
        """ Retrieve the cursor shown in a margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginLeft(self) -> None:
        """ Returns the size in pixels of the left margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginMask(self, margin) -> None:
        """ Retrieve the marker mask of a margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginOptions(self) -> None:
        """ Get the margin options.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginRight(self) -> None:
        """ Returns the size in pixels of the right margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginSensitive(self, margin) -> None:
        """ Retrieve the mouse click sensitivity of a margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginType(self, margin) -> None:
        """ Retrieve the type of a margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginWidth(self, margin) -> None:
        """ Retrieve the width of a margin in pixels.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMargins(self) -> None:
        """ Returns the margins used by the control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarkerSymbolDefined(self, markerNumber) -> None:
        """ Which symbol was defined for markerNumber with MarkerDefine.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMaxLineState(self) -> None:
        """ Retrieve the last line number that has line state.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetModEventMask(self) -> None:
        """ Get which document modification events are sent to the container.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetModify(self) -> None:
        """ Is the document different from when it was last saved?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMouseDownCaptures(self) -> None:
        """ Get whether mouse gets captured.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMouseDwellTime(self) -> None:
        """ Retrieve the time the mouse must sit still to generate a mouse dwell event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMouseSelectionRectangularSwitch(self) -> None:
        """ Whether switching to rectangular mode while selecting with the mouse is allowed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMouseWheelCaptures(self) -> None:
        """ Get whether mouse wheel can be active outside the window.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMultiPaste(self) -> None:
        """ Retrieve the effect of pasting when there are multiple selections.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMultipleSelection(self) -> None:
        """ Whether multiple selections can be made.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetNextTabStop(self, line, x) -> None:
        """ Find the next explicit tab stop position on a line after a position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetNumberOfLines(self) -> None:
        """ Returns the number of lines in the text control buffer.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetOvertype(self) -> None:
        """ Returns True if overtype mode is active otherwise False is returned.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPasteConvertEndings(self) -> None:
        """ Get convert-on-paste setting.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPhasesDraw(self) -> None:
        """ How many phases is drawing done in?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPositionCacheSize(self) -> None:
        """ How many entries are allocated to the position cache?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPrimaryStyleFromStyle(self, style) -> None:
        """ For a secondary style, return the primary style, else return the argument.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPrintColourMode(self) -> None:
        """ Returns the print colour mode.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPrintMagnification(self) -> None:
        """ Returns the print magnification.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPrintWrapMode(self) -> None:
        """ Is printing line wrapped?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetProperty(self, key) -> None:
        """ Retrieve a âpropertyâ value previously set with SetProperty.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPropertyExpanded(self, key) -> None:
        """ Retrieve a âpropertyâ value previously set with SetProperty, with â$()â variable replacement on returned buffer.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPropertyInt(self, key, defaultValue=0) -> None:
        """ Retrieve a âpropertyâ value previously set with SetProperty, interpreted as an int AFTER any â$()â variable replacement.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPunctuationChars(self) -> None:
        """ Get the set of characters making up punctuation characters.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRange(self, from_, to_) -> None:
        """ Returns the string containing the text starting in the positions from  and up to to  in the control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRangePointer(self, position, rangeLength) -> None:
        """ Return a read-only pointer to a range of characters in the
document. May move the gap so that the range is contiguous,
but will only move up to rangeLength bytes.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetReadOnly(self) -> None:
        """ In read-only mode?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionAnchor(self) -> None:
        """ Return the anchor position of the rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionAnchorVirtualSpace(self) -> None:
        """ Return the virtual space of the anchor of the rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionCaret(self) -> None:
        """ Return the caret position of the rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionCaretVirtualSpace(self) -> None:
        """ Return the virtual space of the caret of the rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionModifier(self) -> None:
        """ Get the modifier key used for rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRepresentation(self, encodedCharacter) -> None:
        """ Set the way a character is drawn.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSTCCursor(self) -> None:
        """ Get cursor type.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSTCFocus(self) -> None:
        """ Get internal focus flag.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetScrollWidth(self) -> None:
        """ Retrieve the document width assumed for scrolling.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetScrollWidthTracking(self) -> None:
        """ Retrieve whether the scroll width tracks wide lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSearchFlags(self) -> None:
        """ Get the search flags used by SearchInTarget.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelAlpha(self) -> None:
        """ Get the alpha of the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelEOLFilled(self) -> None:
        """ Is the selection end of line filled?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectedText(self) -> None:
        """ Retrieve the selected text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectedTextRaw(self) -> None:
        """ Retrieve the selected text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelection(self) -> None:
        """ Gets the current selection span.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionEmpty(self) -> None:
        """ Is every selected range empty?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionEnd(self) -> None:
        """ Returns the position at the end of the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionMode(self) -> None:
        """ Get the mode of the current selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNAnchor(self, selection) -> None:
        """ Return the anchor position of the nth selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNAnchorVirtualSpace(self, selection) -> None:
        """ Return the virtual space of the anchor of the nth selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNCaret(self, selection) -> None:
        """ Return the caret position of the nth selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNCaretVirtualSpace(self, selection) -> None:
        """ Return the virtual space of the caret of the nth selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNEnd(self, selection) -> None:
        """ Returns the position at the end of the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNStart(self, selection) -> None:
        """ Returns the position at the start of the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionStart(self) -> None:
        """ Returns the position at the start of the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelections(self) -> None:
        """ How many selections are there?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStatus(self) -> None:
        """ Get error status.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStringSelection(self) -> None:
        """ Gets the text currently selected in the control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyle(self, position, style) -> None:
        """ This method is inherited from TextAreaBase but is not implemented in   wx.stc.StyledTextCtrl.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyleAt(self, pos) -> None:
        """ Returns the style byte at the position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyleBits(self) -> None:
        """ Retrieve number of bits in style bytes used to hold the lexical state.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyleBitsNeeded(self) -> None:
        """ Retrieve the number of bits the current lexer needs for styling.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyleFromSubStyle(self, subStyle) -> None:
        """ For a sub style, return the base style, else return the argument.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyledText(self, startPos, endPos) -> None:
        """ Retrieve a buffer of cells.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSubStyleBases(self) -> None:
        """ Get the set of base styles that can be extended with sub styles.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSubStylesLength(self, styleBase) -> None:
        """ The number of sub styles associated with a base style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSubStylesStart(self, styleBase) -> None:
        """ The starting style number for the sub styles associated with a base style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTabDrawMode(self) -> None:
        """ Retrieve the current tab draw mode.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTabIndents(self) -> None:
        """ Does a tab pressed when caret is within indentation indent?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTabWidth(self) -> None:
        """ Retrieve the visible size of a tab.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTag(self, tagNumber) -> None:
        """ Retrieve the value of a tag from a regular expression search.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTargetEnd(self) -> None:
        """ Get the position that ends the target.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTargetStart(self) -> None:
        """ Get the position that starts the target.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTargetText(self) -> None:
        """ Retrieve the text in the target.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTargetTextRaw(self) -> None:
        """ Retrieve the target text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTechnology(self) -> None:
        """ Get the tech.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetText(self) -> None:
        """ Retrieve all the text in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTextLength(self) -> None:
        """ Retrieve the number of characters in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTextRange(self, startPos, endPos) -> None:
        """ Retrieve a range of text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTextRangeRaw(self, startPos, endPos) -> None:
        """ Retrieve a range of text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTextRaw(self) -> None:
        """ Retrieve all the text in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTwoPhaseDraw(self) -> None:
        """ Is drawing done in two phases with backgrounds drawn before foregrounds?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUndoCollection(self) -> None:
        """ Is undo history being collected?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUseAntiAliasing(self) -> None:
        """ Returns the current UseAntiAliasing setting.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUseHorizontalScrollBar(self) -> None:
        """ Is the horizontal scroll bar visible?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUseTabs(self) -> None:
        """ Retrieve whether tabs will be used in indentation.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUseVerticalScrollBar(self) -> None:
        """ Is the vertical scroll bar visible?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetValue(self) -> None:
        """ Gets the contents of the control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetViewEOL(self) -> None:
        """ Are the end of line characters visible?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetViewWhiteSpace(self) -> None:
        """ Are white space characters currently visible? Returns one of STC_WS_ constants.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetVirtualSpaceOptions(self) -> None:
        """ Return options for virtual space behaviour.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWhitespaceChars(self) -> None:
        """ Get the set of characters making up whitespace for when moving or selecting by word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWhitespaceSize(self) -> None:
        """ Get the size of the dots used to mark space characters.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWordChars(self) -> None:
        """ Get the set of characters making up words for when moving or selecting by word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapIndentMode(self) -> None:
        """ Retrieve how wrapped sublines are placed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapMode(self) -> None:
        """ Retrieve whether text is word wrapped.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapStartIndent(self) -> None:
        """ Retrieve the start indent for wrapped lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapVisualFlags(self) -> None:
        """ Retrieve the display mode of visual flags for wrapped lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapVisualFlagsLocation(self) -> None:
        """ Retrieve the location of visual flags for wrapped lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetXOffset(self) -> None:
        """ Get the xOffset (ie, horizontal scroll position).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetZoom(self) -> None:
        """ Retrieve the zoom level.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GotoLine(self, line) -> None:
        """ Set caret to start of a line and ensure it is visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GotoPos(self, caret) -> None:
        """ Set caret to a position and ensure it is visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HideLines(self, lineStart, lineEnd) -> None:
        """ Make a range of lines invisible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HideSelection(self, hide) -> None:
        """ Draw the selection in normal style or with selection highlighted.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HitTestPos(self, pt) -> None:
        """ Finds the position of the character at the specified point.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HitTest(self, pt) -> None:
        """ Finds the row and column of the character at the specified point.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Home(self) -> None:
        """ Move caret to first position on line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeDisplay(self) -> None:
        """ Move caret to first position on display line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeDisplayExtend(self) -> None:
        """ Move caret to first position on display line extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeExtend(self) -> None:
        """ Move caret to first position on line extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeRectExtend(self) -> None:
        """ Move caret to first position on line, extending rectangular selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeWrap(self) -> None:
        """ Like Home but when word-wrap is enabled goes first to start of display line HomeDisplay, then to start of document line Home.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeWrapExtend(self) -> None:
        """ Like HomeExtend but when word-wrap is enabled extends first to start of display line HomeDisplayExtend, then to start of document line HomeExtend.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorAllOnFor(self, pos) -> None:
        """ Are any indicators present at pos?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorClearRange(self, start, lengthClear) -> None:
        """ Turn an indicator off over a range.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorEnd(self, indicator, pos) -> None:
        """ Where does a particular indicator end?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorFillRange(self, start, lengthFill) -> None:
        """ Turn an indicator on over a range.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetAlpha(self, indicator) -> None:
        """ Get the alpha fill colour of the given indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetFlags(self, indicator) -> None:
        """ Retrieve the attributes of an indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetForeground(self, indicator) -> None:
        """ Retrieve the foreground colour of an indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetHoverForeground(self, indicator) -> None:
        """ Retrieve the foreground hover colour of an indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetHoverStyle(self, indicator) -> None:
        """ Retrieve the hover style of an indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetOutlineAlpha(self, indicator) -> None:
        """ Get the alpha outline colour of the given indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetStyle(self, indicator) -> None:
        """ Retrieve the style of an indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetUnder(self, indicator) -> None:
        """ Retrieve whether indicator drawn under or over text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetAlpha(self, indicator, alpha) -> None:
        """ Set the alpha fill colour of the given indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetFlags(self, indicator, flags) -> None:
        """ Set the attributes of an indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetForeground(self, indicator, fore) -> None:
        """ Set the foreground colour of an indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetHoverForeground(self, indicator, fore) -> None:
        """ Set the foreground hover colour of an indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetHoverStyle(self, indicator, indicatorStyle) -> None:
        """ Set a hover indicator to plain, squiggle or TT.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetOutlineAlpha(self, indicator, alpha) -> None:
        """ Set the alpha outline colour of the given indicator.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetStyle(self, indicator, indicatorStyle) -> None:
        """ Set an indicator to plain, squiggle or TT.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetUnder(self, indicator, under) -> None:
        """ Set an indicator to draw under text or over(default).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorStart(self, indicator, pos) -> None:
        """ Where does a particular indicator start?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorValueAt(self, indicator, pos) -> None:
        """ What value does a particular indicator have at a position?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def InsertText(self, pos, text) -> None:
        """ Insert string at a position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def InsertTextRaw(self, pos, text) -> None:
        """ Insert string at a position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IsEditable(self) -> None:
        """ Returns True if the controls contents may be edited by user (note that it always can be changed by the program).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IsEmpty(self) -> None:
        """ Returns True if the control is currently empty.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IsModified(self) -> None:
        """ Returns True if the text has been modified by user.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IsRangeWord(self, start, end) -> None:
        """ Is the range start..end considered a word?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineCopy(self) -> None:
        """ Copy the line containing the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineCut(self) -> None:
        """ Cut the line containing the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDelete(self) -> None:
        """ Delete the line containing the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDown(self) -> None:
        """ Move caret down one line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDownExtend(self) -> None:
        """ Move caret down one line extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDownRectExtend(self) -> None:
        """ Move caret down one line, extending rectangular selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDuplicate(self) -> None:
        """ Duplicate the current line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEnd(self) -> None:
        """ Move caret to last position on line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndDisplay(self) -> None:
        """ Move caret to last position on display line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndDisplayExtend(self) -> None:
        """ Move caret to last position on display line extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndExtend(self) -> None:
        """ Move caret to last position on line extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndRectExtend(self) -> None:
        """ Move caret to last position on line, extending rectangular selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndWrap(self) -> None:
        """ Like LineEnd but when word-wrap is enabled goes first to end of display line LineEndDisplay, then to start of document line LineEnd.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndWrapExtend(self) -> None:
        """ Like LineEndExtend but when word-wrap is enabled extends first to end of display line LineEndDisplayExtend, then to start of document line LineEndExtend.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineFromPosition(self, pos) -> None:
        """ Retrieve the line containing a position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineLength(self, line) -> None:
        """ How many characters are on a line, including end of line characters?

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineScroll(self, columns, lines) -> None:
        """ Scroll horizontally and vertically.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineScrollDown(self) -> None:
        """ Scroll the document down, keeping the caret visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineScrollUp(self) -> None:
        """ Scroll the document up, keeping the caret visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineTranspose(self) -> None:
        """ Switch the current line with the previous.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineUp(self) -> None:
        """ Move caret up one line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineUpExtend(self) -> None:
        """ Move caret up one line extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineUpRectExtend(self) -> None:
        """ Move caret up one line, extending rectangular selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LinesJoin(self) -> None:
        """ Join the lines in the target.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LinesOnScreen(self) -> None:
        """ Retrieves the number of lines completely visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LinesSplit(self, pixelWidth) -> None:
        """ Split the lines in the target into lines that are less wide than pixelWidth where possible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LoadFile(self, filename) -> None:
        """ Load the contents of filename into the editor.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LoadLexerLibrary(self, path) -> None:
        """ Load a lexer library (dll / so).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LowerCase(self) -> None:
        """ Transform the selection to lower case.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginGetStyle(self, line) -> None:
        """ Get the style number for the text margin for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginGetStyleOffset(self) -> None:
        """ Get the start of the range of style numbers used for margin text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginGetStyles(self, line) -> None:
        """ Get the styles in the text margin for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginGetText(self, line) -> None:
        """ Get the text in the text margin for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginSetStyle(self, line, style) -> None:
        """ Set the style number for the text margin for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginSetStyleOffset(self, style) -> None:
        """ Get the start of the range of style numbers used for margin text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginSetStyles(self, line, styles) -> None:
        """ Set the style in the text margin for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginSetText(self, line, text) -> None:
        """ Set the text in the text margin for a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginTextClearAll(self) -> None:
        """ Clear the margin text on all lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkDirty(self) -> None:
        """ Mark text as modified (dirty).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerAdd(self, line, markerNumber) -> None:
        """ Add a marker to a line, returning an ID which can be used to find or delete the marker.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerAddSet(self, line, markerSet) -> None:
        """ Add a set of markers to a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDefine(self, markerNumber, markerSymbol, foreground=NullColour, background=NullColour) -> None:
        """ Set the symbol used for a particular marker number, and optionally the fore and background colours.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDefineBitmap(self, markerNumber, bmp) -> None:
        """ Define a marker with a   wx.Bitmap.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDefineRGBAImage(self, markerNumber, pixels) -> None:
        """ Define a marker from RGBA data.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDelete(self, line, markerNumber) -> None:
        """ Delete a marker from a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDeleteAll(self, markerNumber) -> None:
        """ Delete all markers with a particular number from all lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDeleteHandle(self, markerHandle) -> None:
        """ Delete a marker.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerEnableHighlight(self, enabled) -> None:
        """ Enable/disable highlight for current folding block (smallest one that contains the caret)

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerGet(self, line) -> None:
        """ Get a bit mask of all the markers set on a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerLineFromHandle(self, markerHandle) -> None:
        """ Retrieve the line number at which a particular marker is located.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerNext(self, lineStart, markerMask) -> None:
        """ Find the next line at or after lineStart that includes a marker in mask.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerPrevious(self, lineStart, markerMask) -> None:
        """ Find the previous line before lineStart that includes a marker in mask.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerSetAlpha(self, markerNumber, alpha) -> None:
        """ Set the alpha used for a marker that is drawn in the text area, not the margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerSetBackground(self, markerNumber, back) -> None:
        """ Set the background colour used for a particular marker number.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerSetBackgroundSelected(self, markerNumber, back) -> None:
        """ Set the background colour used for a particular marker number when its folding block is selected.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerSetForeground(self, markerNumber, fore) -> None:
        """ Set the foreground colour used for a particular marker number.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MoveCaretInsideView(self) -> None:
        """ Move the caret inside current view if itâs not there already.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MoveSelectedLinesDown(self) -> None:
        """ Move the selected lines down one line, shifting the line below before the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MoveSelectedLinesUp(self) -> None:
        """ Move the selected lines up one line, shifting the line above after the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MultiEdgeAddLine(self, column, edgeColour) -> None:
        """ Add a new vertical edge to the view.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MultiEdgeClearAll(self) -> None:
        """ Clear all vertical edges.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MultipleSelectAddEach(self) -> None:
        """ Add each occurrence of the main selection in the target to the set of selections.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MultipleSelectAddNext(self) -> None:
        """ Add the next occurrence of the main selection to the set of selections as main.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def NewLine(self) -> None:
        """ Insert a new line, may use a CRLF, CR or LF depending on EOL mode.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageDown(self) -> None:
        """ Move caret one page down.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageDownExtend(self) -> None:
        """ Move caret one page down extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageDownRectExtend(self) -> None:
        """ Move caret one page down, extending rectangular selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageUp(self) -> None:
        """ Move caret one page up.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageUpExtend(self) -> None:
        """ Move caret one page up extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageUpRectExtend(self) -> None:
        """ Move caret one page up, extending rectangular selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ParaDown(self) -> None:
        """ Move caret down one paragraph (delimited by empty lines).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ParaDownExtend(self) -> None:
        """ Extend selection down one paragraph (delimited by empty lines).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ParaUp(self) -> None:
        """ Move caret up one paragraph (delimited by empty lines).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ParaUpExtend(self) -> None:
        """ Extend selection up one paragraph (delimited by empty lines).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Paste(self) -> None:
        """ Paste the contents of the clipboard into the document replacing the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PointFromPosition(self, pos) -> None:
        """ Retrieve the point in the window where a position is displayed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionAfter(self, pos) -> None:
        """ Given a valid document position, return the next position taking code page into account.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionBefore(self, pos) -> None:
        """ Given a valid document position, return the previous position taking code page into account.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionFromLine(self, line) -> None:
        """ Retrieve the position at the start of a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionFromPoint(self, pt) -> None:
        """ Find the position from a point within the window.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionFromPointClose(self, x, y) -> None:
        """ Find the position from a point within the window but return wx.stc.STC_INVALID_POSITION if not close to text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionRelative(self, pos, relative) -> None:
        """ Given a valid document position, return a position that differs in a number of characters.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionToCoords(self, pos) -> None:
        """ Converts given text position to client coordinates in pixels.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionToXY(self, pos) -> None:
        """ Converts given position to a zero-based column, line number pair.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PrivateLexerCall(self, operation, pointer) -> None:
        """ For private communication between an application and a known lexer.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PropertyNames(self) -> None:
        """ Retrieve a â\nâ separated list of properties understood by the current lexer.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PropertyType(self, name) -> None:
        """ Retrieve the type of a property.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RGBAImageSetHeight(self, height) -> None:
        """ Set the height for future RGBA image data.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RGBAImageSetScale(self, scalePercent) -> None:
        """ Set the scale factor in percent for future RGBA image data.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RGBAImageSetWidth(self, width) -> None:
        """ Set the width for future RGBA image data.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Redo(self) -> None:
        """ Redoes the next action on the undo history.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RegisterImage(self, type, bmp) -> None:
        """ Register an image for use in autocompletion lists.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RegisterRGBAImage(self, type, pixels) -> None:
        """ Register an RGBA image for use in autocompletion lists.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReleaseAllExtendedStyles(self) -> None:
        """ Release all extended (>255) style numbers.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReleaseDocument(self, docPointer) -> None:
        """ Release a reference to the document, deleting document if it fades to black.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Remove(self, from_, to_) -> None:
        """ Removes the text starting at the first given position up to (but not including) the character at the last position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Replace(self, from_, to_, value) -> None:
        """ Replaces the text starting at the first position up to (but not including) the character at the last position with the given text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceSelection(self, text) -> None:
        """ Replace the selected text with the argument text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceSelectionRaw(self, text) -> None:
        """ Replace the current selection with text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceTarget(self, text) -> None:
        """ Replace the target text with the argument text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceTargetRE(self, text) -> None:
        """ Replace the target text with the argument text after \d processing.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceTargetRERaw(self, text, length=-1) -> None:
        """ Replace the current target with text using regular expressions.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceTargetRaw(self, text, length=-1) -> None:
        """ Replace the current target with text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RotateSelection(self) -> None:
        """ Set the main selection to the next selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SaveFile(self, filename) -> None:
        """ Write the contents of the editor to filename.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollRange(self, secondary, primary) -> None:
        """ Scroll the argument positions and the range between them into view giving priority to the primary position then the secondary position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollToColumn(self, column) -> None:
        """ Scroll enough to make the given column visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollToEnd(self) -> None:
        """ Scroll to end of document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollToLine(self, line) -> None:
        """ Scroll enough to make the given line visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollToStart(self) -> None:
        """ Scroll to start of document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SearchAnchor(self) -> None:
        """ Sets the current caret position to be the search anchor.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SearchInTarget(self, text) -> None:
        """ Search for a counted string in the target and set the target to the found range.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SearchNext(self, searchFlags, text) -> None:
        """ Find some text starting at the search anchor.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SearchPrev(self, searchFlags, text) -> None:
        """ Find some text starting at the search anchor and moving backwards.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SelectAll(self) -> None:
        """ Select all the text in the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SelectNone(self) -> None:
        """ Deselects selected text in the control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SelectionDuplicate(self) -> None:
        """ Duplicate the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SelectionIsRectangle(self) -> None:
        """ Is the selection rectangular? The alternative is the more common stream selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SendMsg(self, msg, wp=0, lp=0) -> int:
        """ Scintilla API call.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalCaretForeground(self, fore) -> None:
        """ Set the foreground colour of additional carets.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalCaretsBlink(self, additionalCaretsBlink) -> None:
        """ Set whether additional carets will blink.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalCaretsVisible(self, additionalCaretsVisible) -> None:
        """ Set whether additional carets are visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalSelAlpha(self, alpha) -> None:
        """ Set the alpha of the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalSelBackground(self, back) -> None:
        """ Set the background colour of additional selections.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalSelForeground(self, fore) -> None:
        """ Set the foreground colour of additional selections.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalSelectionTyping(self, additionalSelectionTyping) -> None:
        """ Set whether typing can be performed into multiple selections.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAnchor(self, anchor) -> None:
        """ Set the selection anchor to a position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAutomaticFold(self, automaticFold) -> None:
        """ Set automatic folding behaviours.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetBackSpaceUnIndents(self, bsUnIndents) -> None:
        """ Sets whether a backspace pressed when caret is within indentation unindents.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetBufferedDraw(self, buffered) -> None:
        """ If drawing is buffered then each line of text is drawn into a bitmap buffer before drawing it to the screen to avoid flicker.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretForeground(self, fore) -> None:
        """ Set the foreground colour of the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretLineBackAlpha(self, alpha) -> None:
        """ Set background alpha of the caret line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretLineBackground(self, back) -> None:
        """ Set the colour of the background of the line containing the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretLineVisible(self, show) -> None:
        """ Display the background of the line containing the caret in a different colour.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretLineVisibleAlways(self, alwaysVisible) -> None:
        """ Sets the caret line to always visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretPeriod(self, periodMilliseconds) -> None:
        """ Get the time in milliseconds that the caret is on and off.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretSticky(self, useCaretStickyBehaviour) -> None:
        """ Stop the caret preferred x position changing when the user types.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretStyle(self, caretStyle) -> None:
        """ Set the style of the caret to be drawn.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretWidth(self, pixelWidth) -> None:
        """ Set the width of the insert mode caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCharsDefault(self) -> None:
        """ Reset the set of characters for whitespace and word characters to the defaults.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCodePage(self, codePage) -> None:
        """ Set the code page used to interpret the bytes of the document as characters.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetControlCharSymbol(self, symbol) -> None:
        """ Change the way control characters are displayed: If symbol is < 32, keep the drawn way, else, use the given character.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCurrentPos(self, caret) -> None:
        """ Sets the position of the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetDefaultStyle(self, style) -> None:
        """ This method is inherited from TextAreaBase but is not implemented in   wx.stc.StyledTextCtrl.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetDocPointer(self, docPointer) -> None:
        """ Change the document object used.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEOLMode(self, eolMode) -> None:
        """ Set the current end of line mode.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEdgeColour(self, edgeColour) -> None:
        """ Change the colour used in edge indication.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEdgeColumn(self, column) -> None:
        """ Set the column number of the edge.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEdgeMode(self, edgeMode) -> None:
        """ The edge may be displayed by a line (wxSTC_EDGE_LINE/wxSTC_EDGE_MULTILINE) or by highlighting text that goes beyond it (wx``wx.stc.STC_EDGE_BACKGROUND``) or not displayed at all (wx``wx.stc.STC_EDGE_NONE``).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEditable(self, editable) -> None:
        """ Makes the text item editable or read-only, overriding the wx.TE_READONLY  flag.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEmptySelection(self, caret) -> None:
        """ Set caret to a position, while removing any existing selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEndAtLastLine(self, endAtLastLine) -> None:
        """ Sets the scroll range so that maximum scroll position has the last line at the bottom of the view (default).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetExtraAscent(self, extraAscent) -> None:
        """ Set extra ascent for each line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetExtraDescent(self, extraDescent) -> None:
        """ Set extra descent for each line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFirstVisibleLine(self, displayLine) -> None:
        """ Scroll so that a display line is at the top of the display.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldExpanded(self, line, expanded) -> None:
        """ Show the children of a header line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldFlags(self, flags) -> None:
        """ Set some style options for folding.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldLevel(self, line, level) -> None:
        """ Set the fold level of a line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldMarginColour(self, useSetting, back) -> None:
        """ Set one of the colours used as a chequerboard pattern in the fold margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldMarginHiColour(self, useSetting, fore) -> None:
        """ Set the other colour used as a chequerboard pattern in the fold margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFontQuality(self, fontQuality) -> None:
        """ Choose the quality level for text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHScrollBar(self, bar) -> None:
        """ Set the horizontal scrollbar to use instead of the one thatâs built-in.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHighlightGuide(self, column) -> None:
        """ Set the highlighted indentation guide column.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHint(self, hint) -> None:
        """ Sets a hint shown in an empty unfocused text control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHotspotActiveBackground(self, useSetting, back) -> None:
        """ Set a back colour for active hotspots.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHotspotActiveForeground(self, useSetting, fore) -> None:
        """ Set a fore colour for active hotspots.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHotspotActiveUnderline(self, underline) -> None:
        """ Enable / Disable underlining active hotspots.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHotspotSingleLine(self, singleLine) -> None:
        """ Limit hotspots to single line so hotspots on two lines donât merge.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIMEInteraction(self, imeInteraction) -> None:
        """ Choose to display the IME in a winow or inline.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIdentifier(self, identifier) -> None:
        """ Set the identifier reported as idFrom in notification messages.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIdentifiers(self, style, identifiers) -> None:
        """ Set the identifiers that are shown in a particular style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIdleStyling(self, idleStyling) -> None:
        """ Sets limits to idle styling.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIndent(self, indentSize) -> None:
        """ Set the number of spaces used for one level of indentation.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIndentationGuides(self, indentView) -> None:
        """ Show or hide indentation guides.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIndicatorCurrent(self, indicator) -> None:
        """ Set the indicator used for IndicatorFillRange and IndicatorClearRange.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIndicatorValue(self, value) -> None:
        """ Set the value used for IndicatorFillRange.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetInsertionPoint(self, pos) -> None:
        """ Sets the insertion point at the given position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetInsertionPointEnd(self) -> None:
        """ Sets the insertion point at the end of the text control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetKeyWords(self, keyWordSet, keyWords) -> None:
        """ Set up the key words used by the lexer.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLastKeydownProcessed(self, val) -> None:
        """ Returns the line number of the line with the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLayoutCache(self, cacheMode) -> None:
        """ Sets the degree of caching of layout information.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLexer(self, lexer) -> None:
        """ Set the lexing language of the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLexerLanguage(self, language) -> None:
        """ Set the lexing language of the document based on string name.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLineEndTypesAllowed(self, lineEndBitSet) -> None:
        """ Set the line end types that the application wants to use.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLineIndentation(self, line, indentation) -> None:
        """ Change the indentation of a line to a number of columns.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLineState(self, line, state) -> None:
        """ Used to hold extra styling information for each line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMainSelection(self, selection) -> None:
        """ Set the main selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginBackground(self, margin, back) -> None:
        """ Set the background colour of a margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginCount(self, margins) -> None:
        """ Allocate a non-standard number of margins.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginCursor(self, margin, cursor) -> None:
        """ Set the cursor shown when the mouse is inside a margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginLeft(self, pixelWidth) -> None:
        """ Sets the size in pixels of the left margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginMask(self, margin, mask) -> None:
        """ Set a mask that determines which markers are displayed in a margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginOptions(self, marginOptions) -> None:
        """ Set the margin options.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginRight(self, pixelWidth) -> None:
        """ Sets the size in pixels of the right margin.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginSensitive(self, margin, sensitive) -> None:
        """ Make a margin sensitive or insensitive to mouse clicks.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginType(self, margin, marginType) -> None:
        """ Set a margin to be either numeric or symbolic.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginWidth(self, margin, pixelWidth) -> None:
        """ Set the width of a margin to a width expressed in pixels.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMargins(self, left, right) -> None:
        """ Set the left and right margin in the edit area, measured in pixels.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMaxLength(self, len) -> None:
        """ This function sets the maximum number of characters the user can enter into the control.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetModEventMask(self, eventMask) -> None:
        """ Set which document modification events are sent to the container.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetModified(self, modified) -> None:
        """ Marks the control as being modified by the user or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMouseDownCaptures(self, captures) -> None:
        """ Set whether the mouse is captured when its button is pressed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMouseDwellTime(self, periodMilliseconds) -> None:
        """ Sets the time the mouse must sit still to generate a mouse dwell event.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMouseSelectionRectangularSwitch(self, mouseSelectionRectangularSwitch) -> None:
        """ Set whether switching to rectangular mode while selecting with the mouse is allowed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMouseWheelCaptures(self, captures) -> None:
        """ Set whether the mouse wheel can be active outside the window.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMultiPaste(self, multiPaste) -> None:
        """ Change the effect of pasting when there are multiple selections.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMultipleSelection(self, multipleSelection) -> None:
        """ Set whether multiple selections can be made.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetOvertype(self, overType) -> None:
        """ Set to overtype (True) or insert mode.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPasteConvertEndings(self, convert) -> None:
        """ Enable/Disable convert-on-paste for line endings.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPhasesDraw(self, phases) -> None:
        """ In one phase draw, text is drawn in a series of rectangular blocks with no overlap.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPositionCacheSize(self, size) -> None:
        """ Set number of entries in position cache.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPrintColourMode(self, mode) -> None:
        """ Modify colours when printing for clearer printed text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPrintMagnification(self, magnification) -> None:
        """ Sets the print magnification added to the point size of each style for printing.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPrintWrapMode(self, wrapMode) -> None:
        """ Set printing to line wrapped (wx``wx.stc.STC_WRAP_WORD``) or not line wrapped (wx``wx.stc.STC_WRAP_NONE``).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetProperty(self, key, value) -> None:
        """ Set up a value that may be used by a lexer for some optional feature.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPunctuationChars(self, characters) -> None:
        """ Set the set of characters making up punctuation characters Should be called after SetWordChars.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetReadOnly(self, readOnly) -> None:
        """ Set to read only or read write.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionAnchor(self, anchor) -> None:
        """ Set the anchor position of the rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionAnchorVirtualSpace(self, space) -> None:
        """ Set the virtual space of the anchor of the rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionCaret(self, caret) -> None:
        """ Set the caret position of the rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionCaretVirtualSpace(self, space) -> None:
        """ Set the virtual space of the caret of the rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionModifier(self, modifier) -> None:
        """ On GTK+, allow selecting the modifier key to use for mouse-based rectangular selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRepresentation(self, encodedCharacter, representation) -> None:
        """ Set the way a character is drawn.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSTCCursor(self, cursorType) -> None:
        """ Sets the cursor to one of the STC_CURSOR values.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSTCFocus(self, focus) -> None:
        """ Change internal focus flag.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSavePoint(self) -> None:
        """ Remember the current position in the undo history as the position at which the document was saved.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetScrollWidth(self, pixelWidth) -> None:
        """ Sets the document width assumed for scrolling.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetScrollWidthTracking(self, tracking) -> None:
        """ Sets whether the maximum width line displayed is used to set scroll width.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSearchFlags(self, searchFlags) -> None:
        """ Set the search flags used by SearchInTarget.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelAlpha(self, alpha) -> None:
        """ Set the alpha of the selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelBackground(self, useSetting, back) -> None:
        """ Set the background colour of the main and additional selections and whether to use this setting.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelEOLFilled(self, filled) -> None:
        """ Set the selection to have its end of line filled or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelForeground(self, useSetting, fore) -> None:
        """ Set the foreground colour of the main and additional selections and whether to use this setting.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelection(self, from_, to_) -> None:
        """ Selects the text starting at the first position up to (but not including) the character at the last position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionEnd(self, caret) -> None:
        """ Sets the position that ends the selection - this becomes the caret.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionMode(self, selectionMode) -> None:
        """ Set the selection mode to stream (wx``wx.stc.STC_SEL_STREAM``) or rectangular (wxSTC_SEL_RECTANGLE/wxSTC_SEL_THIN) or by lines (wx``wx.stc.STC_SEL_LINES``).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNAnchor(self, selection, anchor) -> None:
        """ Set the anchor position of the nth selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNAnchorVirtualSpace(self, selection, space) -> None:
        """ Set the virtual space of the anchor of the nth selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNCaret(self, selection, caret) -> None:
        """ Set the caret position of the nth selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNCaretVirtualSpace(self, selection, space) -> None:
        """ Set the virtual space of the caret of the nth selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNEnd(self, selection, caret) -> None:
        """ Sets the position that ends the selection - this becomes the currentPosition.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNStart(self, selection, anchor) -> None:
        """ Sets the position that starts the selection - this becomes the anchor.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionStart(self, anchor) -> None:
        """ Sets the position that starts the selection - this becomes the anchor.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStatus(self, status) -> None:
        """ Change error status - 0 = wx.OK.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStyle(self, start, end, style) -> None:
        """ This method is inherited from TextAreaBase but is not implemented in   wx.stc.StyledTextCtrl.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStyleBits(self, bits) -> None:
        """ Divide each styling byte into lexical class bits (default: 5) and indicator bits (default: 3).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStyleBytes(self, length, styleBytes) -> None:
        """ Set the styles for a segment of the document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStyling(self, length, style) -> None:
        """ Change style from current styling position for length characters to a style and move the current styling position to after this newly styled segment.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTabDrawMode(self, tabDrawMode) -> None:
        """ Set how tabs are drawn when visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTabIndents(self, tabIndents) -> None:
        """ Sets whether a tab pressed when caret is within indentation indents.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTabWidth(self, tabWidth) -> None:
        """ Change the visible size of a tab to be a multiple of the width of a space character.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTargetEnd(self, end) -> None:
        """ Sets the position that ends the target which is used for updating the document without affecting the scroll position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTargetRange(self, start, end) -> None:
        """ Sets both the start and end of the target in one call.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTargetStart(self, start) -> None:
        """ Sets the position that starts the target which is used for updating the document without affecting the scroll position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTechnology(self, technology) -> None:
        """ Set the technology used.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetText(self, text) -> None:
        """ Replace the contents of the document with the argument text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTextRaw(self, text) -> None:
        """ Replace the contents of the document with the argument text.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTwoPhaseDraw(self, twoPhase) -> None:
        """ In twoPhaseDraw mode, drawing is performed in two phases, first the background and then the foreground.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUndoCollection(self, collectUndo) -> None:
        """ Choose between collecting actions into the undo history and discarding them.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUseAntiAliasing(self, useAA) -> None:
        """ Specify whether anti-aliased fonts should be used.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUseHorizontalScrollBar(self, visible) -> None:
        """ Show or hide the horizontal scroll bar.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUseTabs(self, useTabs) -> None:
        """ Indentation will only use space characters if useTabs is False, otherwise it will use a combination of tabs and spaces.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUseVerticalScrollBar(self, visible) -> None:
        """ Show or hide the vertical scroll bar.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetVScrollBar(self, bar) -> None:
        """ Set the vertical scrollbar to use instead of the one thatâs built-in.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetValue(self, value) -> None:
        """ Sets the new text control value.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetViewEOL(self, visible) -> None:
        """ Make the end of line characters visible or invisible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetViewWhiteSpace(self, viewWS) -> None:
        """ Make white space characters invisible, always visible or visible outside indentation.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetVirtualSpaceOptions(self, virtualSpaceOptions) -> None:
        """ Set options for virtual space behaviour.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetVisiblePolicy(self, visiblePolicy, visibleSlop) -> None:
        """ Set the way the display area is determined when a particular line is to be moved to by Find, FindNext, GotoLine, etc.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWhitespaceBackground(self, useSetting, back) -> None:
        """ Set the background colour of all whitespace and whether to use this setting.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWhitespaceChars(self, characters) -> None:
        """ Set the set of characters making up whitespace for when moving or selecting by word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWhitespaceForeground(self, useSetting, fore) -> None:
        """ Set the foreground colour of all whitespace and whether to use this setting.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWhitespaceSize(self, size) -> None:
        """ Set the size of the dots used to mark space characters.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWordChars(self, characters) -> None:
        """ Set the set of characters making up words for when moving or selecting by word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapIndentMode(self, wrapIndentMode) -> None:
        """ Sets how wrapped sublines are placed.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapMode(self, wrapMode) -> None:
        """ Sets whether text is word wrapped.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapStartIndent(self, indent) -> None:
        """ Set the start indent for wrapped lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapVisualFlags(self, wrapVisualFlags) -> None:
        """ Set the display mode of visual flags for wrapped lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapVisualFlagsLocation(self, wrapVisualFlagsLocation) -> None:
        """ Set the location of visual flags for wrapped lines.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetXCaretPolicy(self, caretPolicy, caretSlop) -> None:
        """ Set the way the caret is kept visible when going sideways.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetXOffset(self, xOffset) -> None:
        """ Set the xOffset (ie, horizontal scroll position).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetYCaretPolicy(self, caretPolicy, caretSlop) -> None:
        """ Set the way the line the caret is on is kept visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetZoom(self, zoomInPoints) -> None:
        """ Set the zoom level.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ShowLines(self, lineStart, lineEnd) -> None:
        """ Make a range of lines visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ShowPosition(self, pos) -> None:
        """ Makes the line containing the given position visible.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StartRecord(self) -> None:
        """ Start notifying the container of all key presses and commands.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StartStyling(self, start) -> None:
        """ Set the current styling position to start.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StopRecord(self) -> None:
        """ Stop notifying the container of all key presses and commands.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StutteredPageDown(self) -> None:
        """ Move caret to bottom of page, or one page down if already at bottom of page.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StutteredPageDownExtend(self) -> None:
        """ Move caret to bottom of page, or one page down if already at bottom of page, extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StutteredPageUp(self) -> None:
        """ Move caret to top of page, or one page up if already at top of page.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StutteredPageUpExtend(self) -> None:
        """ Move caret to top of page, or one page up if already at top of page, extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleClearAll(self) -> None:
        """ Clear all the styles and make equivalent to the global default style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetBackground(self, style) -> None:
        """ Get the background colour of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetBold(self, style) -> None:
        """ Get is a style bold or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetCase(self, style) -> None:
        """ Get is a style mixed case, or to force upper or lower case.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetChangeable(self, style) -> None:
        """ Get is a style changeable or not (read only).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetCharacterSet(self, style) -> None:
        """ Get the character get of the font in a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetEOLFilled(self, style) -> None:
        """ Get is a style to have its end of line filled or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetFaceName(self, style) -> None:
        """ Get the font facename of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetFont(self, style) -> None:
        """ Get the font of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetForeground(self, style) -> None:
        """ Get the foreground colour of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetHotSpot(self, style) -> None:
        """ Get is a style a hotspot or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetItalic(self, style) -> None:
        """ Get is a style italic or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetSize(self, style) -> None:
        """ Get the size of characters of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetSizeFractional(self, style) -> None:
        """ Get the size of characters of a style in points multiplied by 100.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetUnderline(self, style) -> None:
        """ Get is a style underlined or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetVisible(self, style) -> None:
        """ Get is a style visible or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetWeight(self, style) -> None:
        """ Get the weight of characters of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleResetDefault(self) -> None:
        """ Reset the default style to its state at startup.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetBackground(self, style, back) -> None:
        """ Set the background colour of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetBold(self, style, bold) -> None:
        """ Set a style to be bold or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetCase(self, style, caseVisible) -> None:
        """ Set a style to be mixed case, or to force upper or lower case.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetChangeable(self, style, changeable) -> None:
        """ Set a style to be changeable or not (read only).

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetCharacterSet(self, style, characterSet) -> None:
        """ Set the character set of the font in a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetEOLFilled(self, style, eolFilled) -> None:
        """ Set a style to have its end of line filled or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetFaceName(self, style, fontName) -> None:
        """ Set the font of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetFont(self, styleNum, font) -> None:
        """ Set style size, face, bold, italic, and underline attributes from a   wx.Fontâs attributes.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetFontAttr(self, styleNum, size, faceName, bold, italic, underline, encoding=FONTENCODING_DEFAULT) -> None:
        """ Set all font style attributes at once.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetFontEncoding(self, style, encoding) -> None:
        """ Set the font encoding to be used by a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetForeground(self, style, fore) -> None:
        """ Set the foreground colour of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetHotSpot(self, style, hotspot) -> None:
        """ Set a style to be a hotspot or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetItalic(self, style, italic) -> None:
        """ Set a style to be italic or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetSize(self, style, sizePoints) -> None:
        """ Set the size of characters of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetSizeFractional(self, style, sizeHundredthPoints) -> None:
        """ Set the size of characters of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetSpec(self, styleNum, spec) -> None:
        """ Extract style settings from a spec-string which is composed of one or more of the following comma separated elements:

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetUnderline(self, style, underline) -> None:
        """ Set a style to be underlined or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetVisible(self, style, visible) -> None:
        """ Set a style to be visible or not.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetWeight(self, style, weight) -> None:
        """ Set the weight of characters of a style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SwapMainAnchorCaret(self) -> None:
        """ Swap that caret and anchor of the main selection.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Tab(self) -> None:
        """ If selection is empty or all on one line replace the selection with a tab character.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def TargetFromSelection(self) -> None:
        """ Make the target range start and end be the same as the selection range start and end.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def TargetWholeDocument(self) -> None:
        """ Sets the target to the whole document.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def TextHeight(self, line) -> None:
        """ Retrieve the height of a particular line of text in pixels.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def TextWidth(self, style, text) -> None:
        """ Measure the pixel width of some text in a particular style.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ToggleCaretSticky(self) -> None:
        """ Switch between sticky and non-sticky: meant to be bound to a key.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ToggleFold(self, line) -> None:
        """ Switch a header line between expanded and contracted.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ToggleFoldShowText(self, line, text) -> None:
        """ Switch a header line between expanded and contracted and show some text after the line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Undo(self) -> None:
        """ Undo one action in the undo history.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def UpperCase(self) -> None:
        """ Transform the selection to upper case.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def UsePopUp(self, popUpMode) -> None:
        """ Set whether a pop up menu is displayed automatically when the user presses the wrong mouse button on certain areas.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def UserListShow(self, listType, itemList) -> None:
        """ Display a list of strings and send notification when user chooses one.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHome(self) -> None:
        """ Move caret to before first visible character on line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeDisplay(self) -> None:
        """ Move caret to before first visible character on display line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeDisplayExtend(self) -> None:
        """ Like VCHomeDisplay but extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeExtend(self) -> None:
        """ Like VCHome but extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeRectExtend(self) -> None:
        """ Move caret to before first visible character on line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeWrap(self) -> None:
        """ Like VCHome but when word-wrap is enabled goes first to start of display line VCHomeDisplay, then behaves like VCHome.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeWrapExtend(self) -> None:
        """ Like VCHomeExtend but when word-wrap is enabled extends first to start of display line VCHomeDisplayExtend, then behaves like VCHomeExtend.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VerticalCentreCaret(self) -> None:
        """ Centre current line in window.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VisibleFromDocLine(self, docLine) -> None:
        """ Find the display line of a document line taking hidden lines into account.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordEndPosition(self, pos, onlyWordCharacters) -> None:
        """ Get position of end of word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordLeft(self) -> None:
        """ Move caret left one word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordLeftEnd(self) -> None:
        """ Move caret left one word, position cursor at end of word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordLeftEndExtend(self) -> None:
        """ Move caret left one word, position cursor at end of word, extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordLeftExtend(self) -> None:
        """ Move caret left one word extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordPartLeft(self) -> None:
        """ Move to the previous change in capitalisation.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordPartLeftExtend(self) -> None:
        """ Move to the previous change in capitalisation extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordPartRight(self) -> None:
        """ Move to the change next in capitalisation.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordPartRightExtend(self) -> None:
        """ Move to the next change in capitalisation extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordRight(self) -> None:
        """ Move caret right one word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordRightEnd(self) -> None:
        """ Move caret right one word, position cursor at end of word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordRightEndExtend(self) -> None:
        """ Move caret right one word, position cursor at end of word, extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordRightExtend(self) -> None:
        """ Move caret right one word extending selection to new caret position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordStartPosition(self, pos, onlyWordCharacters) -> None:
        """ Get position of start of word.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WrapCount(self, docLine) -> None:
        """ The number of display lines needed to wrap a document line.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WriteText(self, text) -> None:
        """ Writes the text into the text control at the current insertion position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def XYToPosition(self, x, y) -> None:
        """ Converts the given zero based column and line number to a position.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ZoomIn(self) -> None:
        """ Magnify the displayed text by increasing the sizes by 1 point.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ZoomOut(self) -> None:
        """ Make the displayed text smaller by decreasing the sizes by 1 point.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def flush(self) -> None:
        """ NOP, for file-like compatibility.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def write(self, text) -> None:
        """ Append text to the textctrl, for file-like compatibility.

            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    AdditionalCaretForeground: None  # See GetAdditionalCaretForeground and SetAdditionalCaretForeground
    AdditionalCaretsBlink: None  # See GetAdditionalCaretsBlink and SetAdditionalCaretsBlink
    AdditionalCaretsVisible: None  # See GetAdditionalCaretsVisible and SetAdditionalCaretsVisible
    AdditionalSelAlpha: None  # See GetAdditionalSelAlpha and SetAdditionalSelAlpha
    AdditionalSelectionTyping: None  # See GetAdditionalSelectionTyping and SetAdditionalSelectionTyping
    AllLinesVisible: None  # See GetAllLinesVisible
    Anchor: None  # See GetAnchor and SetAnchor
    AutomaticFold: None  # See GetAutomaticFold and SetAutomaticFold
    BackSpaceUnIndents: None  # See GetBackSpaceUnIndents and SetBackSpaceUnIndents
    BufferedDraw: None  # See GetBufferedDraw and SetBufferedDraw
    CaretForeground: None  # See GetCaretForeground and SetCaretForeground
    CaretLineBackAlpha: None  # See GetCaretLineBackAlpha and SetCaretLineBackAlpha
    CaretLineBackground: None  # See GetCaretLineBackground and SetCaretLineBackground
    CaretLineVisible: None  # See GetCaretLineVisible and SetCaretLineVisible
    CaretLineVisibleAlways: None  # See GetCaretLineVisibleAlways and SetCaretLineVisibleAlways
    CaretPeriod: None  # See GetCaretPeriod and SetCaretPeriod
    CaretSticky: None  # See GetCaretSticky and SetCaretSticky
    CaretStyle: None  # See GetCaretStyle and SetCaretStyle
    CaretWidth: None  # See GetCaretWidth and SetCaretWidth
    CharacterPointer: None  # See GetCharacterPointer
    CodePage: None  # See GetCodePage and SetCodePage
    ControlCharSymbol: None  # See GetControlCharSymbol and SetControlCharSymbol
    CurLine: None  # See GetCurLine
    CurLineRaw: None  # See GetCurLineRaw
    CurrentLine: None  # See GetCurrentLine
    CurrentPos: None  # See GetCurrentPos and SetCurrentPos
    DefaultStyle: None  # See GetDefaultStyle and SetDefaultStyle
    DirectFunction: None  # See GetDirectFunction
    DirectPointer: None  # See GetDirectPointer
    DocPointer: None  # See GetDocPointer and SetDocPointer
    EOLMode: None  # See GetEOLMode and SetEOLMode
    EdgeColour: None  # See GetEdgeColour and SetEdgeColour
    EdgeColumn: None  # See GetEdgeColumn and SetEdgeColumn
    EdgeMode: None  # See GetEdgeMode and SetEdgeMode
    EndAtLastLine: None  # See GetEndAtLastLine and SetEndAtLastLine
    EndStyled: None  # See GetEndStyled
    ExtraAscent: None  # See GetExtraAscent and SetExtraAscent
    ExtraDescent: None  # See GetExtraDescent and SetExtraDescent
    FirstVisibleLine: None  # See GetFirstVisibleLine and SetFirstVisibleLine
    FontQuality: None  # See GetFontQuality and SetFontQuality
    GapPosition: None  # See GetGapPosition
    HighlightGuide: None  # See GetHighlightGuide and SetHighlightGuide
    Hint: None  # See GetHint and SetHint
    HotspotActiveBackground: None  # See GetHotspotActiveBackground
    HotspotActiveForeground: None  # See GetHotspotActiveForeground
    HotspotActiveUnderline: None  # See GetHotspotActiveUnderline and SetHotspotActiveUnderline
    HotspotSingleLine: None  # See GetHotspotSingleLine and SetHotspotSingleLine
    IMEInteraction: None  # See GetIMEInteraction and SetIMEInteraction
    Identifier: None  # See GetIdentifier and SetIdentifier
    IdleStyling: None  # See GetIdleStyling and SetIdleStyling
    Indent: None  # See GetIndent and SetIndent
    IndentationGuides: None  # See GetIndentationGuides and SetIndentationGuides
    IndicatorCurrent: None  # See GetIndicatorCurrent and SetIndicatorCurrent
    IndicatorValue: None  # See GetIndicatorValue and SetIndicatorValue
    InsertionPoint: None  # See GetInsertionPoint and SetInsertionPoint
    LastKeydownProcessed: None  # See GetLastKeydownProcessed and SetLastKeydownProcessed
    LastPosition: None  # See GetLastPosition
    LayoutCache: None  # See GetLayoutCache and SetLayoutCache
    Length: None  # See GetLength
    Lexer: None  # See GetLexer and SetLexer
    LexerLanguage: None  # See GetLexerLanguage and SetLexerLanguage
    LineCount: None  # See GetLineCount
    LineEndTypesActive: None  # See GetLineEndTypesActive
    LineEndTypesAllowed: None  # See GetLineEndTypesAllowed and SetLineEndTypesAllowed
    LineEndTypesSupported: None  # See GetLineEndTypesSupported
    MainSelection: None  # See GetMainSelection and SetMainSelection
    MarginCount: None  # See GetMarginCount and SetMarginCount
    MarginLeft: None  # See GetMarginLeft and SetMarginLeft
    MarginOptions: None  # See GetMarginOptions and SetMarginOptions
    MarginRight: None  # See GetMarginRight and SetMarginRight
    Margins: None  # See GetMargins
    MaxLineState: None  # See GetMaxLineState
    ModEventMask: None  # See GetModEventMask and SetModEventMask
    Modify: None  # See GetModify
    MouseDownCaptures: None  # See GetMouseDownCaptures and SetMouseDownCaptures
    MouseDwellTime: None  # See GetMouseDwellTime and SetMouseDwellTime
    MouseSelectionRectangularSwitch: None  # See GetMouseSelectionRectangularSwitch and SetMouseSelectionRectangularSwitch
    MouseWheelCaptures: None  # See GetMouseWheelCaptures and SetMouseWheelCaptures
    MultiPaste: None  # See GetMultiPaste and SetMultiPaste
    MultipleSelection: None  # See GetMultipleSelection and SetMultipleSelection
    NumberOfLines: None  # See GetNumberOfLines
    Overtype: None  # See GetOvertype and SetOvertype
    PasteConvertEndings: None  # See GetPasteConvertEndings and SetPasteConvertEndings
    PhasesDraw: None  # See GetPhasesDraw and SetPhasesDraw
    PositionCacheSize: None  # See GetPositionCacheSize and SetPositionCacheSize
    PrintColourMode: None  # See GetPrintColourMode and SetPrintColourMode
    PrintMagnification: None  # See GetPrintMagnification and SetPrintMagnification
    PrintWrapMode: None  # See GetPrintWrapMode and SetPrintWrapMode
    PunctuationChars: None  # See GetPunctuationChars and SetPunctuationChars
    RangePointer: None  # See GetRangePointer
    ReadOnly: None  # See GetReadOnly and SetReadOnly
    RectangularSelectionAnchor: None  # See GetRectangularSelectionAnchor and SetRectangularSelectionAnchor
    RectangularSelectionAnchorVirtualSpace: None  # See GetRectangularSelectionAnchorVirtualSpace and SetRectangularSelectionAnchorVirtualSpace
    RectangularSelectionCaret: None  # See GetRectangularSelectionCaret and SetRectangularSelectionCaret
    RectangularSelectionCaretVirtualSpace: None  # See GetRectangularSelectionCaretVirtualSpace and SetRectangularSelectionCaretVirtualSpace
    RectangularSelectionModifier: None  # See GetRectangularSelectionModifier and SetRectangularSelectionModifier
    STCCursor: None  # See GetSTCCursor and SetSTCCursor
    STCFocus: None  # See GetSTCFocus and SetSTCFocus
    ScrollWidth: None  # See GetScrollWidth and SetScrollWidth
    ScrollWidthTracking: None  # See GetScrollWidthTracking and SetScrollWidthTracking
    SearchFlags: None  # See GetSearchFlags and SetSearchFlags
    SelAlpha: None  # See GetSelAlpha and SetSelAlpha
    SelEOLFilled: None  # See GetSelEOLFilled and SetSelEOLFilled
    SelectedText: None  # See GetSelectedText
    SelectedTextRaw: None  # See GetSelectedTextRaw
    SelectionEmpty: None  # See GetSelectionEmpty
    SelectionEnd: None  # See GetSelectionEnd and SetSelectionEnd
    SelectionMode: None  # See GetSelectionMode and SetSelectionMode
    SelectionStart: None  # See GetSelectionStart and SetSelectionStart
    Selections: None  # See GetSelections
    Status: None  # See GetStatus and SetStatus
    StringSelection: None  # See GetStringSelection
    StyleBits: None  # See GetStyleBits and SetStyleBits
    StyleBitsNeeded: None  # See GetStyleBitsNeeded
    SubStyleBases: None  # See GetSubStyleBases
    TabDrawMode: None  # See GetTabDrawMode and SetTabDrawMode
    TabIndents: None  # See GetTabIndents and SetTabIndents
    TabWidth: None  # See GetTabWidth and SetTabWidth
    TargetEnd: None  # See GetTargetEnd and SetTargetEnd
    TargetStart: None  # See GetTargetStart and SetTargetStart
    TargetText: None  # See GetTargetText
    TargetTextRaw: None  # See GetTargetTextRaw
    Technology: None  # See GetTechnology and SetTechnology
    Text: None  # See GetText and SetText
    TextLength: None  # See GetTextLength
    TextRaw: None  # See GetTextRaw and SetTextRaw
    TwoPhaseDraw: None  # See GetTwoPhaseDraw and SetTwoPhaseDraw
    UndoCollection: None  # See GetUndoCollection and SetUndoCollection
    UseAntiAliasing: None  # See GetUseAntiAliasing and SetUseAntiAliasing
    UseHorizontalScrollBar: None  # See GetUseHorizontalScrollBar and SetUseHorizontalScrollBar
    UseTabs: None  # See GetUseTabs and SetUseTabs
    UseVerticalScrollBar: None  # See GetUseVerticalScrollBar and SetUseVerticalScrollBar
    Value: None  # See GetValue and SetValue
    ViewEOL: None  # See GetViewEOL and SetViewEOL
    ViewWhiteSpace: None  # See GetViewWhiteSpace and SetViewWhiteSpace
    VirtualSpaceOptions: None  # See GetVirtualSpaceOptions and SetVirtualSpaceOptions
    WhitespaceChars: None  # See GetWhitespaceChars and SetWhitespaceChars
    WhitespaceSize: None  # See GetWhitespaceSize and SetWhitespaceSize
    WordChars: None  # See GetWordChars and SetWordChars
    WrapIndentMode: None  # See GetWrapIndentMode and SetWrapIndentMode
    WrapMode: None  # See GetWrapMode and SetWrapMode
    WrapStartIndent: None  # See GetWrapStartIndent and SetWrapStartIndent
    WrapVisualFlags: None  # See GetWrapVisualFlags and SetWrapVisualFlags
    WrapVisualFlagsLocation: None  # See GetWrapVisualFlagsLocation and SetWrapVisualFlagsLocation
    XOffset: None  # See GetXOffset and SetXOffset
    Zoom: None  # See GetZoom and SetZoom



STC_MOD_INSERTCHECK: int

OK: int

STC_INVALID_POSITION: int

STC_EOL_CRLF: int

STC_EOL_CR: int

STC_EOL_LF: int

STC_STYLE_CALLTIP: int

TE_READONLY: int

STC_UNDO_MAY_COALESCE: int

STC_MODEVENTMASKALL: int

STC_STARTACTION: int

STC_MULTILINEUNDOREDO: int

STC_MULTISTEPUNDOREDO: int

STC_LASTSTEPINUNDOREDO: int

STC_TIME_FOREVER: int

STC_WRAPINDENT_FIXED: int

STC_TECHNOLOGY_DIRECTWRITE: int

STC_MARGIN_COLOUR: int

STC_KEYMOD_CTRL: int

STC_KEYMOD_ALT: int

STC_KEYMOD_SUPER: int

STC_TECHNOLOGY_DEFAULT: int

STC_POPUP_NEVER: int

CharBuffer: TypeAlias = Any

