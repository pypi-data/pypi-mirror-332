from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.block_model.BlockModel import BlockModel


class BlockModelPositions(object):

    def __init__(self, block_model: 'BlockModel'):
        self.block_model: 'BlockModel' = block_model


