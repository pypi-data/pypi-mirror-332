import networkx as nx
import numpy as np
from ashlar.reg import EdgeAligner

def neighbors_graph_bounding_box_overlap(aligner):
    """Return graph of neighboring (overlapping) tiles.

    Tiles are considered neighbors if their bounding boxes overlap.

    """
    if not hasattr(aligner, '_neighbors_graph'):
        positions = aligner.metadata.positions  # (N, 2) positions
        tile_h, tile_w = aligner.metadata.size  # Tile height & width

        # Compute bounding boxes: (x1, y1, x2, y2)
        bboxes = np.array([
            [x, y, x + tile_w, y + tile_h]  # (left, top, right, bottom)
            for y, x in positions  # (y, x) -> (x, y) for bounding box
        ])

        def overlap(bbox1, bbox2):
            """Check if two bounding boxes overlap."""
            x1, y1, x2, y2 = bbox1
            x1b, y1b, x2b, y2b = bbox2
            return not (x2 <= x1b or x2b <= x1 or y2 <= y1b or y2b <= y1)

        # Build graph based on bounding box intersections
        graph = nx.Graph()
        num_tiles = len(bboxes)

        for i in range(num_tiles):
            for j in range(i + 1, num_tiles):  # Avoid duplicate checks
                if overlap(bboxes[i], bboxes[j]):
                    graph.add_edge(i, j)

        graph.add_nodes_from(range(num_tiles))  # Ensure all nodes exist
        aligner._neighbors_graph = graph

    return aligner._neighbors_graph

EdgeAligner.neighbors_graph = property(neighbors_graph_bounding_box_overlap)

class GroupMetadata:
    def __init__(self, positions, tile_shape, pixel_size=1.0, pixel_dtype=np.uint16):
        self._positions = np.array(positions)  # positions as (y, x)
        self.tile_shape = tile_shape  # e.g. img_2d.shape (height, width)
        self.pixel_size = pixel_size  # in microns (or 1.0 if not specified)
        self.pixel_dtype = pixel_dtype
        self.num_images = len(positions)
        self.num_channels = 1  # assuming single-channel for registration

    @property
    def positions(self):
        return self._positions

    @property
    def size(self):
        return np.array(self.tile_shape)

    @property
    def origin(self):
        # This provides the minimum coordinate, as expected by Ashlar
        return self._positions.min(axis=0)


class GroupReader:
    def __init__(self, images, metadata):
        self.images = images
        self._metadata = metadata

    @property
    def metadata(self):
        return self._metadata

    def read(self, series, c):
        # Ignores channel (assumes one channel) and returns the representative image.
        return self.images[series]


def register(reg_images, nominal_positions, tile_shape):
    metadata = GroupMetadata(nominal_positions, tile_shape)
    reader = GroupReader(reg_images, metadata)

    # flip positions
    reader.metadata._positions *= [-1, 1]

    # Create an aligner for the group.
    aligner = EdgeAligner(reader=reader, channel=0, max_shift=15, alpha=0.01, verbose=True)
    aligner.run()

    # After running, the aligned positions are available as:
    registered_positions = aligner.positions  # shape: (num_fields, 2)

    # flip positions back
    registered_positions *= [-1, 1]

    return registered_positions
