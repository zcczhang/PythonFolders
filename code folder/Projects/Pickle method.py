"""
pickle
"""
import pickle
"""
pickle the huge data into ',pk1'
"""
huge_data = {'北京': '101010100',
             '天津': '101030100',
             '上海': '101020100',
             '石家庄': '101090101',
             '张家口': '101090301',
             '承德': '101090402',
             '唐山': '101090501',
             '秦皇岛': '101091101',
             '杭州': '101210101',
             '温州': '101210701',
             '重庆': '101040100',
             '海南': '101150401',
             '济南': '101120101',
             '潍坊': '101120601',
             '吐鲁番': '101130501',
             '厦门': '101230201',
             '青岛': '101120201',
             '拉萨': '101140101'}
pickle_file_create = open('hugedata_file.pk1', 'wb')       # store in binary
pickle.dump(huge_data, pickle_file_create)                 # picking: dump the data to the new .pk1 file
pickle_file_create.close()                                          # close the data package

"""
call the huge data in other programs:
"""
with open('hugedata_file.pk1', 'rb') as pickle_file:           # read in binary
    call_data = pickle.load(pickle_file)                       # unpicking: load the data: binary -> object

