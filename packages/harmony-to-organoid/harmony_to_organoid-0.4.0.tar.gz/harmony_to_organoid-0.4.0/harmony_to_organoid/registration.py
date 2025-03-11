import numpy as np
from ashlar.reg import EdgeAligner


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
