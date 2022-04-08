from lib2 import average

def test_average():
    input1 = [11,-11,10,20]
    expected_result = 7.5
    actual_result = average(input1)
    assert expected_result == actual_result

test_average()


# OU

#def test_average():
#    input1 = [11,-11,10,20]
#    expected_result = average(input1)
#    assert expected_result == actual_result

#test_average()