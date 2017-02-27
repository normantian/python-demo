import os
export = []
for root,dirs,files in os.walk('e:/FTP'):
    export.append("\n %s,%s,%s" % (root,dirs,files))
open('e:/1.txt','w').write(''.join(export))
