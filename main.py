from extractor import Extractor
import consts as c

extractorObj = Extractor(
    restUrl = c.URL_TO_RETRIEVE,
    filename=c.FILENAME,
    maxLineLimit = c.MAX_LINE_LIMIT
)

if __name__ == "__main__":
    extractorObj.extract()