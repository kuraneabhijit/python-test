def test_multi_args(arg1,arg2):
        print(arg1)
        print(arg2)
    

test_multi_args('aaa','bbb')
multi_params={'arg1':'test','arg2':'this'}
test_multi_args(**multi_params)