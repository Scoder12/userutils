import userutils
import userutils.examples
from upload import upload

userutils.examples.main()

if userutils.yesNo('upload? '):
    upload()
