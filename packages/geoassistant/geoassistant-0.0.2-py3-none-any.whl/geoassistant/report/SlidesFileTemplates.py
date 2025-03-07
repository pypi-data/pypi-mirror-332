from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from geoassistant.report.SlidesFile import SlidesFile


class SlidesFileTemplates(object):

    def __init__(self, slide_file: 'SlidesFile'):
        self.slide_file = slide_file

    def create(self, images_paths: List[str],
               images_grid: List[int],
               images_titles: Optional[List[str]] = None,
               images_comments: Optional[List[str]] = None):

        self.slide_file.initiateEmptyPresentation()

        imgs_per_slide = int(images_grid[0] * images_grid[1])

        for i, img_path in enumerate(images_paths[::imgs_per_slide]):
            img0 = img_path

            slide = self.slide_file.addEmptySlide(title="")
            slide.addImage(picpath=img0, height=None, width=4.97, left=1.41, top=1.70)

            if images_titles is not None:
                title0 = images_titles[images_grid[0]*i]
                slide.addTextbox(text=title0, height=0.4, width=4.28, left=1.76, top=1.,
                                 font="Calibri", fontsize=18, alignment="center")

            if images_comments is not None:
                comm0 = images_comments[images_grid[0]*i]
                slide.addTextbox(text=comm0, height=0.91, width=4.28, left=1.76, top=5.76,
                                 font="Calibri", fontsize=12, alignment="center")

            if (2 * i + 1) == len(images_paths):
                continue

            img1 = images_paths[images_grid[0] * i + 1]
            slide.addImage(picpath=img1, height=None, width=4.97, left=6.96, top=1.70)
            if images_titles is not None:
                title1 = images_titles[2 * i + 1]
                slide.addTextbox(text=title1, height=0.4, width=4.28, left=7.3, top=1.,
                                 font="Calibri", fontsize=18, alignment="center")

            if images_comments is not None:
                comm1 = images_comments[2 * i + 1]
                slide.addTextbox(text=comm1, height=0.91, width=4.28, left=7.3, top=5.76,
                                 font="Calibri", fontsize=12, alignment="center")



