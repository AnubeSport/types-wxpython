# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

from .. import Object

class XmlResource(Object):
    """ This is the main class for interacting with the XML-based resource
system.

        Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def AddHandler(self, handler) -> None:
        """ Initializes only a specific handler (or custom handler).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def AddSubclassFactory(factory) -> None:
        """ Registers subclasses factory for use in XRC.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def AttachUnknownControl(self, name, control, parent=None) -> None:
        """ Attaches an unknown control to the given panel/window/dialog.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def ClearHandlers(self) -> None:
        """ Removes all handlers and deletes them (this means that any handlers added using AddHandler   must be allocated on the heap).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def CompareVersion(self, major, minor, release, revision) -> None:
        """ Compares the XRC version to the argument.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def FindXRCIDById(numId) -> None:
        """ Returns a string ID corresponding to the given numeric ID.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def Get() -> None:
        """ Gets the global resources object or creates one if none exists.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetDomain(self) -> None:
        """ Returns the domain (message catalog) that will be used to load translatable strings in the XRC.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetFlags(self) -> None:
        """ Returns flags, which may be a bitlist of   wx.xrc.XmlResourceFlags  enumeration values.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetResourceNode(self, name) -> None:
        """ Returns the   wx.xml.XmlNode  containing the definition of the object with the given name or None.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetVersion(self) -> None:
        """ Returns version information (a.b.c.d = d + 256c + 2562b + 2563a).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def GetXRCID(str_id, value_if_not_found=ID_NONE) -> None:
        """ Returns a numeric ID that is equivalent to the string ID used in an XML resource.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def InitAllHandlers(self) -> None:
        """ Initializes handlers for all supported controls/windows.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def InsertHandler(self, handler) -> None:
        """ Add a new handler at the beginning of the handler list.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def Load(self, filemask) -> None:
        """ Loads resources from XML files that match given filemask.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadAllFiles(self, dirname) -> None:
        """ Loads all .xrc files from directory dirname.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadBitmap(self, name) -> None:
        """ Loads a bitmap resource from a file.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadDialog(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadDocument(self, doc, name='') -> None:
        """ Load resources from the XML document containing them.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadFile(self, file) -> None:
        """ Simpler form of Load   for loading a single XRC file.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadFrame(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadFromBuffer(self, data) -> None:
        """ Load the resource from a bytes string or other data buffer compatible object.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadIcon(self, name) -> None:
        """ Loads an icon resource from a file.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadMenu(self, name) -> None:
        """ Loads menu from resource.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadMenuBar(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadObject(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadObjectRecursively(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadPanel(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadToolBar(self, parent, name) -> None:
        """ Loads a toolbar.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def Set(res) -> None:
        """ Sets the global resources object and returns a pointer to the previous one (may be None).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def SetDomain(self, domain) -> None:
        """ Sets the domain (message catalog) that will be used to load translatable strings in the XRC.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def SetFlags(self, flags) -> None:
        """ Sets flags (bitlist of   wx.xrc.XmlResourceFlags  enumeration values).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def Unload(self, filename) -> None:
        """ This function unloads a resource previously loaded by Load .

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    Domain: None  # See GetDomain and SetDomain
    Flags: None  # See GetFlags and SetFlags
    Version: None  # See GetVersion



class XmlResourceHandler(Object):
    """ SizerXmlHandler is a class for resource handlers capable of creating
a Sizer object from an XML node.

        Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def AddStyle(self, name, value) -> None:
        """ Add a style flag (e.g.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def AddWindowStyles(self) -> None:
        """ Add styles common to all Window-derived classes.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CanHandle(self, node) -> None:
        """ Returns True if it understands this node and can create a resource from it, False otherwise.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateChildren(self, parent, this_hnd_only=False) -> None:
        """ Creates children.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateChildrenPrivately(self, parent, rootnode=None) -> None:
        """ Helper function.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateResFromNode(self, node, parent, instance=None) -> None:
        """ Creates a resource from a node.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateResource(self, node, parent, instance) -> None:
        """ Creates an object (menu, dialog, control, â¦) from an XML node.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def DoCreateResource(self) -> None:
        """ Called from CreateResource after variables were filled.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetAnimation(self, param='animation', ctrl=None) -> None:
        """ Creates an animation (see   wx.adv.Animation) from the filename specified in param.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetBitmap(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetBitmapBundle(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetBool(self, param, defaultv=False) -> None:
        """ Gets a bool flag (1, t, yes, on, True are True, everything else is False).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetClass(self) -> None:
        """ After CreateResource has been called this will return the class name of the XML resource node being processed.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetColour(self, param, defaultColour=NullColour) -> None:
        """ Gets colour in HTML syntax (#``RRGGBB``).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetCurFileSystem(self) -> None:
        """ Returns the current file system.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetDimension(self, param, defaultv=0, windowToUse=0) -> None:
        """ Gets a dimension (may be in dialog units).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetDirection(self, param, dirDefault=LEFT) -> None:
        """ Gets a direction.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetFloat(self, param, defaultv=0) -> None:
        """ Gets a float value from the parameter.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetFont(self, param='font') -> None:
        """ Gets a font.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetID(self) -> None:
        """ Returns the wx.xrc.XRCID.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetIcon(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetIconBundle(self, param, defaultArtClient=ART_OTHER) -> None:
        """ Returns an icon bundle.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetImageList(self, param='imagelist') -> None:
        """ Creates an image list from the param  markup data.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetInstance(self) -> None:
        """ After CreateResource has been called this will return the instance that the XML resource content should be created upon, if it has already been created.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetLong(self, param, defaultv=0) -> None:
        """ Gets the integer value from the parameter.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetName(self) -> None:
        """ Returns the resource name.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNode(self) -> None:
        """ After CreateResource has been called this will return the XML node being processed.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeChildren(self, node) -> None:
        """ Gets the first child of the given node or None.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeContent(self, node) -> None:
        """ Gets node content from wx.xml.XML_ENTITY_NODE.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeNext(self, node) -> None:
        """ Gets the next sibling node related to the given node, possibly None.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeParent(self, node) -> None:
        """ Gets the parent of the node given.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParamNode(self, param) -> None:
        """ Finds the node or returns None.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParamValue(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParent(self) -> None:
        """ After CreateResource has been called this will return the current itemâs parent, if any.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParentAsWindow(self) -> None:
        """ After CreateResource has been called this will return the itemâs parent as a   wx.Window.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetPosition(self, param='pos') -> None:
        """ Gets the position (may be in dialog units).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetResource(self) -> None:
        """ After CreateResource has been called this will return the current   wx.xrc.XmlResource  object.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetSize(self, param='size', windowToUse=0) -> None:
        """ Gets the size (may be in dialog units).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetStyle(self, param='style', defaults=0) -> None:
        """ Gets style flags from text in form âflag | flag2| flag3 |â¦â Only understands flags added with AddStyle .

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetText(self, param, translate=True) -> None:
        """ Gets text from param and does some conversions:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def HasParam(self, param) -> None:
        """ Check to see if a parameter exists.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def IsObjectNode(self, node) -> None:
        """ Checks if the given node is an object node.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def IsOfClass(self, node, classname) -> None:
        """ Convenience function.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def ReportError(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def ReportParamError(self, param, message) -> None:
        """ Like ReportError , but uses the node of parameter param  of the currently processed object as the context.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def SetParentResource(self, res) -> None:
        """ Sets the parent resource.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def SetupWindow(self, wnd) -> None:
        """ Sets common window options.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    Animation: None  # See GetAnimation
    Bitmap: None  # See GetBitmap
    BitmapBundle: None  # See GetBitmapBundle
    Class: None  # See GetClass
    CurFileSystem: None  # See GetCurFileSystem
    Font: None  # See GetFont
    ID: None  # See GetID
    Icon: None  # See GetIcon
    ImageList: None  # See GetImageList
    Instance: None  # See GetInstance
    Name: None  # See GetName
    Node: None  # See GetNode
    Parent: None  # See GetParent
    ParentAsWindow: None  # See GetParentAsWindow
    Position: None  # See GetPosition
    Resource: None  # See GetResource
    Size: None  # See GetSize
    Style: None  # See GetStyle



XRCID: int

XML_ENTITY_NODE: int

XmlResourceFlags: TypeAlias = int  # Enumeration

XRC_USE_LOCALE: int

XRC_NO_SUBCLASSING: int

XRC_NO_RELOADING: int

XRC_USE_ENVVARS: int

class XmlSubclassFactory:
    """ None

        Source: https://docs.wxpython.org/wx.xrc.XmlSubclassFactory.html
    """
    def __init__(self) -> None:
        """ None

            Source: https://docs.wxpython.org/wx.xrc.XmlSubclassFactory.html
        """

    def Create(self, className) -> None:
        """ className (String)

            Source: https://docs.wxpython.org/wx.xrc.XmlSubclassFactory.html
        """



Animation: TypeAlias = Any

XmlNode: TypeAlias = Any

