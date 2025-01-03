from typing import Any, overload


batch = ...
browser = ...
media_panel = ...
mediahub = ...
messages = ...
project = ...
projects = ...
timeline = ...
users = ...

class PyActionFamilyNode(PyNode):
    """
    Class derived from PyNode. Represents an Action Family node object.
    """
    all_tabs = ...
    attributes = ...
    cursor_position = ...
    input_sockets = ...
    left_tabs = ...
    media_layers = ...
    node_types = ...
    nodes = ...
    output_sockets = ...
    parent = ...
    right_tabs = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_schematic(arg1: PyActionFamilyNode) -> bool:
        """
        Clear the Action/Image/GMaskTracer schematic of all nodes.
        """
        ...

    def connect_nodes(arg1: PyActionFamilyNode, parent_node: PyFlameObject, child_node: PyFlameObject, link_type: str='Default') -> bool:
        """
        Connect two nodes in the Action/Image/GMaskTracer schematic.
        Keyword argument:
        type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def create_node(arg1: PyActionFamilyNode, node_type: str, file_path: str='', is_udim: bool=False, tile_resolution: int=0) -> Any:
        """
        Add an Action/Image/GMaskTracer object node to the Action/Image/GMaskTracer schematic.
        Keyword argument:
        file_path -- Required by nodes that load an asset, such as Matchbox.
        """
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def disconnect_nodes(arg1: PyActionFamilyNode, parent_node: PyFlameObject, child_node: PyFlameObject, link_type: str='Default') -> bool:
        """
        Disconnect two nodes in the Action/Image/GMaskTracer schematic.
        Keyword argument:
        type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def encompass_nodes(arg1: PyActionFamilyNode, node_list: list) -> Any:
        """
        Create a compass including the node list given as argument
        Keyword argument:
        node_list -- a list of nodes (either string or node objects)
        output_type -- the created compass node
        """
        ...

    def get_node(arg1: PyActionFamilyNode, node_name: str) -> Any:
        """
        Get a node by node name. Doesn't select it in the UI.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def organize(arg1: PyActionFamilyNode) -> bool:
        """
        Clean up the Action/Image/GMaskTracer schematic.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyActionNode(PyActionFamilyNode):
    """
    Class derived from PyActionFamilyNode. Represents an Action node object.
    """
    all_tabs = ...
    attributes = ...
    cursor_position = ...
    input_sockets = ...
    left_tabs = ...
    media_layers = ...
    media_nodes = ...
    node_types = ...
    nodes = ...
    output_sockets = ...
    output_types = ...
    parent = ...
    right_tabs = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def add_media(arg1: PyActionFamilyNode) -> Any:
        """
        Add a Media layer to the Batch Action node.
        Also instantiates a matching Surface node (and Axis) in the Action node schematic.
        """
        ...

    def clear_schematic(arg1: PyActionFamilyNode) -> bool:
        """
        Clear the Action/Image/GMaskTracer schematic of all nodes.
        """
        ...

    def connect_nodes(arg1: PyActionFamilyNode, parent_node: PyFlameObject, child_node: PyFlameObject, link_type: str='Default') -> bool:
        """
        Connect two nodes in the Action/Image/GMaskTracer schematic.
        Keyword argument:
        type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def create_node(arg1: PyActionFamilyNode, node_type: str, file_path: str='', is_udim: bool=False, tile_resolution: int=0) -> Any:
        """
        Add an Action/Image/GMaskTracer object node to the Action/Image/GMaskTracer schematic.
        Keyword argument:
        file_path -- Required by nodes that load an asset, such as Matchbox.
        """
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def disable_output(arg1: PyActionFamilyNode, output_type: str) -> bool:
        """
        Disable the render output_type for the Action node.
        Keyword argument:
        output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectors Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)
        """
        ...

    def disconnect_nodes(arg1: PyActionFamilyNode, parent_node: PyFlameObject, child_node: PyFlameObject, link_type: str='Default') -> bool:
        """
        Disconnect two nodes in the Action/Image/GMaskTracer schematic.
        Keyword argument:
        type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def enable_output(arg1: PyActionFamilyNode, output_type: str) -> bool:
        """
        Enable the render output_type for the Action node.
        Keyword argument:
        output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectoars Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)
        """
        ...

    def encompass_nodes(arg1: PyActionFamilyNode, node_list: list) -> Any:
        """
        Create a compass including the node list given as argument
        Keyword argument:
        node_list -- a list of nodes (either string or node objects)
        output_type -- the created compass node
        """
        ...

    def export_fbx(arg1: PyActionFamilyNode, file_path: str, only_selected_nodes: bool=False, pixel_to_units: float=0.10000000149011612, frame_rate: str='23.976 fps', bake_animation: bool=False, export_axes: bool=True, export_point_locators: bool=False, combine_material: bool=True, duplicate_material: bool=False) -> bool:
        """
        Export Action nodes to an FBX file.
        Keyword argument:
        file_path -- Path to the output FBX file. Mandatory.
        """
        ...

    def get_node(arg1: PyActionFamilyNode, node_name: str) -> Any:
        """
        Get a node by node name. Doesn't select it in the UI.
        """
        ...

    def import_abc(arg1: PyActionFamilyNode, file_path: str, lights: bool=True, cameras: bool=True, models: bool=True, normals: bool=True, mesh_animations: bool=True, frame_rate: str='23.976 fps', auto_fit: bool=False, unit_to_pixels: float=10.0, consolidate_geometry: bool=True, create_object_group: bool=False) -> list:
        """
        Import an Alembic (ABC) file into the Action schematic using the Action Objects mode.
        Keyword argument:
        file_path -- Path to the ABC file. Mandatory.
        """
        ...

    def import_fbx(arg1: PyActionFamilyNode, file_path: str, lights: bool=True, cameras: bool=True, models: bool=True, normals: bool=True, mesh_animations: bool=True, keep_frame_rate: bool=True, bake_animation: bool=False, object_properties: bool=True, auto_fit: bool=False, unit_to_pixels: float=10.0, create_media: bool=True, is_udim: bool=False, relink_material: bool=True) -> list:
        """
        Import an FBX file into the Action schematic using the Action Objects mode.
        Keyword argument:
        file_path -- Path to the FBX file. Mandatory.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def organize(arg1: PyActionFamilyNode) -> bool:
        """
        Clean up the Action/Image/GMaskTracer schematic.
        """
        ...

    def read_abc(arg1: PyActionFamilyNode, file_path: str, lights: bool=True, cameras: bool=True, models: bool=True, normals: bool=True, mesh_animations: bool=True, frame_rate: str='23.976 fps', auto_fit: bool=False, unit_to_pixels: float=10.0, consolidate_geometry: bool=True, create_object_group: bool=False) -> Any:
        """
        Import an Alembic (ABC) file into the Action schematic using the Read File mode.
        Keyword argument:
        file_path -- Path to the ABC file. Mandatory.
        """
        ...

    def read_fbx(arg1: PyActionFamilyNode, file_path: str, lights: bool=True, cameras: bool=True, models: bool=True, normals: bool=True, mesh_animations: bool=True, keep_frame_rate: bool=True, bake_animation: bool=False, object_properties: bool=True, auto_fit: bool=False, unit_to_pixels: float=10.0, is_udim: bool=False, relink_material: bool=True) -> Any:
        """
        Import an FBX file into the Action schematic using the Read File mode.
        Keyword argument:
        file_path -- Path to the FBX file. Mandatory.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyArchiveEntry(PyFlameObject):
    """
    Class derived from PyFlameObject. Base class for any object displayed in the Media Panel.
    """
    attributes = ...
    parent = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...


class PyAttribute:
    """
    <property object at 0x7f1c32738450>
    """
    values = ...

    def __add__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __add__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    @overload
    def __add__(arg1: PyAttribute, arg2: str) -> Any:
        ...

    def __eq__(arg1: PyAttribute, arg2: Any) -> bool:
        ...

    def __floordiv__(arg1: PyAttribute, arg2: Any) -> Any:
        ...

    def __ge__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __ge__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def __gt__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __gt__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def __iadd__(arg1: Any, arg2: float) -> Any:
        ...

    @overload
    def __iadd__(arg1: Any, arg2: int) -> Any:
        ...

    @overload
    def __iadd__(arg1: Any, arg2: str) -> Any:
        ...

    def __idiv__(arg1: Any, arg2: float) -> Any:
        ...

    @overload
    def __idiv__(arg1: Any, arg2: int) -> Any:
        ...

    def __imul__(arg1: Any, arg2: float) -> Any:
        ...

    @overload
    def __imul__(arg1: Any, arg2: int) -> Any:
        ...

    def __isub__(arg1: Any, arg2: float) -> Any:
        ...

    @overload
    def __isub__(arg1: Any, arg2: int) -> Any:
        ...

    def __le__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __le__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def __lt__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __lt__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def __mul__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __mul__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def __ne__(arg1: PyAttribute, arg2: Any) -> bool:
        ...

    def __radd__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __radd__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    @overload
    def __radd__(arg1: PyAttribute, arg2: str) -> Any:
        ...

    def __repr__(arg1: PyAttribute) -> Any:
        ...

    def __rmul__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __rmul__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def __rsub__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __rsub__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def __rtruediv__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __rtruediv__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def __str__(arg1: PyAttribute) -> str:
        ...

    def __sub__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __sub__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def __truediv__(arg1: PyAttribute, arg2: float) -> Any:
        ...

    @overload
    def __truediv__(arg1: PyAttribute, arg2: int) -> Any:
        ...

    def get_value(arg1: PyAttribute) -> Any:
        """
        Get the value of an attribute.
        """
        ...

    def set_value(arg1: PyAttribute, arg2: Any) -> bool:
        """
        Set the value of an attribute.
        """
        ...


class PyAudioTrack(PyFlameObject):
    """
    Object representing an Audio Track.
    """
    attributes = ...
    channels = ...
    parent = ...
    stereo = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def copy_to_media_panel(arg1: PyAudioTrack, destination: PyArchiveEntry, duplicate_action: str='add') -> Any:
        """
        Create a new clip with a copy of the PyObject.
        """
        ...


class PyBatch(PyFlameObject):
    """
    Class derived from PyFlameObject. This class represents a Batch Group.
    """
    attributes = ...
    batch_iterations = ...
    contexts = ...
    current_iteration = ...
    current_iteration_number = ...
    cursor_position = ...
    node_types = ...
    nodes = ...
    opened = ...
    parent = ...
    reels = ...
    shelf_reels = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def append_setup(arg1: PyBatch, setup_path: str, confirm: bool=True) -> bool:
        """
        Append a Batch setup file to the existing Batch setup.
        Keywords arguments:
        setup_path -- A path and a filename must be defined as arguments.
        confirm -- Set to True (default) to display a dialogue box in case of
        """
        ...

    def append_to_batch(arg1: PyBatch, batch_iteration: PyBatchIteration) -> bool:
        """
        Append a Batch Iteration object to the current Batch Group. A duplicate Batch Iteration object is renamed to the next available *vDD*. Batch Iteration objects are displayed in the Iterations folder. Iterations folder is a UI construction, not accessible directly.
        """
        ...

    def append_to_setup(arg1: PyBatch, batch_iteration: PyBatchIteration) -> bool:
        """
        Append a Batch Iteration object to the Batch Group's setup.
        """
        ...

    def clear(arg1: PyBatch, confirm: bool=True) -> bool:
        """
        Clear the Batch Group.
        """
        ...

    def clear_all_contexts(arg1: PyBatch) -> bool:
        """
        Clear all registered Context views in the Batch Group.
        """
        ...

    def clear_context(arg1: PyBatch, index: int) -> bool:
        """
        Clear a specific Context view in the Batch Group.
        """
        ...

    def clear_setup(arg1: PyBatch) -> bool:
        """
        Clear the Batch Group's setup.
        """
        ...

    def close(arg1: PyBatch) -> bool:
        """
        Close the Batch Group. You cannot close the Batch Group currently selected.
        Closing a Batch Group frees up the application it occupies when open. The size of the used memory is significant if in Batch Group schematic hosts many Action nodes with textures or 3D geoms.
        """
        ...

    def connect_nodes(arg1: PyBatch, output_node: PyNode, output_socket_name: str='Default', input_node: PyNode  = None, input_socket_name: str='Default') -> bool:
        """
        Connect two nodes in the Batch schematic.
        Keyword arguments:
        output_node -- The Batch node object, the origin of the connection.
        output_socket_name -- The name of the output socket where the connector starts; use *Default* to use the first output socket, usually *Result*.
        input_node -- The child Batch node object, the target of the connection.
        input_socket_name -- The name of the input socket where the connector ends; use *Default* to use the first input socket, usually *Front*. Using *Default* on an Action node connects to the Background socket. To connect to an Action media node, use <ActionNode>.media_nodes[].
        """
        ...

    def create_batch_group(arg1: PyBatch, name: str, nb_reels: int=4, nb_shelf_reels: int=1, reels: list=None, shelf_reels: list=None, start_frame: int=1, duration: Any=None) -> Any:
        """
        Create a new Batch Group object in the Desktop catalogue.
        Keyword arguments:
        name -- Name of the Batch Group.
        nb_reels -- Number of reels created. *reels* overrides *nb_reels*.
        nb_shelf_reels -- Number of shelf reels. The first shelf reel created is named Batch Renders. *shelf_reels* ovverides *nb_shelf_reels*.
        reels -- A list of reel names. Overrides *nb_reels*.
        shelf_reels -- A list of shelf reel names. Overrides *nb_shelf_reels*.
        start_frame -- The Batch Group's start frame. No timecodes, only a frame value.
        duration -- The number of frames. Sets the Duration field in the Batch UI. Will be set to the first clip duration when not specified.
        """
        ...

    def create_node(arg1: PyBatch, node_type: str, file_path: str='') -> Any:
        """
        Create a Batch node object in the Batch schematic.
         Keyword argument:
        node_type -- Must be a value from the PyBatch.node_types.
        """
        ...

    def create_reel(arg1: PyBatch, name: str) -> Any:
        """
        Create a new Schematic Reel in the Batch Gtroup.
        """
        ...

    def create_shelf_reel(arg1: PyBatch, name: str) -> Any:
        """
        Create a new Shelf Reel in the Batch Group.
        """
        ...

    def disconnect_node(arg1: PyBatch, node: PyNode, input_socket_name: str='') -> bool:
        """
        Disconnect the input links of a given node, given an input socket.
        Keyword arguments:
        node -- The Batch node object, the origin of the connection.
        input_socket_name -- The name of the input socket to disconnect.
        """
        ...

    def encompass_nodes(arg1: PyBatch, nodes: list) -> Any:
        """
        Create a Compass around a list of nodes in the Batch schematic.
         Keyword argument:
        nodes -- List of strings of node names.
        """
        ...

    def frame_all(arg1: PyBatch) -> bool:
        """
        Set the Batch schematic view to frame all the nodes in the Batch schematic.
        """
        ...

    def frame_selected(arg1: PyBatch) -> bool:
        """
        Set the Batch schematic view to frame the nodes selected in the Batch schematic.
        """
        ...

    def get_node(arg1: PyBatch, node_name: str) -> Any:
        """
        Return a Batch node object with a name matching the parameter. Every node in a Batch schematic has a unique name: no duplicates allowed.
        Keyword argument:
        node_name -- Node name.
        """
        ...

    def go_to(arg1: PyBatch) -> bool:
        """
        Display and set the Batch tab as the active environment.
        """
        ...

    def import_clip(arg1: PyBatch, file_path: str, reel_name: str) -> Any:
        """
        Import a clip using the Import node, and create a Clip node.
        Keyword arguments:
        file_path -- The path to the media can be:
         - A path to a single media file.
         - A path to a sequence of media files (ie "/dir/clip.[100-2000].dpx").
         - A pattern to media files (ie "/dir/name_v{version}.{frame}.{extension}").reel_name -- The name of the destination Schematic Reel.
        """
        ...

    def import_clips(arg1: PyBatch, file_paths: Any, reel_name: str) -> Any:
        """
        Import clips using the Import node, and then create Clip nodes in the Schematic Reel.
        Keyword arguments:
        file_paths -- A path, or a list of paths, to the media that can be:
         - A path to a single media file.
         - A path to a sequence of media files (ie "/dir/clip.[100-2000].dpx").
         - A pattern to media files (ie "/dir/name_v{version}.{frame}.{extension}").reel_name -- The name of the destination Schematic Reel.
        """
        ...

    def iterate(arg1: PyBatch, index: int=-1) -> Any:
        """
        Iterate the current Batch Setup, creating a new iteration named BatchSetupName_X, where X is the Batch Iteration's index, and starts at 001.
         Keyword argument:
        index -- Specifies the iteration's index. If none is specified, the iteration is assigned the next available index (max index + 1). If the index matches that of an existing Batch Iteration, its overwrites the iteration without warning.
        """
        ...

    def load_setup(arg1: PyBatch, setup_path: str) -> bool:
        """
        Load a Batch setup from disk and replace the current Batch Group's setup.
         Keyword argument:
        setup_path -- Filepath + Batch Setup filename.
        """
        ...

    def mimic_link(arg1: PyBatch, leader_node: PyNode, follower_node: PyNode) -> bool:
        """
        Create a Mimic Link between two Batch nodes. They must be of the same node_type.
        Keyword arguments:
        leader_node -- The node being mimicked.
        follower_node -- The node doing the mimicking.
        """
        ...

    def open(arg1: PyBatch) -> bool:
        """
        Open the Batch Group and display it in the Batch view.
        """
        ...

    def open_as_batch_group(arg1: PyBatch, confirm: bool=True) -> bool:
        """
        Open a Batch Group as a new Batch Group, adding it to PyDesktop.batch_groups. Can only be called from a Library.
        """
        ...

    def organize(arg1: PyBatch) -> bool:
        """
        Clean up the nodes layout in the Batch schematic.
        """
        ...

    def render(arg1: PyBatch, render_option: str='Foreground', generate_proxies: bool=False, include_history: bool=False) -> bool:
        """
        Trigger the rendering of the Batch Group setup. Every active Render and Write File nodes render. If specified render_option is not supported by the workstation, returns an error.
        Keyword arguments:
        render_option -- Defines the rendering method used. (Foreground, Background Reactor, Burn)
        generate_proxies -- Set to True to render at proxy resolution. (Default: False)
        include_history -- Set to True to create History with the rendering. (Default:False)
        """
        ...

    def replace_setup(arg1: PyBatch, batch_iteration: PyBatchIteration, confirm: bool=True) -> bool:
        """
        Replace the Batch Group setup with the specified Batch Iteration. Cannot be called on the Batch Group currently selected and displayed in the Batch view.
        """
        ...

    def save(arg1: PyBatch) -> Any:
        """
        Save the Batch Group to the location defined by PyDesktop.destination.
        """
        ...

    def save_current_iteration(arg1: PyBatch) -> Any:
        """
        Save the current Batch Group setup to the location defined by PyDesktop.destination.
        """
        ...

    def save_setup(arg1: PyBatch, setup_path: str) -> bool:
        """
        Save the Batch Group setup to disk. Includes media paths for clip node object, but not the media files themselves.
        Keyword argument:
        setup_path -- The filepath includes the filename. File extension must be .batch.
        """
        ...

    def select_nodes(arg1: PyBatch, nodes: Any) -> bool:
        """
        Select nodes.
        Keyword argument:
        nodes -- A list of the names of Batch node objects.
        """
        ...

    def set_viewport_layout(arg1: PyBatch, num_views: Any) -> bool:
        """
        Set the viewport layout for Batch.
        Keyword argument:
        num_views -- The layout used. (1-Up, 2-Up, 3-Up, 3-Up Split Top, 3-Up Split Left, 3-Up Split Right, 3-Up Split Bottom, 4-Up Split, 4-Up)
        """
        ...


class PyBatchIteration(PyArchiveEntry):
    """
    Class derived from PyArchiveEntry. This class represents a Batch Iteration.
    """
    attributes = ...
    iteration_number = ...
    parent = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def open_as_batch_group(arg1: PyBatchIteration, confirm: bool=True) -> bool:
        """
        Open a Batch Iteration as a new Batch Group, adding it to PyDesktop.batch_groups. Can only be called from a Library.
        """
        ...


class PyBrowser:
    """
    This class represents the file browser.
    """
    bit_depth = ...
    colour_space = ...
    frame_ratio = ...
    height = ...
    resize_filter = ...
    resize_mode = ...
    resolution = ...
    scaling_presets_value = ...
    scan_mode = ...
    selection = ...
    sequence_mode = ...
    width = ...

    def show(arg1: PyBrowser, default_path: str, extension: Any='', select_directory: bool=False, multi_selection: bool=False, include_resolution: Any=False, title: str='Load') -> None:
        """
        Show the file browser.Keyword arguments:
        default_path -- Set the path.
        extension -- Set the extension filter. Can be a single extension or a list of extensions. Leave empty to see all files.
        select_directory -- Only show directories.
        multi_selection -- Allow the user to select multiple files.
        include_resolution -- Display the resolution controls. Possible values are False, True, or "Full".  The Full mode includes the new adaptive and scaling presets modes.
        title -- Set the window title.
        """
        ...


class PyClip(PyArchiveEntry):
    """
    CLass derived from PyArchiveEntry. This class represents a Clip.
    """
    archive_date = ...
    archive_error = ...
    attributes = ...
    audio_tracks = ...
    bit_depth = ...
    cached = ...
    colour_primaries = ...
    creation_date = ...
    duration = ...
    essence_uid = ...
    frame_rate = ...
    has_deliverables = ...
    has_history = ...
    height = ...
    markers = ...
    matrix_coefficients = ...
    original_source_uid = ...
    parent = ...
    proxy_resolution = ...
    ratio = ...
    sample_rate = ...
    scan_mode = ...
    source_uid = ...
    start_frame = ...
    subtitles = ...
    transfer_characteristics = ...
    unlinked = ...
    versions = ...
    width = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def cache_media(arg1: PyClip, mode: str='current') -> bool:
        """
        Cache the Clip's linked media.
        Keyword argument:
        mode -- Determine the version to cache (currently selected or all versions). All Versions is only useful with to multi-version clips (Current, All Versions)
        """
        ...

    def change_dominance(arg1: PyClip, scan_mode: str) -> None:
        """
        Change the Clip's dominance. Changes only the clip's metadata.
        Keyword argument:
        scan_mode -- Field dominance. (P, F1, F2)
        """
        ...

    def change_start_frame(arg1: PyClip, start_frame: int, use_segment_connections: bool=True) -> None:
        """
        Modify the start frame of a source Clip.
        Keywords argument:
        start_frame -- New start frame of the clip.
        use_segment_connections -- Sync the start frame of connected segments.
        """
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def close_container(arg1: PyClip) -> None:
        """
        Close the container timeline if the Clip is inside a container.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def create_marker(arg1: PyClip, location: Any) -> Any:
        """
        Add a Marker to the Clip.Keyword argument:
        location -- The frame where the marker gets created.
        """
        ...

    def cut(arg1: PyClip, cut_time: PyTime) -> None:
        """
        Cut all tracks of the Clip.
        """
        ...

    def flush_cache_media(arg1: PyClip, mode: str='current') -> bool:
        """
        Flush the Clip's media cache.
        Keyword argument:
        mode -- Determine the version's cache to flush. (Current, All Versions, All But Current)
        """
        ...

    def flush_renders(arg1: PyClip) -> None:
        """
        Flush the Clip's TimelineFX renders.
        """
        ...

    def get_colour_space(arg1: PyClip, time: PyTime=None) -> str:
        """
        Return the colour space at the requested time. Use current_time when no time is supplied.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def is_rendered(arg1: PyClip, top_only: bool=False, render_quality: str='Full Resolution') -> bool:
        """
        Return if a Clip is rendered.
        The following attributes can be defined: top_only, render_quality.
        """
        ...

    def open_as_sequence(arg1: PyClip) -> Any:
        """
        Open the Clip as a Sequence. Mutates the PyClip object into a PySequence object.
        """
        ...

    def open_container(arg1: PyClip) -> bool:
        """
        Open the container timeline if the Clip is inside a container.
        """
        ...

    def reformat(arg1: PyClip, width: int=0, height: int=0, ratio: float=0.0, bit_depth: int=0, scan_mode: str='', frame_rate: str='', resize_mode: str='Letterbox') -> None:
        """
        Reformat the Clip to the specified format.
        Keywords arguments:
        width -- Integer between 24 and 16384.
        height -- Integer between 24 and 16384.
        ratio -- Frame aspect ratio. Float between 0.01 and 100.
        bit_depth -- Bit depth. (8, 10, 12, 16 or 32)
        scan_mode -- Scan mode of the sequence. (F1, F2, P)
        frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps)
        resize_mode -- Resize mode. (Letterbox, Crop Edges, Fill, Centre)
        """
        ...

    def render(arg1: PyClip, render_mode: str='All', render_option: str='Foreground', render_quality: str='Full Resolution', effect_type: str='', effect_caching_mode: str='Current', include_handles: bool=False) -> bool:
        """
        Trigger a render of the Clip
        The following attributes can be defined: render_mode, render_option, render_quality, effect_type, effect_caching_mode and include_handles.
        """
        ...

    def save(arg1: PyClip) -> bool:
        """
        Save the Clip to the defined save destination.
        """
        ...


class PyClipNode(PyNode):
    """
    Class derived from PyNode. This class represents a Clip node.
    """
    attributes = ...
    clip = ...
    input_sockets = ...
    output_sockets = ...
    parent = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyCoCameraAnalysis(PyCoNode):
    """
    Class derived from PyCoNode. This class represents the camera analysis node in the Action schematic.
    """
    attributes = ...
    parent = ...
    type = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def add_reference(arg1: PyCoNode, frame: Any) -> bool:
        """
        Add a Motion Warp map's reference frame at specified index.
        Keyword argument
        frame -- The reference frame's index. An integer.
        """
        ...

    def analyseRange(arg1: PyCoCameraAnalysis, arg2: Any, start: Any) -> bool:
        """
        Run the analysis for the given frame range using the first frame as a reference if none has been already set.
        """
        ...

    def assign_media(arg1: PyCoNode, media_name: Any) -> bool:
        """
        Assign a media layer to the node.
        Keyword argument
        media_name -- The index of the media layer from Actions' *media_layers*; or the name of the media layer.
        """
        ...

    def cache_range(arg1: PyCoNode, arg2: Any, start: Any) -> bool:
        """
        Cache the selected Map Analysis over the specified range.
        Keyword arguments
        start -- The first frame of the range. An integer.
        end -- The last frame of the range. An integer.
        """
        ...

    def children(arg1: PyCoNode, link_type: str='Default') -> list:
        """
        Return a list of PyCoNode objects that are the children of the action node.
        Keyword argument:
        link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def parents(arg1: PyCoNode, link_type: str='Default') -> list:
        """
        Return a list of PyCoNode objects that are the parents of the action node.
        Keyword argument:
        link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def resetAnalysis(arg1: PyCoCameraAnalysis) -> bool:
        """
        Reset the current analysis.
        """
        ...


class PyCoCompass(PyCoNode):
    """
    Class derived from PyCoNode. This class represents the compass node in the Action schematic.
    """
    attributes = ...
    nodes = ...
    parent = ...
    type = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def add_reference(arg1: PyCoNode, frame: Any) -> bool:
        """
        Add a Motion Warp map's reference frame at specified index.
        Keyword argument
        frame -- The reference frame's index. An integer.
        """
        ...

    def assign_media(arg1: PyCoNode, media_name: Any) -> bool:
        """
        Assign a media layer to the node.
        Keyword argument
        media_name -- The index of the media layer from Actions' *media_layers*; or the name of the media layer.
        """
        ...

    def cache_range(arg1: PyCoNode, arg2: Any, start: Any) -> bool:
        """
        Cache the selected Map Analysis over the specified range.
        Keyword arguments
        start -- The first frame of the range. An integer.
        end -- The last frame of the range. An integer.
        """
        ...

    def children(arg1: PyCoNode, link_type: str='Default') -> list:
        """
        Return a list of PyCoNode objects that are the children of the action node.
        Keyword argument:
        link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def parents(arg1: PyCoNode, link_type: str='Default') -> list:
        """
        Return a list of PyCoNode objects that are the parents of the action node.
        Keyword argument:
        link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...


class PyCoNode(PyFlameObject):
    """
    Class derived from PyFlameObject. This class represents an Action node in the Action schematic.
    """
    attributes = ...
    parent = ...
    type = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def add_reference(arg1: PyCoNode, frame: Any) -> bool:
        """
        Add a Motion Warp map's reference frame at specified index.
        Keyword argument
        frame -- The reference frame's index. An integer.
        """
        ...

    def assign_media(arg1: PyCoNode, media_name: Any) -> bool:
        """
        Assign a media layer to the node.
        Keyword argument
        media_name -- The index of the media layer from Actions' *media_layers*; or the name of the media layer.
        """
        ...

    def cache_range(arg1: PyCoNode, arg2: Any, start: Any) -> bool:
        """
        Cache the selected Map Analysis over the specified range.
        Keyword arguments
        start -- The first frame of the range. An integer.
        end -- The last frame of the range. An integer.
        """
        ...

    def children(arg1: PyCoNode, link_type: str='Default') -> list:
        """
        Return a list of PyCoNode objects that are the children of the action node.
        Keyword argument:
        link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def parents(arg1: PyCoNode, link_type: str='Default') -> list:
        """
        Return a list of PyCoNode objects that are the parents of the action node.
        Keyword argument:
        link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...


class PyCompassNode(PyNode):
    """
    Class derived from PyNode. This class represents a Compass node.
    """
    attributes = ...
    input_sockets = ...
    nodes = ...
    output_sockets = ...
    parent = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyDesktop(PyArchiveEntry):
    """
    Class derived from PyArchiveEntry. This class represents a Desktop.
    """
    attributes = ...
    batch_groups = ...
    children = ...
    parent = ...
    reel_groups = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def create_batch_group(arg1: PyDesktop, name: str, nb_reels: int=4, nb_shelf_reels: int=1, reels: list=None, shelf_reels: list=None, start_frame: int=1, duration: Any=None) -> Any:
        """
        Create a new Batch Group object in the Desktop catalogue.
        Keyword arguments:
        name -- Name of the Batch Group.
        nb_reels -- Number of reels created. *reels* overrides *nb_reels*.
        nb_shelf_reels -- Number of shelf reels. The first shelf reel created is named Batch Renders. *shelf_reels* ovverides *nb_shelf_reels*.
        reels -- A list of reel names. Overrides *nb_reels*.
        shelf_reels -- A list of shelf reel names. Overrides *nb_shelf_reels*.
        start_frame -- The Batch Group's start frame. No timecodes, only a frame value.
        duration -- The number of frames. Sets the Duration field in the Batch UI. Will be set to the first clip duration when not specified.
        """
        ...

    def create_reel_group(arg1: PyDesktop, name: str) -> Any:
        """
        Create a new Reel Group object in the Desktop catalogue.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def save(arg1: PyDesktop) -> bool:
        """
        Save the Desktop to the location defined by the *destination* attribute.
        """
        ...


class PyExporter:
    """
    Object holding export settings.
    """
    Audio = ...
    Autodesk = ...
    Distribution_Package = ...
    Image_Sequence = ...
    Movie = ...
    Project = ...
    Sequence_Publish = ...
    Shared = ...
    Shotgun = ...
    export_all_subtitles = ...
    export_between_marks = ...
    export_subtitles_as_files = ...
    foreground = ...
    include_subtitles = ...
    keep_timeline_fx_renders = ...
    use_top_video_track = ...
    warn_on_mixed_colour_space = ...
    warn_on_no_media = ...
    warn_on_pending_render = ...
    warn_on_reimport_unsupported = ...
    warn_on_unlinked = ...
    warn_on_unrendered = ...
    BackgroundJobSettings = ...
    PresetType = ...
    PresetVisibility = ...

    def __init__(arg1: Any) -> None:
        ...

    def export(arg1: PyExporter, sources: Any, preset_path: str, output_directory: str, background_job_settings: BackgroundJobSettings=None, hooks: Any=None, hooks_user_data: Any=None) -> None:
        """
        Perform export.
        Keyword arguments:
        sources -- Flame clip object, a Flame container object or a list of either first. If a container is passed, a multi-export will be done and structure will be respected as much as possible.
        preset_path -- Absolute path to the export preset to use.
        output_directory -- Absolute path to the output directory root.
        background_job_settings -- Settings of background job(s) created if any.
        hooks -- Export python hooks override. If passed, regular export python hooks implemented in exportHooks.py will be bypassed for this export and methods in the passed object with matching name will be called.
            Instance of object passed should implement the following signature:
        
                class PythonHookOverride(object):
                    def preExport(self, info, userData, *args, **kwargs)
                        pass
        
                    def postExport(self, info, userData, *args, **kwargs):
                        pass
        
                    def preExportSequence(self, info, userData, *args, **kwargs):
                        pass
        
                    def postExportSequence(self, info, userData, *args, **kwargs):
                        pass
        
                    def preExportAsset(self, info, userData, *args, **kwargs):
                        pass
        
                    def postExportAsset(self, info, userData, *args, **kwargs):
                        pass
        
                    def exportOverwriteFile(self, path, *args, **kwargs):
                        return "ask" # or "overwrite"
        
        hooks_user_data -- User data object passed to the export python hooks. This object can be modified by the PythonHookOverride methods but cannot be re-assigned
        """
        ...

    def get_presets_base_dir(preset_visibility: PresetVisibility) -> str:
        """
        Get a presets base directory.
        """
        ...

    def get_presets_dir(preset_visibility: PresetVisibility, preset_type: PresetType) -> str:
        """
        Get a presets directory.
        """
        ...


class PyFlameObject:
    """
    The basic type of all accessible Flame objects from the python API.
    """
    attributes = ...
    parent = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...


class PyFolder(PyArchiveEntry):
    """
    Class derived from PyArchiveEntry. This class represents a Folder.
    """
    attributes = ...
    batch_groups = ...
    batch_iterations = ...
    children = ...
    clips = ...
    desktops = ...
    folders = ...
    parent = ...
    reel_groups = ...
    reels = ...
    sequences = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear(arg1: PyFolder, confirm: bool=True) -> bool:
        """
        Clear the contents of the Folder object.
        """
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def create_folder(arg1: PyFolder, name: str) -> Any:
        """
        Create a new Folder object inside the Folder.
        """
        ...

    def create_reel(arg1: PyFolder, name: str) -> Any:
        """
        Create a new Reel object inside the Folder.
        """
        ...

    def create_reel_group(arg1: PyFolder, name: str) -> Any:
        """
        Create a new Reel Group object inside the Folder.
        """
        ...

    def create_sequence(arg1: PyFolder, name: str='Untitled Sequence', video_tracks: int=1, video_stereo: bool=False, width: int=1920, height: int=1080, ratio: float=1.7777777777777777, bit_depth: int=16, scan_mode: str='P', frame_rate: str='23.976 fps', start_at: Any=..., duration: Any=..., audio_tracks: int=1, audio_stereo: bool=True) -> Any:
        """
        Create a Sequence in a PyReel, PyLibrary, PyFolder.
        Keywords arguments:
        video_tracks -- Number of video tracks. Integer between 1 and 8.
        video_stereo -- Stereoscopy. False for mono, True for stereo.
        width -- Integer between 24 and 16384.
        height -- Integer between 24 and 16384.
        ratio -- Frame aspect ratio. Float between 0.01 and 100.
        scan_mode -- Scan mode of the sequence. (F1, F2, P)
        frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps)
        start_at -- Start timecode. The timecode format must be of the format specified by *frame_rate*.
        duration -- Can be an end timecode or an integer. If an end timecode, format must be of the format specified by *frame_rate*. If an integer, it represents a number of frames.
        audio_tracks -- Number of audio tracks. (0, 1, 2, 4, 8, 12, 16)
        audio_stereo -- Stereophony, apply to all *audio_tracks*. False for mono tracks, True for stereo.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...


class PyGMaskTracerNode(PyActionFamilyNode):
    """
    Class derived from PyActionFamilyNode. Represents a GMask Tracer node object.
    """
    all_tabs = ...
    attributes = ...
    cursor_position = ...
    input_sockets = ...
    left_tabs = ...
    media_layers = ...
    node_types = ...
    nodes = ...
    output_sockets = ...
    output_types = ...
    parent = ...
    right_tabs = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_schematic(arg1: PyActionFamilyNode) -> bool:
        """
        Clear the Action/Image/GMaskTracer schematic of all nodes.
        """
        ...

    def connect_nodes(arg1: PyActionFamilyNode, parent_node: PyFlameObject, child_node: PyFlameObject, link_type: str='Default') -> bool:
        """
        Connect two nodes in the Action/Image/GMaskTracer schematic.
        Keyword argument:
        type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def create_node(arg1: PyActionFamilyNode, node_type: str, file_path: str='', is_udim: bool=False, tile_resolution: int=0) -> Any:
        """
        Add an Action/Image/GMaskTracer object node to the Action/Image/GMaskTracer schematic.
        Keyword argument:
        file_path -- Required by nodes that load an asset, such as Matchbox.
        """
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def disable_output(arg1: PyActionFamilyNode, output_type: str) -> bool:
        """
        Disable the render output_type for the GMask Tracer node.
        Keyword argument:
        output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectors Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)
        """
        ...

    def disconnect_nodes(arg1: PyActionFamilyNode, parent_node: PyFlameObject, child_node: PyFlameObject, link_type: str='Default') -> bool:
        """
        Disconnect two nodes in the Action/Image/GMaskTracer schematic.
        Keyword argument:
        type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def enable_output(arg1: PyActionFamilyNode, output_type: str) -> bool:
        """
        Enable the render output_type for the GMask Tracer node.
        Keyword argument:
        output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectoars Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)
        """
        ...

    def encompass_nodes(arg1: PyActionFamilyNode, node_list: list) -> Any:
        """
        Create a compass including the node list given as argument
        Keyword argument:
        node_list -- a list of nodes (either string or node objects)
        output_type -- the created compass node
        """
        ...

    def export_fbx(arg1: PyActionFamilyNode, file_path: str, only_selected_nodes: bool=False, pixel_to_units: float=0.10000000149011612, frame_rate: str='23.976 fps', bake_animation: bool=False, export_axes: bool=True, export_point_locators: bool=False, combine_material: bool=True, duplicate_material: bool=False) -> bool:
        """
        Export GMask Tracer nodes to an FBX file.
        Keyword argument:
        file_path -- Path to the output FBX file. Mandatory.
        """
        ...

    def get_node(arg1: PyActionFamilyNode, node_name: str) -> Any:
        """
        Get a node by node name. Doesn't select it in the UI.
        """
        ...

    def import_abc(arg1: PyActionFamilyNode, file_path: str, lights: bool=True, cameras: bool=True, models: bool=True, normals: bool=True, mesh_animations: bool=True, frame_rate: str='23.976 fps', auto_fit: bool=False, unit_to_pixels: float=10.0, consolidate_geometry: bool=True, create_object_group: bool=False) -> list:
        """
        Import an Alembic (ABC) file into the GMask Tracer schematic using the GMask Tracer Objects mode.
        Keyword argument:
        file_path -- Path to the ABC file. Mandatory.
        """
        ...

    def import_fbx(arg1: PyActionFamilyNode, file_path: str, lights: bool=True, cameras: bool=True, models: bool=True, normals: bool=True, mesh_animations: bool=True, keep_frame_rate: bool=True, bake_animation: bool=False, object_properties: bool=True, auto_fit: bool=False, unit_to_pixels: float=10.0, create_media: bool=True, is_udim: bool=False, relink_material: bool=True) -> list:
        """
        Import an FBX file into the GMask Tracer schematic using the GMask Tracer Objects mode.
        Keyword argument:
        file_path -- Path to the FBX file. Mandatory.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def organize(arg1: PyActionFamilyNode) -> bool:
        """
        Clean up the Action/Image/GMaskTracer schematic.
        """
        ...

    def read_abc(arg1: PyActionFamilyNode, file_path: str, lights: bool=True, cameras: bool=True, models: bool=True, normals: bool=True, mesh_animations: bool=True, frame_rate: str='23.976 fps', auto_fit: bool=False, unit_to_pixels: float=10.0, consolidate_geometry: bool=True, create_object_group: bool=False) -> Any:
        """
        Import an Alembic (ABC) file into the GMask Tracer schematic using the Read File mode.
        Keyword argument:
        file_path -- Path to the ABC file. Mandatory.
        """
        ...

    def read_fbx(arg1: PyActionFamilyNode, file_path: str, lights: bool=True, cameras: bool=True, models: bool=True, normals: bool=True, mesh_animations: bool=True, keep_frame_rate: bool=True, bake_animation: bool=False, object_properties: bool=True, auto_fit: bool=False, unit_to_pixels: float=10.0, is_udim: bool=False, relink_material: bool=True) -> Any:
        """
        Import an FBX file into the GMask Tracer schematic using the Read File mode.
        Keyword argument:
        file_path -- Path to the FBX file. Mandatory.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyHDRNode(PyNode):
    """
    Object representing a HDR node.
    """
    analysis_status = ...
    attributes = ...
    input_sockets = ...
    mastering_display_ids = ...
    mastering_display_info = ...
    output_sockets = ...
    parent = ...
    sockets = ...
    target_display_ids = ...
    target_display_info = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def analyze(arg1: PyHDRNode, analyze_mode: str='Current Shot') -> None:
        """
        Perform HDR analysis.
        """
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def export_DolbyVision_xml(arg1: PyHDRNode, file_name: str, comment: str='') -> None:
        """
        Export the current HDR to a Dolby Vision XML file.
        """
        ...

    def has_trim(arg1: PyHDRNode, target_display_id: int) -> bool:
        """
        Returns True if the given Target Display ID has trims.
        """
        ...

    def import_DolbyVision_xml(arg1: PyHDRNode, file_name: str, mode: str='Include Frame Based Transitions Trims', shot_idx: int=0) -> None:
        """
        Import the current HDR from a Dolby Vision XML file.
        """
        ...

    def interpolate_trims(arg1: PyHDRNode) -> None:
        """
        Interpolate the current HDR trims.
        """
        ...

    def keep_analysis(arg1: PyHDRNode) -> None:
        """
        Remove the dirty flag from the HDR analysis.
        """
        ...

    def l2_from_l8(arg1: PyHDRNode) -> Any:
        """
        Dictionary containing the L2 values based on L8 values. Not valid in Dolby Vision 2.9.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def reset_analysis(arg1: PyHDRNode) -> None:
        """
        Reset the current HDR analysis.
        """
        ...

    def reset_trims(arg1: PyHDRNode) -> None:
        """
        Reset the current HDR trims.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyHDRTimelineFX(PyTimelineFX):
    """
    Object representing a HDR TimelineFX.
    """
    analysis_status = ...
    attributes = ...
    has_maps_cache_media = ...
    mastering_display_ids = ...
    mastering_display_info = ...
    parent = ...
    target_display_ids = ...
    target_display_info = ...
    type = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def analyze(arg1: PyHDRTimelineFX, analyze_mode: str='Current Shot') -> None:
        """
        Perform HDR analysis.
        """
        ...

    def export_DolbyVision_xml(arg1: PyHDRTimelineFX, file_name: str, shot_only: bool=False, comment: str='') -> None:
        """
        Export the current HDR to a Dolby Vision XML file.
        """
        ...

    def flush_maps_cache_media(arg1: PyTimelineFX) -> bool:
        """
        Flush the Timeline FX Maps and ML cached media.
        """
        ...

    def has_trim(arg1: PyHDRTimelineFX, target_display_id: int) -> bool:
        """
        Returns True if the given Target Display ID has trims.
        """
        ...

    def import_DolbyVision_xml(arg1: PyHDRTimelineFX, file_name: str, mode: str='Include Frame Based Transitions Trims', shot_idx: int=0) -> None:
        """
        Import the current HDR from a Dolby Vision XML file.
        """
        ...

    def interpolate_trims(arg1: PyHDRTimelineFX, arg2: str) -> None:
        """
        Interpolate the current HDR trims.
        """
        ...

    def keep_analysis(arg1: PyHDRTimelineFX) -> None:
        """
        Remove the dirty flag from the HDR analysis.
        """
        ...

    def l2_from_l8(arg1: PyHDRTimelineFX) -> Any:
        """
        Dictionary containing the L2 values based on L8 values. Not valid in Dolby Vision 2.9.
        """
        ...

    def load_setup(arg1: PyTimelineFX, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def reset_analysis(arg1: PyHDRTimelineFX) -> None:
        """
        Reset the current HDR analysis.
        """
        ...

    def reset_trims(arg1: PyHDRTimelineFX) -> None:
        """
        Reset the current HDR trims.
        """
        ...

    def save_setup(arg1: PyTimelineFX, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def slide_keyframes(arg1: PyTimelineFX, offset: float) -> None:
        """
        Slide the keyframes the PySegment.
        Keywords argument:
        offset -- Relative offset to slide the keyframes.
        sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.
        """
        ...

    def sync_connected_segments(arg1: PyTimelineFX) -> None:
        """
        Push the Timeline FX to connected segments.
        """
        ...


class PyImageNode(PyActionFamilyNode):
    """
    Class derived from PyActionFamilyNode. Represents an Image node object.
    """
    all_tabs = ...
    attributes = ...
    cursor_position = ...
    input_sockets = ...
    left_tabs = ...
    media_layers = ...
    media_nodes = ...
    node_types = ...
    nodes = ...
    output_sockets = ...
    parent = ...
    right_tabs = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def add_media(arg1: PyActionFamilyNode) -> Any:
        """
        Add a Media layer to the Batch Image node.
        """
        ...

    def clear_schematic(arg1: PyActionFamilyNode) -> bool:
        """
        Clear the Action/Image/GMaskTracer schematic of all nodes.
        """
        ...

    def connect_nodes(arg1: PyActionFamilyNode, parent_node: PyFlameObject, child_node: PyFlameObject, link_type: str='Default') -> bool:
        """
        Connect two nodes in the Action/Image/GMaskTracer schematic.
        Keyword argument:
        type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def create_node(arg1: PyActionFamilyNode, node_type: str, file_path: str='', is_udim: bool=False, tile_resolution: int=0) -> Any:
        """
        Add an Action/Image/GMaskTracer object node to the Action/Image/GMaskTracer schematic.
        Keyword argument:
        file_path -- Required by nodes that load an asset, such as Matchbox.
        """
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def disconnect_nodes(arg1: PyActionFamilyNode, parent_node: PyFlameObject, child_node: PyFlameObject, link_type: str='Default') -> bool:
        """
        Disconnect two nodes in the Action/Image/GMaskTracer schematic.
        Keyword argument:
        type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def encompass_nodes(arg1: PyActionFamilyNode, node_list: list) -> Any:
        """
        Create a compass including the node list given as argument
        Keyword argument:
        node_list -- a list of nodes (either string or node objects)
        output_type -- the created compass node
        """
        ...

    def get_node(arg1: PyActionFamilyNode, node_name: str) -> Any:
        """
        Get a node by node name. Doesn't select it in the UI.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def organize(arg1: PyActionFamilyNode) -> bool:
        """
        Clean up the Action/Image/GMaskTracer schematic.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyLibrary(PyArchiveEntry):
    """
    Class derived from PyArchiveEntry. This class represents a Library.
    """
    attributes = ...
    batch_groups = ...
    batch_iterations = ...
    children = ...
    clips = ...
    desktops = ...
    folders = ...
    opened = ...
    parent = ...
    reel_groups = ...
    reels = ...
    sequences = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def acquire_exclusive_access(arg1: PyLibrary) -> bool:
        """
        Acquire exclusive access to the Shared Library. Shared Libraries are created locked. Only use with Shared Libraries.
        """
        ...

    def clear(arg1: PyLibrary, confirm: bool=True) -> bool:
        """
        Clear the Library's contents.
        """
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def close(arg1: PyLibrary) -> bool:
        """
        Close a Library to release it from the application memory.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def create_folder(arg1: PyLibrary, name: str) -> Any:
        """
        Create a Folder inside a Library.
        """
        ...

    def create_reel(arg1: PyLibrary, name: str) -> Any:
        """
        Create a Reel inside a Library.
        """
        ...

    def create_reel_group(arg1: PyLibrary, name: str) -> Any:
        """
        Create a Reel Group inside a Library.
        """
        ...

    def create_sequence(arg1: PyLibrary, name: str='Untitled Sequence', video_tracks: int=1, video_stereo: bool=False, width: int=1920, height: int=1080, ratio: float=1.7777777777777777, bit_depth: int=16, scan_mode: str='P', frame_rate: str='23.976 fps', start_at: Any=..., duration: Any=..., audio_tracks: int=1, audio_stereo: bool=True) -> Any:
        """
        Create a Sequence in a PyReel, PyLibrary, PyFolder.
        Keywords arguments:
        video_tracks -- Number of video tracks. Integer between 1 and 8.
        video_stereo -- Stereoscopy. False for mono, True for stereo.
        width -- Integer between 24 and 16384.
        height -- Integer between 24 and 16384.
        ratio -- Frame aspect ratio. Float between 0.01 and 100.
        scan_mode -- Scan mode of the sequence. (F1, F2, P)
        frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps)
        start_at -- Start timecode. The timecode format must be of the format specified by *frame_rate*.
        duration -- Can be an end timecode or an integer. If an end timecode, format must be of the format specified by *frame_rate*. If an integer, it represents a number of frames.
        audio_tracks -- Number of audio tracks. (0, 1, 2, 4, 8, 12, 16)
        audio_stereo -- Stereophony, apply to all *audio_tracks*. False for mono tracks, True for stereo.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def open(arg1: PyLibrary) -> bool:
        """
        Open a Library and load it in the application memory. Until a Library is open, it cannot be accessed. Libraries are created open.
        """
        ...

    def release_exclusive_access(arg1: PyLibrary) -> bool:
        """
        Release exclusive access to the Shared Library. Only used for Shared Libraries. Only use with Shared Libraries.
        """
        ...


class PyMarker(PyFlameObject):
    """
    Object representing a Marker.
    """
    attributes = ...
    parent = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...


class PyMediaHub:
    """
    This class represents the MediaHub.
    """
    archives = ...
    files = ...


class PyMediaHubFilesEntry(PyArchiveEntry):
    """
    Object representing a clip in the MediaHub Files tabs
    """
    attributes = ...
    parent = ...
    path = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...


class PyMediaHubFilesFolder(PyArchiveEntry):
    """
    Object representing a folder in the MediaHub Files tabs
    """
    attributes = ...
    parent = ...
    path = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...


class PyMediaHubFilesTab(PyMediaHubTab):
    """
    This class represents the MediaHub Files tab.
    """
    options = ...

    def get_path(arg1: PyMediaHubTab) -> str:
        """
        Return the MediaHub tab current path.
        """
        ...

    def set_path(arg1: PyMediaHubTab, arg2: str, allow_partial_success: bool=False) -> bool:
        """
        Set the MediaHub tab current path. If allow_partial_success is True, the path will be set to the last valid folder in the path.
        """
        ...


class PyMediaHubFilesTabOptions:
    """
    This class represents the MediaHub Files tab options.
    """
    bit_depth = ...
    cache_and_proxies_all_versions = ...
    cache_mode = ...
    frame_ratio = ...
    height = ...
    multi_channel_mode = ...
    pixel_ratio = ...
    proxies_mode = ...
    resize_filter = ...
    resize_mode = ...
    resolution = ...
    scaling_presets_value = ...
    scan_mode = ...
    sequence_mode = ...
    width = ...

    def set_tagged_colour_space(arg1: PyMediaHubFilesTabOptions, colour_space: str) -> None:
        """
        Import pixel ratio value.  Returns None when resolution is not set to Same As Source.
        """
        ...


class PyMediaHubProjectsEntry(PyArchiveEntry):
    """
    Object representing a clip in the MediaHub Projects tabs
    """
    attributes = ...
    parent = ...
    path = ...
    uid = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...


class PyMediaHubProjectsFolder(PyArchiveEntry):
    """
    Object representing a folder in the MediaHub Projects tabs
    """
    attributes = ...
    parent = ...
    path = ...
    uid = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...


class PyMediaHubTab:
    """
    This class represents a MediaHub tab.
    """

    def get_path(arg1: PyMediaHubTab) -> str:
        """
        Return the MediaHub tab current path.
        """
        ...

    def set_path(arg1: PyMediaHubTab, arg2: str, allow_partial_success: bool=False) -> bool:
        """
        Set the MediaHub tab current path. If allow_partial_success is True, the path will be set to the last valid folder in the path.
        """
        ...


class PyMediaPanel:
    """
    This class represents the media panel.
    """
    dual = ...
    full_height = ...
    full_width = ...
    selected_entries = ...
    visible = ...

    def copy(arg1: PyMediaPanel, source_entries: Any, destination: Any, duplicate_action: str='add') -> Any:
        """
        Copy a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.Return a list of the copied PyObjects.Keyword arguments:
        source_entries -- The PyObject or list of PyObjects to copy.
        destination -- The PyObject that acts as destination.
        duplicate_action -- Action to take when finding an object with the same name (add or replace).
        """
        ...

    def move(arg1: PyMediaPanel, source_entries: Any, destination: Any, duplicate_action: str='add') -> Any:
        """
        Move a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.
        Return a list of the moved PyObjects.
        Keyword arguments:
        source_entries -- The PyObject or list of PyObjects to move.
        destination -- The PyObject that acts as destination.
        duplicate_action -- Action to take when finding an object with the same name (add or replace).
        """
        ...


class PyMessages:
    """
    Module handling message bar in application UI.
    """

    def clear_console(arg1: PyMessages) -> None:
        """
        Remove currently displayed message in the message bar.
        """
        ...

    def show_in_console(arg1: PyMessages, message: str, type: str='info', duration: int=-1) -> None:
        """
        Display an informative message in application message bar.
        message -- Message string to display.
        type -- Message type can be info, warning, or error.
        duration -- An optional time in seconds to keep message on screen.
        """
        ...

    def show_in_dialog(arg1: PyMessages, title: str, message: str, type: str, buttons: list, cancel_button: str='') -> str:
        """
        Display a custom dialog with a selection of options.
        Keywords argument:
        title -- The title of the dialog.
        message -- The message displayed in the center of the dialog.
        type -- The type of dialog. Can be error, info, question, or warning.
        buttons -- The list of titles used to refer to the options
        cancel_button -- The text displayed in the cancel option
        """
        ...


class PyNode(PyFlameObject):
    """
    Object representing a Node.
    """
    attributes = ...
    input_sockets = ...
    output_sockets = ...
    parent = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyOFXNode(PyNode):
    """
    Object representing a OpenFX node.
    """
    attributes = ...
    input_sockets = ...
    output_sockets = ...
    parent = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def change_plugin(arg1: PyOFXNode, plugin_name: str) -> bool:
        """
        Change the active plugin for the openFX node
        """
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyPaintNode(PyNode):
    """
    Object representing a Paint node.
    """
    attributes = ...
    input_sockets = ...
    output_sockets = ...
    parent = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def add_source(arg1: PyPaintNode) -> Any:
        """
        Add a Source layer to a Paint node.
        """
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyProject(PyArchiveEntry):
    """
    Object representing a Project.
    """
    attributes = ...
    current_workspace = ...
    name = ...
    nickname = ...
    parent = ...
    project_name = ...
    shared_libraries = ...
    workspaces_count = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def create_shared_library(arg1: PyProject, name: str) -> Any:
        """
        Create a new Shared Library in the Project.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def refresh_shared_libraries(arg1: PyProject) -> bool:
        """
        Refresh the Shared Libraries list in the Media Panel.
        """
        ...


class PyProjectSelector:
    """
    Object representing the Project manager.
    """
    current_project = ...


class PyReel(PyArchiveEntry):
    """
    Object representing a Reel.
    """
    attributes = ...
    children = ...
    clips = ...
    parent = ...
    sequences = ...
    type = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear(arg1: PyReel, confirm: bool=True) -> bool:
        """
        Clear the Reel content.
        """
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def create_sequence(arg1: PyReel, name: str='Untitled Sequence', video_tracks: int=1, video_stereo: bool=False, width: int=1920, height: int=1080, ratio: float=1.7777777777777777, bit_depth: int=16, scan_mode: str='P', frame_rate: str='23.976 fps', start_at: Any=..., duration: Any=..., audio_tracks: int=1, audio_stereo: bool=True) -> Any:
        """
        Create a Sequence in a PyReel, PyLibrary, PyFolder.
        Keywords arguments:
        video_tracks -- Number of video tracks. Integer between 1 and 8.
        video_stereo -- Stereoscopy. False for mono, True for stereo.
        width -- Integer between 24 and 16384.
        height -- Integer between 24 and 16384.
        ratio -- Frame aspect ratio. Float between 0.01 and 100.
        scan_mode -- Scan mode of the sequence. (F1, F2, P)
        frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps)
        start_at -- Start timecode. The timecode format must be of the format specified by *frame_rate*.
        duration -- Can be an end timecode or an integer. If an end timecode, format must be of the format specified by *frame_rate*. If an integer, it represents a number of frames.
        audio_tracks -- Number of audio tracks. (0, 1, 2, 4, 8, 12, 16)
        audio_stereo -- Stereophony, apply to all *audio_tracks*. False for mono tracks, True for stereo.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def save(arg1: PyReel) -> bool:
        """
        Save the Reel to the defined save destination.
        """
        ...


class PyReelGroup(PyArchiveEntry):
    """
    Object representing a Reel Group.
    """
    attributes = ...
    children = ...
    parent = ...
    reels = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear(arg1: PyReelGroup, confirm: bool=True) -> bool:
        """
        Clear the Reel Group content.
        """
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def create_reel(arg1: PyReelGroup, name: str, sequence: bool=False) -> Any:
        """
        Create a new Reel inside a Reel Group.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def save(arg1: PyReelGroup) -> bool:
        """
        Save the Reel Group to the defined save destination.
        """
        ...


class PyRenderNode(PyNode):
    """
    Class derived from PyNode. This class represents a Render node.
    """
    attributes = ...
    channels = ...
    input_sockets = ...
    output_sockets = ...
    parent = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_channel_name(arg1: PyRenderNode, channel: Any, name: Any) -> None:
        """
        Rename a channel, using its index or front channel name as the index key.
        Keyword arguments:
        channel -- The channel to rename. Can be the channel index or the current name of the channel's front socket.
        name -- The new name of the channel. The type is either a string or a tuple. A Write File node always takes a string. A Render node takes a string or a tuple.
        In a Render node, a string only sets the name of the channel's front socket; the function creates the name of the matte socket by appending '_alpha' to 'name'. In the UI, the channel is flagged 'Sync'. A Write File node has only one socket per channel, and requires only a string to set a socket name.
        In a Render node, a tuple sets the names of the front and matte sockets. In the UI, the channel is not flagged 'Sync'. A Write File node does not accept a tuple.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class PyResolution:
    """
    Object representing a resolution

PyResolution()
PyResolution(width, height, bit_depth, frame_ratio, scan_format)
    """
    bit_depth = ...
    frame_ratio = ...
    height = ...
    resolution = ...
    scan_mode = ...
    width = ...

    def __init__(arg1: Any) -> None:
        ...

    @overload
    def __init__(arg1: Any, arg2: int, arg3: int, arg4: int, arg5: float, arg6: str) -> None:
        ...

    @overload
    def __init__(arg1: Any, arg2: str) -> None:
        ...


class PySearch:
    """
    This class represents the search.
    """
    use_weight = ...

    def activate_search_result(arg1: PySearch, name: str, type: str, tab: str='Tools') -> None:
        """
        Activate a search result.
        """
        ...

    def search_results(arg1: PySearch, search_str: str='*', tab: str='Tools') -> list:
        """
        Search results that match a string.
        """
        ...

    def set_tool_favorite(arg1: PySearch, arg2: str, name: str, type: bool) -> None:
        """
        Return the favorite status of a tool.
        """
        ...

    def set_tool_hidden(arg1: PySearch, arg2: str, name: str, type: bool) -> None:
        """
        Return the hidden status of a tool.
        """
        ...

    def set_tool_weight(arg1: PySearch, arg2: str, name: str, type: int) -> None:
        """
        Return the tool weight.
        """
        ...


class PySegment(PyFlameObject):
    """
    Object representing a Segment.
    """
    attributes = ...
    container_clip = ...
    effect_types = ...
    effects = ...
    file_path = ...
    groups = ...
    head = ...
    markers = ...
    matte_channel = ...
    matte_channels = ...
    matte_mode = ...
    original_source_uid = ...
    parent = ...
    record_duration = ...
    record_in = ...
    record_out = ...
    rgb_channel = ...
    rgb_channels = ...
    source_audio_track = ...
    source_bit_depth = ...
    source_cached = ...
    source_colour_primaries = ...
    source_duration = ...
    source_essence_uid = ...
    source_has_history = ...
    source_height = ...
    source_in = ...
    source_matrix_coefficients = ...
    source_name = ...
    source_out = ...
    source_ratio = ...
    source_sample_rate = ...
    source_scan_mode = ...
    source_transfer_characteristics = ...
    source_uid = ...
    source_unlinked = ...
    source_width = ...
    start_frame = ...
    tail = ...
    tape_name = ...
    type = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def change_start_frame(arg1: PySegment, start_frame: int, use_segment_connections: bool=True) -> None:
        """
        Modify the start frame of the segment.
        Keywords argument:
        start_frame -- New start frame of the segment.
        use_segment_connections -- Sync the start frame of connected segments.
        """
        ...

    def clear_colour(arg1: PySegment) -> None:
        """
        Clear the colour of the Segment.
        """
        ...

    def connected_segments(arg1: PySegment, scoping: str='all reels') -> Any:
        """
        Return a list of the connected segments.
        Keywords argument:
        scoping -- Scopes of the sequences to query (all reels, sequences reels, current reel, current sequence).
         (Default:all reels)
        """
        ...

    def copy_to_media_panel(arg1: PySegment, destination: PyArchiveEntry, duplicate_action: str='add') -> Any:
        """
        Create a new clip with a copy of the PyObject.
        """
        ...

    def create_connection(arg1: PySegment) -> None:
        """
        Create a connected segment connection.
        """
        ...

    def create_effect(arg1: PySegment, effect_type: str, after_effect_type: str='') -> Any:
        """
        Add an effect of effect_type on the Segment.
        after_effect_type can be specified to insert the effect at a specific position.
        """
        ...

    def create_marker(arg1: PySegment, location: Any) -> Any:
        """
        Create a Marker at the specified location on the Segment.
        """
        ...

    def create_unlinked_segment(arg1: PySegment, source_name: str='', tape_name: str='', start_time: Any=0, source_duration: Any=0, head: Any=0, file_path: str='', source_audio_track: int=1, width: int=0, height: int=0, ratio: float=0.0, bit_depth: int=0, scan_mode: str='Same As Sequence', frame_rate: str='Same As Sequence') -> None:
        """
        Replace the gap with an unlinked source media segment.
        Keywords argument:
        source_name -- Name of the source.
        tape_name -- Tape name of the source.
        start_time -- Start time of the source. Must be a PyTime or a frame number.
        source_duration -- Length of the source. Must be a PyTime, a number of frames, or "Infinite".
        head -- Amount of head media to set on the segment.
        file_path -- File path to the media.
        source_audio_track -- Audio track from the source.
        width -- Width of the video media. (0 to use the sequence width)
        height -- Height of the video media. (0 to use the sequence height)
        ratio -- Frame ratio of the video media. (0.0 to use the sequence ratio)
        bit_depth -- Bit depth of the video media. (0 to use the sequence bit depth)
        scan_mode -- Scan mode of the video media. (P, F1, F2, or Same As Sequence)
        frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps, Same As Sequence)
        """
        ...

    def duplicate_source(arg1: PySegment) -> None:
        """
        Insure that the segment's source is not shared anymore.
        """
        ...

    def get_colour_space(arg1: PySegment, time: PyTime=None) -> str:
        """
        Return the colour space at the requested time. Use record_in when no time is supplied.
        """
        ...

    def match(arg1: PySegment, destination: PyArchiveEntry, preserve_handle: bool=False, use_sequence_info: bool=True, include_nested_content: bool=False, include_timeline_fx: bool=False) -> Any:
        """
        Match out the media of the PySegment to the destination.
        Returns a PyClip or a list of PyClip (with the included_nested_content option).
        Keywords argument:
        destination -- The PyObject that acts as the destination.
        preserve_handle -- Prevent the unrolling of the media handles.
        use_sequence_info -- Copy sequence segment information to the new matched clip.
        include_nested_content -- Include all sources found inside a BFX or Matte Container.
        include_timeline_fx -- Copy the Timeline FX present on the original clip to the new matched clip.
        """
        ...

    def remove_connection(arg1: PySegment) -> None:
        """
        Remove the connected segment connection.
        """
        ...

    def set_gap_bars(arg1: PySegment, type: str='smpte', full_luminance: bool=False, softness: float=0.0) -> Any:
        """
        Create colour bars segment for the duration of the gap.
        Returns a new PySegment on success.
        Keywords argument:
        type -- smpte or pal.
        full_luminance -- bars created at 100 or 75 percent luminance.
        softness -- softness to apply between the bars.
        """
        ...

    def set_gap_colour(arg1: PySegment, r: float=0.0, g: float=0.0, b: float=0.0) -> None:
        """
        Create a colour source segment for the duration of the gap, or set the colour of an existing colour source.
        """
        ...

    def set_matte_channel(arg1: PySegment, channel_name: str='', channel_index: int=-1, scope: str='Follow Preferences', matte_mode: str='Custom Matte') -> bool:
        """
        Set the Matte channel of the source specified by channel_index or by channel_name if the matte_mode is set to Custom Matte.
        Keywords argument:
        channel_name -- Name of the channel found in matte_channels.
        channel_index -- Index of the channel found in matte_chanels.
        scope -- Scope of the changes ( Follow Preferences, No Sharing, Follow Source Sharing, Follow Connected Segments).
        matte_mode -- Matte origin (Follow RGB, No Matte, Custom Matte).
        """
        ...

    def set_rgb_channel(arg1: PySegment, channel_name: str='', channel_index: int=-1, scope: str='Follow Preferences') -> bool:
        """
        Set the RGB channel of the source specified by channel_index or by channel_name
        Keywords argument:
        channel_name -- Name of the channel found in rgb_channels.
        channel_index -- Index of the channel found in rgb_chanels.
        scope -- Scope of the changes ( Follow Preferences, No Sharing, Follow Source Sharing, Follow Connected Segments).
        """
        ...

    def shared_source_segments(arg1: PySegment) -> Any:
        """
        Return a list of the segments sharing this segment's source.
        """
        ...

    def slide_keyframes(arg1: PySegment, offset: int, sync: bool=False) -> bool:
        """
        Slide the keyframes the PySegment.
        Keywords argument:
        offset -- Relative offset to slide the keyframes.
        sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.
        """
        ...

    def slip(arg1: PySegment, offset: int, sync: bool=False, keyframes_move_mode: str='Shift') -> bool:
        """
        Slip the media of the PySegment.
        Keywords argument:
        offset -- Relative offset to slip the media.
        sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.
        keyframes_move_mode -- Select how the animation channels are affected ( Pin, Shift, Prop)
        """
        ...

    def smart_replace(arg1: PySegment, source_clip: PyClip) -> None:
        """
        Replace the PySegment by the source_clip segment, including the TimelineFX.
        """
        ...

    def smart_replace_media(arg1: PySegment, source_clip: PyClip) -> None:
        """
        Replace the media of PySegment by the source_clip segment, leaving the PySegment TimelineFX untouched
        """
        ...

    def sync_connected_segments(arg1: PySegment) -> None:
        """
        Sync connected segments with the Timeline FXs of the current segment.
        """
        ...

    def trim_head(arg1: PySegment, offset: int, ripple: bool=False, sync: bool=False, keyframes_move_mode: str='Shift') -> bool:
        """
        Modify the amount of head of the PySegment.
        Keywords argument:
        offset -- Number of frames to add or remove from the head.
        ripple -- Enable to prevent gaps from appearing when performing a trim.
        sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.
        keyframes_move_mode -- Select how the animation channels are affected ( Pin, Shift, Prop)
        """
        ...

    def trim_tail(arg1: PySegment, offset: int, ripple: bool=False, sync: bool=False, keyframes_move_mode: str='Shift') -> bool:
        """
        Modify the amount of tail of the PySegment.
        Keywords argument:
        offset -- Number of frames to add or remove from the tail.
        ripple -- Enable to prevent gaps from appearing when performing a trim.
        sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.
        keyframes_move_mode -- Select how the animation channels are affected ( Pin, Shift, Prop)
        """
        ...


class PySequence(PyClip):
    """
    Object representing a Sequence.
    """
    archive_date = ...
    archive_error = ...
    attributes = ...
    audio_tracks = ...
    bit_depth = ...
    cached = ...
    colour_primaries = ...
    creation_date = ...
    duration = ...
    essence_uid = ...
    frame_rate = ...
    groups = ...
    has_deliverables = ...
    has_history = ...
    height = ...
    markers = ...
    matrix_coefficients = ...
    original_source_uid = ...
    parent = ...
    proxy_resolution = ...
    ratio = ...
    sample_rate = ...
    scan_mode = ...
    source_uid = ...
    start_frame = ...
    subtitles = ...
    transfer_characteristics = ...
    unlinked = ...
    versions = ...
    width = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def cache_media(arg1: PyClip, mode: str='current') -> bool:
        """
        Cache the Clip's linked media.
        Keyword argument:
        mode -- Determine the version to cache (currently selected or all versions). All Versions is only useful with to multi-version clips (Current, All Versions)
        """
        ...

    def change_dominance(arg1: PyClip, scan_mode: str) -> None:
        """
        Change the Clip's dominance. Changes only the clip's metadata.
        Keyword argument:
        scan_mode -- Field dominance. (P, F1, F2)
        """
        ...

    def change_start_frame(arg1: PyClip, start_frame: int, use_segment_connections: bool=True) -> None:
        """
        Modify the start frame of a source Clip.
        Keywords argument:
        start_frame -- New start frame of the clip.
        use_segment_connections -- Sync the start frame of connected segments.
        """
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def close_container(arg1: PyClip) -> None:
        """
        Close the container timeline if the Clip is inside a container.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def copy_selection_to_media_panel(arg1: PySequence, destination: PyArchiveEntry, duplicate_action: str='add') -> Any:
        """
        Create a new clip by copying the currently selected segments.
        Return the new PyClip.
        Keyword arguments:
        destination -- The PyObject that acts as the destination.
        duplicate_action -- Action to take when an object with the same name already exists (add or replace).
        """
        ...

    def create_audio(arg1: PySequence, stereo: bool=False) -> Any:
        """
        Add an Audio Track to the Sequence.
        """
        ...

    def create_container(arg1: PySequence) -> Any:
        """
        Create a container with the selected segments or between the in and out marks.
        """
        ...

    def create_group(arg1: PySequence, name: str) -> Any:
        """
        Creates a new PySequenceGroup.
        The group name must be supplied as argument.
        """
        ...

    def create_marker(arg1: PyClip, location: Any) -> Any:
        """
        Add a Marker to the Clip.Keyword argument:
        location -- The frame where the marker gets created.
        """
        ...

    def create_subtitle(arg1: PySequence) -> Any:
        """
        Add a Subtitle Track to the Sequence.
        """
        ...

    def create_version(arg1: PySequence, stereo: bool=False) -> Any:
        """
        Add a Version to the Sequence.
        """
        ...

    def cut(arg1: PyClip, cut_time: PyTime) -> None:
        """
        Cut all tracks of the Clip.
        """
        ...

    def extract_selection_to_media_panel(arg1: PySequence, destination: PyArchiveEntry=None, duplicate_action: str='add') -> Any:
        """
        Extract the selection from the sequence.
        Return the new PyClip created from the selection when a destination is supplied.
        Keyword arguments:
        destination -- The PyObject that acts as the destination.
        duplicate_action -- Action to take when an object with the same name already exists (add or replace).
        """
        ...

    def flush_cache_media(arg1: PyClip, mode: str='current') -> bool:
        """
        Flush the Clip's media cache.
        Keyword argument:
        mode -- Determine the version's cache to flush. (Current, All Versions, All But Current)
        """
        ...

    def flush_renders(arg1: PyClip) -> None:
        """
        Flush the Clip's TimelineFX renders.
        """
        ...

    def get_colour_space(arg1: PyClip, time: PyTime=None) -> str:
        """
        Return the colour space at the requested time. Use current_time when no time is supplied.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def import_subtitles_file(arg1: PySequence, file_name: str, file_type: Any=None, align_first_event_to_clip_start: bool=False, convert_from_frame_rate: Any=None) -> Any:
        """
        Import a subtitles file into a new Subtitles Track.
        Return the new PySubtitleTrack.
        Keyword arguments:
        file_name -- The path and name of the file to import.
        file_type -- The type of subtitle if it is not the file extension (srt or txt).
        align_first_event_to_clip_start -- Force the first event to be aligned with the clip start.
        convert_from_frame_rate -- frame rate of the imported file (for txt files only).
        """
        ...

    def insert(arg1: PySequence, source_clip: PyClip, insert_time: PyTime=None, destination_track: PyTrack=None) -> bool:
        """
        Creates a new PySequenceGroup.
        The group name must be supplied as argument.
        """
        ...

    def is_rendered(arg1: PyClip, top_only: bool=False, render_quality: str='Full Resolution') -> bool:
        """
        Return if a Clip is rendered.
        The following attributes can be defined: top_only, render_quality.
        """
        ...

    def lift_selection_to_media_panel(arg1: PySequence, destination: PyArchiveEntry=None, duplicate_action: str='add') -> Any:
        """
        Lift the selection from the sequence.
        Return the new PyClip created from the selection when a destination is supplied.
        Keyword arguments:
        destination -- The PyObject that acts as the destination.
        duplicate_action -- Action to take when an object with the same name already exists (add or replace).
        """
        ...

    def open(arg1: PySequence) -> bool:
        """
        Open the Sequence.
        """
        ...

    def open_as_sequence(arg1: PyClip) -> Any:
        """
        Open the Clip as a Sequence. Mutates the PyClip object into a PySequence object.
        """
        ...

    def open_container(arg1: PyClip) -> bool:
        """
        Open the container timeline if the Clip is inside a container.
        """
        ...

    def overwrite(arg1: PySequence, source_clip: PyClip, overwrite_time: PyTime=None, destination_track: PyTrack=None) -> bool:
        """
        Creates a new PySequenceGroup.
        The group name must be supplied as argument.
        """
        ...

    def reformat(arg1: PyClip, width: int=0, height: int=0, ratio: float=0.0, bit_depth: int=0, scan_mode: str='', frame_rate: str='', resize_mode: str='Letterbox') -> None:
        """
        Reformat the Clip to the specified format.
        Keywords arguments:
        width -- Integer between 24 and 16384.
        height -- Integer between 24 and 16384.
        ratio -- Frame aspect ratio. Float between 0.01 and 100.
        bit_depth -- Bit depth. (8, 10, 12, 16 or 32)
        scan_mode -- Scan mode of the sequence. (F1, F2, P)
        frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps)
        resize_mode -- Resize mode. (Letterbox, Crop Edges, Fill, Centre)
        """
        ...

    def render(arg1: PyClip, render_mode: str='All', render_option: str='Foreground', render_quality: str='Full Resolution', effect_type: str='', effect_caching_mode: str='Current', include_handles: bool=False) -> bool:
        """
        Trigger a render of the Clip
        The following attributes can be defined: render_mode, render_option, render_quality, effect_type, effect_caching_mode and include_handles.
        """
        ...

    def save(arg1: PyClip) -> bool:
        """
        Save the Clip to the defined save destination.
        """
        ...


class PySequenceGroup(PyFlameObject):
    """
    Object representing a Group in a Sequence.
    """
    attributes = ...
    parent = ...
    segments = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def add(arg1: PySequenceGroup, segments: Any) -> None:
        """
        Adds a PySegment or list of PySegments to the Group.
        """
        ...

    def remove(arg1: PySequenceGroup, segments: Any) -> None:
        """
        Remove a PySegment or list of PySegments from the Group.
        """
        ...


class PySubtitleTrack(PyTrack):
    """
    Object representing a Subtitle Track.
    """
    attributes = ...
    parent = ...
    segments = ...
    transitions = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def copy_to_media_panel(arg1: PyTrack, destination: PyArchiveEntry, duplicate_action: str='add') -> Any:
        """
        Create a new clip with a copy of the PyObject.
        """
        ...

    def cut(arg1: PyTrack, cut_time: PyTime, sync: bool=False) -> None:
        """
        Cut the Track.
        """
        ...

    def export_as_srt_file(arg1: PySubtitleTrack, file_name: str, character_based_attributes: bool=True, export_colours: bool=False, exclude_colour: str='', use_original_colours: bool=False, use_original_alignment: bool=False, export_alignments: bool=False, alignment_type: str='an', exclude_alignment: str='', start_timecode: str='Same as Clip') -> None:
        """
        Export the Subtitles Track as a SubRip (srt) file.Keyword arguments:
        file_name -- The path and name of the file to write.
        character_based_attributes -- Export the bold, italic, and underline attributes.
        export_colours -- Export colours.
        exclude_colour -- Specify a colour, in hexadecimal or CSS colour name, to ignore.
        use_original_colours -- Reuse hexadecimal or CSS colour names from the imported file.
        use_original_alignment -- Reuse alignment tokens from the imported file .
        export_alignments -- Export alignments.
        alignment_type -- Set to a or an alignment style tokens.
        exclude_alignment -- Specify an alignment to ignore.
        start_timecode -- Specify the timecode mode, Same as Clip or, Relative to Clip Start.
        """
        ...

    def insert_transition(arg1: PyTrack, record_time: PyTime, type: str, duration: int=10, alignment: str='Centred', in_offset: int=0, sync: bool=False) -> Any:
        """
        Insert a Transition on the Track.
        Returns the new PyTransition if successful.
        Keywords argument:
        record_time -- Time at which the Transition is inserted.
        type -- Type of the new Transition.
        duration -- Duration of the new Transition in frames.
        alignment -- Alignment of the new Transition.
        in_offset -- Number of frames on left side of the cut in custom alignment.
        sync -- Perform the operation on all Tracks part of the sync group.
        """
        ...


class PyTime:
    """
    Object representing a time unit

PyTime(timecode, frame_rate)
PyTime(relative_frame)
PyTime(absolute_frame, frame_rate)
    """
    frame = ...
    frame_rate = ...
    relative_frame = ...
    timecode = ...

    def __add__(arg1: PyTime, arg2: PyTime) -> Any:
        ...

    @overload
    def __add__(arg1: PyTime, arg2: int) -> Any:
        ...

    def __eq__(arg1: PyTime, arg2: PyTime) -> bool:
        ...

    def __iadd__(arg1: Any, arg2: PyTime) -> Any:
        ...

    @overload
    def __iadd__(arg1: Any, arg2: int) -> Any:
        ...

    def __init__(arg1: Any, arg2: str, arg3: str) -> None:
        ...

    @overload
    def __init__(arg1: Any, arg2: int) -> None:
        ...

    @overload
    def __init__(arg1: Any, arg2: int, arg3: str) -> None:
        ...

    def __isub__(arg1: Any, arg2: PyTime) -> Any:
        ...

    @overload
    def __isub__(arg1: Any, arg2: int) -> Any:
        ...

    def __ne__(arg1: PyTime, arg2: PyTime) -> bool:
        ...

    def __repr__(arg1: PyTime) -> Any:
        ...

    def __str__(arg1: PyTime) -> str:
        ...

    def __sub__(arg1: PyTime, arg2: PyTime) -> Any:
        ...

    @overload
    def __sub__(arg1: PyTime, arg2: int) -> Any:
        ...


class PyTimeline:
    """
    This class represents the Timeline.
    """
    clip = ...
    current_effect = ...
    current_marker = ...
    current_segment = ...
    current_transition = ...
    type = ...


class PyTimelineFX(PyFlameObject):
    """
    Object representing a TimelineFX.
    """
    attributes = ...
    has_maps_cache_media = ...
    parent = ...
    type = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def flush_maps_cache_media(arg1: PyTimelineFX) -> bool:
        """
        Flush the Timeline FX Maps and ML cached media.
        """
        ...

    def load_setup(arg1: PyTimelineFX, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def save_setup(arg1: PyTimelineFX, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def slide_keyframes(arg1: PyTimelineFX, offset: float) -> None:
        """
        Slide the keyframes the PySegment.
        Keywords argument:
        offset -- Relative offset to slide the keyframes.
        sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.
        """
        ...

    def sync_connected_segments(arg1: PyTimelineFX) -> None:
        """
        Push the Timeline FX to connected segments.
        """
        ...


class PyTrack(PyFlameObject):
    """
    Object representing a Track.
    """
    attributes = ...
    parent = ...
    segments = ...
    transitions = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def copy_to_media_panel(arg1: PyTrack, destination: PyArchiveEntry, duplicate_action: str='add') -> Any:
        """
        Create a new clip with a copy of the PyObject.
        """
        ...

    def cut(arg1: PyTrack, cut_time: PyTime, sync: bool=False) -> None:
        """
        Cut the Track.
        """
        ...

    def insert_transition(arg1: PyTrack, record_time: PyTime, type: str, duration: int=10, alignment: str='Centred', in_offset: int=0, sync: bool=False) -> Any:
        """
        Insert a Transition on the Track.
        Returns the new PyTransition if successful.
        Keywords argument:
        record_time -- Time at which the Transition is inserted.
        type -- Type of the new Transition.
        duration -- Duration of the new Transition in frames.
        alignment -- Alignment of the new Transition.
        in_offset -- Number of frames on left side of the cut in custom alignment.
        sync -- Perform the operation on all Tracks part of the sync group.
        """
        ...


class PyTransition(PyFlameObject):
    """
    Object representing a Transition.
    """
    attributes = ...
    in_offset = ...
    parent = ...
    record_time = ...
    type = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def set_dissolve_to_from_colour(arg1: PyTransition, r: float=0.0, g: float=0.0, b: float=0.0) -> None:
        """
        Make a dissolve transition dissolve to/from a colour.
        """
        ...

    def set_fade_to_from_silence(arg1: PyTransition) -> None:
        """
        Make a fade dip to/from silence.
        """
        ...

    def set_transition(arg1: PyTransition, type: str, duration: int=10, alignment: str='Centred', in_offset: int=0) -> Any:
        """
        Replace the Transition with another type of Transition.
        Returns the new PyTransition if successful.
        Keywords argument:
        type -- Type of the new Transition.
        duration -- Duration of the new Transition in frames.
        alignment -- Alignment of the new Transition.
        in_offset -- Number of frames on left side of the cut in custom alignment.
        """
        ...

    def slide(arg1: PyTransition, offset: int, sync: bool=False) -> bool:
        """
        Slide the Transition.
        Keywords argument:
        offset -- Amount of frames to slide the Transition with.
        sync -- Enable to perform the same operation on transitions that belong to the same sync group as the current PyTransition.
        """
        ...


class PyUser:
    """
    Object representing a User.
    """
    name = ...
    nickname = ...


class PyUsers:
    """
    Object representing the User manager.
    """
    current_user = ...


class PyVersion(PyFlameObject):
    """
    Object representing a Version.
    """
    attributes = ...
    parent = ...
    stereo = ...
    tracks = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def copy_to_media_panel(arg1: PyVersion, destination: PyArchiveEntry, duplicate_action: str='add') -> Any:
        """
        Create a new clip with a copy of the PyObject.
        """
        ...

    def create_track(arg1: PyVersion, track_index: int=-1, hdr: bool=False) -> Any:
        """
        Add a track to the Version.Keywords arguments:
        track_index -- Index to insert the new track at, -1 to append at the top.
        hdr -- Set to True to create an HDR track.
        """
        ...

    def import_DolbyVision_xml(arg1: PyVersion, file_name: str, mode: str='Include Frame Based Transitions Trims', track_index: int=-1) -> Any:
        """
        Add a track to the Version.Keywords arguments:
        track_index -- Index to insert the new track at, -1 to append at the top.
        hdr -- Set to True to create an HDR track.
        """
        ...


class PyWorkspace(PyArchiveEntry):
    """
    Object representing a Workspace.
    """
    attributes = ...
    desktop = ...
    libraries = ...
    parent = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def clear_colour(arg1: PyArchiveEntry) -> None:
        """
        Clear the colour of an object in the Media Panel.
        """
        ...

    def commit(arg1: PyArchiveEntry) -> None:
        """
        Commit to disk the Media Panel object or its closest container possible.
        """
        ...

    def create_library(arg1: PyWorkspace, name: str) -> Any:
        """
        Create a new Library in a Workspace.
        """
        ...

    def get_wiretap_node_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def get_wiretap_storage_id(arg1: PyArchiveEntry) -> str:
        """
        Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.
        """
        ...

    def replace_desktop(arg1: PyWorkspace, desktop: PyDesktop) -> bool:
        """
        Replace the Workspace active Desktop with another one.
        """
        ...

    def set_desktop_reels(arg1: PyWorkspace, group: Any=None) -> bool:
        """
        Set the Desktop Reels view mode.
        """
        ...

    def set_freeform(arg1: PyWorkspace, reel: Any=None) -> bool:
        """
        Set the Freeform view mode.
        """
        ...


class PyWriteFileNode(PyRenderNode):
    """
    Class derived from PyRenderNode. This class represents a WriteFile node.
    """
    attributes = ...
    channels = ...
    input_sockets = ...
    output_sockets = ...
    parent = ...
    sockets = ...

    def __getattr__(arg1: PyFlameObject, arg2: str) -> Any:
        ...

    def __setattr__(arg1: PyFlameObject, arg2: str, arg3: Any) -> None:
        ...

    def delete(arg1: PyFlameObject, confirm: bool=True) -> bool:
        """
        Delete the node.
        """
        ...

    def duplicate(arg1: PyNode, keep_node_connections: bool=False) -> Any:
        """
        Duplicate the node.
        """
        ...

    def get_resolved_media_path(arg1: PyWriteFileNode, show_extension: bool=True, translate_path: bool=True, frame: Any=None) -> Any:
        """
        Return the resolved media path.
        Keyword arguments:
        show_extension -- Set True to display the extension.
        translate_path -- Set True to apply the Media Location Path Translation.
        frame -- Pass a frame number, between range_start and range_end, to get the path for that frame.
        """
        ...

    def load_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Load a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def save_node_setup(arg1: PyNode, file_name: str) -> bool:
        """
        Save a Node setup. A path and a file name must be defined as arguments.
        """
        ...

    def set_channel_name(arg1: PyRenderNode, channel: Any, name: Any) -> None:
        """
        Rename a channel, using its index or front channel name as the index key.
        Keyword arguments:
        channel -- The channel to rename. Can be the channel index or the current name of the channel's front socket.
        name -- The new name of the channel. The type is either a string or a tuple. A Write File node always takes a string. A Render node takes a string or a tuple.
        In a Render node, a string only sets the name of the channel's front socket; the function creates the name of the matte socket by appending '_alpha' to 'name'. In the UI, the channel is flagged 'Sync'. A Write File node has only one socket per channel, and requires only a string to set a socket name.
        In a Render node, a tuple sets the names of the front and matte sockets. In the UI, the channel is not flagged 'Sync'. A Write File node does not accept a tuple.
        """
        ...

    def set_context(arg1: PyNode, index: int, socket_name: str='Default') -> bool:
        """
        Set a Context view on a Node socket. An index and a socket name must be defined as arguments.
        """
        ...


class BuiltinImporter(object):
    """
    Meta path import for built-in modules.

    All methods are either class or static methods to avoid the need to
    instantiate the class.
    """
    ...


def delete(object: PyFlameObject, confirm: bool=True) -> bool:
    """
    Delete the target object.
    """
    ...

def duplicate(object: PyFlameObject, keep_node_connections: bool=False) -> Any:
    """
    Duplicate the target object.
    """
    ...

def duplicate_many(object_list: list, keep_node_connections: bool=False) -> list:
    """
    Duplicate the target objects.
    """
    ...

def execute_command(command: str, blocking: bool=True, shell: bool=False, capture_stdout: bool=False, capture_stderr: bool=False) -> tuple:
    """
    Execute command line through the Autodesk Flame Multi-Purpose Daemon.
    This way of starting new processes is better since any native python
    subprocess command (os.system, subprocess, Popen, etc) will call fork()
    which will duplicate the process memory before calling exec().
     This can be costly especially for a process like Flame.
    
    command -- Command line to execute.
    blocking -- If True, will not return until the command line has completed.
    shell -- Should the command be executed in a sh shell.
             WARNING Using shell=True can be a security hazard.
    capture_stdout -- If True, stdout of the command will be captured and
                      returned instead of forwarded to the application stdout.
                      Requires blocking=True
    capture_stderr -- If True, stdout of the command will be captured and
                      returned instead of forwarded to the application stderr.
                      Requires blocking=True
    
    Note: Environment variables will not be forwarded to the executed command.
    """
    ...

def execute_shortcut(description: str, update_list: bool=True) -> bool:
    """
    Execute the Flame shortcut.
    description  -- The description in the Keyboard Shortcut editor.
    """
    ...

def exit() -> None:
    """
    Exit the application.
    """
    ...

def find_by_name(name: str, parent: Any=None) -> list:
    """
    Find a Flame object in the Media Panel by name.
    """
    ...

def find_by_uid(uid: str) -> Any:
    """
    Find a Flame object in the Media Panel by UID.
    """
    ...

def find_by_wiretap_node_id(node_id: str) -> Any:
    """
    Find a Flame object in the Media Panel by Wiretap Node ID.
    """
    ...

def get_current_tab() -> str:
    """
    Get the current tab name.
    """
    ...

def get_home_directory() -> str:
    """
    Get the application home directory.
    """
    ...

def get_init_cfg_path() -> str:
    """
    Get the application init configuration file.
    """
    ...

def get_version() -> str:
    """
    Get the application version.
    """
    ...

def get_version_major() -> str:
    """
    Get the application major version.
    """
    ...

def get_version_minor() -> str:
    """
    Get the application minor version.
    """
    ...

def get_version_patch() -> str:
    """
    Get the application patch version.
    """
    ...

def get_version_stamp() -> str:
    """
    Get the application version stamp.
    """
    ...

def go_to(tab: str) -> bool:
    """
    Deprecated / use set_current_tab() instead.
    """
    ...

def import_clips(path: Any, destination: Any=None) -> list:
    """
    Import one or many clips from a path.
    Keyword arguments:
    path -- The path to the media can be:
     - A path to a single media file.
     - A path to a sequence of media files (ie "/dir/clip.[100-2000].dpx").
     - A folder containing media files.
     - A pattern to media files (ie "/dir/{name}_v{version}.{frame}.{extension}").
     - A list of paths.
    destination -- Flame object containing a clip like a reel or a folder object.
    """
    ...

def schedule_idle_event(function: Any, delay: int=0) -> None:
    """
    Register a function callback that will be called eventually when the application is idle. The function must not block and be quick since it will be executed in the main application thread.
    Keyword arguments:
    function -- Callable object to be called.
    delay -- Minimum time (in seconds) to wait before calling function.
    """
    ...

def set_current_tab(arg1: str) -> bool:
    """
    Set the given tab as the active environment.
    Keyword arguments:
    tab -- The tab to set active (MediaHub, Conform, Timeline, Effects, Batch, Tools)
    """
    ...

def set_render_option(render_option: str, render_context: str='') -> bool:
    """
    Set the default render option.
    Keyword arguments:
    render_option -- Defines the rendering method used. (Foreground, Background Reactor, Background Reactor (Auto), Burn)
    render_context -- Defines the rendering context. (Timeline, Conform, Effects, BFX, Batch). None for all of them.
    Note: Batch does not support Background Reactor (Auto) and will
          default to Background Reactor if (Auto) is passed.
    """
    ...
