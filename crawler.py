

class Crawler:

    """
    tuchong restful API crawler fires requests each time
    1. fetch the initial tag specific information (default pages = 100, photo_array size = 20 for each page
    2. fetch the album information for each photo, a .json file is created for each photo
    3. the images in each album is downloaded given the linked fetched in step 1 and 2
    """

    def __init__(self, tag, subject, page=100, order='new'):
        self.url = ["https://tuchong.com/rest/tags/%s/posts?type=%s&page=%d&order=%s" % (tag, subject, i, order)
                    for i in xrange(1, page + 1)]

    def fetch_tag(self):
        """
        just fetch initial post info for each pages
        call process_response
        :return: None
        """
        pass

    def process_response(self):
        """
        this function filter out images/albums has no tag
        for images/albums has tag names longer than 4, strip off those tags 
        dump albums to mongodb
        :return: None
        """
        pass

    def fetch_photo_info(self):
        """
        fetch photo info and complete mongodb entry
        :return: None
        """
        pass

    def download_photo(self):
        """
        query mongodb for photo info
        download_photos to mongodb 
        :return: 
        """
        pass

    def run(self):
        """
        execute a crawler task
        :return: None
        """
        pass
