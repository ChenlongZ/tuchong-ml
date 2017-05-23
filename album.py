class Album:

    """
    A model class as a album abstraction, should have
    tags:   []
    images: [
        imageElement : {
            id:             long
            author_id:      long
            large_url:      ""
            medium_url:     ""
            small_url:      ""
            grid_url:       ""
            height:         int
            width:          int
            exif:           {
                camera:         ""
                lens:           ""
                aperture:       ""
                shutter_speed:  ""
                focus_length:   ""
                iso:            ""
            }
        }
    ]
    likes:      int
    comments:   int
    type:       ""
    author: {
        name:           ""
        followers:      int
        site:           ""
        id:             long
        thumbnail_url:  ""
    }
    post_url:           ""
    site_url:           ""
    """

    def __init__(self):
        pass