import optparse

# optparse
parser = optparse.OptionParser('usage Calc.py -n <tgtNum> -o <operation>')
parser.add_option('-n', dest='tgtNum', type='string', help='write numbers with comma')
parser.add_option('-o', dest='operation', type='string', help='specify operation + - * / %')
(option, args) = parser.parse_args()