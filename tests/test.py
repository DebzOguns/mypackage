from mypackage import myModule
def test_top_n():
    '''
     make sure top_n works correctly
    '''
    assert myModule.top_n([8,4,3,5,7,6], 3)== [8,7,6], 'incorrect'
    assert myModule.top_n([10,46,23,14,5,6], 2)== [46,23], 'incorrect'
    assert myModule.top_n([12,15,16,13,19], 5)== [19,16,15,13,12], 'incorrect'