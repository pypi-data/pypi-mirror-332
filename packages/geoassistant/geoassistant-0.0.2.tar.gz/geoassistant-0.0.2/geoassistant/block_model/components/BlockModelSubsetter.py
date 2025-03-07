from geoassistant.block_model.BlockModel import BlockModel


class BlockModelSubsetter(object):

    def __init__(self, block_model: 'BlockModel'):
        self.block_model: 'BlockModel' = block_model

