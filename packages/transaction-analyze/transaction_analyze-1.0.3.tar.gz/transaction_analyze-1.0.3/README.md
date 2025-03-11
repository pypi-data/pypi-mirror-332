#Explain about the arguments..
#'-s', '--seeds', help='target blockchain address(es)', dest='seeds'
#'-o', '--output', help='output file to save raw JSON data', dest='output'
#'-d', '--depth', help='depth of crawling', dest='depth', type=int, default=3
#'-t', '--top', help='number of addresses to crawl from results', dest='top', type=int, default=5
#'-l', '--limit', help='maximum number of addresses to fetch from one address', dest='limit', type=int, default=100

#example commands
#python test.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F
#python test.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F,1ETBbsHPvbydW7hGWXXKXZ3pxVh3VFoMaX
#python test.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -l 100
#python test.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -d 2
#python test.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -t 20
#python test.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -o output.graphmlx