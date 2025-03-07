import os
import tempfile
from typing import Optional, TYPE_CHECKING

from geoassistant.report.SlidesFile import SlidesFile
from geoassistant.statistics.histogram.CategoricHistogram import CategoricHistogram

if TYPE_CHECKING:
    from geoassistant.block_model.BlockModel import BlockModel


class BlockModelReporter(object):

    def __init__(self, block_model: 'BlockModel'):
        self.block_model: 'BlockModel' = block_model

    def createVariablesReport(self, savepath: Optional[str]) -> None:
        sf = SlidesFile()
        sf.initiateEmptyPresentation()

        for v in self.block_model.getFieldsNames():
            v_slide = sf.addEmptySlide(title=v)

            field = self.block_model.getField(field_id=v)

            if field.isCategoric():
                h = CategoricHistogram()
                h.setCategories(categories=field.getUniqueValues())
                h.setData(data=field.getData())

                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name  # Get the file path
                    h.save(savepath=temp_file_path)

                v_slide.addImage(temp_file_path, height=3.5, width=None, left=6.2, top=2.2)
                os.remove(temp_file_path)

            if field.isCategoric():
                v_slide.addTextbox(text=f"{len(field.getUniqueValues())} unique values.",
                                   height=0.4, width=4.28, left=0.5, top=1.05, alignment="left")

            txt = '\n'.join([str(s) for s in field.getRandomValues()])
            v_slide.addTextbox(text=f"{txt}", height=0.4, width=4.28, left=0.5, top=1.4, alignment="left")

        sf.savePresentation(savepath=savepath)

